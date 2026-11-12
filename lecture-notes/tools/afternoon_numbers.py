#!/usr/bin/env python3
"""Every number of the afternoon lecture notes (bandits-and-large-scale-computing.tex), computed from copies of the
data of the weekend 2 games and of the computing clusters deck.

Run from lecture-notes/:

    python3 -I tools/afternoon_numbers.py            compute, check, write generated/bandits-*.tex, computing-*.tex
    python3 -I tools/afternoon_numbers.py FILE.pdf   the same, then check the built PDF

The data below are copies. Everything of the games is invented for them.
  SEASON, PRODUCTS, CUSTOMERS,      w2-cx-private 03_bandits/source/game/core.js: MB.SEASON, MB.PRODUCTS,
  COLLECTIONS, ETE_N, EPS, RACE,    MB.CUSTOMERS, MB.COLLECTIONS, MB.ETE_N, MB.EPS, MB.RACE and MB.raceSeed
  STREAMS
  URN_W, URN_N                      the same folder, sec1.js (Cinderella's urn for the mattress)
  NS, AVG_S, NEAR                   the same folder, sec3.js (the challenge's n, the seasons and the band of the last
                                    chart of section 3, "Choosing n is hard")
  UCB_AT                            the same folder, sec5.js, XT (the board of "The dark bar and the light bar")
  mulberry32 ... ete_averages       the same folder, sim.js (MB.sim), in Python; the moods and the strategies' streams
                                    give the game's seasons morning by morning
  GRID                              w2-cx-private 02_matrix_factorization/grid-sketch/data.js (window.GRID, generated
                                    there by tools/make_data.py)
  ROOM, POOL                        the same folder, grid.html (the memory of a computer, the computers of slide 2)
  DECK_NUMBERS                      clusters-deck/block5-computing-clusters.tex and alps-platform-frame.tex, in this
                                    repository: each number as a frame prints it
When w2-cx-private is checked out beside this repository (../../w2-cx-private), every copy is compared with it, and
with node on the PATH the seasons and the averages are compared with sim.js itself. The deck's numbers are looked up
in the deck's source, which is in this repository.
The loss of matrix factorization is the TOTAL of the ratings' losses, as in every game since 2026-11-11.
"""
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

NOTES = Path(__file__).resolve().parent.parent          # lecture-notes/
OUT = NOTES / "generated"
REPO = NOTES.parent                                      # w2-recsys-bandits-lecture/
PRIVATE = REPO.parent / "w2-cx-private"
BANDITS = PRIVATE / "03_bandits/source/game"
GRID_DIR = PRIVATE / "02_matrix_factorization/grid-sketch"
DECK = [REPO / "clusters-deck/block5-computing-clusters.tex", REPO / "clusters-deck/alps-platform-frame.tex"]

# THE DATA: ONCE UPON A MIRROR

SEASON = 100
PRODUCTS = ["Robot vacuum", "Rope ladder", "Leaf blower", "Memory-foam mattress", "Satnav"]
SHORT = ["vacuum", "ladder", "blower", "mattress", "satnav"]
CUSTOMERS = {"Cinderella": [0.6, 0.2, 0.2, 0.4, 0.2], "Rapunzel": [0.4, 0.8, 0.2, 0.2, 0.2]}
COLLECTIONS = {
    "Ready for the ball": ("Cinderella", [("Silk gloves", 0.6), ("Tiara", 0.9), ("Evening bag", 0.6),
                                          ("Ball gown", 0.95), ("Lipstick", 0.6)]),
    "Long hair": ("Rapunzel", [("Scissors", 0.02), ("Cap", 0.02), ("Ribbon", 0.95), ("Razor", 0.02),
                               ("Haircut voucher", 0.02)]),
}
ETE_N = 20
EPS = 0.2
RACE = 103993
STREAMS = {"random": 1, "ete": 2, "eg": 3, "ucb": 4}     # a strategy's stream: 10 * RACE + this
URN_W, URN_N = 2, 5
NS = [0, 3, 10, 25, 50, 95]
AVG_S = 10000
NEAR = 0.005
UCB_AT = 10
TOL = 1e-9

# THE DATA: MATCHMAKER ON A GRID

GRID = {"seed": 20261106, "eps": 0.01, "alpha": 0.014, "tol": 0.01,
        "customers": ["Lena", "Omar", "Rosa", "Tim", "Uma", "Zoe"],
        "films": ["Paddington", "The Martian", "The Intouchables", "Apollo 13", "Men in Black", "Interstellar"],
        "R": [[-2, -2, -1, 0, 2, 1], [-2, -2, 0, 1, 1, 1], [0, 0, 1, 1, -1, 0], [2, 2, 1, 0, -2, -1],
              [0, 0, 2, 2, -2, 0], [-2, -2, 1, 2, 0, 1]],
        "U0": [[-2, 1], [1, 0], [2, 1], [-1, -2], [-2, 0], [-1, 2]],
        "V0": [[-2, -1], [2, -1], [-1, -1], [1, 2], [1, -2], [2, 2]],
        "hop": {"film": 2, "k": 0}, "rounds": 51, "play": 78}
