#!/usr/bin/env python3
"""
Send the capstone trials to the deployed FitFindr service and write a run log.

    python run_render.py --label before        3 trials, report in results/
    python run_render.py --label after         after your improvement
    python run_render.py --trials 1            a quick check

Each trial sends 5 valid queries and 5 bad requests. The report records what the
client saw (HTTP status, response fields, client-side time) and the UTC time each
request was sent, so you can find its line in Render's Logs tab.

It does NOT read Render's logs. Tokens, model_calls, run_ms and the
one-log-line-per-request check (criteria 1, 3, 4) are scored from the log lines you
copy from Render into the report. It also does not decide MET or MISSED.
Run with AI201_CACHE=0 set on Render, or cached answers will look like free passes.
"""

import argparse
import datetime as dt
import time
from pathlib import Path

import requests

ROOT = Path(__file__).parent
RESULTS = ROOT / "results"

BASE_URL = "https://fitfindr-p6is.onrender.com"
SERVICE_URL = BASE_URL + "/ask"

# valid query requests (5)
VALID_QUERIES = [
    "vintage graphic tee under $30",
    "vintage blazer in size L",
    "platform sneakers in size 8",
    "cozy oversized cardigan",
    "long sleeve in size L under $40",
]

# missing / empty query requests (5)
BAD_REQUESTS = [
    {},
    {"query": ""},
    {"query": "   "},
    {"": "leather jacket"},
    {"query": ""},
]


def utc_now():
    return dt.datetime.now(dt.timezone.utc)


def post(payload, timeout):
    """One POST. Returns a dict describing what the client saw."""
    rec = {"http": None, "data": {}, "problem": None}
    try:
        resp = requests.post(SERVICE_URL, json=payload, timeout=timeout)
        rec["http"] = resp.status_code
        try:
            rec["data"] = resp.json()
        except ValueError:
            rec["problem"] = "response was not JSON"
    except Exception as e:  # noqa: BLE001 — timeout, connection error...
        rec["problem"] = f"{type(e).__name__}: {e}"
    return rec


def run_trial(n):
    print(f"\n==================== TRIAL {n} ====================")
    rows = []

    print("\n--- 5 valid queries ---")
    for i, q in enumerate(VALID_QUERIES, 1):
        rec = post({"query": q}, timeout=90)
        data = rec["data"]
        # The response is the session dict, so these are its real keys.
        rec["fields_ok"] = (all(data.get(k) for k in ("selected_item", "outfit_suggestion", "fit_card"))
                            and data.get("error") is None)
        rec["kind"], rec["label"] = "valid", q
        rows.append(rec)
        print(f"  [{i}/5] {q!r} -> HTTP {rec['http']}, "
              f"fields ok: {rec['fields_ok']}" + (f"  ({rec['problem']})" if rec["problem"] else ""))
        time.sleep(1)

    print("\n--- 5 bad requests ---")
    for i, payload in enumerate(BAD_REQUESTS, 1):
        rec = post(payload, timeout=30)
        rec["fields_ok"] = rec["http"] == 400 and "error" in rec["data"]
        rec["kind"], rec["label"] = "bad", str(payload)
        rows.append(rec)
        print(f"  [{i}/5] {payload} -> HTTP {rec['http']}, error present: {'error' in rec['data']}"
              + (f"  ({rec['problem']})" if rec["problem"] else ""))

    valid_ok = sum(1 for r in rows if r["kind"] == "valid" and r["http"] == 200 and r["fields_ok"])
    bad_ok = sum(1 for r in rows if r["kind"] == "bad" and r["fields_ok"])
    print(f"\n>>> Trial {n}: valid queries answered with HTTP 200 and all fields: {valid_ok}/5")
    print(f">>> Trial {n}: bad requests rejected with HTTP 400 and an error: {bad_ok}/5")
    return {"rows": rows, "valid_ok": valid_ok, "bad_ok": bad_ok}


def write_report(trials, label):
    RESULTS.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    suffix = f"_{label}" if label else ""
    path = RESULTS / f"run_render_{stamp}{suffix}.md"
    n = len(trials)
    cols = " | ".join(f"Run {i}" for i in range(1, n + 1))
    blank = " | ".join([" "] * n)

    L = [
        f"# Capstone run log{f' - {label}' if label else ''}",
        "",
        "- Produced by: `run_render.py` (requests) and `serve.py::_log_request` (log lines)",
        f"- Service: {BASE_URL}",
        f"- When: {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "- Log lines: copied by hand from Render's Logs tab (see the blocks below)",
        "",
        "Fill the Run columns and the Verdict from `criteria.md` after you inspect the",
        "client results and paste the structured log lines.",
        "",
        f"| Criterion | Target | {cols} | Verdict |",
        f"|---|:---:|{'|'.join([':---:'] * n)}|:---:|",
        f"| 1. Token consumption per run stays within budget (<= 1,300 tokens) | 4 of 5 | {blank} |  |",
        f"| 2. Bad request rejects missing query without running the agent | 5 of 5 | {blank} |  |",
        f"| 3. Every request produces a structured log record | 5 of 5 | {blank} |  |",
        f"| 4. Warm request execution latency completes under 10 seconds | 4 of 5 | {blank} |  |",
        f"| 5. Model failure returns readable error and logs error status | 5 of 5 | {blank} |  |",
        "",
        "---",
        "",
    ]

    for i, t in enumerate(trials, 1):
        L += [
            f"## Trial {i}",
            "",
            f"Client-side: valid {t['valid_ok']}/5 answered with HTTP 200 and all fields, "
            f"bad {t['bad_ok']}/5 rejected with HTTP 400 and an error.",
            "",
            "| # | kind | request | HTTP | response ok |",
            "|---|---|---|---|---|",
        ]
        for j, r in enumerate(t["rows"], 1):
            note = f" ({r['problem']})" if r["problem"] else ""
            L.append(f"| {j} | {r['kind']} | {r['label']} | {r['http']} | {r['fields_ok']}{note} |")
        L += [
            "",
            f"Render log lines for trial {i} (paste the 10 JSON lines here, unedited):",
            "",
            "```json",
            "",
            "```",
            "",
        ]

    path.write_text("\n".join(L), encoding="utf-8")
    return path

def main():
    ap = argparse.ArgumentParser(description="Send the capstone trials to the deployed service.")
    ap.add_argument("--label", default="", help="a name for this run, e.g. 'before'")
    ap.add_argument("--trials", type=int, default=3, help="trials to run (default 3)")
    ap.add_argument("--pause", type=float, default=5.0, help="seconds between trials")
    args = ap.parse_args()

    print(f"Targeting: {SERVICE_URL}")
    print("Waking the instance with GET /health (a cold start can take about a minute)...")
    try:
        r = requests.get(BASE_URL + "/health", timeout=120)
        print(f"Awake (HTTP {r.status_code}). Starting {args.trials} trial(s).")
    except Exception as e:  # noqa: BLE001
        print(f"Warm-up notice: {e}")

    trials = []
    for n in range(1, args.trials + 1):
        trials.append(run_trial(n))
        if n < args.trials:
            print(f"\nWaiting {args.pause:.0f} seconds before the next trial...")
            time.sleep(args.pause)

    path = write_report(trials, args.label)
    print(f"\nWrote {path.relative_to(ROOT)}")
    print("Next: copy each trial's log lines from Render's Logs tab into that file,")
    print("then fill the table and commit it the same session.")


if __name__ == "__main__":
    main()
