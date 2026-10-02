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

---

## 5. Search respects a price ceiling 

Given a query with an explicit price limit (e.g. 'under $30'), every item returned 
in `session["search_results"]` costs less than or equal to that price limit - 5 of 5 tries. 

**Why this target:** Filtering listings by price is deterministic code that compares the listings' price against the `max_price`, so it should return the listings correctly every time based on the price ceiling set. 

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 4 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 4. Something about the fit card

         The fit card is different every time.

         **Why this target:** ...

         > **Revised in unit 4:** For 5 different items, the 5 fit cards share
         > no opening sentence.
         >
         > **Why revised:** "different" wasn't checkable — two cards that
         > differed by one word still counted. The new version is something I
         > can actually score.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said the empty search stops it 5 of 5 times, but I got 3 of 5,
            so 3 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
