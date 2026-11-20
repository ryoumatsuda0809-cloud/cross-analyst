# Source Registry / 参照先台帳 — 「まずここを見る」

A curated, tiered list of where to look **first** when verifying a claim — so we stop searching reactively (and stop landing on commercial blogs and paywalls, as we did on 2026-07-19). Check Tier 1 before anything else; use Tier 2 to *find* the original; never let Tier 3 be the basis of a claim.

主張を検証するとき、**最初に当たる場所**を決めておくための台帳。毎回ゼロから検索して、たまたま確認できる出典を祈るのをやめる。Tier 1 から当たり、Tier 2 は「原典を探す道具」、Tier 3 は根拠にしない。

---

## The iron rule / 鉄則

The whole point of this project is that **we cite what we can open and read ourselves** — not a summary of it, not a blog about it, not an abstract we couldn't get past. Discovery tools (Tier 2) and AI summarizers are for *finding* the paper. The claim is only ✅ once a human has opened the **primary full text** in Tier 1 and confirmed it.

このプロジェクトの核は「**自分で開いて読めるものだけを引く**」こと。要約でも、それについてのブログでもなく、本文。Tier 2 やAI要約ツールは原典を「探す」ための道具。人間が Tier 1 の**一次情報の本文**を開いて確認して初めて ✅ になる。

**Workflow / 手順**
1. **Tier 1 で本文を開いて確認する。** これがゴール。
2. 見つからなければ **Tier 2 で探して、Tier 1 の原典（DOI/PMC/arXiv）に到達する。**
3. **ペイウォールなら、無料で読める裏付けを必ず併記する** — PMC版・著者PDF・プレプリント・その論文を引用しているオープンアクセス論文（例：Bond & DePaulo 2006 はペイウォール → Levine 2021 [PMC8333997] が引用・確認しており誰でも読める）。読者が確認できない出典は ✅ にしない。
4. **Tier 3 は主張の根拠にしない。** きっかけ・言い換えの参考まで。

---

## Tier 1 — Primary, free full text（そのまま出典に使える／最優先）

自分で本文を開ける。ここに原典があれば ✅ の資格あり。

### AI・機械学習
| Source | URL | Note |
|---|---|---|
| arXiv | https://arxiv.org/ | ML/AI最大のプレプリント。全文無料。査読前である点だけ注意 |
| OpenReview | https://openreview.net/ | トップ学会の査読プロセスまで公開。他研究者の評価も読める |
| Papers with Code | https://paperswithcode.com/ | 論文＋実装コード＋SOTAランキング。タスク別の最新性能が一目 |
| 各社公式Research | OpenAI / DeepMind / Meta AI / Anthropic | 一次発表。企業の主張である点は明記して引く |

### 心理・組織・社会科学（査読済みで無料全文）
| Source | URL | Note |
|---|---|---|
| PubMed Central (PMC) | https://pmc.ncbi.nlm.nih.gov/ | 無料全文の宝庫。**このセッションでMCP直結**（下記）。ペイウォール論文の無料版探しにも最適 |
| PLOS | https://plos.org/ | 全編オープンアクセス |
| Frontiers | https://www.frontiersin.org/ | オープンアクセス（Levine 2021 の掲載誌） |
| DOAJ | https://doaj.org/ | オープンアクセス査読誌の横断検索 |

### 公的統計・機関
| Source | URL | Note |
|---|---|---|
| OECD / e-Stat / 政府統計 | https://www.oecd.org/ ほか | 一次データ。市場規模・労働・生産性などの数字はここを優先 |

---

## Tier 2 — Discovery tools（探す道具。要約は出典にしない）

原典に「たどり着く」ために使う。**ここの要約・スコア・AI回答をそのまま引用しない** — 必ず Tier 1 の本文に降りて確認する。

| Source | URL | Note |
|---|---|---|
| Semantic Scholar | https://www.semanticscholar.org/ | Ai2製。引用数・関連論文。**abstractは根拠にできるが本文は別途確認** |
| Google Scholar | https://scholar.google.com/ | 網羅性・引用数。無料PDFリンクが出ることも |
| Connected Papers | https://www.connectedpapers.com/ | 1本を起点に関連論文のグラフ。周辺・反証を見つけるのに強い |
| Crossref | https://www.crossref.org/ | DOI・書誌の実在確認（捏造引用チェックに使用済み） |
| Consensus | https://consensus.app/ | 質問→査読論文から根拠を要約。**このセッションでMCP直結**。要約は出発点、原典で確認 |
| Elicit | https://elicit.com/ | テーマ→関連論文を表で整理。同上、原典で確認 |

### このセッションで直接呼べるMCP（Web検索より速い場合あり）
- **PubMed**：`mcp__plugin_bio-research_pubmed__*`（検索・全文取得・引用確認）。心理系の原典（DePaulo等）に直行できる
- **Consensus**：`mcp__plugin_bio-research_consensus__search`
- **bioRxiv/medRxiv**：`mcp__plugin_bio-research_biorxiv__*`（生物・医学プレプリント）
- ※接続状況はセッションごとに変わる。使えないときは通常のWeb検索へ

---

## Tier 3 — Secondary / do NOT cite（きっかけだけ。根拠にしない）

日本語で速く概観するには便利。ただし**主張の根拠には絶対に使わない** — ここで見た話は必ず Tier 1 の原典を突き止めてから引く。

| Source | URL | Note |
|---|---|---|
| Ledge.ai | https://ledge.ai/ | 国内AIニュース。トレンド把握のみ |
| AI-SCHOLAR | https://ai-scholar.tech/ | 海外論文の日本語解説。**解説を引かず、紹介元の原典を引く** |
| 一般の商用ブログ・メディア | — | リード（手がかり）まで。数字・主張の出典にしない |

---

## Changelog
- **2026-07-19** 新規作成。きっかけ：DePaulo 2003 / Bond & DePaulo 2006 がペイウォールで読者確認不能だった件と、商用ブログを出典にしかけた件。反応型検索から「先に信頼できる参照先を持つ」運用へ切り替え。
