# Theme 2: Tacit Knowledge — what can't be told? / 暗黙知 — 語れないものは移せるか

**Status:** ✅ All 6 rows human-verified 2026-09-04 — second theme fully checked (after Theme 1). Evidence gathered 2026-07-19; **B demoted 2026-07-27 after reading it in full, then human-verified 2026-07-31** (its 94.9% counts runs where every column *name* was mentioned, and its "employees" are LLM simulations holding fragments of an existing text), so the "AI can surface relational tacit knowledge" side now rests on Brynjolfsson alone. **E's own genre turned out to be misrecorded** — not a peer-review-adjacent working paper but an unreviewed teaching slide deck, discovered on full read 2026-09-04; this reinforces rather than changes its 2026-07-25 demotion to supplementary-only. Per-row state is tagged `［depth｜claim-support｜human-check］` — see the [legend](README.md#状態ラベルの読み方2026-07-27-導入).
**Verification note:** A, B, C, D, E and F are all ✅. Rule: [the-fabricated-citation.md](../the-fabricated-citation.md).

---

## なぜ暗黙知を調べるのか

クロス分析のB軸で最も価値が高いのは「暗黙の判断」——ベテランが崩れた手書きFAXを読める、「至急」の本当の意味を知っている——だと定義した。この分類の根っこには「暗黙知は言語化できず、だからAIに移せない」という前提がある（Polanyi の「我々は語れる以上のことを知っている」）。

だが、この前提には**強力な反証**がある。検証済み台帳にすでに載っている Brynjolfsson（QJE 2025）は、まさに「**AIがトップ層の暗黙知を新人へ波及させた**」ことを +14%/+34% の生産性向上のメカニズムとして挙げている。つまり私たち自身の台帳の中に、「暗黙知は人間の領域」説とぶつかる証拠がある。この衝突を解かないと、分類が自己矛盾する。

## 何がわかったか（構図）

衝突を解く鍵は、**「暗黙知」がひとつの塊ではない**こと。社会学者 Harry Collins の3分類が、証拠の割れ方ときれいに対応する。

### 分類の道具：Collins の暗黙知3種

1. **関係的暗黙知（relational）** — 原理上は言語化**できる**が、まだ誰もしていないだけの知識。（例：ベテランの頭の中の判断基準の多く）
2. **身体的暗黙知（somatic）** — 身体に宿り、命題の形にできない。（例：自転車の乗り方、手触りでの品質判定）
3. **集合的暗黙知（collective）** — 個人ではなく**社会的実践の中に**宿り、個人単位では言語化に抵抗する。（例：職場の空気の読み方、業界の商習慣の機微）

### AIが移せる・引き出せる側

- **Brynjolfsson & Li & Raymond（QJE 2025・✅検証済み）**：AI支援がトップ実績者の暗黙知パターンを新人に波及させ、生産性 +14%（新人+34%）。
- ~~**LLMによる暗黙知の発掘（2025）**：LLMエージェントが従業員への反復インタビューで暗黙知を抽出・整理し、高い再現率（94.9%と報告）。~~ **【2026-07-27 全文確認で大幅に格下げ】** Zuin et al. の 94.9% は「回収できた知識の割合」ではなく**「最終報告に全カラム名への言及があった実行の割合」**（864回中820回）。**中身の再現度は METEOR 0.17 と低い。** さらに相手の「従業員」は**LLMで模擬されたエージェント**で、配られる知識は**元から存在するテーブル説明テキストの断片**。＝**語れないものを扱う設計になっておらず、暗黙知の抽出をテストできていない**。実企業での検証は著者自身が今後の課題としている。→ この研究は「AIが暗黙知を引き出せる」根拠には使わない。
- **重要な補足**：**したがって「AIが移せる」側を実データで支えているのは、実質 Brynjolfsson（QJE 2025・✅検証済み）ただ一つ**。それが移しているのは Collins の言う**関係的暗黙知**（言語化可能だが未言語化だった部分）で、インタビューや行動ログから引き出せるのはこの層、という骨格自体は保つ。

