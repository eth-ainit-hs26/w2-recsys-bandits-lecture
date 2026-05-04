#!/usr/bin/env python3
"""
Build a clean MovieLens 100K subset for the real-data block-diagonal puzzle.

The toy 21x16 matrix in the slides is rank-2 by construction.  This is real
ratings; the same trick (sort users and movies by SVD latent embedding)
reveals the same blocks.

We hand-curate four genre clusters (Children's & Family, Action & Adventure,
Drama, Comedy), each with 7 popular and reasonably polarising movies.  We
pick 50 users with the highest overlap on these 28 movies and adequate rating
variance.  After SVD on the centred matrix we cluster users and movies with
k-means (k=4) and order them by cluster-then-angle.

Output: visualizations/shared/movielens_subset.json
"""
import json
import math
import os
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(HERE, "movielens", "ml-100k")
OUT  = os.path.join(ROOT, "visualizations", "shared", "movielens_subset.json")

N_USERS  = 40
N_USER_CLUSTERS = 4
USER_MIN_OVERLAP = 22  # tighter: users who rated nearly every selected movie

# Hand-curated genre clusters.  Movie ids from MovieLens 100K's u.item.
CLUSTERS = {
    "Family":  [1, 132, 71, 95, 8, 588, 419],     # Toy Story, Wizard of Oz, Lion King, Aladdin, Babe, Beauty & Beast, Mary Poppins
    "Action":  [50, 174, 117, 172, 79, 210, 222], # Star Wars, Raiders, The Rock, Empire, Fugitive, Indy 3, ST: First Contact
    "Drama":   [100, 56, 98, 318, 64, 357, 191],  # Fargo, Pulp Fiction, Silence of the Lambs, Schindler's, Shawshank, Cuckoo's Nest, Amadeus
    "Comedy":  [294, 168, 269, 25, 238, 153, 194],# Liar Liar, Monty Python, Full Monty, Birdcage, Raising Arizona, Fish Called Wanda, The Sting
}
CLUSTER_NAMES = list(CLUSTERS.keys())
N_MOVIES = sum(len(v) for v in CLUSTERS.values())  # 28

# ---- read data ------------------------------------------------------
GENRES = []
with open(os.path.join(DATA, "u.genre")) as f:
    for line in f:
        line = line.strip()
        if not line: continue
        n, _ = line.split("|"); GENRES.append(n)

movies = {}
with open(os.path.join(DATA, "u.item"), encoding="latin-1") as f:
    for line in f:
        p = line.strip().split("|")
        gs = [GENRES[i] for i, b in enumerate(p[5:24]) if int(b)]
        movies[int(p[0])] = {"title": p[1], "genres": gs}

ratings = []
with open(os.path.join(DATA, "u.data")) as f:
    for line in f:
        u, m, r, _ = line.strip().split("\t")
        ratings.append((int(u), int(m), int(r)))

uratings = defaultdict(list)
mratings = defaultdict(list)
for u, m, r in ratings:
    uratings[u].append(r); mratings[m].append(r)

# ---- selected movies ------------------------------------------------
selected_mids = []
movie_curated_cluster = {}  # mid -> cluster name
for cname, mids in CLUSTERS.items():
    for mid in mids:
        selected_mids.append(mid)
        movie_curated_cluster[mid] = cname
selected_set = set(selected_mids)

print(f"Selected {len(selected_mids)} movies in {len(CLUSTERS)} clusters")
for cname, mids in CLUSTERS.items():
    print(f"  {cname}:")
    for mid in mids:
        rs = mratings[mid]
        print(f"     {movies[mid]['title'][:50]:<50}  "
              f"n={len(rs):>3} mean={np.mean(rs):.2f} std={np.std(rs):.2f}")

# ---- selected users -------------------------------------------------
user_overlap = defaultdict(int)
for u, m, _r in ratings:
    if m in selected_set:
        user_overlap[u] += 1

# require a reasonable rating variance so opinions actually differ
user_std = {u: float(np.std(rs)) for u, rs in uratings.items() if len(rs) >= 30}
cand = [u for u, c in user_overlap.items()
        if c >= USER_MIN_OVERLAP and user_std.get(u, 0) >= 1.0]
cand.sort(key=lambda u: (-user_overlap[u], -user_std.get(u, 0), u))
SHORTLIST = cand[:max(N_USERS * 3, 120)]
print(f"\nShortlist: {len(SHORTLIST)} users with overlap>={USER_MIN_OVERLAP} "
      f"and std>=1.0")

def build_R(user_ids):
    Rm = np.full((len(user_ids), N_MOVIES), np.nan)
    uid_idx = {u: i for i, u in enumerate(user_ids)}
    mid_idx = {m: i for i, m in enumerate(selected_mids)}
    for u, m, r in ratings:
        if u in uid_idx and m in mid_idx:
            Rm[uid_idx[u], mid_idx[m]] = r
    return Rm

