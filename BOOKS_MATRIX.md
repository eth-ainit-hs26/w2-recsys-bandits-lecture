# The books matrix — design

The protagonist of the lecture. Every viz, every slide, and every example in `NARRATIVE_PLAN.md` resolves through this object. Designed for two simultaneous goals: **maximum pedagogical truth** (the math model has to recover what we put in) and **maximum audience entertainment** (recognizable titles, characters they can identify with, designed surprises that pay off later).

---

## 1 · The 16 books

Four per quadrant, on the axes **Fiction / Nonfiction** × **Light / Demanding**. Numerical IDs (1–16) used in the rating table; short labels used everywhere else.

### Light · Fiction (LF) — *the airport-paperback corner*

| ID | Label | Title | Author | Year |
|---|---|---|---|---|
| 1 | *Potter* | Harry Potter and the Philosopher's Stone | J. K. Rowling | 1997 |
| 2 | *Christie* | Murder on the Orient Express | Agatha Christie | 1934 |
| 3 | *Hunger* | The Hunger Games | Suzanne Collins | 2008 |
| 4 | *DaVinci* | The Da Vinci Code | Dan Brown | 2003 |

### Demanding · Fiction (DF) — *the modernist canon*

| ID | Label | Title | Author | Year |
|---|---|---|---|---|
| 5 | *Ulysses* | Ulysses | James Joyce | 1922 |
| 6 | *War&Peace* | War and Peace | Leo Tolstoy | 1869 |
| 7 | *Borges* | Ficciones | Jorge Luis Borges | 1944 |
| 8 | *Lighthouse* | To the Lighthouse | Virginia Woolf | 1927 |

> *Pedagogical detail.* Borges is in the matrix on purpose. The lecture opens with his story *Funes the Memorious* (Scene 2) and closes inside his quote (Scene 27). At Scene 11 the audience will see Borges's name appear inside the very object the lecture is decoding. A small loop the alert listener will catch.

### Light · Nonfiction (LN) — *the practical shelf*

| ID | Label | Title | Author | Year |
|---|---|---|---|---|
| 9 | *EatPray* | Eat, Pray, Love | Elizabeth Gilbert | 2006 |
| 10 | *Switzerland* | Lonely Planet: Switzerland | (travel guide) | 2024 |
| 11 | *7Habits* | The 7 Habits of Highly Effective People | Stephen R. Covey | 1989 |
| 12 | *JoyCook* | The Joy of Cooking | Irma S. Rombauer | 1931 |

### Demanding · Nonfiction (DN) — *the foundational treatises*

| ID | Label | Title | Author | Year |
|---|---|---|---|---|
| 13 | *Kant* | Critique of Pure Reason | Immanuel Kant | 1781 |
| 14 | *Smith* | The Wealth of Nations | Adam Smith | 1776 |
| 15 | *Darwin* | On the Origin of Species | Charles Darwin | 1859 |
| 16 | *Russell* | A History of Western Philosophy | Bertrand Russell | 1945 |

> *Carousel anchor (Scene 11).* Russell is the anchor item for the **Customer-Urns Carousel**. Each reader's urn shows the probability they would finish *A History of Western Philosophy*. Russell is chosen because: (a) the test discriminates sharply (Scholars love it, everyone else avoids it), (b) the title is recognisable without intimidation, (c) it pairs naturally with the closing arithmetic-coding-on-text demo where a paragraph of Russell becomes the input to the Compression-Prediction Twin (Scene 25).

---

## 2 · The 4 archetypes

Each archetype is a 2-D latent vector. The two latent axes are the same as the slide axes: $x = $ Fiction (+) / Nonfiction (−), $y = $ Light (+) / Demanding (−).

