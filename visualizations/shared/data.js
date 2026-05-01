// Shared data for W2 Recsys visualizations.
// Codifies the books matrix described in /BOOKS_MATRIX.md.
// All viz import via window.RECSYS for backward compatibility with the
// previous household-items deck.
//
// Latent axes: x = Fiction (+) / Nonfiction (-),  y = Light (+) / Demanding (-).
// Quadrants: LF = (+,+) Light Fiction · DF = (+,-) Demanding Fiction
//            LN = (-,+) Light Nonfiction · DN = (-,-) Demanding Nonfiction.
// Archetypes: A1 Commuter, A2 Literary, A3 Practical, A4 Scholar.

window.RECSYS = (function () {

  // ---------- Archetypes (4) ----------
  const ARCHETYPES = [
    { id: 'A1', name: 'Commuter',  embedding: [+1, +1], blurb: 'Reads on the train; thrillers and fantasy.' },
    { id: 'A2', name: 'Literary',  embedding: [+1, -1], blurb: 'Rereads Joyce; lit-crit blogs.' },
    { id: 'A3', name: 'Practical', embedding: [-1, +1], blurb: 'Self-help, travel, the cookbook on the counter.' },
    { id: 'A4', name: 'Scholar',   embedding: [-1, -1], blurb: 'Underlines Kant; dips into Darwin on weekends.' },
  ];

  // ---------- Books (16) ----------
  // Field `embedding` is the latent vector v_j; `quadrant` is the cluster id.
  const BOOKS = [
    // Light Fiction (LF) — embedding [+1, +1]
    { id: 1,  label: 'Potter',      title: 'Harry Potter and the Philosopher’s Stone', author: 'J. K. Rowling',     year: 1997, quadrant: 'LF', embedding: [+1, +1] },
    { id: 2,  label: 'Christie',    title: 'Murder on the Orient Express',                   author: 'Agatha Christie',   year: 1934, quadrant: 'LF', embedding: [+1, +1] },
    { id: 3,  label: 'Hunger',      title: 'The Hunger Games',                               author: 'Suzanne Collins',   year: 2008, quadrant: 'LF', embedding: [+1, +1] },
    { id: 4,  label: 'DaVinci',     title: 'The Da Vinci Code',                              author: 'Dan Brown',         year: 2003, quadrant: 'LF', embedding: [+1, +1] },
    // Demanding Fiction (DF) — embedding [+1, -1]
    { id: 5,  label: 'Ulysses',     title: 'Ulysses',                                        author: 'James Joyce',       year: 1922, quadrant: 'DF', embedding: [+1, -1] },
    { id: 6,  label: 'War&Peace',   title: 'War and Peace',                                  author: 'Leo Tolstoy',       year: 1869, quadrant: 'DF', embedding: [+1, -1] },
    { id: 7,  label: 'Borges',      title: 'Ficciones',                                      author: 'Jorge Luis Borges', year: 1944, quadrant: 'DF', embedding: [+1, -1] },
    { id: 8,  label: 'Lighthouse',  title: 'To the Lighthouse',                              author: 'Virginia Woolf',    year: 1927, quadrant: 'DF', embedding: [+1, -1] },
    // Light Nonfiction (LN) — embedding [-1, +1]
    { id: 9,  label: 'EatPray',     title: 'Eat, Pray, Love',                                author: 'Elizabeth Gilbert', year: 2006, quadrant: 'LN', embedding: [-1, +1] },
    { id: 10, label: 'Switzerland', title: 'Lonely Planet: Switzerland',                     author: '(travel guide)',    year: 2024, quadrant: 'LN', embedding: [-1, +1] },
    { id: 11, label: '7Habits',     title: 'The 7 Habits of Highly Effective People',        author: 'Stephen R. Covey',  year: 1989, quadrant: 'LN', embedding: [-1, +1] },
    { id: 12, label: 'JoyCook',     title: 'The Joy of Cooking',                             author: 'Irma S. Rombauer',  year: 1931, quadrant: 'LN', embedding: [-1, +1] },
    // Demanding Nonfiction (DN) — embedding [-1, -1]
    { id: 13, label: 'Kant',        title: 'Critique of Pure Reason',                        author: 'Immanuel Kant',     year: 1781, quadrant: 'DN', embedding: [-1, -1] },
    { id: 14, label: 'Smith',       title: 'The Wealth of Nations',                          author: 'Adam Smith',        year: 1776, quadrant: 'DN', embedding: [-1, -1] },
    { id: 15, label: 'Darwin',      title: 'On the Origin of Species',                       author: 'Charles Darwin',    year: 1859, quadrant: 'DN', embedding: [-1, -1] },
    { id: 16, label: 'Russell',     title: 'A History of Western Philosophy',                author: 'Bertrand Russell',  year: 1945, quadrant: 'DN', embedding: [-1, -1] },
  ];

  // ---------- Readers (21) ----------
  // The four pure-archetype groups (R1-R16) plus five special readers (R17-R21).
  // `special` is null for pure archetypes; otherwise a tag matching the design doc.
  const READERS = [
    // A1 — Commuters
    { id: 1,  name: 'Alice',  archetype: 'A1', embedding: [+1, +1], special: null },
    { id: 2,  name: 'Ben',    archetype: 'A1', embedding: [+1, +1], special: null },
    { id: 3,  name: 'Clara',  archetype: 'A1', embedding: [+1, +1], special: null },
    { id: 4,  name: 'David',  archetype: 'A1', embedding: [+1, +1], special: null },
    // A2 — Literary
    { id: 5,  name: 'Eleni',  archetype: 'A2', embedding: [+1, -1], special: null },
    { id: 6,  name: 'Felix',  archetype: 'A2', embedding: [+1, -1], special: null },
    { id: 7,  name: 'Greta',  archetype: 'A2', embedding: [+1, -1], special: null },
    { id: 8,  name: 'Hugo',   archetype: 'A2', embedding: [+1, -1], special: null },
    // A3 — Practical
    { id: 9,  name: 'Iris',   archetype: 'A3', embedding: [-1, +1], special: null },
    { id: 10, name: 'Jonas',  archetype: 'A3', embedding: [-1, +1], special: null },
    { id: 11, name: 'Karin',  archetype: 'A3', embedding: [-1, +1], special: null },
    { id: 12, name: 'Liam',   archetype: 'A3', embedding: [-1, +1], special: null },
    // A4 — Scholars
    { id: 13, name: 'Maya',   archetype: 'A4', embedding: [-1, -1], special: null },
    { id: 14, name: 'Nico',   archetype: 'A4', embedding: [-1, -1], special: null },
    { id: 15, name: 'Oksana', archetype: 'A4', embedding: [-1, -1], special: null },
    { id: 16, name: 'Petros', archetype: 'A4', embedding: [-1, -1], special: null },
    // Special readers (the pedagogical surprises)
    { id: 17, name: 'Quinn',  archetype: 'mixed', embedding: [+1,  0], special: 'fiction-axis'   },
    { id: 18, name: 'Rosa',   archetype: 'mixed', embedding: [ 0, +1], special: 'light-axis'     },
    { id: 19, name: 'Samir',  archetype: 'A1?',   embedding: [+0.5, +0.5], special: 'eclectic'   },
    { id: 20, name: 'Tessa',  archetype: 'A1',    embedding: [+1, +1], special: 'twin-of-alice'  },
    { id: 21, name: 'Ursula', archetype: 'A1',    embedding: [+1, +1], special: 'borges-outlier' },
  ];

  // ---------- Cold-start reader (introduced separately at scene 11) ----------
  const COLD_START_READER = {
    id: 22,
    name: 'Vera',
    trueArchetype: 'A1',
    trueEmbedding: [+1, +1],
    visibleRatings: { 2: +1 }, // bookId 2 = Christie, ✅
    // Two yes/no questions = 2 bits = the entropy needed to identify one of
    // four archetypes. Each question toggles the sign on one latent axis.
    profileQuestions: [
      { q: 'Fiction or nonfiction?',  options: ['fiction', 'nonfiction'], correctAnswer: 'fiction',  axis: 'x', signalIfCorrect: +1 },
      { q: 'Light or demanding?',     options: ['light',   'demanding'],  correctAnswer: 'light',    axis: 'y', signalIfCorrect: +1 },
    ],
  };

  // ---------- Ratings (21 readers × 16 books) ----------
  // Order: rows in READERS order, columns in BOOKS order.
  // Values: 1 = ✅ liked · -1 = ❌ disliked · 0 = ? ambiguous · null = — unread.
  // v2 RATINGS — rank-2-clean. Each pure archetype is ✅ in own quadrant,
  // ❌ in opposite, and ? (zero) in the two adjacent quadrants. This restores
  // the rank-2 structure of the underlying generative model and gives the
  // Spectral Microscope a sharp k=2 elbow.
  const RATINGS = [
    /* R1  Alice  (A1)        */ [ 1, 1, 1, 1,   0, 0, 0, 0,   0, 0, 0, 0,  -1,-1,-1,-1 ],
    /* R2  Ben    (A1)        */ [ 1, 1, 1, 1,   0, 0, 0, 0,   0, 0, 0, 0,  -1,-1,-1,-1 ],
    /* R3  Clara  (A1)        */ [ 1, 1, 1, 1,   0, 0, 0, 0,   0, 0, 0, 0,  -1,-1,-1,-1 ],
    /* R4  David  (A1)        */ [ 1, 1, 1, 1,   0, 0, 0, 0,   0, 0, 0, 0,  -1,-1,-1,-1 ],
    /* R5  Eleni  (A2)        */ [ 0, 0, 0, 0,   1, 1, 1, 1,  -1,-1,-1,-1,   0, 0, 0, 0 ],
    /* R6  Felix  (A2)        */ [ 0, 0, 0, 0,   1, 1, 1, 1,  -1,-1,-1,-1,   0, 0, 0, 0 ],
    /* R7  Greta  (A2)        */ [ 0, 0, 0, 0,   1, 1, 1, 1,  -1,-1,-1,-1,   0, 0, 0, 0 ],
    /* R8  Hugo   (A2)        */ [ 0, 0, 0, 0,   1, 1, 1, 1,  -1,-1,-1,-1,   0, 0, 0, 0 ],
    /* R9  Iris   (A3)        */ [ 0, 0, 0, 0,  -1,-1,-1,-1,   1, 1, 1, 1,   0, 0, 0, 0 ],
    /* R10 Jonas  (A3)        */ [ 0, 0, 0, 0,  -1,-1,-1,-1,   1, 1, 1, 1,   0, 0, 0, 0 ],
    /* R11 Karin  (A3)        */ [ 0, 0, 0, 0,  -1,-1,-1,-1,   1, 1, 1, 1,   0, 0, 0, 0 ],
    /* R12 Liam   (A3)        */ [ 0, 0, 0, 0,  -1,-1,-1,-1,   1, 1, 1, 1,   0, 0, 0, 0 ],
    /* R13 Maya   (A4)        */ [-1,-1,-1,-1,   0, 0, 0, 0,   0, 0, 0, 0,   1, 1, 1, 1 ],
    /* R14 Nico   (A4)        */ [-1,-1,-1,-1,   0, 0, 0, 0,   0, 0, 0, 0,   1, 1, 1, 1 ],
    /* R15 Oksana (A4)        */ [-1,-1,-1,-1,   0, 0, 0, 0,   0, 0, 0, 0,   1, 1, 1, 1 ],
    /* R16 Petros (A4)        */ [-1,-1,-1,-1,   0, 0, 0, 0,   0, 0, 0, 0,   1, 1, 1, 1 ],
    /* R17 Quinn  (★ fiction) */ [ 1, 1, 1, 1,   1, 1, 1, 1,  -1,-1,-1,-1,  -1,-1,-1,-1 ],
    /* R18 Rosa   (★ light)   */ [ 1, 1, 1, 1,  -1,-1,-1,-1,   1, 1, 1, 1,  -1,-1,-1,-1 ],
    /* R19 Samir  (★ weak A1) */ [ 1, 0, 1, 0,   0, 0, 0, 0,   0, 0, 0, 0,  -1, 0,-1, 0 ],
    /* R20 Tessa  (★ twin)    */ [ 1, 1, 1, 1,   0, 0, 0, 0,   0, 0, 0, 0,  -1,-1,-1,-1 ], // identical to Alice
    /* R21 Ursula (★ outlier) */ [ 1, 1, 1, 1,   0, 0, 1, 0,   0, 0, 0, 0,  -1,-1,-1,-1 ], // ✅ on Borges (col 7) — the rank-3 surprise
  ];

  // ---------- Color palette ----------
  // Okabe-Ito CVD-safe palette — preserved from prior viz.
  // The four latent-axis colors were named after the old Indoor/Outdoor × Simple/Tech.
  // The new books axes (Fiction/Nonfiction × Light/Demanding) reuse the SAME hex
  // values via aliases so existing viz continue to render correctly during
  // retrofit. Use the new aliases (`fiction`, `nonfiction`, `light`, `demanding`)
  // in any new viz.
  const COLORS = {
    // Books axes (preferred names)
    fiction:    '#CC79A7',  // reddish purple
    nonfiction: '#E69F00',  // orange
    light:      '#56B4E9',  // sky blue
    demanding:  '#009E73',  // bluish green
    // Legacy aliases (kept so retrofit work in progress doesn't break)
    simple:  '#E69F00', tech: '#CC79A7',
    outdoor: '#56B4E9', indoor: '#009E73',
    // Quadrant solids
    LF: '#56B4E9',  // light fiction  ~ light + fiction → use light's blue, the light-axis dominates
    DF: '#CC79A7',  // demanding fiction → fiction's purple
    LN: '#E69F00',  // light nonfiction → nonfiction's orange (light + nonfiction balance)
    DN: '#009E73',  // demanding nonfiction → demanding's green
    // Rating cell colors
    pos:     '#0072B2', posBg:     '#D6E6F2',  // ✅ blue
    neg:     '#D55E00', negBg:     '#FCE4D6',  // ❌ vermillion
    neutral: '#6C757D', neutralBg: '#F8F9FA',  // ?
    unknown: '#B8860B', unknownBg: '#FFF6CC',  // — (unread)
    // Chrome
    bg:        '#FFFFFF',
    border:    '#E9ECEF',
    text:      '#212529',
    textMuted: '#6C757D',
    headerStart: '#2C3E50',
    headerEnd:   '#34495E',
  };

  // ---------- Helpers ----------
  function dot(a, b) {
    let s = 0;
    for (let i = 0; i < a.length; i++) s += a[i] * b[i];
    return s;
  }
  function predictRating(readerEmb, bookEmb) { return dot(readerEmb, bookEmb); }
  function ratingSign(r) {
    if (r === null || r === undefined) return null;
    if (r > 0.5)  return  1;
    if (r < -0.5) return -1;
    return 0;
  }

  function getBook(idOrLabelOrTitle) {
    if (typeof idOrLabelOrTitle === 'number') return BOOKS.find(b => b.id === idOrLabelOrTitle);
    return BOOKS.find(b => b.label === idOrLabelOrTitle || b.title === idOrLabelOrTitle);
  }
  function getReader(idOrName) {
    if (typeof idOrName === 'number') return READERS.find(r => r.id === idOrName);
    return READERS.find(r => r.name === idOrName);
  }
  function getRating(reader, book) {
    const r = typeof reader === 'object' ? reader : getReader(reader);
    const b = typeof book === 'object' ? book : getBook(book);
    if (!r || !b) return undefined;
    return RATINGS[r.id - 1][b.id - 1];
  }

  // Pretty cell text for any rating value.
  function ratingGlyph(v) {
    if (v === null || v === undefined) return '—'; // —
    if (v === 1)  return '✅';                       // ✅
    if (v === -1) return '❌';                       // ❌
    if (v === 0)  return '?';                            // ?
    return String(v);
  }

  // Numeric ratings matrix in canonical reader×book order, with NaN for ?.
  // Suitable for SVD / linear algebra; null (unread) becomes NaN as well, but
  // most viz that need a dense matrix should call `ratingsForFactorization()`
  // instead, which fills missing entries with 0.
  function ratingsByEmbeddingOrder() {
    return RATINGS.map(row => row.map(v => v === null ? NaN : (v === 0 ? NaN : v)));
  }

  // For matrix-factorization / SVD demos: returns a dense 21×16 array where
  // unread (—) and ambiguous (?) cells are 0, ✅ is +1, ❌ is -1.
  function ratingsForFactorization() {
    return RATINGS.map(row => row.map(v => v === null ? 0 : v));
  }

  // Mask of which cells are *visible* to the recsys (for matrix-completion viz).
  function visibleMask() {
    return RATINGS.map(row => row.map(v => v === null ? 0 : 1));
  }

  // ---------- Backward-compatibility aliases ----------
  // Older viz expected ITEMS / PEOPLE / PERSON_ORDER / ITEM_ORDER and indexed
  // RATINGS by alphabetical order. We expose aliases so retrofitted viz can
  // keep their old code paths until they are explicitly modernised.
  const ITEMS  = BOOKS;        // old name
  const PEOPLE = READERS;      // old name
  const PERSON_ORDER = READERS.map(r => r.name);  // canonical (not alphabetical)
  const ITEM_ORDER   = BOOKS.map(b => b.label);   // canonical (not alphabetical)

  return {
    // New canonical API
    BOOKS, READERS, ARCHETYPES, COLD_START_READER, RATINGS, COLORS,
    dot, predictRating, ratingSign, ratingGlyph,
    getBook, getReader, getRating,
    ratingsByEmbeddingOrder, ratingsForFactorization, visibleMask,
    // Backward-compat
    ITEMS, PEOPLE, PERSON_ORDER, ITEM_ORDER,
  };
})();
