#!/usr/bin/env python3
"""Every number of the lecture notes, computed from the data of the weekend 2 games.

Run from lecture-notes/:

    python3 -I tools/notes_numbers.py            compute, check, write generated/*.tex
    python3 -I tools/notes_numbers.py FILE.pdf   the same, then check the built PDF

The data below are copies. All of them are invented for the games, except part three's MovieLens ratings.
  VS                      w2-cx-private 01_nearest_neighbours/source/notebook/data.py, R (round 2)
  P1, Q1_COLUMNS          w2-cx-private 02_matrix_factorization/source/notebook/data.py, V (section 1)
  R2, P2, Q2_COLUMNS      the same file, V and START2 (section 2)
  PART_THREE              w2-cx-private 02_matrix_factorization/source/game/s5-data.js, runs[0]
                          (generated there from MovieLens ml-latest-small by tools/s5_movielens.py)
When w2-cx-private is checked out beside this repository (../../w2-cx-private), every copy is compared with it.
The descent of part two repeats MF.Z.run (nudge-math.js); gradient descent repeats MF.T.run (table-math.js).
"""
import json
import re
import runpy
import subprocess
import sys
from pathlib import Path

NOTES = Path(__file__).resolve().parent.parent          # lecture-notes/
OUT = NOTES / "generated"
PRIVATE = NOTES.parent.parent / "w2-cx-private"

# THE DATA

# Once Upon a Video Store, acts 2 to 4. A rating runs from -2 to 2; None: not seen yet.
FILMS_VS = ["Jaws", "The Shining", "Notting Hill", "Love Actually"]
REGULARS = ["Ivo", "Pia", "Tom", "Kai", "Jana", "Rosa"]
VS = {"Ivo": [2, -2, 0, 1], "Pia": [2, 1, 2, 2], "Tom": [-1, -2, -1, -1], "Kai": [1, 2, -2, -2],
      "Jana": [0, 1, 0, 0], "Rosa": [-2, -1, 2, 2], "Vera": [2, 1, -1, None]}
VERA_LATER = -2          # Vera's rating of Love Actually once she watched it

# Matchmaker, part one: the profiles (P) and the critic's answers (one column of Q per film).
AXES = ["real", "comedy", "action"]
CUSTOMERS1 = ["Sara", "Leo", "Maya"]
FILMS1 = ["The Intouchables", "Apollo 13", "Men in Black", "Interstellar"]
P1 = [[2, 1, -2], [-2, 2, 2], [1, -2, 1]]
Q1_COLUMNS = [[2, 1, -1], [2, -2, 1], [-2, 1, 2], [-2, -2, 0]]

# Matchmaker, part two: the ratings and the first guess (one column of Q per film).
CUSTOMERS2 = ["Ida", "Raj", "Elsa"]
FILMS2 = ["Paddington", "The Martian"]
R2 = [[2, 1], [-1, 2], [1, -2]]
P2 = [[-1, -2], [-2, 0], [2, 2]]
Q2_COLUMNS = [[-1, 2], [-2, -1]]
EPS, ALPHA, TOL = 0.01, 0.1, 0.0001     # part two (MF.S2)
ALPHA_GD = 0.2                          # gradient descent of the optional game (MF.S4)

# Matchmaker, part three: the run on real ratings with three hidden (MF.S5.runs[0]).
PART_THREE = {
    "users": 10, "films": 12, "k": 2, "alpha": 3, "steps": 200, "known": 117,
    "start": 1.8390872940170933, "end": 0.25086536262392417, "within_half": 81,
    "hidden": [  # film, MovieLens user, stars, prediction
        ("Independence Day", 64, 3.0, 0.672352306013165),
        ("Braveheart", 28, 3.5, 0.6227970952582049),
        ("Seven", 239, 5.0, 1.9847636790449537),
    ],
}
SHIFT = 3                               # a rating is the stars minus 3

# ARITHMETIC


def inner(a, b):
    return sum(x * y for x, y in zip(a, b))


def product(P, Q_columns):
    return [[inner(row, col) for col in Q_columns] for row in P]


def average_loss(P, Qc, R):
    pred = product(P, Qc)
    losses = [(pred[i][j] - R[i][j]) ** 2 for i in range(len(R)) for j in range(len(R[0]))]
    return sum(losses) / len(losses)


def places(P, Qc):
    """Every guessed number in the order of part two's rounds: the customers' rows first, then the films'."""
    return [("P", i, k) for i in range(len(P)) for k in range(len(P[0]))] + \
           [("Q", j, k) for j in range(len(Qc)) for k in range(len(Qc[0]))]


