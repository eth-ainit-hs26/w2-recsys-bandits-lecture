# Books matrix — design audit log

A live log of the matrix-design work, written as it happens. If the session hangs, this file shows the last completed checkpoint.

---

**Step 1 — Started.**
Goal: produce `BOOKS_MATRIX.md` with the 16 titles, 4 archetypes, 21 readers, latent vectors, generation rule, full 21×16 rating table, the cold-start reader, and the designed-in pedagogical surprises. Bounded scope; no second-guessing.

**Step 2 — Locked the 16 titles.**
Four per quadrant: Light/Fiction, Demanding/Fiction, Light/Nonfiction, Demanding/Nonfiction. Gender balance ~7F / 9M. Era spread 1776–2008. Borges deliberately included as a book in the matrix so the lecture's opening quote and the matrix point at the same author.

**Step 3 — Locked the 4 archetypes.**
Commuter (Light/Fiction), Literary (Demanding/Fiction), Practical (Light/Nonfiction), Scholar (Demanding/Nonfiction). 2D latent space: x = Fiction–Nonfiction, y = Light–Demanding. Archetypes at the four corners of the (±1, ±1) box.

**Step 4 — Designed the 21 readers.**
16 pure archetype readers (4 each) + 5 special readers carrying the pedagogical surprises (one fiction-axis reader, one light-axis reader, one weak-signal eclectic, one identical twin to demonstrate redundancy, one Borges-loving outlier). Plus 1 cold-start reader (Vera) introduced separately at scene 11.

**Step 5 — Generation rule fixed.**
`score(i,j) = u_i · v_j + ε_ij`, ε ~ Uniform(−0.4, 0.4). Threshold to ✅ / ❌ / ?. Independently, ~25% of cells are masked as "—" (unread) to give the matrix-completion problem its substance.

**Step 6 — Hand-crafted the 21×16 table.**
The math model gives the skeleton; some cells are then nudged by hand to (a) make the block-diagonal puzzle clean to find, (b) embed the surprises clearly, and (c) keep the unread cells distributed so cold-start has data to work with.

**Step 7 — Wrote `BOOKS_MATRIX.md`.**
Full design committed.

**Step 8 — Done.**
Markdown deliverable in place. `shared/data.js` is the next deliverable, downstream of this — not built in this turn to keep scope honest.
