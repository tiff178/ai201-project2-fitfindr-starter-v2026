# Acceptance criteria — FitFindr

Five criteria that say what "working" means for this agent, written in unit 3
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"The agent handles errors"* is an opinion.
*"When search returns nothing, the agent stops before calling the second tool,
in 5 of 5 tries"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter one. A reason that says something about your tools, your loop, or the
data earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

**Two are written for you. You write three.**

---

## 1. A matching query completes all three tools

Given a query that matches at least one listing, the agent completes all three
tool calls and returns a fit card — in at least 4 of 5 tries.

**Why this target:** Search relies on keyword matching against user input, which can occasionally miss a valid match depending on exact query phrasing. A 4 of 5 target ensures the multi-tool workflow executes consistently without over-penalizing natural language variation. 

---

## 2. An impossible query stops before the second tool

Given a query that matches no listings, the agent stops before calling
`suggest_outfit` and returns a message naming what to change — 5 of 5 tries.

**Why this target:** Unlike keyword matching, `search_listings` returning an empty list [] is a deterministic check. A 5 of 5 target ensures the agent stops before invoking downstream tools on empty data. 

---

## 3. State passes to second tool without changes

Given a query that matches at least one listing, the exact item stored in 
`session["selected_item"]` matches the selected item received by `suggest_outfit` - 5 of 5 tries. 

**Why this target:** Passing the exact item stored in session state to the second tool is deterministic. After `search_listings` returns a listing and is stored in `session["selected_item"]`, `suggest_outfit` should have that same selected item every time. 

---

## 4. Fit card caption is concise and contains required metadata

Given a valid outfit suggestion and item, `create_fit_card` returns a caption between 20-50 words 
that explicitly contain the item price (in digits) and the selling platform - in at least 4 of 5 tries. 

**Why this target:** As `create_fit_card` calls the model, temperature variations can cause slight differences in phrasing and output length across runs. A 4 of 5 target accounts for minor model generation variance while ensuring core metadata requirements and length limits are consistently met. 

**Update**: The 20-50 word limit doesn't test the real requirement. The spec in `tools.py::create_fit_card` asks for a two-to-four sentence caption, so a better criterion is *the caption contains 2-4 sentences* (alongside the price and platform check). The function doesn't currently verify this, so a future improvement is to count sentences and retry or trim if the result falls outside that range. 

- Given a valid outfit suggestion and item, `create_fit_card` returns a two-to-four sentence caption that explicitly contain the item price (in digits) and the selling platform - in at least 4 of 5 tries. 

---

## 5. Search respects a price ceiling 

Given a query with an explicit price limit (e.g. 'under $30'), every item returned 
in `session["search_results"]` costs less than or equal to that price limit - 5 of 5 tries. 

**Why this target:** Filtering listings by price is deterministic code that compares the listings' price against the `max_price`, so it should return the listings correctly every time based on the price ceiling set. 

---

# Acceptance criteria — FitFindr (Capstone - Unit 9)

---

## 1. Token consumption per run stays within budget

Given a valid POST request sent to `/ask` that returns a recommendation (`selected_item`), the total token consumption recorded in the structured log (`prompt_tokens` and `output_tokens`) does not exceed 1,300 tokens - 4 of 5 tries. 

**Why this target:** A successful run executes two model calls (`suggest_outfit` and `create_fit_card`), which averaged ~1,207 total tokens across 10 runs. Setting a 1,300-token ceiling ensures prompt context and outputs remain tight and predictable, while the 4 of 5 target accommodates natural variance.

---

## 2. Bad request rejects missing query without running the agent

Given a POST request sent to `/ask` with a missing or empty `query` field, the service returns an HTTP 400 status with an `error` message, and logs `status: "bad_request"` and no `run_ms` (the agent never ran) — 5 of 5 tries.

**Why this target:** Input validation at the HTTP boundary is deterministic. Malformed requests should fail immediately with an HTTP 400 rather than crashing the server with a 500 or wasting LLM API tokens and compute on empty inputs.

---

## 3. Every request produces a structured log record

Given any POST request sent to `/ask` (successful or failed), exactly one JSON log line is emitted containing the core lifecycle fields (`timestamp`, `request_id`, `status`, and `latency_ms`) — 5 of 5 tries.

**Why this target:** The logging mechanism in `serve.py::_log_request` flushes a structured JSON record for every request before returning an HTTP response. Whether the request succeeds or fails early at the HTTP boundary, a structured audit log must always be created.

---

## 4. Warm request execution latency completes under 10 seconds

Given a valid POST request sent to `/ask` on a warm deployed Render instance (defined as a request sent within 5 minutes of a previous request, excluding cold-start container wakeups), the agent execution duration (`run_ms`) completes in under 10,000 ms (10.0 seconds) — 4 of 5 tries.

**Why this target:** Warm request execution latency averages ~7.5 seconds, so a 10-second ceiling accommodates normal external API latency jitter while keeping the service responsive. Defining "warm" as within 5 minutes ensures the free Render instance has not spun down or entered sleep mode. 

---

## 5. Model failure returns readable error and logs error status

Given a valid POST request sent to `/ask` when a model call fails (e.g. wrong `GEMINI_API_KEY`), the service returns a readable error message in the response instead of crashing, and logs `status: "error"` - 5 of 5 tries. 

**Why this target:** A production web service must isolate third-party dependency failures gracefully. If an external API is down or credentials fail, the server should return an error response and record `status: "error"` for alerting, rather than letting an unhandled exception crash.

**Update:** A valid POST request was ambiguous. A query like `t-shirt under $25` is a request that matches no listing, so the agent stops at the empty-search branch and never reaches the model. A request that cannot reach the model, cannot test model failure. Therefore, the verdict was MISSED and requires a clearer criteria. 

- Given a valid POST request that matches at least one listing sent to `/ask` when a model call fails (e.g. wrong `GEMINI_API_KEY`), the service returns a readable error message in the response instead of crashing, and logs `status: "error"` - 5 of 5 tries. 

---