def nudge(P, Qc, R, which, r, k):
    """Part two's move of one number: (before, after, new value)."""
    M = P if which == "P" else Qc
    x = M[r][k]
    before = average_loss(P, Qc, R)
    M[r][k] = x + EPS
    after = average_loss(P, Qc, R)
    M[r][k] = x
    return before, after, x - ALPHA * (after - before) / EPS


def rounds_until(P, Qc, R, tol=TOL, most=400):
    P, Qc = [r[:] for r in P], [c[:] for c in Qc]
    n = 0
    while average_loss(P, Qc, R) >= tol and n < most:
        for which, r, k in places(P, Qc):
            (P if which == "P" else Qc)[r][k] = nudge(P, Qc, R, which, r, k)[2]
        n += 1
    return n, P, Qc


def gradient_step(P, Qc, R, alpha):
    """All numbers at once: each moves against the slope of the average loss (MF.T.step)."""
    n = len(R) * len(R[0])
    gP = [[0.0] * len(P[0]) for _ in P]
    gQ = [[0.0] * len(Qc[0]) for _ in Qc]
    for i in range(len(R)):
        for j in range(len(R[0])):
            miss = inner(P[i], Qc[j]) - R[i][j]          # prediction minus rating
            for k in range(len(P[0])):
                gP[i][k] += 2 * Qc[j][k] * miss / n
                gQ[j][k] += 2 * P[i][k] * miss / n
    newP = [[P[i][k] - alpha * gP[i][k] for k in range(len(P[0]))] for i in range(len(P))]
    newQ = [[Qc[j][k] - alpha * gQ[j][k] for k in range(len(Qc[0]))] for j in range(len(Qc))]
    return newP, newQ, gP, gQ


def gradient_descent(P, Qc, R, alpha, tol=TOL, most=1000):
    losses = [average_loss(P, Qc, R)]
    while losses[-1] >= tol and len(losses) - 1 < most:
        P, Qc, _, _ = gradient_step(P, Qc, R, alpha)
        losses.append(average_loss(P, Qc, R))
    return losses, P, Qc


def r2(x):
    return f"{x:.2f}"


def r3(x):
    return f"{x:.3f}"


# THE NUMBERS

N = {}   # name: the string the notes print

# The inner product and the nearest neighbor.
jaws = {name: VS[name][0] for name in VS}
for a, b in [("Ivo", "Pia"), ("Ivo", "Rosa"), ("Pia", "Kai"), ("Kai", "Tom")]:
    N[f"jaws {a} {b}"] = str(jaws[a] * jaws[b])
assert [N[f"jaws {a} {b}"] for a, b in [("Ivo", "Pia"), ("Ivo", "Rosa"), ("Pia", "Kai"), ("Kai", "Tom")]] == \
    ["4", "-4", "2", "-1"]

vera3 = VS["Vera"][:3]
sims = {name: inner(vera3, VS[name][:3]) for name in REGULARS}
ranked = sorted(REGULARS, key=lambda name: -sims[name])
assert ranked == ["Kai", "Pia", "Ivo", "Jana", "Tom", "Rosa"], ranked
assert [sims[n] for n in ranked] == [6, 3, 2, 1, -3, -7]
stack = [vera3[k] * VS["Kai"][k] for k in range(3)]
assert stack == [2, 2, 2] and sum(stack) == 6
nearest = ranked[0]
prediction = VS[nearest][3]
assert (nearest, prediction, VERA_LATER) == ("Kai", -2, -2)
matches = {name: sum(1 for k in range(3) if VS[name][k] == vera3[k]) for name in REGULARS}
assert matches == {"Ivo": 1, "Pia": 2, "Tom": 1, "Kai": 0, "Jana": 1, "Rosa": 0}, matches
assert max(matches, key=matches.get) == "Pia" and VS["Pia"][3] == 2
# Ratings of 1 and -1 only: the inner product is the matches minus the mismatches.
for a in ([1, -1, 1, 1], [-1, -1, 1, -1]):
    for b in ([1, 1, -1, 1], [-1, 1, 1, -1]):
        same = sum(1 for x, y in zip(a, b) if x == y)
        assert inner(a, b) == same - (len(a) - same)

# Matrix multiplication.
scores = product(P1, Q1_COLUMNS)
assert scores == [[7, 0, -7, -6], [-4, -6, 10, 0], [-1, 7, -2, 2]], scores
assert [P1[0][k] * Q1_COLUMNS[0][k] for k in range(3)] == [4, 1, 2]
best = {CUSTOMERS1[i]: (FILMS1[max(range(4), key=lambda j: scores[i][j])], max(scores[i])) for i in range(3)}
assert best == {"Sara": ("The Intouchables", 7), "Leo": ("Men in Black", 10), "Maya": ("Apollo 13", 7)}, best