| Archetype | Label | Vector $u$ | Personality |
|---|---|---|---|
| A1 | The **Commuter** | $(+1, +1)$ | reads on the train; thrillers and fantasy; flips through *7 Habits* once |
| A2 | The **Literary** | $(+1, -1)$ | rereads Joyce; lit-crit blogs; will tolerate Russell as fiction-adjacent |
| A3 | The **Practical** | $(-1, +1)$ | self-help and travel; cooks with the Rombauer open; never finishes a novel |
| A4 | The **Scholar** | $(-1, -1)$ | skips fiction entirely; underlines Kant; dips into Darwin on weekends |

The book vectors are placed at the same four corners:
- LF books (1–4): $v = (+1, +1)$
- DF books (5–8): $v = (+1, -1)$
- LN books (9–12): $v = (-1, +1)$
- DN books (13–16): $v = (-1, -1)$

> *Why identical vectors per quadrant?* So the SVD of the underlying ratings matrix has rank exactly 2. The Spectral Microscope (Scene 9) will reveal: at $k=1$ one cluster appears; at $k=2$ the four-corner geometry snaps into focus; $k>2$ adds only noise. That is Eckart–Young (Scene 10) made physical.

---

## 3 · The 21 readers

16 pure-archetype readers (4 per archetype) plus 5 *special* readers carrying the pedagogical surprises. The 22nd reader (cold-start) is introduced separately at Scene 11.

### Pure archetype readers

| ID | Name | Archetype | $u$ |
|---|---|---|---|
| R1 | Alice | A1 — Commuter | $(+1, +1)$ |
| R2 | Ben | A1 | $(+1, +1)$ |
| R3 | Clara | A1 | $(+1, +1)$ |
| R4 | David | A1 | $(+1, +1)$ |
| R5 | Eleni | A2 — Literary | $(+1, -1)$ |
| R6 | Felix | A2 | $(+1, -1)$ |
| R7 | Greta | A2 | $(+1, -1)$ |
| R8 | Hugo | A2 | $(+1, -1)$ |
| R9 | Iris | A3 — Practical | $(-1, +1)$ |
| R10 | Jonas | A3 | $(-1, +1)$ |
| R11 | Karin | A3 | $(-1, +1)$ |
| R12 | Liam | A3 | $(-1, +1)$ |
| R13 | Maya | A4 — Scholar | $(-1, -1)$ |
| R14 | Nico | A4 | $(-1, -1)$ |
| R15 | Oksana | A4 | $(-1, -1)$ |
| R16 | Petros | A4 | $(-1, -1)$ |

### Special readers (the pedagogical surprises)

| ID | Name | Role | $u$ | What they teach |
|---|---|---|---|---|
| R17 | **Quinn** | The Fiction-Axis reader | $(+1, 0)$ | a single latent dimension can dominate; loves *all* fiction, ignores nonfiction. The recsys places her on the x-axis without committing to a y-quadrant. |
| R18 | **Rosa** | The Light-Axis reader | $(0, +1)$ | the orthogonal version of Quinn. Loves all *light* books regardless of fiction/nonfiction. Together with Quinn, demonstrates that the two axes are real and independent. |
| R19 | **Samir** | The Eclectic | $(+0.5, +0.5)$ | a noisy weak-A1 signal. The recsys is uncertain about him; the Carousel's archetype-mixture badge will show ~50% A1, 25% A2, 25% A3. Demonstrates that mixtures are continuous, not categorical. |
| R20 | **Tessa** | The Twin | $(+1, +1)$ identical to Alice | the matrix has redundancy. SVD will collapse Alice and Tessa onto the same point. *Pedagogical reveal at Scene 11:* "two readers are the same person to the algorithm." |
| R21 | **Ursula** | The Borges-loving Commuter | $(+1, +1)$ but with one anomalous ✅ on Borges | real preferences carry noise the model cannot fit. The recsys *will* miss her Borges love — and that's correct behaviour, not a bug. Sets up the KL-divergence-as-inefficiency line at Scene 26. |

### The cold-start reader

| ID | Name | Role | $u$ (truth) | Visible to the system at Scene 11 |
|---|---|---|---|---|
| R22 | **Vera** | The new arrival | $(+1, +1)$ — A1 | a single rating: *Christie* ✅. Three optional profile answers ("Indoor or outdoor reader?", "Fiction or nonfiction?", "Light or demanding?"). |