ROOM, POOL = 21, 15
BS = 2                                                   # a block: 2 customers by 2 films

# THE DATA: THE COMPUTING CLUSTERS DECK. Each entry: the number as the deck prints it, then the frame.

DECK_NUMBERS = {
    "gh200 rate": ("990 \\times 10^{12}$ FLOP/s", "One computer, then and now"),
    "bits": ("16 bits per number", "One computer, then and now"),
    "cap": ("660 W on Alps", "One computer, then and now"),
    "hbm": ("96 GB of HBM3 at 4 TB/s", "A GH200 is a CPU and a GPU on one module"),
    "grace hopper": ("Between them 900 GB/s", "A GH200 is a CPU and a GPU on one module"),
    "nodes": ("2,688 nodes $\\times$ 4 modules $=$ 10,752 sockets", "Nodes and sockets"),
    "alps rate": ("$= 10.6 \\times 10^{18}$ FLOP/s", "CSCS and Alps, the machine behind Apertus"),
    "cabinets": ("one of 24 cabinets:\\\\ 8 chassis", "Alps is an HPE Cray EX254n"),
    "blades": ("7 used at Alps", "Alps is an HPE Cray EX254n"),
    "hbm bandwidth": ("4.023 \\times 10^{12}\\ \\text{bytes/s}", "Two hundred and forty six operations per byte"),
    "intensity": ("246\\ \\text{FLOP per byte}", "Two hundred and forty six operations per byte"),
    "link hbm": ("4,023 GB/s}/{the GPU to its HBM3}", "Four links, and each step down costs you"),
    "link grace": ("900 GB/s}/{Grace to Hopper}", "Four links, and each step down costs you"),
    "link socket": ("150 GB/s}/{socket to socket}", "Four links, and each step down costs you"),
    "link nodes": ("25 GB/s per GPU}/{between nodes}", "Four links, and each step down costs you"),
    "end to end": ("End to end, 161 times", "Four links, and each step down costs you"),
    "kwh": ("0.66 kWh", "A watt is a rate, a kilowatt hour is an amount"),
    "rappen": ("5.3 Rappen", "A wattage becomes a bill in two multiplications"),
    "price": ("8 Rappen per kWh assumed", "A wattage becomes a bill in two multiplications"),
    "mw": ("7.1 megawatts, about 570 francs an hour", "A wattage becomes a bill in two multiplications"),
    "mini": ("$= 6.00 \\times 10^{12}$ FLOP", "A million by a million is two minutes"),
    "laptop": ("$50 \\times 10^{9}$ FLOP/s", "A million by a million is two minutes"),
    "seconds": ("120 seconds", "A million by a million is two minutes"),
    "apertus n": ("$N = 70 \\times 10^{9}$", "The same formula on Apertus-70B"),
    "apertus d": ("$D = 15 \\times 10^{12}$", "The same formula on Apertus-70B"),
    "apertus c": ("$= 6.30 \\times 10^{24}$ FLOP", "The same formula on Apertus-70B"),
    "gpu hours": ("over 6 million GPU hours, on up to\n       4,096 GPUs", "From one GPU hour to the whole run"),
    "days": ("for \\textbf{61 days}", "From one GPU hour to the whole run"),
    "span": ("about 91 days,\\\\ so \\textbf{2,747} on average", "From one GPU hour to the whole run"),
    "energy": ("$=$ \\textbf{3.96 GWh}", "From one GPU hour to the whole run"),
    "francs": ("\\textbf{0.32 million francs}", "From one GPU hour to the whole run"),
    "cloud": ("6M h $\\times$ \\$2.50 $=$ \\$15.0M", "Six million hours, priced at cloud rates"),
}

# THE SIMULATION (MB.sim of sim.js, in Python)


