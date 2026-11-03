#!/usr/bin/env python3
"""Builds three-portraits.ipynb, the weekend 2 Colab notebook of AI in Industry (HS26).

Usage: python3 build_notebook.py [output.ipynb]
The notebook is written without outputs; Colab fills them in when it runs.
"""
import json
import sys

CELLS = []


def md(text):
    CELLS.append({"cell_type": "markdown", "metadata": {}, "source": text.strip("\n")})


def code(text):
    CELLS.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                  "outputs": [], "source": text.strip("\n")})


# ----------------------------------------------------------------------------------------------
md(r'''
# Three portraits of a product

**AI in Industry, weekend 2: Representation Learning.** A modern recommender on real Amazon data, built from start to finish in one Colab notebook.

A shop can describe each of its products in three ways. Each way is a list of numbers, which the field calls an *embedding*:

1. **Portrait 1, what the shop says about it.** A ready-made language model reads the product's name, shelf and brand, and turns them into 384 numbers. Products described alike get similar numbers. This model never sees what customers do.
2. **Portrait 2, what customers do with it.** A recommender learns 64 numbers per product from 800,000 reviews. Products reviewed by the same customers get similar numbers. This model never reads a product name.
3. **Portrait 3, where it sits in the shop.** The numbers of portrait 1 are sorted into aisles and shelves, so every product gets a short address such as `12-07-3`. A small generative model then writes the address of a customer's next product, one number at a time, the way a chatbot writes the next word.

The third portrait follows the newest recommenders at YouTube, Meta and Kuaishou, which write a customer's next product the way a chatbot writes the next word. Here you build all three portraits on 25,612 video games, consoles and accessories, compare what they recommend, and measure which one guesses a customer's next purchase most often.

**How to run it.** In the menu choose *Runtime > Change runtime type > T4 GPU*, then *Runtime > Run all*. On a T4 the whole notebook takes about 8 minutes. Each grey box is one step: its title says what it does, and *Show code* reveals how it does it. The boxes marked **Your turn** have a field you can change before you run them again.
''')

code(r'''
# @title Setup: libraries, random seed and GPU check { display-mode: "form" }
import importlib.util, subprocess, sys
if importlib.util.find_spec("sentence_transformers") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "sentence-transformers"], check=True)

import gzip, json, os, random, re, time, unicodedata, urllib.request
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from IPython.display import display

SEED = 0
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
rng = np.random.default_rng(SEED)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
if DEVICE == "cuda":
    print("Running on a GPU:", torch.cuda.get_device_name(0))
else:
    print("No GPU found. Everything still works, only more slowly.")
    print("For speed: Runtime > Change runtime type > T4 GPU, then Runtime > Run all.")
START = time.time()

# Chart colours, checked for colour-blind readers, and a quiet chart style
INK, INK2, PAPER, GRID = "#0b0b0b", "#52514e", "#fcfcfb", "#e5e4e0"
BLUE, ORANGE = "#2a78d6", "#eb6834"
FAMILY_COLOURS = {"PlayStation": "#2a78d6", "Nintendo": "#eb6834", "Xbox": "#1baf7a",
                  "PC and Mac": "#eda100", "Other": "#a3a29c"}
plt.rcParams.update({"figure.facecolor": PAPER, "axes.facecolor": PAPER, "axes.edgecolor": INK2,
                     "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "text.color": INK, "axes.spines.top": False, "axes.spines.right": False,
                     "font.size": 10})


def short(text, n=60):
    text = str(text)
    return text if len(text) <= n else text[: n - 3] + "..."


def show(df):
    display(df.style.hide(axis="index").set_properties(**{"text-align": "left"}))
''')

# ----------------------------------------------------------------------------------------------
md(r'''
## 1. The shop

The data are the *Video Games* category of **Amazon Reviews 2023**, collected by the McAuley Lab at UC San Diego (Hou et al., ACL 2026). We use its "5-core" version, in which every customer and every product has at least five reviews. A review stands in for a purchase, so the shop we see is the part of Amazon that its reviewers left a trace in.

The next step downloads about 115 MB: who reviewed what and when, and the catalogue with the name and the shelf of every product.
''')

code(r'''
# @title Download the reviews and the catalogue (about 115 MB) { display-mode: "form" }
BASE = "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023"
FILES = {"Video_Games.csv.gz": BASE + "/benchmark/5core/rating_only/Video_Games.csv.gz",
         "meta_Video_Games.jsonl.gz": BASE + "/raw/meta_categories/meta_Video_Games.jsonl.gz"}
os.makedirs("data", exist_ok=True)
for name, url in FILES.items():
    path = os.path.join("data", name)
    if not os.path.exists(path):
        print("Downloading", name, "...")
        urllib.request.urlretrieve(url, path + ".part")
        os.replace(path + ".part", path)

reviews = pd.read_csv("data/Video_Games.csv.gz")
wanted = set(reviews["parent_asin"])
catalogue = []
with gzip.open("data/meta_Video_Games.jsonl.gz", "rt", encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        if r["parent_asin"] in wanted:
            catalogue.append({"asin": r["parent_asin"],
                              "title": (r.get("title") or "").strip() or "(no name)",
                              "store": (r.get("store") or "").strip(),
                              "path": (r.get("categories") or [])[1:]})
products = pd.DataFrame(catalogue)

# Number the products from the most reviewed (number 0) to the least reviewed.
products["reviews"] = products["asin"].map(reviews["parent_asin"].value_counts())
products = products.sort_values(["reviews", "asin"], ascending=[False, True], ignore_index=True)
N = len(products)
TITLE = products["title"].to_numpy()
reviews["item"] = reviews["parent_asin"].map(dict(zip(products["asin"], range(N))))

FAMILIES = [("Nintendo", r"\b(Nintendo|Wii|GameCube|Game Boy|3DS|Switch)\b"),
            ("PlayStation", r"\b(PlayStation|PS2|PS3|PS4|PS5|PSP|PS Vita)\b"),
            ("Xbox", r"\bXbox\b"),
            ("PC and Mac", r"\b(PC|Mac|macOS|Windows|Linux|Steam)\b")]


def family(path, title):
    for text in (" ".join(path[:3]), title):
        for name, pattern in FAMILIES:
            if re.search(pattern, text):
                return name
    return "Other"


products["family"] = [family(p, t) for p, t in zip(products["path"], products["title"])]


def plain(text):
    """Small letters and no accents, so that "pokemon" also finds the accented spelling."""
    return "".join(c for c in unicodedata.normalize("NFKD", str(text)) if not unicodedata.combining(c)).lower()


PLAIN = pd.Series([plain(t) for t in TITLE])


def find(words):
    """The most reviewed product whose name contains these words (capitals and accents do not matter)."""
    hits = np.flatnonzero(PLAIN.str.contains(plain(words.strip()), regex=False).to_numpy())
    return int(hits[0]) if len(hits) else None


years = pd.to_datetime(reviews["timestamp"], unit="ms").dt.year
print(f"{reviews['user_id'].nunique():,} customers, {N:,} products and {len(reviews):,} reviews, "
      f"written between {years.min()} and {years.max()}.")
print("Products per console family:", ", ".join(f"{k} {v:,}" for k, v in products["family"].value_counts().items()))
print()
print("The ten most reviewed products:")
show(pd.DataFrame({"product": [short(t, 75) for t in TITLE[:10]], "reviews": products["reviews"].head(10)}))
''')