> *The Carousel's Stage 3 demo (Scene 11):* Vera's true preferences are A1. With one rating (Christie ✅), the system places her near A1 with high uncertainty. With three profile answers, it places her *exactly* at A1 with high confidence — *without ever drawing another ball from her urn*. This is the matrix-factorization business case in 90 seconds.

---

## 4 · The generation rule

For each (reader, book) cell:

$$\text{score}(i,j) \;=\; u_i \cdot v_j \;+\; \varepsilon_{ij}, \qquad \varepsilon_{ij} \sim \mathrm{Uniform}(-0.4,\, +0.4)$$

then thresholded:

| Condition | Cell |
|---|---|
| $\text{score} > +0.5$ | ✅ |
| $\text{score} < -0.5$ | ❌ |
| else | ? |

Independently, **~25% of cells are masked as "—" (unread)** before the matrix is shown to the audience. These are the cells the recsys must predict — the matrix-completion task that Scene 12 (`07_embeddings-that-learn`) and the Cold-Start Carousel build on.

The seed is fixed; the matrix is reproducible bit-for-bit.

> *Why noise at all?* Without noise, the matrix is rank 2 and Eckart–Young recovers it perfectly at $k=2$. With small noise, rank-2 captures ~90% of variance and rank-3 captures ~95% — the Spectral Microscope's error curve has the shape of a real elbow, which is what the audience needs to *feel* Eckart–Young rather than merely hear it stated.

---

## 5 · The 21 × 16 rating matrix

Rows: readers. Columns: books, in the order LF1 LF2 LF3 LF4 · DF1 DF2 DF3 DF4 · LN1 LN2 LN3 LN4 · DN1 DN2 DN3 DN4.

Cells: ✅ liked · ❌ disliked · ? ambiguous · — unread.

|        | Pot | Chr | Hun | DaV | Uly | W&P | **Bor** | Lig | Eat | Swi | 7Hb | Joy | Kan | Smi | Dar | **Rus** |
|--------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Alice** (A1)   | ✅ | ✅ | ✅ | ✅ | ? | ? | ? | ? | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ |
| **Ben** (A1)     | ✅ | ✅ | ✅ | ✅ | ? | ? | ? | ? | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ |
| **Clara** (A1)   | ✅ | ✅ | ✅ | ✅ | ? | ? | ? | ? | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ |
| **David** (A1)   | ✅ | ✅ | ✅ | ✅ | ? | ? | ? | ? | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ |
| **Eleni** (A2)   | ? | ? | ? | ? | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ? | ? | ? | ? |
| **Felix** (A2)   | ? | ? | ? | ? | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ? | ? | ? | ? |
| **Greta** (A2)   | ? | ? | ? | ? | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ? | ? | ? | ? |
| **Hugo** (A2)    | ? | ? | ? | ? | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ? | ? | ? | ? |
| **Iris** (A3)    | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ? | ? | ? | ? |
| **Jonas** (A3)   | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ? | ? | ? | ? |
| **Karin** (A3)   | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ? | ? | ? | ? |
| **Liam** (A3)    | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ? | ? | ? | ? |
| **Maya** (A4)    | ❌ | ❌ | ❌ | ❌ | ? | ? | ? | ? | ? | ? | ? | ? | ✅ | ✅ | ✅ | ✅ |
| **Nico** (A4)    | ❌ | ❌ | ❌ | ❌ | ? | ? | ? | ? | ? | ? | ? | ? | ✅ | ✅ | ✅ | ✅ |
| **Oksana** (A4)  | ❌ | ❌ | ❌ | ❌ | ? | ? | ? | ? | ? | ? | ? | ? | ✅ | ✅ | ✅ | ✅ |
| **Petros** (A4)  | ❌ | ❌ | ❌ | ❌ | ? | ? | ? | ? | ? | ? | ? | ? | ✅ | ✅ | ✅ | ✅ |
| **Quinn** (★)    | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Rosa** (★)     | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Samir** (★)    | ✅ | ? | ✅ | ? | ? | ? | ? | ? | ? | ? | ? | ? | ❌ | ? | ❌ | ? |
| **Tessa** (★)    | ✅ | ✅ | ✅ | ✅ | ? | ? | ? | ? | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ |
| **Ursula** (★)   | ✅ | ✅ | ✅ | ✅ | ? | ? | **✅** | ? | ? | ? | ? | ? | ❌ | ❌ | ❌ | ❌ |