### 人間に残る側

- **身体的暗黙知**：命題化そのものができない。熟練エンジニアがプルリクエストを「説明できる前に**おかしいと感じる**」——瞬時の認識と、後づけの言語化の間には埋まらないギャップがある。
- **集合的暗黙知**：社会的実践に宿るため、個人から抽出できない。医学教育の研究でも、暗黙知の伝達には師弟の密な相互作用（徒弟制）が必要とされる。
- **文書化されないものは学習データに存在しない**：AIの訓練データは「書かれたもの」の集合。書かれ得ないもの（身体知・実践知）は、原理的にそこにない。

### ひねり：AI自身が暗黙知の塊になった

現代のニューラルネットは明示的ルールではなくデータから「暗黙的に」学ぶ。つまり**AI自身が「語れる以上のことを知っている」状態**になり、解釈可能性・頑健性の問題を抱えている。Polanyi のパラドックスは人間からAIに引き継がれた——これは「AIが暗黙知を克服した」のではなく「暗黙知問題が場所を変えた」ことを意味する。

## この割れ方が意味すること（分類の核）

| 暗黙知の種類 | AIは移せるか | 根拠 | なぜ |
|---|---|---|---|
| 関係的（未言語化なだけ） | **移せる・引き出せる** | Brynjolfsson✅（**実データはこれのみ**。LLM発掘研究＝Zuinは2026-07-27の全文確認で根拠から除外し、2026-07-31に✅人間確認） | 言語化可能な層は、反復質問・ログ分析で表に出せる |
| 身体的（身体に宿る） | **移せない** | Polanyi論・専門家認知研究 | 命題化できないものは訓練データに存在し得ない |
| 集合的（実践に宿る) | **移せない** | Collins分類・医学教育研究 | 個人から抽出できず、実践への参加でしか伝わらない |
| （逆転）AI自身の暗黙知 | — | 解釈可能性研究 | AIも自分の判断を説明できない。問題は消えず移動した |

**分類の結論（暫定）：** 「暗黙知＝人間の領域」は粗すぎ、「AIが暗黙知を波及させる」も粗すぎる。**言語化可能なのにされていなかった層（関係的）はAIの強力な守備範囲**。Brynjolfsson との矛盾は矛盾ではなく、彼らが移したのがこの層だということ。**身体と実践に宿る層は原理的に残る**——「原理的に」というのが重要で、モデルの性能向上では超えられない種類の壁。

## クロス分析への含意

1. **B軸の「暗黙の判断」も二層に分けるべき** — ①聞けば言語化できる判断基準（関係的）→ AIの反復質問で externalize できる。むしろ積極的にAIを使って書き起こすべき層。②現場で身体が覚えている察知・実践の機微（身体的・集合的）→ **現場に居る人間**にしか拾えない。
3. **「ツールは①を効率化できても②は移せない」**（DIAGNOSIS-TEMPLATE の洞察）は、Collins の枠組みでそのまま学術的に裏付けられる。診断で顧客に説明するときの理論武装になる。
2. **手順と判断を分ける Nacit の分解は、関係的/身体的の分解と一致していた** — 経験則が理論と合流した形。

## まだわからない・要検証（次にやること）

- ✅【人間確認済 2026-07-31】「94.9%」は**「全カラム名に言及できた実行の割合」**であり知識の回収率ではないと確定。加えて**相手はLLMで模擬された従業員・配られる知識は既存テキストの断片**＝暗黙知の抽出をテストできる設計ではない。**この行は根拠から除外**（詳細は下の台帳B）。内容品質の指標は割れる（METEOR 0.17／G-Eval Coherence 2.65 vs Faithfulness 4.37）。掲載はIJCNN 2025（IEEE）。
- ✅【人間確認済 2026-09-04】Collins 3分類は Soler & Zwart 2013（Philosophia Scientiæ 17-3, 査読誌）の全文PDFで定義を逐語照合し確定。加えて、この論文自体の主眼はRTK（関係的）の名称・定義への批判である点も判明（詳細は下の台帳C）。原典書籍そのものの通読は任意のまま。
- 身体的暗黙知は Theme 1（身体性）と重なる → 統合時に整理。
- 「プルリクを感じで見抜く」系の逸話は魅力的だが逸話。定量研究を探す。