md(r'''
**One customer's story.** For every customer we hide the last product they reviewed. That review is the purchase the recommenders must guess. Everything before it is the customer's *history*, and it is all the recommenders may learn from.
''')

code(r'''
# @title Hide every customer's last review, and look at one customer { display-mode: "form" }
reviews["user"] = pd.factorize(reviews["user_id"])[0]
reviews = reviews.sort_values(["user", "timestamp", "item"], kind="stable", ignore_index=True)
sequences = reviews.groupby("user", sort=True)["item"].agg(list).tolist()
U = len(sequences)
histories = [s[:-1] for s in sequences]          # what the recommenders may learn from
hidden = np.array([s[-1] for s in sequences])    # the purchase they must guess
train_counts = np.bincount(np.concatenate([np.asarray(h) for h in histories]), minlength=N)

candidates = [u for u, s in enumerate(sequences) if 7 <= len(s) <= 10 and max(s) < 2000]
story = int(rng.choice(candidates))
mine = reviews[reviews["user"] == story]
table = pd.DataFrame({"date": pd.to_datetime(mine["timestamp"], unit="ms").dt.strftime("%Y-%m-%d").to_numpy(),
                      "product": [short(TITLE[i], 80) for i in mine["item"]]})
table.loc[len(table) - 1, "date"] += "  (hidden)"
print(f"Customer number {story} reviewed {len(mine)} products. The last one is hidden from all recommenders:")
show(table)
''')

# ----------------------------------------------------------------------------------------------
md(r'''
## 2. Portrait 1: what the shop says

For each product, the notebook joins three facts from Amazon's catalogue into one line of text, its *description*: the product's name, its shelf and its brand. A small language model from the Sentence Transformers project (*all-MiniLM-L6-v2*, 22 million parameters; Reimers and Gurevych, EMNLP 2019) reads that line and returns 384 numbers.

The model writes nothing, and the notebook does not train it: it is downloaded and used as it is. Its authors trained it once, on more than a billion pairs of related texts, such as a question and its answer, or a comment and the reply to it. During that training it had to pick out which text belonged with which, and so it learned to give texts with similar meaning similar numbers. It knows nothing about this shop or its customers.
''')

code(r'''
# @title Portrait 1: 384 numbers per product, read from its description { display-mode: "form" }
from huggingface_hub.utils import logging as hub_logging
from sentence_transformers import SentenceTransformer

hub_logging.set_verbosity_error()   # hides a notice about downloading the model without a Hugging Face account
reader = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device=DEVICE)
products["description"] = [". ".join([t] + ([" > ".join(p)] if p else []) + ([s] if s else []))
                           for t, p, s in zip(products["title"], products["path"], products["store"])]
t0 = time.time()
text_vec = reader.encode(products["description"].tolist(), batch_size=256, convert_to_numpy=True,
                         normalize_embeddings=True, show_progress_bar=True).astype(np.float32)
print(f"{N:,} products, {text_vec.shape[1]} numbers each, computed in {time.time() - t0:.0f} seconds.")
ex = find("Super Mario Odyssey")
print()
print("For example, the description:", repr(products["description"][ex]))
print("becomes the numbers", ", ".join(f"{x:+.3f}" for x in text_vec[ex, :6]), "and 378 more.")
''')

md(r'''
The numbers mean little one by one. What matters is which products end up close together. Closeness is measured with the *inner product*: multiply the two lists of numbers place by place, then add up the 384 results. The larger the sum, the more alike the two descriptions. Here are the five products closest to three well-known ones:
''')

code(r'''
# @title The five closest products in portrait 1 { display-mode: "form" }
def closest(vectors, item, k=5):
    sims = vectors @ vectors[item]
    sims[TITLE == TITLE[item]] = -np.inf   # the product itself, and copies of it listed under the same name
    top = np.argpartition(-sims, k)[:k]
    return top[np.argsort(-sims[top])]


SHOWCASE = ["Super Mario Odyssey", "DualShock 4 Wireless Controller", "PlayStation Plus: 12 Month"]
rows = []
for words in SHOWCASE:
    i = find(words)
    for r, j in enumerate(closest(text_vec, i)):
        rows.append({"product": short(TITLE[i], 45) if r == 0 else "",
                     "the five closest by description": short(TITLE[j], 75)})
show(pd.DataFrame(rows))
''')

