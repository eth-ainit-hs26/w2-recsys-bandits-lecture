# CLAUDE.md : colab/three-portraits, the weekend 2 Colab notebook

"Three portraits of a product", a Colab notebook for weekend 2 of AI in Industry HS26
(13 and 14 November 2026, "Representation Learning"), built on 2026-11-02 and 2026-11-03. The
audience is managers with little formal maths: every step is a form cell with a plain title, the
code hides behind *Show code*, and the prose sits in markdown cells between the steps.

It builds three embeddings of the same 25,612 products and compares them:

1. Portrait 1, from the description: `all-MiniLM-L6-v2` (Sentence Transformers), 384 numbers.
2. Portrait 2, from behaviour: a two-tower model in the style of YouTube (Covington et al.,
   RecSys 2016). One shared table of 64 numbers per product, the customer vector is a Linear layer
   on the masked mean of the last 20 products, trained with full-softmax cross-entropy, 10 passes.
3. Portrait 3, semantic IDs: hierarchical k-means on portrait 1 (64 aisles, shelves of about nine,
   the place on the shelf by popularity), and a small causal Transformer, the "code writer"
   (d=128, 3 layers, 4 heads), that writes the next address; constrained beam search (beam 50)
   over addresses that exist.

Then a scoreboard (hit rate at 10 on 10,000 random customers, the last review of each customer
hidden), the same split by bestsellers and niche products, a cold-start cell and a "be the
customer" cell.

## Files

| File | What it is |
|---|---|
| `build_notebook.py` | The generator. **Edit this, never the notebook.** Every cell is an `md()` or `code()` call. |
| `three-portraits.ipynb` | Built by the generator, without outputs. This is what participants open. |

Build and check:

```bash
python3 -I build_notebook.py three-portraits.ipynb
python3 -I build_notebook.py test.ipynb code   # a test copy: code cells only, plus a digest cell
```

The test copy appends a cell that prints an md5 fingerprint of the code and every output as text
(it reads the notebook back through `google.colab._message.blocking_request("get_ipynb")`). It was
needed when the notebook had to be copied into Drive by hand; with the upload route below it is
optional.

Participants open it from GitHub:
`https://colab.research.google.com/github/eth-ainit-hs26/w2-recsys-bandits-lecture/blob/main/colab/three-portraits/three-portraits.ipynb`

## Data

Amazon Reviews 2023 (McAuley Lab, UC San Diego; Hou et al., ACL 2026), category Video Games,
"5-core" version, downloaded by the notebook itself from
`https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023`:
`/benchmark/5core/rating_only/Video_Games.csv.gz` (12.8 MB) and
`/raw/meta_categories/meta_Video_Games.jsonl.gz` (103 MB). Both answer plain HTTP without a login.
94,762 customers, 25,612 products, 814,586 reviews, written 1999 to 2023. A review stands in for a
purchase; the notebook says so.

## How it was tested, and how to test it again

**Do not run it locally**: Carlos's machine has no GPU. Test on his Colab Pro account,
ccarlos@ethz.ch, in his own Chrome through the Claude in Chrome extension. He is signed in there,
and the built-in browser pane has no sign-in of his. The route that works:

1. Build the notebook into this folder. The extension uploads only files from the session's
   working folders, and the scratchpad lies outside them.
2. In Colab, *File > Upload notebook*, then `file_upload` on the dialog's file input. Colab saves
   the copy in the ETH account's Drive and opens it with a T4, because the notebook's metadata asks
   for one.
3. *Run all*. Read the outputs as text with JavaScript in the page:
   `colab.global.notebookModel.cells[k].toJson()` returns a cell with its outputs. The extension
   refuses to return text that looks like a query string, so replace `=`, `&` and `?` before
   returning it. Look at the charts with zoomed screenshots.
4. Delete the runtime afterwards (*Runtime > Disconnect and delete runtime*): it uses his compute
   units.

To try a change on a live runtime without rebuilding, type a one-line cell
`exec(__import__("base64").b64decode("...").decode())`. Typing several lines into Colab's editor
breaks the indentation.