## 出典（要・人間検証）

| # | 主張の核 | 一次リンク | 状態 |
|---|---|---|---|
| A | AIがトップ層の暗黙知を新人に波及（+14%/+34%） | https://www.nber.org/papers/w31161 | ✅（検証済み・台帳既存） |
| B | LLMエージェントが暗黙知を反復抽出（94.9% full-knowledge recall と報告） | https://arxiv.org/abs/2507.03811 （Zuin, Mastelini, Loures & Veloso, "Leveraging Large Language Models for Tacit Knowledge Discovery in Organizational Contexts", **査読済み会議録＝2025 International Joint Conference on Neural Networks (IJCNN), IEEE, doi:10.1109/IJCNN64981.2025.11227259**。読んだのは著者版のarXiv PDF） | ✅**確認済み（2026-07-31）**。全文をvision付きで再読し、下記の数値・引用をすべて原文で照合済み（経緯：2026-07-19 arXiv要旨で確認→2026-07-25「864回の合成シミュレーション」と注記→2026-07-27にテキスト抽出で全文精査・3点訂正→2026-07-31にPDF原本で最終確認）<br>**訂正①：94.9%の意味を取り違えていた。** 旧記述「反復対話で回収できた知識の割合」は誤り。原文の定義は "An agent is considered to have achieved full-knowledge recall in an experiment run if it succeeded in at least **reproducing all table columns** in its final report."＝**「最終報告に全カラム名への言及があったか」の実行単位の二値判定**で、864回中820回が該当。**知識の回収率ではない。**<br>**訂正②：内容品質の指標は割れている（94.9%だけでは語れない）。** 同じ論文が報告する内容品質は **METEOR 0.17**（カラム説明文と正解テキストの語彙一致度）、**G-Eval Coherence 2.65/5**、**G-Eval Faithfulness 4.37/5**（G-Evalは1〜5点）。語彙一致と一貫性は低〜中だが**忠実性は高め**で、著者自身 "looking directly at the value of those metrics is insufficient to evaluate the quality of the created texts definitively" と留保している。**また94.9%に届かなかった44回でも平均約77%のカラムは再現**。**自己評価の甘さは要注意**：正解テキストを見せると自己批評スコアは 7.43→6.75 に下がる。<br>　※**2026-07-27 自己訂正**：この欄に最初「説明の中身は原文と大きく違う」と書いたが**言い過ぎだった**。METEORが低いのは語彙一致が低いという意味で、内容の相違を意味しない（だからこそ著者はG-Evalを併用している）。**不利な指標(0.17/2.65)だけを引いて有利な指標(4.37)を落としていた**＝この監査が正そうとしているチェリーピッキングを自分でやっていた。<br>**訂正③：相手は実在の人間ではない。** 「従業員」も**LLMで模擬されたエージェント**。しかも「真の知識 k*」＝**既存のテーブル説明テキストそのもの**で、1カラム＝1"fact" としてSIモデルでネットワークに配布される。**つまり最初から書かれたテキストを分割して配り、それを集め直せるかを測っている**——語れないものを扱う設計ではないので、**この研究は原理的に暗黙知の抽出をテストできていない**（Collinsの分類でいえば関係的暗黙知ですらなく、単なる明示知の分散回収）。著者自身 "we are implementing our approach at Kunumi, letting the agent interact with **real employees**" と実企業検証を**今後の課題**として明記。<br>**利害関係**：著者4名全員が Kunumi 所属、"funded by the authors' individual grants from Kunumi"。<br>**→ 結論：この行は「AIが暗黙知を抽出できる」証拠として使わない。** 使うなら「明示化済みの知識が組織に分散している場合、LLMエージェントが人づてに集め直せるという**シミュレーション上の**示唆」まで。<br>**訂正④（2026-07-27・査読状態）：「査読前プレプリント」は誤りだった。** Crossrefで確認したところ **IJCNN 2025（IEEE）に採録・出版済み**（doi:10.1109/IJCNN64981.2025.11227259, 2025-06-30）。arXivにあることだけを見て未査読と書いていた（arXivメタデータにはjournal_ref・comment欄が無く、PDFの "©2025 IEEE" 表記だけが手がかりだった）。**格下げの理由は査読の有無ではなく、上記①〜③の設計上の限界である**点は変わらない |
| C | Collins: 関係的/身体的/集合的の3分類 | 原典＝Collins, *Tacit and Explicit Knowledge* (Univ. of Chicago Press, 2010, 書籍)。裏付け→ https://journals.openedition.org/philosophiascientiae/892 （Soler & Zwart, "Collins's Taxonomy of Tacit Knowledge: Critical Analyses and Possible Extensions", *Philosophia Scientiæ* 17-3, 2013, pp.107-134, DOI: 10.4000/philosophiascientiae.892） | ✅**［全文｜③✓｜人間確認:無料全文（PDF・2026-09-04）］** 3分類の定義を原文で逐語照合——身体的「knowledge *stored in* the muscles, nerve pathways, and synaptic connections」(p.118)／集合的「knowledge *located in* society」「a property of society rather than the individual」(p.118)／関係的「could be made explicit ... but is not made explicit」(p.110)。**この論文自体の主眼はむしろRTK＝「関係的」という名称・定義への批判**——Collinsの5下位事例のうち真に人間関係由来なのは2つのみと論証し、「relational」を「contingent（偶発的）tacit knowledge」への改名を提案している。台帳が使うのは3分類の定義部分のみで、この改名論自体は未採用 |
| D | 医学教育: 暗黙知の伝達は師弟の密な相互作用が必要 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12927663/ （Papadimos, Hsu & Pappada, "Insights From Michael Polanyi: Tacit Knowledge and Its Critical Importance in Medical Education", Cureus 18(1):e102205, 2026-01-24, doi:10.7759/cureus.102205） | ✅**［全文｜③✓(注記あり)｜人間確認:無料全文（PDF・2026-09-04）］** 出版社PDF原本で4引用すべて逐語再照合——「To pass this knowledge on to a learner, trust and sustained close personal interaction with a teacher or mentor are essential.」／「a learner who is not physically present with their teacher or mentor when examining a patient or performing a procedure is highly likely to fail in replicating that specific task or skill.」／種別＝誌面表記どおり**Editorial**／結論「Current models cannot fully replace an instructor.」もすべて一致、訂正なし。**必須注記（据え置き）**：この論説は反AIではない。結論は「ML/AIと高精度シミュレーションは暗黙知伝達の**有用な補助(adjunct)**になりうるが、現行モデルは指導者を完全に置き換えられない」。人間側の証拠として使うとき、著者の立場を"AI否定"に読み替えないこと。Polanyi核 "we know more than we can tell" の引用も確認＝C/E/Fのアンカーにも使える |
| E | 暗黙知・身体知は訓練データに存在し得ない（Polanyi論） | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5292030 （Garg & Gohil, 実物タイトルは"Does AI Know? A Tacit Knowledge Perspective"（SSRN掲載タイトル"Can AI understand Tacit Knowledge?"とは不一致）, IIM Indore, 2025） | ✅**［全文（79ページ・PDF・2026-09-04）｜③△(格下げ・強化)｜人間確認:無料全文］** **ジャンル訂正が最大の発見**：査読前ワーキングペーパーではなく、**IIM Indore教員（Swapnil Garg）＋学部生助手による講義/発表用スライド資料**（査読なし、"Fun Fact"等の雑談スライドを含む、本文の大半はPolanyi原著テキストを教員チームがコーディングし直した解説）。AIへの直接言及は確認できる（p.72「AI (as of June 2025) is incapable of capturing tacit knowledge」「the internalized knowledge of the expert cannot be captured or perceived by AI」）が、根拠は**建設業DPR（詳細プロジェクト報告書）をAIに読ませた単一の逸話的試行のみ**——手法・サンプル数・評価指標の記載は一切なし。**＝02-Eが掲げる強い断定「訓練データに存在し得ない」という原理的主張までは述べていない、という2026-07-25の格下げ判断は全文読了でも維持・むしろ強化される。強い主張はC(Soler & Zwart 査読)＋D(Cureus)＋F(Kambhampati 全文確認)が支える。02-Eは"話題が近い補助"に留め、単独の根拠に使わない（外しても分類は成立）** |
| F | ニューラルネット自身が「語れない知」を持つ（問題の移動＝Polanyiの逆襲） | 著者公開PDF: https://rakaposhi.eas.asu.edu/Polanyis-Revenge-CACM-Print.pdf （Kambhampati, "Polanyi's Revenge and AI's New Romance with Tacit Knowledge", CACM 64(2):31-32, 2021, doi:10.1145/3446369） | ✅**［全文｜③✓｜人間確認:無料全文（2026-09-04）］** 著者公開PDFを直接開いて本文を人間確認。「解釈可能性・バイアス・頑健性の問題は、データから暗黙知を学ぶ一極集中に直接遡れる」「生データから独自表現を学ぶ推論は解釈可能である理由がない」を確認。著者＝元AAAI会長。**種別＝CACM Viewpoint（論説）だが、③整合は全文で確認済み（AI確認2026-07-19/25、人間確認2026-09-04）＝主張と一致** |