# ----------------------------------------------------------------------------------------------
md(r'''
## 3. Portrait 2: what customers do

In *Once Upon a Cinema* you placed films on two axes by hand, and a customer's rating was the agreement between the customer's two numbers and the film's two numbers: multiply axis by axis, then add up. This model does the same with 64 axes, and the computer chooses the axes itself.

- Every product starts with 64 random numbers.
- A customer's 64 numbers are the average of the numbers of the products in their history (the last 20 at most), adjusted by one small learned step.
- A product's score for a customer is the agreement of the two lists of numbers.
- Training goes through every step of every history and nudges all the numbers, so that the product the customer reviewed next scores higher than the other 25,611.

Engineers call this a *two-tower model*: one tower computes the customer's numbers, the other the product's. YouTube described this design for its video recommendations in 2016 (Covington et al., RecSys 2016). The model sees only who reviewed what, and in which order. It never sees a name, a price or a picture.
''')

code(r'''
# @title Portrait 2: learn 64 numbers per product from who reviewed what { display-mode: "form" }
DIM, LAST, EPOCHS, BATCH = 64, 20, 10, 1024
PAD = N   # an extra, empty product that fills up short histories

# Every step of every history becomes one example: the (at most 20) products before it, and the product itself.
flat = np.concatenate([np.asarray(h, dtype=np.int64) for h in histories])
lengths = np.array([len(h) for h in histories])
position = np.arange(len(flat)) - np.repeat(np.cumsum(lengths) - lengths, lengths)
steps = np.flatnonzero(position >= 1)
offsets = np.arange(-LAST, 0)
inside = offsets[None, :] >= -position[steps][:, None]
past = torch.tensor(np.where(inside, flat[np.clip(steps[:, None] + offsets[None, :], 0, None)], PAD), device=DEVICE)
nxt = torch.tensor(flat[steps], device=DEVICE)
print(f"{len(nxt):,} training examples, each a history and the product reviewed right after it.")


class TwoTower(nn.Module):
    def __init__(self, n_products, dim):
        super().__init__()
        self.product = nn.Embedding(n_products + 1, dim, padding_idx=n_products)
        nn.init.normal_(self.product.weight, std=0.1)
        with torch.no_grad():
            self.product.weight[n_products].zero_()
        self.adjust = nn.Linear(dim, dim)

    def customer(self, hist):
        mask = (hist != PAD).unsqueeze(-1).float()
        average = (self.product(hist) * mask).sum(1) / mask.sum(1).clamp(min=1.0)
        return self.adjust(average)

    def scores(self, hist):
        return self.customer(hist) @ self.product.weight[:-1].T


tower = TwoTower(N, DIM).to(DEVICE)
optimiser = torch.optim.Adam(tower.parameters(), lr=2e-3)
print(f"A blind guess among {N:,} products has an average surprise of {np.log(N):.2f}.")
t0 = time.time()
for epoch in range(EPOCHS):
    tower.train()
    order = torch.randperm(len(nxt), device=DEVICE)
    total = 0.0
    for b in range(0, len(order), BATCH):
        idx = order[b:b + BATCH]
        loss = F.cross_entropy(tower.scores(past[idx]), nxt[idx])
        optimiser.zero_grad()
        loss.backward()
        optimiser.step()
        total += loss.item() * len(idx)
    print(f"pass {epoch + 1} of {EPOCHS}: average surprise {total / len(nxt):.2f}   ({time.time() - t0:.0f} s)")
tower.eval()
behaviour_vec = F.normalize(tower.product.weight[:-1].detach(), dim=1).cpu().numpy()
''')

md(r'''
The *surprise* printed above measures how unexpected the true next product was to the model; lower is better. Now the same three products, with their closest neighbours in both portraits side by side:
''')

code(r'''
# @title The same three products in both portraits { display-mode: "form" }
def side_by_side(i, k=5):
    a, b = closest(text_vec, i, k), closest(behaviour_vec, i, k)
    return pd.DataFrame({"Portrait 1: described alike": [short(TITLE[j], 58) for j in a],
                         "Portrait 2: reviewed by the same customers": [short(TITLE[j], 58) for j in b]})


for words in SHOWCASE:
    i = find(words)
    print(TITLE[i])
    show(side_by_side(i))
''')

md(r'''
**What to notice.** Portrait 1 finds look-alikes: other editions, colours and bundles of the same product. A shop shows such a list as *similar items*. Portrait 2 finds what the same customers also reviewed: for Super Mario Odyssey, a Switch controller, a screen protector and other things for the Switch; for the PlayStation controller, gaming headsets and games for other machines, a hint that its buyers play on more than one. A shop shows such a list as *customers also bought*. The two lists answer different questions, and a shop needs both.
''')

md(r'''
**Your turn.** Type part of a product name (for example *Pokemon*, *headset*, *Minecraft* or *racing wheel*) and run the box again. It takes the most reviewed product whose name contains your words.
''')

code(r'''
# @title Your turn: any product, in both portraits { display-mode: "form" }
words = "Pokemon"  # @param {type:"string"}
i = find(words)
if i is None:
    print(f"No product name contains {words!r}. Try a shorter word.")
else:
    print(f"{TITLE[i]}  ({products['reviews'][i]:,} reviews)")
    show(side_by_side(i))
''')

md(r'''
### Two maps of the same shop

Each portrait places the 2,000 most reviewed products in a space of many dimensions. The next step flattens both spaces onto a page with t-SNE (van der Maaten and Hinton, 2008), a method that keeps close products close, and colours each product by its console family. Six well-known products are circled.
''')

