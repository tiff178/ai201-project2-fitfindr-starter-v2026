# FitFindr

# Unit 3

## What This Does

Fitfindr is a three-tool agent that finds thrifted clothing listings matching your search description, size, and/or price budget. It suggests complete outfit ideas using items from your existing wardrobe and generates a short, social-media-style caption with the item's price and platform.

To begin: `python app.py ask '...'` (e.g. python app.py ask '90s track jacket in size M)

---

## Tool Inventory

### `search_listings`

- **What it does:** Searches the local clothing catalogue by description keywords, with optional size and maximum-price filters; size matching uses whole tokens and the price limit is inclusive 
- **Inputs:** description: str, size: str | None = None, max_price: float | None = None
- **Returns:** A list of matching listing dictionaries, ranked by keyword match and then lower price; each includes fields such as id, title, description, category, style_tags, size, condition, price, colors, brand, and platform
- **When it has nothing:** Returns an empty list [], not None or an exception   

### `suggest_outfit`

- **What it does:** Suggests two outfits built around a selected listing, using items from the user's wardrobe when available
- **Inputs:** new_item: dict (a listing), wardrobe: dict (with an items list)
- **Returns:** A non-empty str with two outfit suggestions; when the wardrobe has items, it names those pieces as written
- **When it has nothing:** Still returns general outfit ideas and says they are general because no wardrobe is saved 

### `create_fit_card`

- **What it does:** Writes a short social-media-style caption about the selected second-hand find and how it could be worn
- **Inputs:** outfit: str, new_item: dict (a listing)
- **Returns:** A str of two to four sentences that includes the price written with digits and the selling platform
- **When it has nothing:** If outfit is empty or whitespace, returns a helpful fallback message instead of calling the model or raising an exception. 

---

## Planning Loop

**Branch rule:** If `search_listings` return an empty list [], call `agent.py::_nothing_found_message` to put a message in `session["error"]` stating what the user could change and return the session without calling `suggest_outfit` or `create_fit_card`. Otherwise take the first result, put it in `session["selected_item"]`, and continue. 

**Where it lives:** `agent.py::run_agent` | `agent.py::_nothing_found_message` for empty-case message

**How the query is parsed:** The query is parsed through regex in `agent.py::parse_query` for consistent inputs rather than raw text. 

**What moves through the session:** `search_listings` writes to `session["search_results"]`; then reads `session["search_results"][0]` back out and writes to `session["selected_item"]`; `suggest_outfit` is called with that. 

---

## Sample Run

**One full query**

```
$ python app.py ask 'vintage graphic tee under $30'

  Found:    Y2K Baby Tee — Butterfly Print — $18.0 on depop

  Outfit:   Here are two outfit ideas that combine the Y2K butterfly baby tee with pieces already in their wardrobe:

### Outfit 1: Streetwear Contrast (Y2K Meets Denim)
This look leans into the vintage Y2K aesthetic by balancing the fitted, feminine crop top with structured, baggy bottoms. 
* **Top:** The new **Y2K Baby Tee** (Butterfly Print)
* **Bottoms:** **Baggy straight-leg jeans** (dark wash)
* **Outerwear:** **Vintage black denim jacket** (slightly cropped)
* **Shoes:** **Chunky white sneakers**
* **Accessories:** **Black crossbody bag**

*Why it works:* The fitted crop of the baby tee pairs naturally with high-waisted, baggy jeans to create a flattering proportion play. Throwing the slightly cropped black denim jacket on top ties the look together, while the chunky white sneakers and crossbody bag keep the streetwear vibe grounded and casual.

---

### Outfit 2: Casual Earth-Tone Mix (Eclectic Casual)
This outfit takes the pink, purple, and white butterfly graphic and uses it to add a pop of color and playful energy to a more neutral, relaxed bottom.
* **Top:** The new **Y2K Baby Tee** (Butterfly Print)
* **Bottoms:** **Wide-leg khaki trousers**
* **Shoes:** **Chunky white sneakers**
* **Accessories:** **Brown leather belt** and **Black crossbody bag**

*Why it works:* The khaki trousers bring a minimal, earth-tone balance that tones down the sweetness of the butterfly graphic, making the outfit feel effortless and cool rather than overly costume-y. Tucking the baby tee in and adding the brown leather belt adds definition at the waist, while the white sneakers tie in the white base of the shirt.

  Fit card: scored this y2k butterfly baby tee on depop for just $18 and i am officially obsessed 🦋✨ can’t wait to style this all summer long!

```

**The three tools, tested one at a time**

```
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"

[{'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.', 'category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_017', 'title':'Mesh Long-Sleeve Top — Black', 'description': 'Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.', 'category': 'tops', 'style_tags': ['y2k', 'grunge', 'goth', 'layering'], 'size': 'S/M', 'condition': 'excellent', 'price': 15.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie —Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'}]

```

```
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"

Here are two specific outfit suggestions combining the vintage Levi's 501s with pieces from your existing wardrobe:

### Outfit 1: Casual Streetwear Classic
* **Top:** White ribbed tank top
* **Outerwear:** Vintage black denim jacket (worn over the tank)
* **Bottoms:** Vintage Levi's 501 Jeans (new item)
* **Shoes:** Chunky white sneakers
* **Accessories:** Black crossbody bag 

**Why it works:** This is an effortless, timeless pairing. The fitted white tank balances the straight-leg cut of the 501s, while the slightly cropped black denim jacket adds a cool double-denim edge without looking too heavy. Finished with chunky white sneakers and your everyday black bag, it’s an ideal, foolproof everyday outfit.

---

### Outfit 2: Laid-Back Grunge & Contrast
* **Top:** Black cropped zip hoodie
* **Bottoms:** Vintage Levi's 501 Jeans (new item)
* **Shoes:** Black combat boots
* **Accessories:** Brown leather belt, Black crossbody bag

**Why it works:** The medium-wash 501s provide a great vintage contrast against the darker tones of the black hoodie and combat boots. Tucking the front of the hoodie slightly (or letting the crop sit right at the waistband) highlights the jeans' classic rise, while adding the brown leather belt pulls in a subtle textural contrast with the boots and hardware.

```

```
$ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"

Scored these vintage Levi's 501s on Depop for just $38 and I am never taking them off. Honestly, nothing beats the fade on a real broken-in pair of denim. Just throwing them on with some fresh white sneakers and calling it a day!

```

---

## How I Used AI

**Moment 1**

- *What I asked for:* "Here are five acceptance criteria for a multi-tool agent. For each one, tell me exactly how you would test it using only what the sentence says. Don't suggest improvements — just tell me what you'd do." (with my five acceptance criteria included)
- *What came back:* Claude described how it would test each criteria, using only the wording given - no instrumentation or changes beyond what's needed to observe the stated behavior.
- *What I changed:* As Claude was able to describe a test for each of them, there was no major changes needed to be made on my criteria. Therefore, I just refined my acceptance criteria by making sure it had named a clear target (such as count/number, etc.). 

**Moment 2**

- *What I asked for:* I gave Claude my `search_listings` spec to help me as a starting point to work on the code (same as with `suggest_outfit` and `create_fit_card`). 
- *What came back:* Claude provided the code as a starting point and I read through each line to see what I had to fix. 
- *What I changed:* Specifically for `search_listings`, I had to adjust the code to match case-insensitively for the size - "M" should match "S/M."

<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.

     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |  |  |
| 2.  |  |  |  |  |  |  |  |
| 3.  |  |  |  |  |  |  |  |
| 4.  |  |  |  |  |  |  |  |
| 5.  |  |  |  |  |  |  |  |

**Real output from one try**, pasted as text, naming the file and function
that produced it:

```

```

---

## Verdicts and Diagnoses

<!-- MET or MISSED per criterion against LAST UNIT's target, plus a sentence on
     how you decided.

     Then, for every miss: which of the four places it happened — a tool, the
     loop's branch, the session, or the model's output — AND the mechanism.

     Not a diagnosis:  "The fit card was bad."
     A diagnosis:      "The fit card criterion missed on 2 of 5 items. Both had
                        an empty brand field. My prompt puts the brand in the
                        first sentence, so the card opened with a blank and read
                        like a fragment. The tool worked; the prompt assumed a
                        field that isn't always there."

     Look for a pattern. Three misses on the same tool is one problem, not
     three. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**



---

## Loop Trace

<!-- One full run, printed step by step, with the MCP call visible in it.

     `python app.py ask '...' --trace` once you've added the trace.step()
     calls in Milestone 2.

     Worth pasting BOTH the happy path and the empty-search path. The empty
     one should be visibly shorter, because it stops. If your two traces are
     the same length, your branch isn't working — and this is the fastest way
     anyone will ever find that out. -->

**Happy path**

```

```

**Empty search**

```

```

**On the MCP move:** <!-- what changed in your code, and whether anything
behaved differently afterwards. If the rewire didn't work, say exactly where it
broke — the error text and the last thing that worked. That earns the point in
full. -->



---

## The Improvement

<!-- What you changed, why your diagnosis pointed at it, and the after-run in
     the same table format. One change, measured properly.

     `python run_eval.py --label after` -->

**What I changed:**

**Which failure it was meant to fix:**

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |  |  |
| 2.  |  |  |  |  |  |  |  |
| 3.  |  |  |  |  |  |  |  |
| 4.  |  |  |  |  |  |  |  |
| 5.  |  |  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it made things worse, say that. Honestly reported, that earns full
     credit and is more interesting than one that worked. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped where
     you did. "I ran out of time" is fine if it's true. Pretending nothing is
     left is not. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