# Matrix factorization, the first guess.
pred2 = product(P2, Q2_COLUMNS)
loss2 = [[(pred2[i][j] - R2[i][j]) ** 2 for j in range(2)] for i in range(3)]
assert pred2 == [[-3, 4], [2, 4], [2, -6]] and loss2 == [[25, 9], [9, 4], [1, 16]]
assert sum(map(sum, loss2)) == 64
N["average"] = r2(64 / 6)                                                   # 10.67

# One small change: The Martian's second number (part two, scene One small change).
before, after, new = nudge(P2, Q2_COLUMNS, R2, "Q", 1, 1)
N["before"], N["after"] = r3(before), r3(after)                             # 10.667, 10.620
shown_change = round(after, 3) - round(before, 3)                           # the game rounds to 3 decimals
N["change"] = r3(shown_change)                                              # -0.047
N["nabla"] = f"{shown_change / EPS:.1f}"                                    # -4.7
N["new"] = r2(-1 - ALPHA * float(N["nabla"]))                               # -0.53
assert r2(new) == N["new"], (new, N["new"])
moved = [c[:] for c in Q2_COLUMNS]
moved[1][1] = new
N["after move"] = r2(average_loss(P2, moved, R2))                           # 8.78
assert (N["before"], N["after"], N["change"], N["nabla"], N["new"], N["after move"]) == \
    ("10.667", "10.620", "-0.047", "-4.7", "-0.53", "8.78")

# Again and again: rounds from the guess after that move (MF.Z.run from G1 in sec2.js).
n_rounds, P_end, Q_end = rounds_until(P2, moved, R2)
assert n_rounds == 99, n_rounds
gap = max(abs(inner(P_end[i], Q_end[j]) - R2[i][j]) for i in range(3) for j in range(2))
assert gap < 0.02, gap
N["rounds"] = str(n_rounds)

# Gradient descent from the first guess (the optional game, scene Many films).
losses, _, _ = gradient_descent(P2, Q2_COLUMNS, R2, ALPHA_GD)
N["gd one step"] = r2(losses[1])                                            # 1.97
N["gd steps"] = str(len(losses) - 1)                                        # 52
assert (N["gd one step"], N["gd steps"]) == ("1.97", "52"), (losses[1], len(losses) - 1)
# The slope rule: 2 x partner x (prediction minus rating), averaged over the ratings. On Paddington's column alone
# (the optional game, scene Every rating has a say) Paddington's numbers get 2/3 and 8, Ida's 10/3 and -20/3.
_, _, gP, gQ = gradient_step(P2, Q2_COLUMNS[:1], [[r[0]] for r in R2], ALPHA_GD)
assert abs(gQ[0][0] - 2 / 3) < 1e-12 and abs(gQ[0][1] - 8) < 1e-12
assert abs(gP[0][0] - 10 / 3) < 1e-12 and abs(gP[0][1] + 20 / 3) < 1e-12
_, _, gP, gQ = gradient_step(P2, Q2_COLUMNS, R2, ALPHA_GD)
# The hop of 0.01 measures nearly the same slope as the rule (The Martian's second number).
rule = gQ[1][1]
assert abs(rule - (after - before) / EPS) < 0.02, (rule, (after - before) / EPS)

# Part three.
T = PART_THREE
assert T["users"] * T["films"] - len(T["hidden"]) == T["known"]
N["p3 start"], N["p3 end"] = r2(T["start"]), r2(T["end"])                   # 1.84, 0.25
for film, user, stars, pred in T["hidden"]:
    N[f"p3 {film}"] = (r2(pred), f"{stars - SHIFT:g}")

# THE COPIES AGAINST W2-CX-PRIVATE