code(r'''
# @title Two maps of the shop (about a minute) { display-mode: "form" }
from sklearn.manifold import TSNE

TOP = 2000
fam = products["family"].to_numpy()[:TOP]
LANDMARKS = {"Super Mario Odyssey": "Super Mario Odyssey", "DualShock 4 Wireless Controller": "DualShock 4 controller",
             "PlayStation Plus: 12 Month": "PlayStation Plus", "Nintendo Switch Pro Controller": "Switch Pro Controller",
             "Xbox Live Gold": "Xbox Live Gold", "Skyrim VR": "Skyrim VR"}
marked = [(find(words), name) for words, name in LANDMARKS.items()]
marked = [(i, name) for i, name in marked if i is not None and i < TOP]
halo = [pe.withStroke(linewidth=3, foreground=PAPER)]
SPOTS = [(r, a) for r in (10, 35, 60, 85) for a in (45, 315, 135, 225, 90, 270, 0, 180)]


def label(ax, points, names):
    """Write each name beside its point where it covers no name written before, with a thin line if it moved away."""
    renderer = ax.figure.canvas.get_renderer()
    placed = []
    for (x, y), name in zip(points, names):
        for r, angle in SPOTS:
            dx, dy = r * np.cos(np.radians(angle)), r * np.sin(np.radians(angle))
            text = ax.annotate(name, (x, y), xytext=(dx, dy), textcoords="offset points", fontsize=9, color=INK,
                               ha="left" if dx > 1 else "right" if dx < -1 else "center",
                               va="bottom" if dy > 1 else "top" if dy < -1 else "center", path_effects=halo)
            box = text.get_window_extent(renderer).expanded(1.04, 1.2)
            if (r, angle) == SPOTS[-1] or not any(box.overlaps(b) for b in placed):
                placed.append(box)
                if r > 10:
                    ax.annotate("", (x, y), xytext=(dx, dy), textcoords="offset points",
                                arrowprops={"arrowstyle": "-", "color": INK2, "linewidth": 0.6, "shrinkA": 0, "shrinkB": 5})
                break
            text.remove()


fig, axes = plt.subplots(1, 2, figsize=(15, 7.2))
maps = []
for ax, (title, vectors) in zip(axes, [("Portrait 1: described alike", text_vec),
                                       ("Portrait 2: reviewed by the same customers", behaviour_vec)]):
    xy = TSNE(n_components=2, init="pca", perplexity=30, random_state=SEED).fit_transform(vectors[:TOP])
    maps.append(xy)
    for name, colour in FAMILY_COLOURS.items():
        m = fam == name
        ax.scatter(xy[m, 0], xy[m, 1], s=14, color=colour, edgecolors=PAPER, linewidths=0.4,
                   label=f"{name} ({m.sum():,})")
    ax.scatter(xy[[i for i, _ in marked], 0], xy[[i for i, _ in marked], 1], s=90, facecolors="none",
               edgecolors=INK, linewidths=1.3)
    ax.set_title(title, loc="left", fontsize=13)
    ax.set_xticks([])
    ax.set_yticks([])
    for side in ax.spines.values():
        side.set_visible(False)
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles[:5], labels[:5], loc="lower center", ncol=5, frameon=False, fontsize=10, markerscale=2)
fig.tight_layout(rect=(0, 0.06, 1, 1))
fig.canvas.draw()   # fixes the layout, so that the names can be placed where they do not overlap
for ax, xy in zip(axes, maps):
    label(ax, [xy[i] for i, _ in marked], [name for _, name in marked])
plt.show()
''')

md(r'''
**What to notice.** In portrait 1 the console families form clear regions, because the names say *PlayStation* or *Switch*. Portrait 2 never read a name, and still the Nintendo products gather in regions of their own: people who buy for a Nintendo console mostly stay with Nintendo. PlayStation and Xbox mix much more, a sign that many customers own both. And the six circled bestsellers sit close together in portrait 2, whatever their console: all kinds of customers buy them.
''')

# ----------------------------------------------------------------------------------------------
md(r'''
## 4. Portrait 3: an address in the shop, and a model that writes addresses

Portrait 3 starts from the numbers of portrait 1 and gives every product an address in an imaginary shop:

1. the 25,612 products are sorted into 64 **aisles**, so that products with similar descriptions share an aisle;
2. each aisle is split into **shelves** of products that are even more alike, about nine per shelf on average;
3. on each shelf, the most reviewed product gets **place** 0, the next one place 1, and so on.

Researchers call such addresses *semantic IDs*. This recipe of groups within groups comes from search engines (Tay et al., NeurIPS 2022); Google's TIGER brought addresses of this kind to recommendation (Rajput et al., NeurIPS 2023).
''')

code(r'''
# @title Portrait 3: give every product an address (aisle, shelf, place) { display-mode: "form" }
from sklearn.cluster import KMeans

AISLES, PER_SHELF, MAX_SHELVES = 64, 8, 64
t0 = time.time()
aisle_model = KMeans(n_clusters=AISLES, n_init=3, random_state=SEED).fit(text_vec)
aisle = aisle_model.labels_.astype(int)
shelf = np.zeros(N, dtype=int)
shelf_models = {}
for a in range(AISLES):
    members = np.flatnonzero(aisle == a)
    k = int(min(MAX_SHELVES, max(1, round(len(members) / PER_SHELF))))
    if k > 1:
        shelf_models[a] = KMeans(n_clusters=k, n_init=3, random_state=SEED).fit(text_vec[members])
        shelf[members] = shelf_models[a].labels_
place = np.zeros(N, dtype=int)
filled = {}
for i in range(N):   # products are numbered from the most reviewed, so place 0 holds a shelf's bestseller
    key = (aisle[i], shelf[i])
    place[i] = filled.get(key, 0)
    filled[key] = place[i] + 1
SHELVES, PLACES = int(shelf.max()) + 1, int(place.max()) + 1


def address(i):
    return f"{aisle[i]:02d}-{shelf[i]:02d}-{place[i]}"


print(f"{AISLES} aisles and {len(filled):,} shelves, with 1 to {PLACES} products per shelf ({time.time() - t0:.0f} s).")
print()
print("The twelve busiest aisles:")
busiest = pd.Series(products["reviews"].to_numpy()).groupby(aisle).sum().sort_values(ascending=False).index[:12]
show(pd.DataFrame({"aisle": [f"{a:02d}" for a in busiest],
                   "products": [int((aisle == a).sum()) for a in busiest],
                   "its three bestsellers": [" | ".join(short(TITLE[i], 42) for i in np.flatnonzero(aisle == a)[:3])
                                             for a in busiest]}))
print("Three addresses, each with the next products on the same shelf:")
for words in SHOWCASE:
    i = find(words)
    print()
    print(f"  {address(i)}  {short(TITLE[i], 70)}")
    for j in [j for j in np.flatnonzero((aisle == aisle[i]) & (shelf == shelf[i])) if j != i][:4]:
        print(f"  {address(j)}  {short(TITLE[j], 70)}")
''')