def svd_embed(Rm):
    """Mean-impute, double-centre, SVD; return user-2d, movie-2d, sigma."""
    Rfilled = Rm.copy()
    for i in range(Rfilled.shape[0]):
        rm = np.nanmean(Rfilled[i])
        if np.isnan(rm):
            rm = float(np.nanmean(Rfilled))
        Rfilled[i, np.isnan(Rfilled[i])] = rm
    Rfilled -= Rfilled.mean(axis=1, keepdims=True)
    Rfilled -= Rfilled.mean(axis=0, keepdims=True)
    U_, S_, Vt_ = np.linalg.svd(Rfilled, full_matrices=False)
    return U_[:, :2] * S_[:2], Vt_[:2, :].T * S_[:2], S_

# Pass 1 -- big shortlist; pick the most opinionated by latent magnitude
R_big = build_R(SHORTLIST)
U2_big, _V2_big, _S = svd_embed(R_big)
mags = np.linalg.norm(U2_big, axis=1)
top_idx = np.argsort(-mags)[:N_USERS]
selected_users = [SHORTLIST[i] for i in top_idx]
selected_users.sort(key=lambda u: (-user_overlap[u], u))
print(f"Final: {len(selected_users)} users (top-{N_USERS} by latent magnitude)")

# ---- build the chosen-users matrix ---------------------------------
R = build_R(selected_users)
uid_to_idx = {u: i for i, u in enumerate(selected_users)}
mid_to_idx = {m: i for i, m in enumerate(selected_mids)}

obs = np.isnan(R).sum()
print(f"Matrix shape {R.shape}, missing {obs}/{R.size} = {obs/R.size*100:.1f}%")

# Mean-centred ternary: relative preference.
# Each user has their own rating mean; if a rating is at least USER_MEAN + 0.5
# above their mean we call it a like (+1); at least 0.5 below, a dislike (-1);
# else a neutral (0).  This strips out per-user lenience bias and brings out
# the cluster structure that absolute ratings hide.
mat_t = [[None] * N_MOVIES for _ in range(N_USERS)]
THRESH = 0.5
for i in range(N_USERS):
    rs = R[i, :]
    obs = ~np.isnan(rs)
    if obs.sum() == 0:
        continue
    user_mean = float(np.nanmean(rs))
    for j in range(N_MOVIES):
        if np.isnan(rs[j]):
            mat_t[i][j] = None
        elif rs[j] >= user_mean + THRESH:
            mat_t[i][j] = 1
        elif rs[j] <= user_mean - THRESH:
            mat_t[i][j] = -1
        else:
            mat_t[i][j] = 0

flat = [v for row in mat_t for v in row]
print(f"Ternary distribution: +1={sum(1 for v in flat if v==1)}  "
      f"-1={sum(1 for v in flat if v==-1)}  "
      f"0={sum(1 for v in flat if v==0)}  "
      f"null={sum(1 for v in flat if v is None)}")

# ---- SVD ------------------------------------------------------------
# impute missing with the user mean, then double-centre
R_imp = R.copy()
for i in range(N_USERS):
    rm = np.nanmean(R_imp[i])
    R_imp[i, np.isnan(R_imp[i])] = rm
um = R_imp.mean(axis=1, keepdims=True); R_imp -= um
mm = R_imp.mean(axis=0, keepdims=True); R_imp -= mm
U, S, Vt = np.linalg.svd(R_imp, full_matrices=False)
print(f"\nSingular values (top 5): {[round(s, 2) for s in S[:5]]}")

U2 = U[:, :2] * S[:2]
V2 = Vt[:2, :].T * S[:2]

# ---- k-means clustering on user / movie embeddings ------------------
def kmeans(X, k, n_iter=100, seed=11):
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(X), size=k, replace=False)
    centers = X[idx].copy()
    labels = np.zeros(len(X), dtype=int)
    for _ in range(n_iter):
        d = np.linalg.norm(X[:, None] - centers[None, :], axis=2)
        new_labels = d.argmin(axis=1)
        if (new_labels == labels).all():
            break
        labels = new_labels
        for j in range(k):
            mask = labels == j
            if mask.any():
                centers[j] = X[mask].mean(axis=0)
    return labels, centers

u_labels, u_centers = kmeans(U2, N_USER_CLUSTERS)
# For movies we already have curated clusters; reuse those for the labelling
m_label_to_idx = {c: i for i, c in enumerate(CLUSTER_NAMES)}
m_labels = np.array([m_label_to_idx[movie_curated_cluster[mid]]
                     for mid in selected_mids])
m_centers = np.array([V2[m_labels == c].mean(axis=0) for c in range(len(CLUSTER_NAMES))])

# ---- order clusters by polar angle of centroids --------------------
def order_by_angle(centers):
    angles = np.arctan2(centers[:, 1], centers[:, 0])
    return np.argsort(angles)

u_cluster_order = order_by_angle(u_centers).tolist()
m_cluster_order = order_by_angle(m_centers).tolist()