Counts: 336 cells = 72 ✅ · 72 ❌ · 191 ? · 1 anomalous (Ursula × Borges) · 0 — (every cell rated; the cold-start narrative is carried entirely by Vera the new arrival, not by within-matrix unread cells).

> *Why pure-archetype rows are bit-identical within each archetype.* The four readers in each archetype (Alice/Ben/Clara/David, etc.) carry the same rating row by design. This is the cleanest possible expression of "compression discovers redundancy" — at Scene 5 the audience finds *four* groups of four duplicate rows. At Scene 12, the embeddings-that-learn viz collapses each archetype to a single point. The Twin (Tessa = Alice) is one redundancy among many.

> *Note on Tessa.* Her row is bit-identical to Alice's. This is a designed redundancy. When the audience plays the block-diagonal puzzle (Scene 5), Alice and Tessa will fall on top of each other every time. When the embeddings-that-learn viz (Scene 12) finishes, Alice and Tessa will be the same dot. A 30-second debrief: *"compression is the discovery of redundancy. The matrix held 21 readers; the algorithm sees twenty."*

> *Note on Ursula.* Her ✅ on Borges (column 7) is the only deviation from a clean A1 row. The recsys, learning from the rest of the matrix, will predict ❌ for her on Borges — *contrary to her actual preference*. This is the inescapable inefficiency the closing equation names: $\text{cross-entropy} = H(p) + \mathrm{KL}(p \| \hat p)$. Ursula's Borges cell is one bit of KL, made physical.

---

## 6 · Designed-in pedagogical surprises (cross-referenced to scenes)

| # | Surprise | Reveal scene | What it teaches |
|---|---|---|---|
| 1 | **Borges in the matrix** | scenes 11, 27 | the lecture quotes the same author whose book is in column 7. Closes the loop. |
| 2 | **Russell as Carousel anchor** | scene 11 | the test item discriminates sharply across archetypes — exactly what the urn metaphor needs. Bridges to Scene 25's text-compression demo on a Russell paragraph. |
| 3 | **Alice ≡ Tessa** | scenes 5, 12 | compression *is* deduplication. The matrix has 21 rows but only 20 distinct points. |
| 4 | **Quinn (fiction-axis) and Rosa (light-axis)** | scenes 5, 7 | the latent axes are not labels we invented; they are degrees of freedom that real readers actually inhabit. |
| 5 | **Samir's "?" cells** | scene 7 | a weak-signal reader sits in the middle of the latent space. Mixtures are continuous, not categorical. |
| 6 | **Ursula's anomalous Borges ✅** | scenes 12, 26 | real preferences carry irreducible noise. The recsys's failure to fit it is the KL gap above the entropy floor. |
| 7 | **Vera the cold-start** | scene 11 (Stage 3) | one rating, three profile questions: the system places her with confidence the urn-sampling alone cannot match. |

---

## 7 · Sanity checks (to be verified once `shared/data.js` is built)

