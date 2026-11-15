# Capstone run log - before

- Produced by: `run_render.py` (requests) and `serve.py::_log_request` (log lines)
- Service: https://fitfindr-p6is.onrender.com
- When: 2026-11-14 19:24
- Log lines: copied by hand from Render's Logs tab (see the blocks below)

Fill the Run columns and the Verdict from `criteria.md` after you inspect the
client results and paste the structured log lines.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|:---:|:---:|:---:|:---:|:---:|
| 1. Token consumption per run stays within budget (<= 1,300 tokens) | 4 of 5 |   |   |   |  |
| 2. Bad request rejects missing query without running the agent | 5 of 5 |   |   |   |  |
| 3. Every request produces a structured log record | 5 of 5 |   |   |   |  |
| 4. Warm request execution latency completes under 10 seconds | 4 of 5 |   |   |   |  |
| 5. Model failure returns readable error and logs error status | 5 of 5 |   |   |   |  |

---

## Trial 1

Client-side: valid 5/5 answered with HTTP 200 and all fields, bad 5/5 rejected with HTTP 400 and an error.

| # | kind | request | HTTP | response ok |
|---|---|---|---|---|
| 1 | valid | vintage graphic tee under $30 | 200 | True |
| 2 | valid | vintage blazer in size L | 200 | True |
| 3 | valid | platform sneakers in size 8 | 200 | True |
| 4 | valid | cozy oversized cardigan | 200 | True |
| 5 | valid | long sleeve in size L under $40 | 200 | True |
| 6 | bad | {} | 400 | True |
| 7 | bad | {'query': ''} | 400 | True |
| 8 | bad | {'query': '   '} | 400 | True |
| 9 | bad | {'': 'leather jacket'} | 400 | True |
| 10 | bad | {'query': ''} | 400 | True |

Render log lines for trial 1 (paste the 10 JSON lines here, unedited):

```json
{"timestamp": "2026-11-15T03:22:56.307002+00:00", "request_id": "3a847ea7", "query": "vintage graphic tee under $30", "status": "ok", "error": null, "selected_item": "Y2K Baby Tee — Butterfly Print", "latency_ms": 4302, "queue_wait_ms": 0, "run_ms": 4302, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:02.409264+00:00", "request_id": "afc5b258", "query": "vintage blazer in size L", "status": "ok", "error": null, "selected_item": "Vintage Linen Blazer — Cream", "latency_ms": 4499, "queue_wait_ms": 0, "run_ms": 4499, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:08.914864+00:00", "request_id": "f2b49ca3", "query": "platform sneakers in size 8", "status": "ok", "error": null, "selected_item": "Platform Sneakers — White Chunky Sole", "latency_ms": 4967, "queue_wait_ms": 0, "run_ms": 4967, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:14.809547+00:00", "request_id": "805e7ed8", "query": "cozy oversized cardigan", "status": "ok", "error": null, "selected_item": "Knit Cardigan — Chunky Brown", "latency_ms": 4231, "queue_wait_ms": 0, "run_ms": 4231, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:20.609598+00:00", "request_id": "3724e2f6", "query": "long sleeve in size L under $40", "status": "ok", "error": null, "selected_item": "Tie-Dye Long Sleeve — Pastel", "latency_ms": 4197, "queue_wait_ms": 0, "run_ms": 4196, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:22.167431+00:00", "request_id": "2af2be8d", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:23:22.634309+00:00", "request_id": "70a74b9c", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:23:23.080346+00:00", "request_id": "fd8ef38a", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:23:23.588396+00:00", "request_id": "8f4b915e", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:23:24.045546+00:00", "request_id": "73ae71b9", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
```

## Trial 2

Client-side: valid 5/5 answered with HTTP 200 and all fields, bad 5/5 rejected with HTTP 400 and an error.

| # | kind | request | HTTP | response ok |
|---|---|---|---|---|
| 1 | valid | vintage graphic tee under $30 | 200 | True |
| 2 | valid | vintage blazer in size L | 200 | True |
| 3 | valid | platform sneakers in size 8 | 200 | True |
| 4 | valid | cozy oversized cardigan | 200 | True |
| 5 | valid | long sleeve in size L under $40 | 200 | True |
| 6 | bad | {} | 400 | True |
| 7 | bad | {'query': ''} | 400 | True |
| 8 | bad | {'query': '   '} | 400 | True |
| 9 | bad | {'': 'leather jacket'} | 400 | True |
| 10 | bad | {'query': ''} | 400 | True |