md(r'''
**The code writer.** A small Transformer, the architecture of ChatGPT in miniature, reads a customer's history as a string of addresses, for example `12 07 3 | 12 41 0 | 03 15 2`, and learns to write the next address one number at a time: first the aisle, then the shelf, then the place. Its training is the "guess the next word" training of language models: it reads every history and tries to continue it.

To recommend ten products, it writes the ten most likely addresses of products that exist in the shop and that the customer has not reviewed yet.
''')

code(r'''
# @title Portrait 3: train the code writer { display-mode: "form" }
BOS, BLANK = 0, 1             # a start sign, and a blank that fills up short histories
A0 = 2                        # the aisles come first among the code writer's "words", then shelves, then places
S0 = A0 + AISLES
P0 = S0 + SHELVES
VOCAB = P0 + PLACES
ITEMS = 20                    # the writer reads at most the last 20 products of a history
LENGTH = 1 + 3 * ITEMS


def tokens(i):
    return [A0 + int(aisle[i]), S0 + int(shelf[i]), P0 + int(place[i])]


rows = []
for h in histories:
    for end in range(len(h), 0, -ITEMS):
        seq = [BOS] + [t for i in h[max(0, end - ITEMS):end] for t in tokens(i)]
        rows.append(seq + [BLANK] * (LENGTH - len(seq)))
writer_data = torch.tensor(rows, dtype=torch.long)
print(f"{len(writer_data):,} histories written as addresses. Customer {story}'s history ends like this:")
print("   " + " | ".join(address(i).replace("-", " ") for i in histories[story][-5:]))


class CodeWriter(nn.Module):
    def __init__(self, vocab, length, d=128, layers=3, heads=4):
        super().__init__()
        self.token = nn.Embedding(vocab, d)
        self.position = nn.Embedding(length, d)
        layer = nn.TransformerEncoderLayer(d, heads, 4 * d, dropout=0.1, batch_first=True, norm_first=True)
        self.body = nn.TransformerEncoder(layer, layers, enable_nested_tensor=False)
        self.norm = nn.LayerNorm(d)
        self.head = nn.Linear(d, vocab)
        self.register_buffer("future", torch.triu(torch.ones(length, length, dtype=torch.bool), diagonal=1),
                             persistent=False)

    def forward(self, x, at=None):
        L = x.shape[1]
        h = self.norm(self.body(self.token(x) + self.position.weight[:L], mask=self.future[:L, :L]))
        if at is not None:
            h = h[torch.arange(len(x), device=x.device), at]
        return self.head(h)


writer = CodeWriter(VOCAB, LENGTH - 1).to(DEVICE)
print(f"The code writer has {sum(p.numel() for p in writer.parameters()):,} numbers to learn.")
EPOCHS_W, BATCH_W = 12, 256
optimiser = torch.optim.AdamW(writer.parameters(), lr=1e-3, weight_decay=0.01)
t0 = time.time()
for epoch in range(EPOCHS_W):
    writer.train()
    order = torch.randperm(len(writer_data))
    total, count = 0.0, 0
    for b in range(0, len(order), BATCH_W):
        x = writer_data[order[b:b + BATCH_W]]
        x = x[:, : int((x != BLANK).sum(1).max())].to(DEVICE)
        target = x[:, 1:]
        loss = F.cross_entropy(writer(x[:, :-1]).reshape(-1, VOCAB), target.reshape(-1), ignore_index=BLANK)
        optimiser.zero_grad()
        loss.backward()
        optimiser.step()
        n = int((target != BLANK).sum())
        total, count = total + loss.item() * n, count + n
    print(f"pass {epoch + 1} of {EPOCHS_W}: average surprise per number {total / count:.2f}   ({time.time() - t0:.0f} s)")
writer = writer.eval()
''')