def mulberry32(seed):
    state = seed & 0xFFFFFFFF

    def nxt():
        nonlocal state
        state = (state + 0x6D2B79F5) & 0xFFFFFFFF
        t = ((state ^ (state >> 15)) * (1 | state)) & 0xFFFFFFFF
        t = ((t + (((t ^ (t >> 7)) * (61 | t)) & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296
    return nxt


def argmax_all(v):
    mx = -math.inf
    for x in v:
        if x > mx + TOL:
            mx = x
    return [k for k, x in enumerate(v) if abs(x - mx) <= TOL]


def pick_tie(tied, r):
    return tied[int(r() * len(tied))] if len(tied) > 1 else tied[0]


def moods(seed, T=SEASON):
    r = mulberry32(seed)
    return [r() for _ in range(T)]


def play(p, u, choose):
    """A season: a list of mornings (row shown, tap, phase). choose(t, shown, taps) -> (row, phase)."""
    K = len(p)
    shown, taps, out = [0] * K, [0] * K, []
    for t in range(len(u)):
        i, phase = choose(t, shown, taps)
        tap = u[t] < p[i]
        shown[i] += 1
        taps[i] += tap
        out.append((i, tap, phase))
    return out


def est_of(shown, taps):
    return [taps[k] / s if s else 0 for k, s in enumerate(shown)]


def queen(p, u):
    best = p.index(max(p))
    return play(p, u, lambda t, s, k: (best, "queen"))


def random_mirror(p, u, seed):
    r = mulberry32(seed)
    return play(p, u, lambda t, s, k: (int(r() * len(p)), "random"))


def ete(p, u, seed, n):
    r, K, state = mulberry32(seed), len(p), {"winner": None}

    def choose(t, shown, taps):
        if t < K:
            return t, "init"
        if t < K + n:
            return int(r() * K), "test"
        if state["winner"] is None:
            state["winner"] = pick_tie(argmax_all(est_of(shown, taps)), r)
        return state["winner"], "exploit"
    return play(p, u, choose)


def eg(p, u, seed, eps):
    r, K = mulberry32(seed), len(p)

    def choose(t, shown, taps):
        if t < K:
            return t, "init"
        if r() < eps:
            return int(r() * K), "explore"
        return pick_tie(argmax_all(est_of(shown, taps)), r), "exploit"
    return play(p, u, choose)


def ucb(p, u, seed):
    r, K = mulberry32(seed), len(p)

    def choose(t, shown, taps):
        if t < K:
            return t, "init"
        score = [e + 1 / math.sqrt(n) for e, n in zip(est_of(shown, taps), shown)]
        return pick_tie(argmax_all(score), r), "ucb"
    return play(p, u, choose)


def race(p, seed=RACE):
    u = moods(seed)
    s = lambda key: 10 * seed + STREAMS[key]
    return {"queen": queen(p, u), "random": random_mirror(p, u, s("random")), "ete": ete(p, u, s("ete"), ETE_N),
            "eg": eg(p, u, s("eg"), EPS), "ucb": ucb(p, u, s("ucb"))}


def rows(season, upto=None):
    out = [[] for _ in PRODUCTS]
    for i, tap, _ in season[:upto]:
        out[i].append(tap)
    return out


def taps_of(season):
    return sum(tap for _, tap, _ in season)


def ete_averages(p, T, S):
    """Estimate then exploit's average rate for every n from 0 to T - K over S seasons (MB.sim.eteAverages): season s
    has the moods of seed 5000000 + s and the strategy's stream 7000000 + s."""
    K, N = len(p), T - len(p)
    rate = [0.0] * (N + 1)
    for s in range(S):
        m, r = mulberry32(5000000 + s), mulberry32(7000000 + s)
        u = [m() for _ in range(T)]
        v = [r() for _ in range(N + 1)]
        after = []
        for k in range(K):
            a = [0] * (T + 1)
            for t in range(T - 1, -1, -1):
                a[t] = a[t + 1] + (u[t] < p[k])
            after.append(a)
        shown = [1] * K
        taps = [1 if u[k] < p[k] else 0 for k in range(K)]
        total = sum(taps)
        for n in range(N + 1):
            t = K + n
            if t >= T:
                rate[n] += total / T
                break
            est = [taps[k] / shown[k] for k in range(K)]
            mx = -math.inf
            for e in est:
                if e > mx + TOL:
                    mx = e
            tied = [k for k in range(K) if abs(est[k] - mx) <= TOL]
            w = tied[int(v[n] * len(tied))] if len(tied) > 1 else tied[0]
            rate[n] += (total + after[w][t]) / T
            i = int(v[n] * K)
            shown[i] += 1
            if u[t] < p[i]:
                taps[i] += 1
                total += 1
    return [x / S for x in rate]


def dec(x):
    """At most two decimals, as the game writes a number: 0.6, 0.67, 1, 0."""
    text = "%.2f" % (round(x * 100) / 100)
    return text.rstrip("0").rstrip(".") if "." in text else text


# THE NUMBERS: BANDITS

N = {}   # name: the string the notes print

assert URN_W / URN_N == CUSTOMERS["Cinderella"][3] == 0.4
CIN, RAP = CUSTOMERS["Cinderella"], CUSTOMERS["Rapunzel"]
RACES = {"Cinderella": race(CIN), "Rapunzel": race(RAP)}
TAPS = {who: {key: taps_of(s) for key, s in r.items()} for who, r in RACES.items()}
assert TAPS["Cinderella"] == {"queen": 60, "random": 31, "ete": 47, "eg": 47, "ucb": 52}, TAPS["Cinderella"]
assert TAPS["Rapunzel"] == {"queen": 78, "random": 32, "ete": 61, "eg": 67, "ucb": 70}, TAPS["Rapunzel"]
RC = RACES["Cinderella"]
assert all(i == 0 for i, _, _ in RC["queen"])                        # the Queen's mirror: the vacuum every morning
assert all(i == 1 for i, _, _ in RACES["Rapunzel"]["queen"])         # at Rapunzel's: the ladder

# Estimate then exploit: the board after the test (initialize, then 20 cards from the hat: mornings 1 to 25).
K = len(PRODUCTS)
TEST = K + ETE_N
ETE_ROWS = rows(RC["ete"], TEST)
assert [[int(x) for x in r] for r in ETE_ROWS] == [[0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0],
                                                    [0, 0, 0, 0, 1]], ETE_ROWS
ETE_EST = [sum(r) / len(r) for r in ETE_ROWS]
WIN = argmax_all(ETE_EST)
assert WIN == [0] and dec(ETE_EST[0]) == "0.67" and dec(ETE_EST[3]) == "0.38"
assert all(i == 0 and ph == "exploit" for i, _, ph in RC["ete"][TEST:])
N["ete test taps"] = sum(tap for _, tap, _ in RC["ete"][:TEST])
N["ete after taps"] = sum(tap for _, tap, _ in RC["ete"][TEST:])
assert (N["ete test taps"], N["ete after taps"]) == (6, 41)

# Choosing n: the average rate of every n over AVG_S seasons for both collections (the last chart of section 3).
AVERAGES = {}
for title, (who, items) in COLLECTIONS.items():
    v = ete_averages([q for _, q in items], SEASON, AVG_S)
    mx = max(v)
    near = [n for n, x in enumerate(v) if x > mx - NEAR]
    AVERAGES[title] = {"v": v, "best": v.index(mx), "near": near}
N["ball near"] = "%d to %d" % (AVERAGES["Ready for the ball"]["near"][0], AVERAGES["Ready for the ball"]["near"][-1])
N["hair near"] = "%d to %d" % (AVERAGES["Long hair"]["near"][0], AVERAGES["Long hair"]["near"][-1])

# Epsilon-greedy: the hat's count, the morning from which the medal always picked the vacuum, the rows at the end.
EGS = RC["eg"]
HATS = sum(1 for _, _, ph in EGS if ph == "explore")
SPINS = SEASON - K
last_off = max(t for t, (i, _, ph) in enumerate(EGS) if ph == "exploit" and i != 0)
LOCK = next(t for t in range(max(last_off + 1, K), SEASON) if EGS[t][2] == "exploit")
EG_SHOWN = [len(r) for r in rows(EGS)]
assert (HATS, SPINS, LOCK + 1, EG_SHOWN) == (16, 95, 19, [71, 6, 2, 16, 5]), (HATS, SPINS, LOCK + 1, EG_SHOWN)

# UCB: the board after 10 mornings (the dark bar and the light bar), each number in hundredths as the game shows it.
UCB_ROWS = rows(RC["ucb"], UCB_AT)
UCB_BOARD = []
for k, r in enumerate(UCB_ROWS):
    n, t = len(r), sum(r)
    e, b = round(100 * t / n), round(100 / math.sqrt(n))
    UCB_BOARD.append({"n": n, "t": t, "e": e / 100, "b": b / 100, "s": (e + b) / 100})
assert [(x["n"], x["t"]) for x in UCB_BOARD] == [(4, 3), (1, 0), (1, 0), (3, 1), (1, 0)], UCB_BOARD
LEAD = argmax_all([x["s"] for x in UCB_BOARD])
assert LEAD == [0] and dec(UCB_BOARD[0]["s"]) == "1.25" and dec(UCB_BOARD[3]["s"]) == "0.91"
assert RC["ucb"][UCB_AT][0] == 0                                     # morning 11 shows the vacuum

# THE NUMBERS: MATRIX FACTORIZATION ON A GRID


def predict(U, V):
    return [[sum(U[i][k] * V[j][k] for k in range(2)) for j in range(6)] for i in range(6)]


def block_sums(U, V, R):
    P = predict(U, V)
    out = [[0.0] * 3 for _ in range(3)]
    for i in range(6):
        for j in range(6):
            out[i // BS][j // BS] += (R[i][j] - P[i][j]) ** 2
    return out


def total(U, V, R):
    return sum(map(sum, block_sums(U, V, R)))


def slopes(U, V, R, eps):
    """Every number's slope from a hop of eps at the same guess, in closed form (grid.html, slopesAt):
    (total after - total before) / eps = sum of -2 x partner x (rating - prediction) + eps x partner^2."""
    P = predict(U, V)
    su = [[sum(-2 * V[j][k] * (R[i][j] - P[i][j]) + eps * V[j][k] ** 2 for j in range(6)) for k in range(2)]
          for i in range(6)]
    sv = [[sum(-2 * U[i][k] * (R[i][j] - P[i][j]) + eps * U[i][k] ** 2 for i in range(6)) for k in range(2)]
          for j in range(6)]
    return su, sv


R, U0, V0, G_EPS, G_ALPHA = GRID["R"], GRID["U0"], GRID["V0"], GRID["eps"], GRID["alpha"]
NR, NG = 36, 24
JOB = NR + NG + NR + NR
assert (JOB, POOL * ROOM, 4 + 4 + 4 + 4 + 4 + 1) == (132, 315, ROOM)
assert NR > ROOM and NG > ROOM and 12 <= ROOM          # neither table fits; one factor alone would
SUMS0 = block_sums(U0, V0, R)
assert SUMS0 == [[50, 5, 46], [42, 54, 87], [40, 21, 42]] and total(U0, V0, R) == 387, SUMS0
f, kk = GRID["hop"]["film"], GRID["hop"]["k"]
V1 = [row[:] for row in V0]
V1[f][kk] = round(V1[f][kk] + G_EPS, 9)
SUMS1 = block_sums(U0, V1, R)
L0, L1 = total(U0, V0, R), total(U0, V1, R)
SLOPE = (L1 - L0) / G_EPS
NEXT = V0[f][kk] - G_ALPHA * SLOPE
column = [SUMS1[b][f // BS] for b in range(3)]
assert [round(x, 4) for x in column] == [4.9005, 53.8005, 21.0405], column
assert all(SUMS1[b][c] == SUMS0[b][c] for b in range(3) for c in range(3) if c != f // BS)
assert round(L1, 4) == 386.7415 and round(SLOPE, 2) == -25.85 and round(NEXT, 4) == -0.6381, (L1, SLOPE, NEXT)
su, sv = slopes(U0, V0, R, G_EPS)
assert abs(sv[f][kk] - SLOPE) < 1e-9
# The run: every number moves at once, round after round, while the total falls.
U, V, losses = U0, V0, [L0]
for _ in range(200):
    su, sv = slopes(U, V, R, G_EPS)
    U = [[U[i][k] - G_ALPHA * su[i][k] for k in range(2)] for i in range(6)]
    V = [[V[j][k] - G_ALPHA * sv[j][k] for k in range(2)] for j in range(6)]
    losses.append(total(U, V, R))
    if len(losses) > 2 and losses[-1] >= losses[-2]:
        break
FALLS = len(losses) - 2                                  # the last round whose total is lower than the one before
assert FALLS == GRID["play"] == 78, FALLS
first_below = lambda x: next(r for r, l in enumerate(losses) if l < x)
BELOW = {x: first_below(x) for x in (1, 0.1, 0.01)}
assert BELOW == {1: 30, 0.1: 40, 0.01: 51} and BELOW[0.01] == GRID["rounds"], BELOW
U, V = U0, V0
for _ in range(FALLS):
    su, sv = slopes(U, V, R, G_EPS)
    U = [[U[i][k] - G_ALPHA * su[i][k] for k in range(2)] for i in range(6)]
    V = [[V[j][k] - G_ALPHA * sv[j][k] for k in range(2)] for j in range(6)]
END = total(U, V, R)
GAP = max(abs(p - r) for pr, rr in zip(predict(U, V), R) for p, r in zip(pr, rr))
assert "%.4f" % END == "0.0028" and GAP < 0.022 and "%.4f" % GAP == "0.0216", (END, GAP)

# THE NUMBERS: COMPUTING CLUSTERS, each derived number recomputed from the deck's inputs.

assert 2688 * 4 == 10752 and 24 * 8 * 7 * 2 == 2688                  # cabinets, chassis, blades, nodes, sockets
assert round(990e12 / 4.023e12) == 246                               # FLOP per byte
assert round(4023 / 25) == 161                                       # the four links, end to end
assert 660 * 1 / 1000 == 0.66 and round(0.66 * 8, 1) == 5.3          # kWh of one hour, Rappen at 8 per kWh
assert round(10752 * 660 / 1e6, 1) == 7.1 and round(10752 * 660 / 1000 * 0.08, -1) == 570
assert 6 * 10**6 * 10**6 == 6 * 10**12 and 6 * 10**12 / (50 * 10**9) == 120
assert abs(6 * 70e9 * 15e12 - 6.30e24) < 1e12
assert round(6e6 / 4096 / 24) == 61 and round(6e6 / (91 * 24)) == 2747
assert abs(6e6 * 660 / 1e9 * 1e3 - 3.96e3) < 1e-6                    # GPU hours x W = Wh: 3.96 GWh
assert round(6e6 * 660 / 1000 * 0.08 / 1e6, 2) == 0.32 and 6e6 * 2.5 == 15.0e6

# THE COPIES AGAINST THEIR SOURCES


def node_json(script):
    out = subprocess.run(["node", "-e", script], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def compare_with_private():
    if not PRIVATE.is_dir():
        print("w2-cx-private not found beside this repository: the copies of the games were not compared")
        return
    core = (BANDITS / "core.js").read_text()
    assert "MB.SEASON = %d;" % SEASON in core
    assert re.findall(r'name: "([^"]+)", short:', core) == PRODUCTS
    for who, p in CUSTOMERS.items():
        m = re.search(r'name: "%s".*?p: \[([^\]]+)\]' % who, core)
        assert [float(x) for x in m.group(1).split(",")] == p, who
    for title, (who, items) in COLLECTIONS.items():
        block = core[core.index('title: "%s"' % title):]
        block = block[:block.index("] }")]
        assert [(a, float(b)) for a, b in re.findall(r'name: "([^"]+)", p: ([0-9.]+)', block)] == items, title
    assert "MB.ETE_N = %d;" % ETE_N in core and "MB.EPS = %s;" % EPS in core and "seed: %d" % RACE in core
    for key, k in STREAMS.items():
        assert "%s: 10 * MB.RACE.seed + %d" % (key, k) in core, key
    sec1 = (BANDITS / "sec1.js").read_text()
    assert "const URN_W = %d, URN_N = %d;" % (URN_W, URN_N) in sec1
    sec3 = (BANDITS / "sec3.js").read_text()
    assert "const NS = %s;" % json.dumps(NS) in sec3 and "const AVG_S = %d;" % AVG_S in sec3
    assert "if (x > mx - %s) near.push(n);" % NEAR in sec3
    assert "const XT = %d," % UCB_AT in (BANDITS / "sec5.js").read_text()
    grid_js = (GRID_DIR / "data.js").read_text()
    g = json.loads(re.search(r"window\.GRID = (\{.*\});", grid_js).group(1))
    for key in ("seed", "eps", "alpha", "tol", "customers", "R", "U0", "V0", "hop", "rounds", "play"):
        assert g[key] == GRID[key], key
    assert [x["t"] for x in g["films"]] == GRID["films"]
    html = (GRID_DIR / "grid.html").read_text()
    assert "var ROOM = %d;" % ROOM in html and "var POOL = %d;" % POOL in html
    print("the copies equal the data of w2-cx-private")
    if not shutil.which("node"):
        print("node not found: the seasons were not compared with sim.js")
        return
    sim = json.dumps(str(BANDITS / "sim.js"))
    script = """
const S = require(%s), out = {};
for (const [who, p] of Object.entries(%s)) {
  const u = S.moods(%d, %d), s = (k) => 10 * %d + k;
  const seasons = { queen: S.queen(p, u), random: S.random(p, u, s(1)), ete: S.ete(p, u, s(2), %d),
    eg: S.eg(p, u, s(3), %s), ucb: S.ucb(p, u, s(4)) };
  out[who] = {};
  for (const [k, z] of Object.entries(seasons)) out[who][k] = z.mornings.map((m) => [m.i, m.tap ? 1 : 0]);
}
out.avg = {};
for (const [title, c] of Object.entries(%s)) out.avg[title] = S.eteAverages(c, %d, %d).rate;
process.stdout.write(JSON.stringify(out));
""" % (sim, json.dumps(CUSTOMERS), RACE, SEASON, RACE, ETE_N, EPS,
       json.dumps({t: [q for _, q in items] for t, (_, items) in COLLECTIONS.items()}), SEASON, AVG_S)
    js = node_json(script)
    for who, r in RACES.items():
        for key, season in r.items():
            assert js[who][key] == [[i, int(tap)] for i, tap, _ in season], (who, key)
    for title, a in AVERAGES.items():
        assert all(abs(x - y) < 1e-12 for x, y in zip(js["avg"][title], a["v"])), title
    print("the seasons and the averages equal those of sim.js, morning by morning")


def compare_with_deck():
    text = "\n".join(p.read_text() for p in DECK if p.exists())
    if not text:
        print("the clusters deck was not found: its numbers were not compared")
        return
    missing = [name for name, (s, _) in DECK_NUMBERS.items() if s not in text]
    assert not missing, "not in the deck: %s" % missing
    print("the deck prints all %d of its numbers that the notes use" % len(DECK_NUMBERS))


# THE TABLES


def write(name, text):
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text("% GENERATED by tools/afternoon_numbers.py: do not edit, run the script.\n" + text)


def num(x):
    return "$%s$" % x


def probabilities_table():
    lines = [r"\begin{tabular}{|l|" + "c|" * K + "}", r"\hline",
             " & " + " & ".join(PRODUCTS) + r" \\ \hline"]
    for who, p in CUSTOMERS.items():
        lines.append(who + " & " + " & ".join(num(dec(x)) for x in p) + r" \\ \hline")
    lines.append(r"\end{tabular}")
    write("bandits-probabilities.tex", "\n".join(lines) + "\n")


def dots(row):
    return r"\,".join(r"$\bullet$" if x else r"$\circ$" for x in row)


def ete_board():
    lines = [r"\begin{tabular}{|c|c|l|l|}", r"\hline", r"$\hat p$ & & Product & Showings \\ \hline"]
    for k, r in enumerate(ETE_ROWS):
        lines.append("%s & $%d/%d$ & %s & %s \\\\ \\hline" % (num(dec(ETE_EST[k])), sum(r), len(r), PRODUCTS[k],
                                                              dots(r)))
    lines.append(r"\end{tabular}")
    write("bandits-ete-board.tex", "\n".join(lines) + "\n")


def ucb_table():
    """The board of UCB after UCB_AT mornings; the estimate's fraction gives the taps and the showings."""
    lines = [r"\begin{tabular}{|l|c|c|c|}", r"\hline",
             r"Product & Estimate & Bonus & \begin{tabular}[b]{@{}c@{}}Estimate\\ + bonus\end{tabular} \\ \hline"]
    for k, (r, x) in enumerate(zip(UCB_ROWS, UCB_BOARD)):
        assert (x["t"], x["n"]) == (sum(r), len(r))
        bonus = r"$1/\sqrt{%d} = %s$" % (x["n"], dec(x["b"])) if x["n"] > 1 else r"$1/\sqrt{1} = 1$"
        lines.append("%s & $%d/%d = %s$ & %s & %s \\\\ \\hline" % (
            PRODUCTS[k], x["t"], x["n"], dec(x["e"]), bonus, num(dec(x["s"]))))
    lines.append(r"\end{tabular}")
    write("bandits-ucb.tex", "\n".join(lines) + "\n")


def race_table():
    names = [("queen", "Queen's mirror"), ("ucb", "UCB"), ("eg", r"Epsilon-greedy, $\varepsilon = %s$" % EPS),
             ("ete", "Estimate then exploit, $n = %d$" % ETE_N), ("random", "Random")]
    lines = [r"\begin{tabular}{|l|c|c|}", r"\hline", r"Mirror & Cinderella & Rapunzel \\ \hline"]
    for key, name in names:
        lines.append("%s & %d & %d \\\\ \\hline" % (name, TAPS["Cinderella"][key], TAPS["Rapunzel"][key]))
    lines.append(r"\end{tabular}")
    write("bandits-race.tex", "\n".join(lines) + "\n")


def grid_figure():
    """The grid of slide 3 of Matchmaker on a Grid: A computers on the left, B computers on top, C computers where
    they meet, each C with the sum of its 4 losses at the first guess."""
    cw, ch, aw, bh = 3.2, 0.55, 2.8, 1.2                                # cm
    out = [r"\begin{tikzpicture}[x=1cm, y=1cm, every node/.style={font=\small, align=center, inner sep=2pt}]"]
    cust, films = GRID["customers"], GRID["films"]
    for b in range(3):
        x = aw + 0.3 + b * (cw + 0.2) + cw / 2
        out.append(r"\node[draw, text width=%.2fcm, minimum height=%.2fcm] at (%.2f, 0) {B%d\\ "
                   r"{\footnotesize %s\\ %s\strut}};" % (cw - 0.2, bh, x, b + 1, films[2 * b], films[2 * b + 1]))
    for a in range(3):
        y = -(bh / 2 + 0.2 + ch / 2) - a * (ch + 0.15)
        out.append(r"\node[draw, text width=%.2fcm, minimum height=%.2fcm] at (%.2f, %.2f) {A%d: "
                   r"{\footnotesize %s, %s}};" % (aw - 0.2, ch, aw / 2, y, a + 1, cust[2 * a], cust[2 * a + 1]))
        for b in range(3):
            x = aw + 0.3 + b * (cw + 0.2) + cw / 2
            out.append(r"\node[draw, text width=%.2fcm, minimum height=%.2fcm] at (%.2f, %.2f) {C%d%d: sum %d};"
                       % (cw - 0.2, ch, x, y, a + 1, b + 1, SUMS0[a][b]))
    out.append(r"\node at (%.2f, 0) {total loss\\ %d};" % (aw / 2, L0))
    out.append(r"\end{tikzpicture}")
    write("computing-grid.tex", "\n".join(out) + "\n")


# THE PDF

BALL, HAIR = dict(COLLECTIONS["Ready for the ball"][1]), dict(COLLECTIONS["Long hair"][1])
assert sorted(BALL.values()) == [0.6, 0.6, 0.6, 0.9, 0.95] and sorted(HAIR.values()) == [0.02] * 4 + [0.95]
EXPECTED = [  # strings the PDF must contain (a minus sign is read as a hyphen, a times sign as x)
    "2/5 = 0.4",
    "Random: %d taps, rate %s" % (TAPS["Cinderella"]["random"], dec(TAPS["Cinderella"]["random"] / SEASON)),
    "%d taps, rate %s" % (TAPS["Cinderella"]["queen"], dec(TAPS["Cinderella"]["queen"] / SEASON)),
    "1 in %d" % K, "ladder, p = %s" % dec(RAP[1]),
    "mornings 1 to %d. The vacuum leads with %s; the mirror shows it on mornings %d to %d" % (
        TEST, dec(ETE_EST[0]), TEST + 1, SEASON),
    "over {:,} seasons, best n within {}".format(AVG_S, NEAR),
    "satnav %d. Taps: %d" % (EG_SHOWN[4], TAPS["Cinderella"]["eg"]),
    "after %d mornings" % UCB_AT, "Taps in the season: %d" % TAPS["Cinderella"]["ucb"],
    "keeps %d numbers: %d ratings, %d guessed numbers, %d predictions, %d losses" % (JOB, NR, NG, NR, NR),
    "%d computers of %d places each, %d in all" % (POOL, ROOM, POOL * ROOM),
    "with alpha = %s" % G_ALPHA,
    "Taps: %d on mornings 1 to %d, %d after, %d in all" % (N["ete test taps"], TEST, N["ete after taps"],
                                                   TAPS["Cinderella"]["ete"]),
    "best n %s" % N["ball near"], "best n %s" % N["hair near"],
    "ball gown %s, tiara %s, three products at %s" % (dec(BALL["Ball gown"]), dec(BALL["Tiara"]),
                                                      dec(BALL["Silk gloves"])),
    "ribbon %s, four products at %s" % (dec(HAIR["Ribbon"]), dec(HAIR["Scissors"])),
    "%d times in %d spins" % (HATS, SPINS), "From morning %d on" % (LOCK + 1),
    "vacuum %d, ladder %d, blower %d, mattress %d, satnav %d" % tuple(EG_SHOWN),
    "the vacuum, %s" % dec(UCB_BOARD[0]["s"]), "on morning %d" % (UCB_AT + 1),
    "387", "4.9005", "53.8005", "21.0405", "386.7415", "(386.7415 - 387)/0.01 = -25.85",
    "-1 - 0.014 x (-25.85) = -0.64", "after round %d" % BELOW[1], "after round %d" % BELOW[0.01],
    "after round %d, at 0.0028" % FALLS, "within 0.022",
    "132", "315", "10,752", "246 FLOP per byte", "161 times", "4,023 GB/s", "900 GB/s", "150 GB/s",
    "25 GB/s per GPU", "5.3 Rappen", "120 seconds", "2,747", "3.96 GWh",
    "0.32 million francs", "15.0 million",
]
FORBIDDEN = ["average loss", "10.75"]   # the loss of matrix factorization is the total since 2026-11-11


def check_pdf(pdf):
    # Two extractions: -layout keeps the lines of a table, -raw (content order) keeps a text set beside a table whole.
    text = "\n".join(subprocess.run(["pdftotext"] + mode + [str(pdf), "-"], capture_output=True, text=True,
                                    check=True).stdout for mode in (["-layout"], ["-raw"]))
    dashes = [c for c in text if c in (chr(8211), chr(8212))]
    assert not dashes, "%d en or em dashes in the PDF" % len(dashes)
    flat = re.sub(r"\s+", " ", text.replace(chr(8722), "-").replace(chr(215), "x").replace(chr(945), "alpha"))
    missing = [s for s in EXPECTED if s not in flat]
    assert not missing, "not in the PDF: %s" % missing
    found = [s for s in FORBIDDEN if s.lower() in flat.lower()]
    assert not found, "still in the PDF: %s" % found
    print("%s: no dashes, all %d expected strings present, none of %s" % (pdf.name, len(EXPECTED), FORBIDDEN))


def main():
    compare_with_private()
    compare_with_deck()
    probabilities_table()
    ete_board()
    ucb_table()
    race_table()
    grid_figure()
    print("race season, taps:", TAPS)
    print("estimate then exploit after the test:", [f"{sum(r)}/{len(r)}" for r in ETE_ROWS],
          "taps in the test and after:", N["ete test taps"], N["ete after taps"])
    print("best n:", {t: (a["near"][0], a["near"][-1], a["best"]) for t, a in AVERAGES.items()})
    print("epsilon-greedy: hats %d in %d spins, the vacuum from morning %d, showings %s" % (HATS, SPINS, LOCK + 1,
                                                                                         EG_SHOWN))
    print("UCB after %d mornings:" % UCB_AT, [(x["t"], x["n"], dec(x["s"])) for x in UCB_BOARD])
    print("grid: total %s, column %s, after %.4f, slope %.2f, next %.4f, below %s, falls %d to %.4f, gap %.4f"
          % (L0, [round(x, 4) for x in column], L1, SLOPE, NEXT, BELOW, FALLS, END, GAP))
    for pdf in [a for a in sys.argv[1:] if a.endswith(".pdf")]:
        check_pdf(NOTES / pdf)


if __name__ == "__main__":
    main()