*【2026-07-19 更新】C・Fは二次ブログから原典（Soler & Zwart 2013 OA／Kambhampati CACM 2021 著者PDF）へ差替済み。*

*【2026-07-27 更新】**Bを全文で読み直して格下げ**——94.9%は「知識の回収率」ではなく「最終報告に全カラム名への言及があった実行の割合」、かつ被験者はLLMで模擬され配布される知識は既存テキストの断片だった（詳細は台帳B）。**この結果、AIが移せる側を実データで支えるのはA（Brynjolfsson・✅）のみになった。** 深度はB=全文／C=代替OA本文／D・F=全文。査読状態も訂正（Bは「プレプリント」ではなくIJCNN 2025出版済み）。Eは2026-07-25に補助へ格下げ済み。各行の状態は `［深度｜③｜人間確認］` を参照。*

*【2026-09-04 更新】**Cを人間確認（✅化）**——Soler & Zwart 2013 の全文PDFで3分類の定義を逐語照合。加えて、この論文の主眼はRTK（関係的）という名称・定義そのものへの批判である点も判明（Collinsの5下位事例のうち真に人間関係由来なのは2つのみ、「contingent」への改名を提案）。台帳が使うのは3分類の定義部分のみで、改名論自体は未採用。*

*【2026-09-04 更新②】**Dも人間確認（✅化）**——Cureus出版社PDF原本で4引用すべて逐語再照合、訂正なしのクリーンな確認。*

*【2026-09-04 更新③】**Eも人間確認（✅化）**——SSRN PDF全79ページを読了。最大の発見は**ジャンル訂正**：査読前ワーキングペーパーではなく、IIM Indore教員＋学部生助手による講義/発表用スライド資料だった（実物タイトルもSSRN掲載タイトルと不一致）。AIへの直接言及はあるが、根拠は建設DPRをAIに読ませた単一の逸話的試行のみ。2026-07-25の格下げ判断（強い断定の裏付けにはならない）は全文読了でも維持・強化。*

*【2026-09-04 更新④】**Fも人間確認（✅化）**——著者公開PDFを直接開いて本文の2引用を確認。**テーマ2はA〜Fの全6行が✅、Theme 1に続き2つ目のテーマ完走。***