u_label_rank = {int(c): r for r, c in enumerate(u_cluster_order)}
m_label_rank = {int(c): r for r, c in enumerate(m_cluster_order)}

u_angle = np.arctan2(U2[:, 1], U2[:, 0])
m_angle = np.arctan2(V2[:, 1], V2[:, 0])

def reveal(labels, label_rank, angles, n):
    return sorted(range(n), key=lambda i: (label_rank[int(labels[i])], angles[i]))

reveal_users  = reveal(u_labels, u_label_rank, u_angle, N_USERS)
reveal_movies = reveal(m_labels, m_label_rank, m_angle, N_MOVIES)

# ---- describe each user cluster by avg per movie cluster ------------
def user_cluster_profile(c):
    members = [i for i in range(N_USERS) if u_labels[i] == c]
    profile = {}
    for cn in CLUSTER_NAMES:
        midxs = [j for j in range(N_MOVIES)
                 if movie_curated_cluster[selected_mids[j]] == cn]
        vals = [R[i, j] for i in members for j in midxs if not np.isnan(R[i, j])]
        profile[cn] = float(np.mean(vals)) if vals else None
    return profile

# ---- output JSON ----------------------------------------------------
def safe(x, d=4):
    if x is None: return None
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)): return None
    return round(float(x), d)

users_out = []
for i, u in enumerate(selected_users):
    users_out.append({
        "id": int(u),
        "n_ratings_in_subset": int(user_overlap[u]),
        "embedding": [safe(U2[i, 0]), safe(U2[i, 1])],
        "cluster": int(u_labels[i]),
    })

movies_out = []
for i, m in enumerate(selected_mids):
    movies_out.append({
        "id": int(m),
        "title": movies[m]["title"],
        "genres": movies[m]["genres"],
        "n_ratings_total": int(len(mratings[m])),
        "embedding": [safe(V2[i, 0]), safe(V2[i, 1])],
        "cluster_name": movie_curated_cluster[m],
        "cluster": int(m_labels[i]),
    })

user_clusters_meta = []
for c in u_cluster_order:
    members = [i for i in range(N_USERS) if u_labels[i] == c]
    user_clusters_meta.append({
        "cluster": int(c),
        "n": len(members),
        "profile": user_cluster_profile(c),
    })

movie_clusters_meta = []
for c in m_cluster_order:
    members = [i for i in range(N_MOVIES) if m_labels[i] == c]
    movie_clusters_meta.append({
        "cluster": int(c),
        "name":    CLUSTER_NAMES[c],
        "n":       len(members),
    })

out = {
    "n_users": N_USERS, "n_movies": N_MOVIES,
    "users":   users_out, "movies": movies_out,
    "matrix":  mat_t,
    "matrix_raw": [[None if math.isnan(R[i, j]) else int(R[i, j])
                    for j in range(N_MOVIES)] for i in range(N_USERS)],
    "singular_values": [safe(s) for s in S[:6]],
    "reveal": {"user_order": reveal_users, "movie_order": reveal_movies},
    "user_clusters":  user_clusters_meta,
    "movie_clusters": movie_clusters_meta,
    "cluster_names":  CLUSTER_NAMES,
    "source": {
        "name":     "MovieLens 100K",
        "url":      "https://grouplens.org/datasets/movielens/100k/",
        "citation": "F. M. Harper and J. A. Konstan, "
                    "The MovieLens Datasets: History and Context, "
                    "ACM TiiS 5(4), 2015.",
    },
    "subset_params": {
        "n_users": N_USERS, "n_movies": N_MOVIES,
        "user_min_overlap": USER_MIN_OVERLAP,
    },
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(out, f, separators=(",", ":"))
print(f"\nWrote {OUT}  ({os.path.getsize(OUT)} bytes)")

# ---- ASCII reveal sanity-check --------------------------------------
def render(matrix, urs, mrs):
    chars = {1: "+", -1: "-", 0: ".", None: " "}
    return "\n".join("".join(chars[matrix[ui][mi]] for mi in mrs) for ui in urs)

print("\n--- scrambled (input order) ---")
print(render(mat_t, list(range(N_USERS)), list(range(N_MOVIES))))
print("\n--- reveal (cluster-sorted) ---")
print(render(mat_t, reveal_users, reveal_movies))
print("\nuser-cluster sizes (in reveal order):",
      [int((u_labels == c).sum()) for c in u_cluster_order])
print("movie-cluster sizes (in reveal order):",
      [int((m_labels == c).sum()) for c in m_cluster_order])
print("user-cluster names (by avg rating):")
for cm in user_clusters_meta:
    pr = cm["profile"]
    best = max(pr, key=lambda k: pr[k] if pr[k] is not None else -99)
    print(f"  cluster {cm['cluster']}: n={cm['n']}  best genre = {best} "
          f"(avg {pr[best]:.2f}); profile = "
          f"{ {k: round(v,2) if v else None for k,v in pr.items()} }")
print("movie-cluster names (in reveal order):",
      [CLUSTER_NAMES[c] for c in m_cluster_order])