Render log lines for trial 2 (paste the 10 JSON lines here, unedited):

```json
{"timestamp": "2026-11-15T03:23:33.805329+00:00", "request_id": "6b6b3639", "query": "vintage graphic tee under $30", "status": "ok", "error": null, "selected_item": "Y2K Baby Tee — Butterfly Print", "latency_ms": 4297, "queue_wait_ms": 0, "run_ms": 4297, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:39.603530+00:00", "request_id": "bb847de5", "query": "vintage blazer in size L", "status": "ok", "error": null, "selected_item": "Vintage Linen Blazer — Cream", "latency_ms": 4240, "queue_wait_ms": 0, "run_ms": 4240, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:45.506725+00:00", "request_id": "3777007d", "query": "platform sneakers in size 8", "status": "ok", "error": null, "selected_item": "Platform Sneakers — White Chunky Sole", "latency_ms": 4379, "queue_wait_ms": 0, "run_ms": 4379, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:51.211877+00:00", "request_id": "5f413923", "query": "cozy oversized cardigan", "status": "ok", "error": null, "selected_item": "Knit Cardigan — Chunky Brown", "latency_ms": 4149, "queue_wait_ms": 0, "run_ms": 4148, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:57.409541+00:00", "request_id": "d1015652", "query": "long sleeve in size L under $40", "status": "ok", "error": null, "selected_item": "Tie-Dye Long Sleeve — Pastel", "latency_ms": 4648, "queue_wait_ms": 0, "run_ms": 4647, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:23:58.873669+00:00", "request_id": "c9d49759", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:23:59.313548+00:00", "request_id": "0189883c", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:23:59.728226+00:00", "request_id": "0c1cddb8", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:24:00.156838+00:00", "request_id": "3bd9724c", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:24:00.649673+00:00", "request_id": "5f30cd79", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
```

## Trial 3

Client-side: valid 5/5 answered with HTTP 200 and all fields, bad 5/5 rejected with HTTP 400 and an error.

| # | kind | request | HTTP | response ok |
|---|---|---|---|---|
| 1 | valid | vintage graphic tee under $30 | 200 | True |
| 2 | valid | vintage blazer in size L | 200 | True |
| 3 | valid | platform sneakers in size 8 | 200 | True |
| 4 | valid | cozy oversized cardigan | 200 | True |
| 5 | valid | long sleeve in size L under $40 | 200 | True |
| 6 | bad | {} | 400 | True |
| 7 | bad | {'query': ''} | 400 | True |
| 8 | bad | {'query': '   '} | 400 | True |
| 9 | bad | {'': 'leather jacket'} | 400 | True |
| 10 | bad | {'query': ''} | 400 | True |

Render log lines for trial 3 (paste the 10 JSON lines here, unedited):

```json
{"timestamp": "2026-11-15T03:24:11.603035+00:00", "request_id": "4113d16e", "query": "vintage graphic tee under $30", "status": "ok", "error": null, "selected_item": "Y2K Baby Tee — Butterfly Print", "latency_ms": 5455, "queue_wait_ms": 0, "run_ms": 5455, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:24:18.103541+00:00", "request_id": "128c2d6b", "query": "vintage blazer in size L", "status": "ok", "error": null, "selected_item": "Vintage Linen Blazer — Cream", "latency_ms": 4639, "queue_wait_ms": 0, "run_ms": 4639, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:24:24.308852+00:00", "request_id": "43460d77", "query": "platform sneakers in size 8", "status": "ok", "error": null, "selected_item": "Platform Sneakers — White Chunky Sole", "latency_ms": 4469, "queue_wait_ms": 0, "run_ms": 4469, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:24:30.807191+00:00", "request_id": "75e064df", "query": "cozy oversized cardigan", "status": "ok", "error": null, "selected_item": "Knit Cardigan — Chunky Brown", "latency_ms": 4823, "queue_wait_ms": 0, "run_ms": 4823, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:24:37.207738+00:00", "request_id": "da13c59b", "query": "long sleeve in size L under $40", "status": "ok", "error": null, "selected_item": "Tie-Dye Long Sleeve — Pastel", "latency_ms": 4602, "queue_wait_ms": 0, "run_ms": 4602, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T03:24:38.808030+00:00", "request_id": "c0a87dc3", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:24:39.351674+00:00", "request_id": "5c43e5c4", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:24:39.949828+00:00", "request_id": "6a7a6183", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:24:40.445444+00:00", "request_id": "e7765ca9", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T03:24:40.912351+00:00", "request_id": "875a8080", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
```