The Drive connector of these sessions runs as c.m.cotrini@gmail.com and cannot update a file's
content, and a notebook created through it must be transcribed by hand. Use the upload route.

## Results of the test runs (Colab Pro, Tesla T4)

Run of 2026-11-03, first version (two-tower trained 6 passes), 7.0 minutes in all:

| Method | Hit rate at 10, 10,000 customers | Next purchase a bestseller (3,373) | Niche (6,627) |
|---|---|---|---|
| Bestsellers | 2.5 | 7.4 | 0.0 |
| Portrait 1, description | 2.2 | 2.5 | 2.0 |
| Portrait 2, two-tower | 7.4 | 17.3 | 2.3 |
| Portrait 3, code writer | 7.2 | 17.9 | 1.8 |

Second run, same day, the committed code (two-tower trained 10 passes, duplicate names skipped, labels
placed without overlaps), 7.4 minutes in all, no errors or warnings:

| Method | Hit rate at 10, 10,000 customers | Next purchase a bestseller (3,373) | Niche (6,627) |
|---|---|---|---|
| Bestsellers | 2.5 | 7.4 | 0.0 |
| Portrait 1, description | 2.2 | 2.5 | 2.0 |
| Portrait 2, two-tower | 7.7 | 17.2 | 2.9 |
| Portrait 3, code writer | 7.4 | 18.1 | 1.9 |

After that run only four markdown cells changed (the "What to notice" notes and the industry
section), so the committed code cells are byte for byte the ones that ran. The executed copy, with
all outputs, is `three-portraits.ipynb` in the Drive of ccarlos@ethz.ch (Colab file id
`1dXrhsPOilW_ARyML8Gr7Mc7oVxNpeKx8`). The first test copy, code only, is in the Drive folder "AINIT HS26
weekend 2 notebook drafts" of c.m.cotrini@gmail.com, shared with the ETH account.

The 95% range of each overall rate is about plus or minus 0.5, so portraits 2 and 3 tie. GPU runs are
not bit for bit reproducible: the markdown cells quote rounded numbers ("2 to 3 in 100", "about
three times as often"), and they must be checked again after any change to a model.

## Gotchas

- **Portrait 2's neighbours are complements.** For the DualShock 4 controller they are headsets
  and PC games (PC players use that controller), for a Switch game a screen protector and a gift
  card. That is behaviour, and the notebook now teaches it ("similar items" against "customers also
  bought"). On 2026-11-03 three changes were tried on a live runtime and none helped: a popularity
  number per product (hit rate 7.7 after 10 passes, the neighbours unchanged), centring the vectors,
  and separate tables for the history and the product (hit rate 7.2). Measured as the share of the 10
  nearest neighbours in the same console family, over the 2,000 most reviewed products: portrait 1
  82%, every portrait 2 variant 54 to 64%.
- The bestsellers sit close together near the middle of the portrait 2 map, so the map labels the six
  circled products with a small placement routine (`label()` in the maps cell) that avoids overlaps.
- `find()` ignores capitals and accents. Product names say "Pokémon"; without that, "Pokemon" found a
  controller.
- Amazon lists some products twice under the same name; `closest()` skips copies of the query.
- Colab displays the value of a cell's last expression: `writer.eval()` printed the whole
  Transformer until it became `writer = writer.eval()`.
- The Hugging Face hub prints a notice about downloading without an account; the portrait 1 cell
  silences it with `hub_logging.set_verbosity_error()`.
- The industry section quotes HSTU (1.5 trillion parameters, +12.4% in online A/B tests, ICML 2024),
  OneRec (about 25% of the requests in the main scenes of the Kuaishou apps, technical report 2025)
  and PLUM (WWW 2026). Check them again before reusing them elsewhere.

## Maintenance contract

- This file is the working memory for this folder. After any major change here, meaning a new or
  removed cell, a changed model or dataset, a changed build or test procedure, or new measured
  results, UPDATE THIS FILE IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself
  carry this same maintenance contract, including this propagation rule. When you create a
  subdirectory, create its CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost
  someone an hour. Do not restate what the code already says plainly.