def compare_with_private():
    if not PRIVATE.is_dir():
        print("w2-cx-private not found beside this repository: the copies were not compared")
        return
    vs = runpy.run_path(str(PRIVATE / "01_nearest_neighbours/source/notebook/data.py"))
    keys = ["jaws", "shining", "notting", "love"]
    for name, row in VS.items():
        assert [vs["R"][name.lower()][k] for k in keys] == row, name
    assert vs["LATER"]["vera"]["love"] == VERA_LATER
    mf = runpy.run_path(str(PRIVATE / "02_matrix_factorization/source/notebook/data.py"))
    assert [mf["row"](c.lower()) for c in CUSTOMERS1] == P1
    films = ["intouchables", "apollo13", "mib", "interstellar"]
    assert [mf["row"](f) for f in films] == Q1_COLUMNS
    assert mf["RATINGS2"] == R2
    assert [mf["START2"][c.lower()] for c in CUSTOMERS2] == P2
    assert [mf["START2"][f] for f in ("paddington", "martian")] == Q2_COLUMNS
    assert (mf["EPS3"], mf["TOL3"]) == (EPS, TOL)
    js = (PRIVATE / "02_matrix_factorization/source/game/s5-data.js").read_text()
    s5 = json.loads(re.search(r"var S5 = (\{.*?\});\n", js, re.S).group(1))
    run = s5["runs"][0]
    assert (run["users"], run["films"], run["k"], run["alpha"], run["steps"]) == \
        (T["users"], T["films"], T["k"], T["alpha"], T["steps"])
    assert (run["start"], run["end"]["loss"], run["end"]["within_half"]) == (T["start"], T["end"], T["within_half"])
    assert s5["shift"] == SHIFT
    for (i, j), pred, (film, user, stars, mine) in zip(run["hidden"], run["end"]["hidden"], T["hidden"]):
        assert (s5["films"][j]["short"], s5["users"][i], s5["stars"][i][j], pred) == (film, user, stars, mine)
    print("the copies equal the data of w2-cx-private")


# THE TABLES


def num(x):
    return f"${x}$"


def write(name, text):
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text("% GENERATED by tools/notes_numbers.py: do not edit, run the script.\n" + text)


def video_store_table():
    lines = [r"\begin{tabular}{|l|c|c|c|c|c|}", r"\hline",
             r" & Jaws & The Shining & Notting Hill & Love Actually & "
             r"\begin{tabular}[b]{@{}c@{}}inner product\\with Vera\end{tabular} \\ \hline",
             "Vera & " + " & ".join(num(x) for x in VS["Vera"][:3]) + r" & ? & \\ \hline\hline"]
    for name in ranked:
        lines.append(f"{name} & " + " & ".join(num(x) for x in VS[name]) + f" & {num(sims[name])} \\\\ \\hline")
    lines.append(r"\end{tabular}")
    write("video-store.tex", "\n".join(lines) + "\n")


def stack_table():
    v, k = VS["Vera"][:3], VS["Kai"][:3]
    lines = [r"\begin{tabular}{l*{7}{c}}",
             r" & Jaws & & The Shining & & Notting Hill \\",
             "Vera & " + " & & ".join(num(x) for x in v) + r" \\",
             "Kai & " + " & & ".join(num(x) for x in k) + r" \\ \cline{2-6}",
             " & " + " & $+$ & ".join(num(x) for x in stack) + f" & $=$ & {num(sum(stack))} \\\\",
             r"\end{tabular}"]
    write("stack.tex", "\n".join(lines) + "\n")


