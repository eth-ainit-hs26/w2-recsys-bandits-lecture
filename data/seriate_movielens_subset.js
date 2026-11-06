#!/usr/bin/env node
/*
 * Re-sort the MovieLens subset for Demo 2 so that the sorted view looks sorted.
 *
 * Run after build_movielens_subset.py:  node data/seriate_movielens_subset.js [path.json]
 *
 * The builder's order (k-means on a 2-D SVD) barely beats a random shuffle on
 * this data: neighbour agreement 57% against 35% for a shuffle. This script
 * orders the table the way a player does in Demo 1, with Demo 1's score:
 *   - people: adjacent rows that rated the movies alike are put side by side
 *     (simulated annealing on the sum of max(0, row_k · row_k+1));
 *   - movies: the same within each genre, and the four genres in the order
 *     that scores best, so the genre labels still hold;
 *   - groups: the ordered list of people is cut into four runs of at least
 *     three people, at the cuts that leave each run most uniform;
 *   - diagonal: the runs are put in the order that places each group's
 *     favourite genre on the diagonal, as in Demo 1. This moves whole blocks
 *     and changes no rating.
 * It rewrites `reveal`, `user_clusters`, `movie_clusters` and each user's
 * `cluster` in visualizations/shared/movielens_subset.json and .js. Seeded, so
 * the output is the same on every run.
 */
const fs = require('fs');
const path = require('path');

const OUT = process.argv[2] ||
  path.join(__dirname, '..', 'visualizations', 'shared', 'movielens_subset.json');
const OUT_JS = OUT.replace(/\.json$/, '.js');
const N_GROUPS = 4, MIN_GROUP = 3;

const d = JSON.parse(fs.readFileSync(OUT, 'utf8'));
const M = d.matrix.map(r => r.map(v => (v === null ? 0 : v)));
const nU = M.length, nM = M[0].length;

let seed = 7;
const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;

const dot = (a, b) => a.reduce((s, x, i) => s + x * b[i], 0);
const rowVec = i => M[i];
const colVec = j => M.map(r => r[j]);
function agreement(order, vec) {
  let s = 0;
  for (let k = 0; k + 1 < order.length; k++) s += Math.max(0, dot(vec(order[k]), vec(order[k + 1])));
  return s;
}

function seriate(items, vec, restarts) {
  let best = -1, bestOrder = items;
  for (let r = 0; r < restarts; r++) {
    let o = items.slice().sort(() => rnd() - 0.5), s = agreement(o, vec), T = 6;
    for (let it = 0; it < 40000; it++) {
      const i = (rnd() * o.length) | 0, j = (rnd() * o.length) | 0;
      if (i === j) continue;
      const p = o.slice();
      p.splice(j, 0, p.splice(i, 1)[0]);
      const t = agreement(p, vec);
      if (t >= s || rnd() < Math.exp((t - s) / T)) { o = p; s = t; }
      T *= 0.9998;
      if (s > best) { best = s; bestOrder = o.slice(); }
    }
  }
  return bestOrder;
}

// ---- people ----
const userOrder = seriate([...Array(nU).keys()], rowVec, 80);

// ---- movies: best order inside each genre, then the best order of genres ----
const genres = [...new Set(d.movies.map(m => m.cluster))];
const within = genres.map(g =>
  seriate(d.movies.map((m, j) => (m.cluster === g ? j : -1)).filter(j => j >= 0), colVec, 20));
const perms = a => (a.length <= 1 ? [a]
  : a.flatMap((x, i) => perms([...a.slice(0, i), ...a.slice(i + 1)]).map(p => [x, ...p])));
let movieOrder = null, genreOrder = null, bestCols = -1;
for (const p of perms(genres.map((_, k) => k))) {
  const o = p.flatMap(k => within[k]);
  const s = agreement(o, colVec);
  if (s > bestCols) { bestCols = s; movieOrder = o; genreOrder = p.map(k => genres[k]); }
}

// ---- cut the ordered people into N_GROUPS runs (dynamic programming) ----
function runCost(a, b) {          // squared distance to the run's mean row, rows a..b-1
  let c = 0;
  for (let j = 0; j < nM; j++) {
    let s = 0;
    for (let k = a; k < b; k++) s += M[userOrder[k]][j];
    const mean = s / (b - a);
    for (let k = a; k < b; k++) c += (M[userOrder[k]][j] - mean) ** 2;
  }
  return c;
}
const INF = 1e18;
const best = Array.from({ length: N_GROUPS + 1 }, () => new Array(nU + 1).fill(INF));
const cut = Array.from({ length: N_GROUPS + 1 }, () => new Array(nU + 1).fill(0));
best[0][0] = 0;
for (let g = 1; g <= N_GROUPS; g++) {
  for (let b = g * MIN_GROUP; b <= nU; b++) {
    for (let a = (g - 1) * MIN_GROUP; a <= b - MIN_GROUP; a++) {
      const c = best[g - 1][a] + runCost(a, b);
      if (c < best[g][b]) { best[g][b] = c; cut[g][b] = a; }
    }
  }
}
const bounds = [nU];
for (let g = N_GROUPS, b = nU; g > 0; g--) { b = cut[g][b]; bounds.unshift(b); }

// ---- put each group's favourite genre on the diagonal ----
const runs = [];
for (let g = 0; g < N_GROUPS; g++) runs.push(userOrder.slice(bounds[g], bounds[g + 1]));
function blockMean(people, genre) {
  let s = 0, n = 0;
  people.forEach(i => d.movies.forEach((m, j) => {
    const v = d.matrix[i][j];
    if (m.cluster === genre && v !== null) { s += v; n++; }
  }));
  return s / n;
}
let runOrder = null, bestDiag = -Infinity;
for (const p of perms(runs.map((_, k) => k))) {
  const s = p.reduce((acc, r, k) => acc + blockMean(runs[r], genreOrder[k]), 0);
  if (s > bestDiag) { bestDiag = s; runOrder = p; }
}
const finalUserOrder = runOrder.flatMap(r => runs[r]);

// ---- write back ----
const userClusters = runOrder.map((r, g) => {
  runs[r].forEach(i => { d.users[i].cluster = g; });
  return { cluster: g, n: runs[r].length };
});
d.user_clusters = userClusters;
d.movie_clusters = genreOrder.map(g => ({
  cluster: g,
  name: d.movies.find(m => m.cluster === g).cluster_name,
  n: d.movies.filter(m => m.cluster === g).length,
}));
d.reveal = { user_order: finalUserOrder, movie_order: movieOrder };

fs.writeFileSync(OUT, JSON.stringify(d));
fs.writeFileSync(OUT_JS, 'window.MOVIELENS = ' + JSON.stringify(d) + ';\n');

const total = (ro, co) => agreement(ro, rowVec) + agreement(co, colVec);
console.log('group sizes:', userClusters.map(c => c.n).join(' '));
console.log('genre order:', d.movie_clusters.map(c => c.name).join(' '));
console.log('neighbour agreement, sorted:', total(finalUserOrder, movieOrder));
console.log(`Wrote ${OUT}\nWrote ${OUT_JS}`);