1. **Rank check.** SVD of the rating matrix (with ✅ → +1, ❌ → −1, ? → 0, — masked) should show two dominant singular values ($\sigma_1 \approx \sigma_2 \gg \sigma_3 \approx \dots$). If the gap between $\sigma_2$ and $\sigma_3$ is less than 5×, regenerate with a smaller noise amplitude.
2. **Archetype recovery.** Top-2 left singular vectors, after rotation, should align with the four reader archetypes in 2D. Specifically: Alice and Tessa should be co-located; Quinn should sit on the x-axis; Rosa on the y-axis; Samir near the origin.
3. **Twin redundancy.** Cosine distance between Alice's and Tessa's reconstructed vectors after rank-2 truncation must be < 0.01.
4. **Cold-start prediction.** With Vera's single Christie ✅ rating and three profile answers, the predicted top-3 books should be {*Potter*, *Hunger*, *DaVinci*} in some order — i.e., the rest of the LF quadrant.
5. **Ursula's KL bit.** Predicted rating for Ursula on *Borges* must be ❌ even though the truth is ✅. Confirms that the model isn't memorising her anomaly.

---

## 8 · Reproducibility

- Random seed: `42`.
- Noise distribution: `Uniform(-0.4, +0.4)`, drawn once per cell.
- Mask probability: `0.13` per cell, sampled independently with the same seed stream.
- Hand-edits to the table override the generated values; they are listed below.

### Hand-edits applied to the generated table

| Cell | Generated | Final | Reason |
|---|---|---|---|
| Ursula × *Borges* | ❌ | ✅ | designed surprise #6 (anomalous outlier) |
| Tessa × all books | (regen) | copy of Alice's row | designed surprise #3 (the twin) |
| Samir's row | mostly ✅ / ❌ | introduce six ? cells | designed surprise #5 (weak signal) |
| Quinn × LN/DN | mixed | force all ❌ | clean fiction-axis archetype for surprise #4 |
| Rosa × DF/DN | mixed | force all ❌ | clean light-axis archetype for surprise #4 |

These five edits are the entire deviation from the math model. Everything else is `score(i, j) = u_i · v_j + ε_{ij}` thresholded.

---

## 9 · What this matrix does *not* contain

- **Genre tags or text content.** The matrix is preferences, not content metadata. The Spectral Microscope and the Carousel work without ever opening the books.
- **Ratings on a 1–5 scale.** Binary ✅/❌ (with the small ? class) is enough for the bandit-urn bridge at Scene 11; introducing a 5-point scale would force a separate model and we don't have time.
- **Time dynamics.** The lecture treats preferences as static. Cold-start is the only temporal element, and it is told as a single before/after at Scene 11.

These are deliberate omissions. Scope honesty.

---

## 10 · Cross-references

- `NARRATIVE_PLAN.md` — every scene that touches the matrix is tagged in the narrative plan.
- `shared/data.js` (downstream, not yet written) — codification of this design as a JS module imported by every viz.
- The Customer-Urns Carousel (Scene 11) and the Compression-Prediction Twin (Scene 25) depend most heavily on this matrix; their viz specs will reference specific reader IDs and the Russell/Christie cells.

---

## Changelog

- **v2 (current):** rank-2-clean ratings. The original hand-crafted v1 ratings inadvertently broke the rank-2 structure by placing ✅s in adjacent quadrants (e.g., Alice ✅ on Light Nonfiction, Iris ✅ on Light Fiction). Empirically the SVD showed σ₂/σ₃ = 1.6 instead of the claimed ≥ 5; the embeddings-that-learn viz collapsed all readers along a single axis. v2 fixes this by setting *every* adjacent-quadrant cell to `?` (zero), keeping ✅ only in own quadrants and ❌ only in opposite quadrants. Pure-archetype readers within an archetype are now bit-identical. The cold-start narrative is carried entirely by Vera (not by within-matrix unread cells) so v2 has no `—` cells in the in-matrix readers. Surprises preserved: Quinn (fiction-axis), Rosa (light-axis), Samir (weak A1, with `?`s in own and opposite quadrants), Tessa = Alice (twin), Ursula (Borges anomaly = a small rank-3 perturbation, σ₃ ~ 1).
- **v1:** initial design. 16 books locked. 4 archetypes named. 21 readers + 1 cold-start. Five hand-edits documented. Five sanity checks listed. Withdrawn: rank-2 structure not recovered by SVD.