code(r'''
# @title Four ways to suggest 10 products, and the code writer at work { display-mode: "form" }
text_t = torch.tensor(text_vec, device=DEVICE)
pop_order = np.argsort(-train_counts, kind="stable")


def exclude(scores, part):
    """No product the customer has already reviewed may be suggested."""
    r = torch.tensor([r for r, h in enumerate(part) for _ in h], device=DEVICE)
    c = torch.tensor([i for h in part for i in h], device=DEVICE)
    scores[r, c] = float("-inf")
    return scores


def bestsellers(hists, k=10):
    out = []
    for h in hists:
        seen = set(h)
        out.append([int(i) for i in pop_order[: k + len(seen)] if i not in seen][:k])
    return np.array(out)


@torch.no_grad()
def portrait1(hists, k=10, chunk=1024):
    out = []
    for c in range(0, len(hists), chunk):
        part = hists[c:c + chunk]
        profile = torch.stack([text_t[torch.tensor(h[-LAST:], device=DEVICE)].mean(0) for h in part])
        scores = exclude(F.normalize(profile, dim=1) @ text_t.T, part)
        out.append(scores.topk(k, dim=1).indices.cpu().numpy())
    return np.concatenate(out)


@torch.no_grad()
def portrait2(hists, k=10, chunk=1024):
    out = []
    for c in range(0, len(hists), chunk):
        part = hists[c:c + chunk]
        h = torch.full((len(part), LAST), PAD, dtype=torch.long)
        for r, hh in enumerate(part):
            recent = hh[-LAST:]
            h[r, : len(recent)] = torch.tensor(recent)
        scores = exclude(tower.scores(h.to(DEVICE)), part)
        out.append(scores.topk(k, dim=1).indices.cpu().numpy())
    return np.concatenate(out)


ta, ts, tp = (torch.as_tensor(v, dtype=torch.long) for v in (aisle, shelf, place))
valid_shelf = torch.zeros(AISLES, SHELVES, dtype=torch.bool)
valid_place = torch.zeros(AISLES, SHELVES, PLACES, dtype=torch.bool)
product_at = torch.full((AISLES, SHELVES, PLACES), -1, dtype=torch.long)
valid_shelf[ta, ts] = True
valid_place[ta, ts, tp] = True
product_at[ta, ts, tp] = torch.arange(N)
valid_shelf, valid_place, product_at = valid_shelf.to(DEVICE), valid_place.to(DEVICE), product_at.to(DEVICE)
NEG = float("-inf")


@torch.no_grad()
def portrait3(hists, k=10, beam=50, chunk=128):
    """Write the most likely next addresses (a beam search that only follows addresses that exist)."""
    out = []
    for c in range(0, len(hists), chunk):
        part = hists[c:c + chunk]
        n = len(part)
        seqs = [[BOS] + [t for i in h[-(ITEMS - 1):] for t in tokens(i)] for h in part]
        lens = torch.tensor([len(s) for s in seqs], device=DEVICE)
        x = torch.full((n, int(lens.max()) + 2), BLANK, dtype=torch.long)
        for r, s in enumerate(seqs):
            x[r, : len(s)] = torch.tensor(s)
        x = x.to(DEVICE)
        # 1. the aisle
        logp = writer(x, at=lens - 1)[:, A0:A0 + AISLES].log_softmax(-1)
        b1 = min(beam, AISLES)
        score1, a1 = logp.topk(b1, dim=1)
        # 2. the shelf, among the shelves of that aisle
        x2, l2 = x.repeat_interleave(b1, 0), lens.repeat_interleave(b1)
        rows2 = torch.arange(len(x2), device=DEVICE)
        x2[rows2, l2] = A0 + a1.reshape(-1)
        logits = writer(x2, at=l2)[:, S0:S0 + SHELVES]
        logp = torch.nan_to_num(logits.masked_fill(~valid_shelf[a1.reshape(-1)], NEG).log_softmax(-1), nan=NEG)
        b2 = min(beam, b1 * SHELVES)
        score2, flat2 = (score1.reshape(-1, 1) + logp).reshape(n, b1 * SHELVES).topk(b2, dim=1)
        a2, s2 = torch.gather(a1, 1, flat2 // SHELVES), flat2 % SHELVES
        # 3. the place, among the places on that shelf
        x3, l3 = x.repeat_interleave(b2, 0), lens.repeat_interleave(b2)
        rows3 = torch.arange(len(x3), device=DEVICE)
        x3[rows3, l3] = A0 + a2.reshape(-1)
        x3[rows3, l3 + 1] = S0 + s2.reshape(-1)
        logits = writer(x3, at=l3 + 1)[:, P0:P0 + PLACES]
        logp = torch.nan_to_num(logits.masked_fill(~valid_place[a2.reshape(-1), s2.reshape(-1)], NEG).log_softmax(-1), nan=NEG)
        score3, flat3 = (score2.reshape(-1, 1) + logp).reshape(n, b2 * PLACES).topk(beam, dim=1)
        src = flat3 // PLACES
        found = product_at[torch.gather(a2, 1, src), torch.gather(s2, 1, src), flat3 % PLACES].cpu().numpy()
        score3 = score3.cpu().numpy()
        for r, h in enumerate(part):
            seen = set(h)
            picks = [int(i) for i, s in zip(found[r], score3[r]) if i >= 0 and np.isfinite(s) and i not in seen][:k]
            out.append(picks + [-1] * (k - len(picks)))
    return np.array(out)


METHODS = {"Bestsellers": bestsellers, "Portrait 1: description": portrait1,
           "Portrait 2: two-tower": portrait2, "Portrait 3: code writer": portrait3}

mine = portrait3([histories[story]])[0]
print(f"Customer {story}: the last products of the history, with their addresses")
for i in histories[story][-4:]:
    print(f"   {address(i)}  {short(TITLE[i], 70)}")
print("The code writer's first five suggestions:")
for i in mine[:5]:
    print(f"   {address(i)}  {short(TITLE[i], 70)}")
verdict = "is among its 10 suggestions" if hidden[story] in mine else "is outside its 10 suggestions"
print(f"The hidden next purchase, {short(TITLE[hidden[story]], 60)} ({address(hidden[story])}), {verdict}.")
''')

# ----------------------------------------------------------------------------------------------
md(r'''
## 5. The scoreboard

**Make a guess before you run the next box.** For each customer, every method suggests 10 products the customer has not reviewed yet. Which method most often has the hidden next purchase among its 10 suggestions?

- **Bestsellers**: the 10 most reviewed products. No portrait at all, the baseline any shop starts with.
- **Portrait 1**: average the numbers of the products in the customer's history (the last 20 at most), place by place, and suggest the products closest to that average.
- **Portrait 2**: the two-tower model.
- **Portrait 3**: the code writer.

The test uses 10,000 customers drawn at random.
''')