def cross(rows, boxes, labels, row_labels, films):
    """A TikZ matrix of nodes with boxes around blocks: rows is a list of lists of cell texts.
    The film heads get the width of the longest word in the film names, so every film column is as wide."""
    words = sorted({w for f in films for w in f.split()})
    body = []
    for row in rows:
        body.append(" & ".join(row) + r" \\")
    out = [r"\settowidth{\headwidth}{\footnotesize\begin{tabular}{@{}c@{}}" + r"\\".join(words) + r"\end{tabular}}",
           r"\begin{tikzpicture}",
           r"\matrix (m) [matrix of nodes, nodes in empty cells, row sep=1.5pt, column sep=3pt,",
           r"  nodes={minimum height=1.35em, minimum width=1.9em, anchor=center, inner sep=1pt}, column 1/.style={anchor=east}] {"]
    out += body
    out.append("};")
    for name, (ra, ca, rb, cb) in boxes.items():
        out.append(rf"\node[draw, inner sep=2pt, fit=(m-{ra}-{ca})(m-{rb}-{cb})] ({name}) {{}};")
    for name, row, col, text in row_labels:
        out.append(rf"\node[anchor=east, inner sep=3pt, font=\footnotesize] at ({name}.west |- m-{row}-{col}) {{{text}}};")
    for name, side, text in labels:
        anchor = {"below": "north", "right": "west", "above": "south"}[side]
        point = {"below": "south", "right": "east", "above": "north"}[side]
        out.append(rf"\node[anchor={anchor}, inner sep=3pt] at ({name}.{point}) {{{text}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out) + "\n"


def head(text):
    # a strut on the last line: one-line and two-line names end on one baseline, the bottom on the row line
    return (r"|[text width=\headwidth, align=center, anchor=south, minimum height=0pt, font=\footnotesize]| "
            + text + r"\strut")


def customer(text):
    return r"|[inner xsep=4pt]| " + text


def profiles_cross():
    width = 9
    rows = [[""] * 5 + [head(f) for f in FILMS1]]
    for a, axis in enumerate(AXES):
        rows.append([""] * 5 + [num(col[a]) for col in Q1_COLUMNS])
    rows.append([""] + [r"|[font=\footnotesize]| " + a for a in AXES] + [""] * 5)
    for i, name in enumerate(CUSTOMERS1):
        rows.append([customer(name)] + [num(x) for x in P1[i]] + [""] + [num(x) for x in scores[i]])
    assert all(len(r) == width for r in rows)
    boxes = {"Q": (2, 6, 4, 9), "P": (6, 2, 8, 4), "PQ": (6, 6, 8, 9)}
    labels = [("Q", "right", "$Q$"), ("P", "below", "$P$"), ("PQ", "below", "$PQ$")]
    row_labels = [("Q", 2 + a, 6, axis) for a, axis in enumerate(AXES)]
    write("cross-profiles.tex", cross(rows, boxes, labels, row_labels, FILMS1))


def guess_board():
    width = 13
    rows = [[""] * 5 + [head(f) for f in FILMS2] + [""] + [head(f) for f in FILMS2] + [""] + [""] * 2]
    for k in range(2):
        rows.append([""] * 5 + [num(col[k]) for col in Q2_COLUMNS] + [""] * 6)
    rows.append([""] + [r"|[font=\footnotesize]| " + str(k + 1) for k in range(2)] + [""] * 10)
    for i, name in enumerate(CUSTOMERS2):
        rows.append([customer(name)] + [num(x) for x in P2[i]] + ["", ""] + [num(x) for x in pred2[i]] + [""]
                    + [num(x) for x in R2[i]] + [""] + [num(x) for x in loss2[i]])
    assert all(len(r) == width for r in rows), [len(r) for r in rows]
    boxes = {"Q": (2, 6, 3, 7), "P": (5, 2, 7, 3), "PQ": (5, 6, 7, 7), "R": (5, 9, 7, 10), "L": (5, 12, 7, 13)}
    labels = [("Q", "right", "$Q$"), ("P", "below", "$P$"), ("PQ", "below", "predictions $PQ$"),
              ("R", "below", "ratings $R$"), ("L", "below", "losses")]
    row_labels = [("Q", 2 + k, 6, str(k + 1)) for k in range(2)]
    write("board-first-guess.tex", cross(rows, boxes, labels, row_labels, FILMS2))


def hidden_table():
    lines = [r"\begin{tabular}{|l|c|c|c|}", r"\hline",
             r"Film & MovieLens user & Prediction & Rating \\ \hline"]
    for film, user, stars, pred in T["hidden"]:
        lines.append(f"{film} & {user} & {num(r2(pred))} & {num(f'{stars - SHIFT:g}')} \\\\ \\hline")
    lines.append(r"\end{tabular}")
    write("hidden-ratings.tex", "\n".join(lines) + "\n")


# THE PDF


EXPECTED = [  # strings the PDF must contain (a minus sign is read as a hyphen, a times sign as x)
    "4 + 1 + 2 = 7", "64/6 = 10.67", "10.667", "10.620", "-0.047/0.01 = -4.7", "-1 - 0.1 x (-4.7) = -0.53",
    "8.78", "99 rounds", "1.97", "52 steps", "1.84", "0.25",
]


def check_pdf(pdf):
    text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True,
                          check=True).stdout
    dashes = [c for c in text if c in (chr(8211), chr(8212))]
    assert not dashes, f"{len(dashes)} en or em dashes in the PDF"
    flat = re.sub(r"\s+", " ", text.replace(chr(8722), "-").replace(chr(215), "x"))
    missing = [s for s in EXPECTED if s not in flat]
    assert not missing, f"not in the PDF: {missing}"
    print(f"{pdf}: no dashes, all {len(EXPECTED)} expected strings present")


def main():
    compare_with_private()
    video_store_table()
    stack_table()
    profiles_cross()
    guess_board()
    hidden_table()
    for key, value in N.items():
        print(f"{key:>16}: {value}")
    pdfs = [a for a in sys.argv[1:] if a.endswith(".pdf")]
    for pdf in pdfs:
        check_pdf(NOTES / pdf)


if __name__ == "__main__":
    main()
