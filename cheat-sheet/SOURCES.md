# Sources of cheat-sheet.pdf

## The concepts

- The lecture rows of the three weekends: the master spreadsheet "AINIT HS26 master spreadsheet", Syllabus tab,
  and the course site's `src/data/weekends.ts` (repository `eth-ainit-hs26/AINIT-PAGE`), both read on 2026-11-11.
  The spreadsheet's address is in `git_ainit/CLAUDE.md` on Carlos's machine, kept out of this public repository.
- The project of each weekend: the same Syllabus tab (LLM marketing agent; recommender for online retail; RL vehicle
  routing).
- The wording of the cards follows the course's own material: weekend 1 the LLM, ladder, OPRO, GEPA, reasoning and
  MLOps decks and the guest talk on harnesses (`w1-lecture-material`); weekend 2 the games of `w2-cx-private`, the
  case decks and the computing clusters deck of this repository; weekend 3 `rl-arcade/slides/rl-slides.tex` (FS26).

## Named cases

Every company, product and year on the page. READ means the sentence quoted was read at the source on 2026-11-11;
"course" means the case and its source are in a course deck, where they were read.

| Card | On the page | Source | Grade |
|---|---|---|---|
| RAG | DoorDash's support bot answers couriers from its help articles (2024) | Jia, Wang, Bamba, Wang (DoorDash), "Path to high-quality LLM-based Dasher support automation", DoorDash blog, 17 September 2024 (https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation/): "a retrieval augmented generation system, or RAG"; "a RAG system that retrieves information from knowledge base articles to generate a response that resolves Dasher issues". The site refuses curl (403); read in the built-in browser. | READ |
| GEPA | Databricks: an open model with its prompts beat costlier models at extracting data from documents (2025) | The Databricks AI Research Team, "Building State-of-the-Art Enterprise Agents 90x Cheaper with Automated Prompt Optimization", Databricks blog, 24 September 2025 (https://www.databricks.com/blog/building-state-art-enterprise-agents-90x-cheaper-automated-prompt-optimization): "leveraging GEPA ... gpt-oss-120b surpasses state-of-the-art proprietary models Claude Sonnet 4 and Claude Opus 4.1 by ~3% while being roughly 20x and 90x cheaper"; the tasks are IE Bench, "Information Extraction (IE)", "converting unstructured sources such as PDFs or scanned documents into structured records". | READ |
| Supervised fine-tuning | InstructGPT (OpenAI, 2022) | Ouyang and others (OpenAI), "Training language models to follow instructions with human feedback", NeurIPS 2022 (https://arxiv.org/abs/2203.02155); step 1 of its method is supervised fine-tuning on demonstrations written by labelers. In the ladder deck (`w1-lecture-material/ladder-deck/SOURCES.md`). | course |
| Human feedback (RLHF) | ChatGPT (OpenAI, 2022) | OpenAI, "ChatGPT: Optimizing Language Models for Dialogue", 30 November 2022, the copy of 2 December 2022 in the Internet Archive (http://web.archive.org/web/20221202010338/https://openai.com/blog/chatgpt/): "We trained this model using Reinforcement Learning from Human Feedback (RLHF), using the same methods as InstructGPT". | READ |
| Verifiable rewards (RLVR) | DeepSeek-R1 (2025) | Guo and others (DeepSeek-AI), "DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning", Nature 645, 633-638, 17 September 2025, DOI 10.1038/s41586-025-09422-z (title, journal, volume, pages and date checked at Crossref). | READ (metadata) |
| Planning strategies | AlphaDev found faster sorting code by tree search, now in a standard C++ library (DeepMind, 2023) | Mankowitz and others (DeepMind), "Faster sorting algorithms discovered using deep reinforcement learning", Nature 618, 257-263 (2023), DOI 10.1038/s41586-023-06004-9 (https://www.nature.com/articles/s41586-023-06004-9): "guides a Monte Carlo tree search (MCTS) planning procedure using a deep neural network"; "These algorithms have been integrated into the LLVM standard C++ sort library". | READ |
| MLOps | Uber's Michelangelo, one platform for all its teams (2024) | Uber Engineering, "From Predictive to Generative: How Michelangelo Accelerates Uber's AI Journey", May 2024, the source of the weekend 1 MLOps slide "Uber's Michelangelo: one ML platform shared by every team since 2016" (`mlops-slides-hs26.pdf` on the course site). | course |
| Nearest neighbors | Etsy (2024) | Jha, Subramaniyam, Benjamin, Taula (Etsy), "Unified Embedding Based Personalized Retrieval in Etsy Search", IEEE FMLDS 2024, DOI 10.1109/FMLDS63805.2024.00055; `../cases-deck/README.md`. | course |
| Nearest neighbors | Airbnb (2025) | Abdool and others, "Embedding-Based Retrieval for Airbnb Search", Airbnb's engineering blog, April 2025 (https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/), and the preprint arXiv 2601.06873; `../cases-deck/README.md`. | course |
| Matrix factorization | audiobook recommendations at Spotify, with the numbers learned by networks (2024) | De Nadai and others (Spotify), "Personalized Audiobook Recommendations at Spotify Through Graph Neural Networks", WWW '24 Companion, DOI 10.1145/3589335.3648339: 128 numbers per listener and per audiobook from two networks and a graph, scored by their inner product. The case of the matrix factorization block (`../cases-deck/spotify-frames.tex`). | course |
| Epsilon-greedy | the mix of music and podcasts on Spotify's home page (2025) | Feijer and others (Spotify), "Calibrated Recommendations with Contextual Bandits", CONSEQUENCES workshop at RecSys 2025, arXiv 2509.05460; in production as of March 2025 (`../cases-deck/spotify-home-frames.tex`). | course |
| UCB | Amazon tested it on the application pages of Amazon Payments (2026) | John and Gozluklu (Amazon), "Uplifting conversion across the acquisition funnel with personalization using contextual bandits on AWS", AWS Machine Learning Blog, 1 October 2026: a 7-week A/B test against the fixed page (`../cases-deck/amazon-frames.tex`). The card says "tested" because the post reports a test. | course |
| Parallelized matrix factorization | LinkedIn trains its ranking models on many GPUs at once (2024) | Borisyuk and others (LinkedIn), "LiRank: Industrial Large Scale Ranking Models at LinkedIn", KDD '24, DOI 10.1145/3637528.3671561, Sec. 4.1: "We utilized Horovod to scale out synchronous training with multiple GPUs." (`../cases-deck/tools/cases_numbers.py`). | course |
| Computing clusters | Apertus, the Swiss open LLM, trained on Alps at CSCS (2025) | EPFL AI Center, "Apertus: a fully open, transparent, multilingual language model", published 2 September 2025 (https://ai.epfl.ch/apertus-a-fully-open-transparent-multilingual-language-model/): "EPFL, ETH Zurich and the Swiss National Supercomputing Centre (CSCS) released Apertus today"; "an investment of over 10 million GPU hours on 'Alps' by CSCS". Also `../clusters-deck/` frame 7. | READ |
| SARSA and Q-learning | Lyft matches riders and drivers by future earnings learned from live trips (2024) | Azagirre, Balwally and others (Lyft), "A Better Match for Drivers and Riders: Reinforcement Learning at Lyft", INFORMS Journal on Applied Analytics 54(1), 71-83, January 2024, DOI 10.1287/inte.2023.0083: "We use a novel online reinforcement learning approach that estimates the future earnings of drivers in real time"; "we use temporal difference (TD)-based value updates"; "Lyft rolled out the algorithm globally in 2021". The updates learn the value of a driver's state, the update family of SARSA and Q-learning. | READ |

Lines without a name (for example "coding agents, deep research, support bots that act") state a kind of use and
need no source.

Checked and left off the page: Morgan Stanley's assistant for financial advisors (September 2023), seen only in
secondary reports; ANYmal's walking policy (Miki and others, Science Robotics 2022, arXiv 2201.08117), trained with PPO, a
descendant of REINFORCE, left off because the REINFORCE card already links to weekend 1.