code(r'''
# @title The scoreboard: 10,000 customers, 10 suggestions each { display-mode: "form" }
TEST = rng.choice(U, size=10_000, replace=False)
test_hists = [histories[u] for u in TEST]
test_hidden = hidden[TEST]
hits = {}
for label, method in METHODS.items():
    t0 = time.time()
    hits[label] = (method(test_hists) == test_hidden[:, None]).any(axis=1)
    print(f"{label:<25} found the hidden purchase of {100 * hits[label].mean():4.1f} customers in 100   ({time.time() - t0:.0f} s)")

labels = list(METHODS)[::-1]
rates = np.array([100 * hits[l].mean() for l in labels])
errors = np.array([196 * np.sqrt(hits[l].mean() * (1 - hits[l].mean()) / len(TEST)) for l in labels])
fig, ax = plt.subplots(figsize=(8.5, 3.2))
ax.barh(labels, rates, xerr=errors, color=BLUE, height=0.55,
        error_kw={"ecolor": INK2, "elinewidth": 1, "capsize": 3})
for y, (r, e) in enumerate(zip(rates, errors)):
    ax.text(r + e + 0.15, y, f"{r:.1f}", va="center", color=INK)
ax.set_xlabel("customers in 100 whose next purchase is among the 10 suggestions")
ax.grid(axis="x", color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
plt.tight_layout()
plt.show()
print("Thin black lines: the 95% range of uncertainty from testing on 10,000 customers.")
''')

md(r'''
**What to notice.** The bestsellers and portrait 1 find the next purchase for 2 to 3 customers in 100. Portraits 2 and 3, which learned from what customers did, find it about three times as often. The two of them overlap within their uncertainty: on this data, writing addresses works as well as the classic two-tower model. Now split the customers by what their hidden purchase was:
''')

code(r'''
# @title Bestsellers or niche products: who finds which? { display-mode: "form" }
rank = np.empty(N, dtype=int)
rank[pop_order] = np.arange(N)
popular = rank[test_hidden] < 1000
groups = [("next purchase among the 1,000 bestsellers", popular, BLUE),
          (f"next purchase among the other {N - 1000:,} products", ~popular, ORANGE)]
fig, ax = plt.subplots(figsize=(8.5, 3.8))
y = np.arange(len(labels))
for g, (name, mask, colour) in enumerate(groups):
    vals = np.array([100 * hits[l][mask].mean() for l in labels])
    ax.barh(y + (0.2 if g == 0 else -0.2), vals, height=0.38, color=colour,
            label=f"{name} ({mask.sum():,} customers)")
    for yy, v in zip(y + (0.2 if g == 0 else -0.2), vals):
        ax.text(v + 0.2, yy, f"{v:.1f}", va="center", color=INK, fontsize=9)
ax.set_yticks(y, labels)
ax.set_xlabel("customers in 100 whose next purchase is among the 10 suggestions")
ax.grid(axis="x", color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=1, frameon=False)
plt.tight_layout()
plt.show()
''')

md(r'''
**What to notice.** About a third of the hidden purchases are among the 1,000 bestsellers, and that is where portraits 2 and 3 shine: they find nearly one in five of them. On the other two thirds, the niche products, the methods that learned from behaviour lose almost all of their lead: they find 2 or 3 in 100, about as many as portrait 1, which only reads descriptions. The bestseller list, by design, finds none of them. Recommenders that learn from behaviour favour what is already popular. Descriptions also reach the long tail, and the products nobody has bought yet.
''')

# ----------------------------------------------------------------------------------------------
md(r'''
## 6. A product nobody has bought yet

Every week a shop adds products that nobody has reviewed yet. Portrait 2 cannot place them, because its numbers come only from purchases. Portraits 1 and 3 need only a description.

**Your turn.** Describe a product that does not exist (or keep the example) and run the box.
''')

code(r'''
# @title Your turn: invent a product { display-mode: "form" }
new_product = "Pink carrying case for the Nintendo Switch with room for 12 game cards"  # @param {type:"string"}
v = reader.encode([new_product], convert_to_numpy=True, normalize_embeddings=True).astype(np.float32)
print("Portrait 1, the products described most alike:")
for j in np.argsort(-(text_vec @ v[0]))[:5]:
    print(f"   {short(TITLE[j], 80)}")
a = int(aisle_model.predict(v)[0])
s = int(shelf_models[a].predict(v)[0]) if a in shelf_models else 0
mates = np.flatnonzero((aisle == a) & (shelf == s))
print()
print(f"Portrait 3, its address: aisle {a:02d}, shelf {s:02d}, place {len(mates)}, next to:")
for j in mates[:5]:
    print(f"   {address(j)}  {short(TITLE[j], 70)}")
print()
print("Portrait 2 has nothing to say: nobody has reviewed this product, so it has no numbers yet.")
print("Engineers call this the cold-start problem.")
''')

md(r'''
## 7. Your turn: be the customer

Write a few products separated by semicolons. The box takes, for each, the most reviewed product whose name contains your words, treats them as your history, and asks the four methods for suggestions.
''')

code(r'''
# @title Your turn: four recommenders, one customer { display-mode: "form" }
my_products = "Zelda; Pro Controller; Mario Kart"  # @param {type:"string"}
picked = []
for words in my_products.split(";"):
    if words.strip():
        i = find(words)
        print(f"{words.strip()!r}: " + (TITLE[i] if i is not None else "nothing found, try another word"))
        if i is not None and i not in picked:
            picked.append(i)
if picked:
    show(pd.DataFrame({label: [short(TITLE[i], 40) if i >= 0 else "" for i in method([picked])[0]]
                       for label, method in METHODS.items()}))
print(f"The whole notebook ran in {(time.time() - START) / 60:.1f} minutes.")
''')

