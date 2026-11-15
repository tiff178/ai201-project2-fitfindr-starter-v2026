# Capstone run log - after

- Produced by: `run_render.py` (requests) and `serve.py::_log_request` (log lines)
- Service: https://fitfindr-p6is.onrender.com
- When: 2026-11-14 22:20
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
{"timestamp": "2026-11-15T06:18:06.609189+00:00", "request_id": "d898b661", "query": "vintage graphic tee under $30", "status": "ok", "error": null, "selected_item": "Y2K Baby Tee — Butterfly Print", "latency_ms": 22114, "queue_wait_ms": 0, "run_ms": 22113, "model_calls": 2, "prompt_tokens": 803, "output_tokens": 319, "cache_enabled": true}
{"timestamp": "2026-11-15T06:18:16.084385+00:00", "request_id": "a8b912ba", "query": "vintage blazer in size L", "status": "ok", "error": null, "selected_item": "Vintage Linen Blazer — Cream", "latency_ms": 7701, "queue_wait_ms": 0, "run_ms": 7701, "model_calls": 2, "prompt_tokens": 920, "output_tokens": 454, "cache_enabled": true}
{"timestamp": "2026-11-15T06:18:24.499963+00:00", "request_id": "1b8e8aaf", "query": "platform sneakers in size 8", "status": "ok", "error": null, "selected_item": "Platform Sneakers — White Chunky Sole", "latency_ms": 6876, "queue_wait_ms": 0, "run_ms": 6876, "model_calls": 2, "prompt_tokens": 864, "output_tokens": 375, "cache_enabled": true}
{"timestamp": "2026-11-15T06:18:32.578235+00:00", "request_id": "5acda4c8", "query": "cozy oversized cardigan", "status": "ok", "error": null, "selected_item": "Knit Cardigan — Chunky Brown", "latency_ms": 6552, "queue_wait_ms": 0, "run_ms": 6551, "model_calls": 2, "prompt_tokens": 874, "output_tokens": 391, "cache_enabled": true}
{"timestamp": "2026-11-15T06:18:41.555152+00:00", "request_id": "e69b8875", "query": "long sleeve in size L under $40", "status": "ok", "error": null, "selected_item": "Tie-Dye Long Sleeve — Pastel", "latency_ms": 7316, "queue_wait_ms": 0, "run_ms": 7316, "model_calls": 2, "prompt_tokens": 741, "output_tokens": 256, "cache_enabled": true}
{"timestamp": "2026-11-15T06:18:43.095575+00:00", "request_id": "a48a73e5", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:18:43.660057+00:00", "request_id": "d98626d3", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:18:44.326360+00:00", "request_id": "6cf4ec3f", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:18:44.831217+00:00", "request_id": "1193896a", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:18:45.391891+00:00", "request_id": "c7dec22e", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
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
{"timestamp": "2026-11-15T06:18:55.511714+00:00", "request_id": "5795d3d9", "query": "vintage graphic tee under $30", "status": "ok", "error": null, "selected_item": "Y2K Baby Tee — Butterfly Print", "latency_ms": 4412, "queue_wait_ms": 0, "run_ms": 4412, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:19:01.708146+00:00", "request_id": "3a2ebcba", "query": "vintage blazer in size L", "status": "ok", "error": null, "selected_item": "Vintage Linen Blazer — Cream", "latency_ms": 4649, "queue_wait_ms": 0, "run_ms": 4648, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:19:07.903615+00:00", "request_id": "2cafc6f5", "query": "platform sneakers in size 8", "status": "ok", "error": null, "selected_item": "Platform Sneakers — White Chunky Sole", "latency_ms": 4573, "queue_wait_ms": 0, "run_ms": 4573, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:19:13.912604+00:00", "request_id": "b33b0d9c", "query": "cozy oversized cardigan", "status": "ok", "error": null, "selected_item": "Knit Cardigan — Chunky Brown", "latency_ms": 4578, "queue_wait_ms": 0, "run_ms": 4578, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:19:20.406900+00:00", "request_id": "7cafa056", "query": "long sleeve in size L under $40", "status": "ok", "error": null, "selected_item": "Tie-Dye Long Sleeve — Pastel", "latency_ms": 4889, "queue_wait_ms": 0, "run_ms": 4889, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:19:21.924425+00:00", "request_id": "fd3c2150", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:19:22.387608+00:00", "request_id": "97d13d56", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:19:22.971698+00:00", "request_id": "6a636e7d", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:19:23.498592+00:00", "request_id": "d670a4ea", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:19:23.935801+00:00", "request_id": "d9fbd6e5", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
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
{"timestamp": "2026-11-15T06:19:33.906727+00:00", "request_id": "abb37338", "query": "vintage graphic tee under $30", "status": "ok", "error": null, "selected_item": "Y2K Baby Tee — Butterfly Print", "latency_ms": 4278, "queue_wait_ms": 0, "run_ms": 4278, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:19:40.407328+00:00", "request_id": "7990e977", "query": "vintage blazer in size L", "status": "ok", "error": null, "selected_item": "Vintage Linen Blazer — Cream", "latency_ms": 4916, "queue_wait_ms": 0, "run_ms": 4915, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:19:46.607781+00:00", "request_id": "1f15684b", "query": "platform sneakers in size 8", "status": "ok", "error": null, "selected_item": "Platform Sneakers — White Chunky Sole", "latency_ms": 4188, "queue_wait_ms": 0, "run_ms": 4188, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:19:52.810204+00:00", "request_id": "c22589d1", "query": "cozy oversized cardigan", "status": "ok", "error": null, "selected_item": "Knit Cardigan — Chunky Brown", "latency_ms": 4297, "queue_wait_ms": 0, "run_ms": 4297, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:19:58.810129+00:00", "request_id": "9755e694", "query": "long sleeve in size L under $40", "status": "ok", "error": null, "selected_item": "Tie-Dye Long Sleeve — Pastel", "latency_ms": 4299, "queue_wait_ms": 0, "run_ms": 4299, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "cache_enabled": true}
{"timestamp": "2026-11-15T06:20:00.346394+00:00", "request_id": "1119d607", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:20:01.263824+00:00", "request_id": "49dd2f84", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:20:01.988848+00:00", "request_id": "22660cb0", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:20:02.562653+00:00", "request_id": "31bd6d0d", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
{"timestamp": "2026-11-15T06:20:03.267429+00:00", "request_id": "7909afce", "query": "", "status": "bad_request", "error": "missing 'query' field", "latency_ms": 0, "queue_wait_ms": 0}
```