# ----------------------------------------------------------------------------------------------
md(r'''
## 8. What this means in industry

This notebook is a small version of what large platforms run, and three of its lessons carry over.

1. **Behaviour finds more, descriptions reach further.** The portraits learned from customers found the next purchase more than three times as often as the one that reads descriptions. But most of their lead comes from bestsellers, and they cannot place a product that nobody has bought. Real systems therefore combine both kinds of numbers.
2. **The two-tower model is the workhorse.** The products' numbers can be computed in advance, so finding the best matches for a customer among millions of products takes milliseconds. Many large shops and streaming services use a version of it to pick a few hundred candidates, which slower models then put in order.
3. **Generative recommenders are the new wave.** Meta's HSTU reads a user's actions the way a language model reads words; with 1.5 trillion parameters it improved its metrics by 12.4% in online A/B tests (Zhai et al., ICML 2024). Kuaishou's OneRec replaces the chain of retrieval and ranking models with one model that writes the semantic IDs of the next videos; in 2025 it answered about 25% of all requests in the main scenes of the Kuaishou apps. YouTube's PLUM teaches a pre-trained language model to write the semantic IDs of videos (He et al., WWW 2026). In this notebook the code writer only matches the two-tower model. The published gains come with far more data, and with models more than a million times larger than our code writer.

**What this notebook does not show.** A review only approximates a purchase, so the hidden last review is a rough stand-in for a customer's next decision. Scores measured on past data do not replace an A/B test, which is how shops decide, by measuring sales, watch time or returns. And real systems use many more signals: price, stock, time of day, and what the customer just searched for.

### Sources

- Y. Hou, J. Li, X. Fu, Z. He, A. Yan, X. Chen, J. McAuley. *Bridging Language and Items for Retrieval and Recommendation: Benchmarking LLMs as Semantic Encoders.* ACL 2026. The data: [amazon-reviews-2023.github.io](https://amazon-reviews-2023.github.io/).
- N. Reimers, I. Gurevych. *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks.* EMNLP 2019. The model: [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2).
- P. Covington, J. Adams, E. Sargin. *Deep Neural Networks for YouTube Recommendations.* RecSys 2016.
- L. van der Maaten, G. Hinton. *Visualizing Data using t-SNE.* Journal of Machine Learning Research, 2008.
- Y. Tay et al. *Transformer Memory as a Differentiable Search Index.* NeurIPS 2022.
- S. Rajput et al. *Recommender Systems with Generative Retrieval.* NeurIPS 2023.
- J. Zhai et al. *Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations.* ICML 2024.
- Kuaishou OneRec Team (G. Zhou et al.). *OneRec Technical Report.* arXiv 2506.13695, 2025.
- R. He et al. *PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations.* WWW 2026.
''')


DIGEST = r'''
# @title TEST ONLY: a fingerprint of the code and a digest of every output { display-mode: "form" }
import hashlib, html
from google.colab import _message


def _src(x):
    return x if isinstance(x, str) else "".join(x)


def _text(o):
    if o.get("output_type") == "stream":
        return _src(o.get("text", ""))
    if o.get("output_type") == "error":
        return "ERROR " + o.get("ename", "") + ": " + o.get("evalue", "")
    d = o.get("data", {})
    if "text/html" in d:
        h = re.sub(r"<style.*?</style>", "", _src(d["text/html"]), flags=re.S)
        h = re.sub(r"</t[dh]>", " | ", h)
        h = re.sub(r"</tr>", "\n", h)
        return html.unescape(re.sub(r"<[^>]+>", "", h))
    if "image/png" in d:
        return "[image]"
    return _src(d.get("text/plain", ""))


_nb = _message.blocking_request("get_ipynb", timeout_sec=60)["ipynb"]
_code = [c for c in _nb["cells"] if c["cell_type"] == "code"][:-1]
print("fingerprint", hashlib.md5("\n\n".join(_src(c["source"]).rstrip() for c in _code).encode()).hexdigest(), len(_code), "cells")
print("per cell", " ".join(hashlib.md5(_src(c["source"]).rstrip().encode()).hexdigest()[:6] for c in _code))
for n, c in enumerate(_code):
    print(f"==== cell {n:02d} {_src(c['source']).splitlines()[0][9:75]}")
    for o in c.get("outputs", []):
        lines = [l for l in _text(o).splitlines() if l.strip() and "it/s]" not in l and "%|" not in l]
        print("\n".join(lines)[:2500])
'''


def fingerprint(cells):
    import hashlib
    code_cells = [c for c in cells if c["cell_type"] == "code"]
    print("per cell", " ".join(hashlib.md5(c["source"].rstrip().encode()).hexdigest()[:6] for c in code_cells))
    return hashlib.md5("\n\n".join(c["source"].rstrip() for c in code_cells).encode()).hexdigest()


def build(path, code_only=False):
    for n, cell in enumerate(CELLS):
        cell["metadata"]["id"] = f"cell{n:02d}"
        if cell["cell_type"] == "code":
            cell["metadata"]["cellView"] = "form"
    cells = [dict(c) for c in CELLS if c["cell_type"] == "code" or not code_only]
    if code_only:   # a test copy for Colab runs: code only, plus a digest cell at the end
        print("fingerprint", fingerprint(cells), len(cells), "cells")
        cells.append({"cell_type": "code", "metadata": {"id": "digest", "cellView": "form"},
                      "execution_count": None, "outputs": [], "source": DIGEST.strip("\n")})
    for c in cells:
        c["source"] = c["source"].splitlines(True)
    nb = {"nbformat": 4, "nbformat_minor": 0,
          "metadata": {"accelerator": "GPU",
                       "colab": {"provenance": [], "gpuType": "T4", "toc_visible": True},
                       "kernelspec": {"name": "python3", "display_name": "Python 3"},
                       "language_info": {"name": "python"}},
          "cells": cells}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=code_only)
        f.write("\n")


if __name__ == "__main__":
    # python3 build_notebook.py [output.ipynb] [code]   ("code" writes a compact copy without the text cells)
    build(sys.argv[1] if len(sys.argv) > 1 else "three-portraits.ipynb", code_only="code" in sys.argv[2:])
