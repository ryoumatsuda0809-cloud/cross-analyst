# Theme 1: Embodied Presence — being there / 身体でその場にいること

**Status: ✅ all 7 rows human-verified (2026-07-27) — this theme's sources are done.** Gathered 2026-07-19, claim-support audited 2026-07-26/27, then checked row by row against primaries. The theme survived but narrowed: **A and C are opinion pieces** (a column and an editorial) and carry no evidential weight on their own; **B is a Neuron Perspective that explicitly declines to say AI is barred from embodiment**; so the in-principle claim rests on **D (Ziemke, peer-reviewed review)** alone. E1/E2 stand, with the caveat that both paywalled originals remain unread behind an open-access stand-in.
**Verification note:** Per-row state is tagged `［depth｜claim-support｜human-check］` — see the [legend](README.md#状態ラベルの読み方2026-07-27-導入). **All seven rows were opened and checked against primaries on 2026-07-27.** Three corrections came out of it: D is open access rather than paywalled (the earlier note mistook a bot-block for a paywall, same pattern as the Lucas 2014 dead link); **E1's free source does not actually cite DePaulo 2003**, so it backs the claim independently but is not a citation trail to the original; and **B, read in its published form, turns out to be agnostic about whether AI can acquire internal embodiment** — it proposes functional analogs for AI rather than arguing a limit, so it can no longer carry the "in principle" framing of this theme (D does). No row here is ⚠️ any more; keep the rule for anything added later. Rule: [the-fabricated-citation.md](../the-fabricated-citation.md).

---

## なぜ身体性を調べるのか

B軸の分担表で「AIは現場に座れない」と書いた。これが比喩なのか、原理的な限界なのかを確定させたい。もし「センサーとカメラを増やせば解決する」類の話なら、B軸の人間優位は時間の問題で崩れる。原理的な話なら、分類の土台になる。

**結果は二重だった**：身体性の議論には確かな土台がある。だが同時に、**私たち自身の主張2つに限定がついた**——①「人間は現場で非言語を読める」（テーマ4）は検出精度の話としては成立しない、②「AIには原理的に無理」も、最強アンカーだと思っていたKadambiが**その主張をしていない**ことが分かった（2026-07-27）。

## 何がわかったか

### 身体の不在は深い限界——ただし「原理的」と言い切れる範囲は限られる（人間側の土台）

- **LLMには身体がない（AI & SOCIETY 2026）**：身体的知識は言語に依存しない層にあり、言語モデルは身体的知識との接続に構造的に苦労する。
- **身体性は2領域に分かれる（Kadambi et al. 2026, Neuron）**：**内的身体**＝自分の内部状態を持続的にモデル化する働き（内受容感覚とホメオスタシス調整。原文の例は空腹・体温調節・ホルモン・血糖・水分バランス）と、**外的身体**＝物理世界との相互作用（運動実行・実世界フィードバック）。原著の力点は「AI研究はロボティクス等の**外的**身体に偏り、**内的**身体は手つかず」という点にある。LLMについて原著はこう書く——「"heat"を暖かさを感じることなく解釈し、"hunger"を必要を知ることなく解析し、身体動作を一度も行わずに記述する。その理解は統計的で、経験的な接地を欠く」。知能は身体から切り離せる計算ではなく、身体が「何を検出し、学び、できるか」を規定する（身体化された認知）。
  - ※以前ここに書いていた「疲労・不確かさの自覚」は**原著の例ではない**（2026-07-26の全文確認で修正）。内的身体の例は上記の生理的・内受容的なもの。「疲労・違和感・不確かさ」は本プロジェクト側の解釈・拡張として扱う。
  - ※**重要な限定（2026-07-27・掲載版で確認）：Kadambiらは「AIには原理的に無理」とは言っていない。** 彼らは内的身体を "functional and non-phenomenological framing" で定義し、"**our proposal remains agnostic about whether artificial systems similarly require such internal, subjective experiences**"、AIに要るのは "internal **functional analogs**... which need not require or replicate biological fidelity" と明言する。**本論はAIの改良提案**であって、身体性が原理的な壁だという論証ではない。→ **この見出し（原理的な限界）の根拠にKadambiを使わない。**
- **記号接地問題**：身体・状況・必要という統一構造を欠くため、AIの学習は文脈の接地でつまずく。
- **「原理的」と言えるのはどこまでか（2026-07-27整理）**：この見出しを支えるのは実質 **D（Ziemke 2016）** ——生きた身体のホメオスタシス的自己調整が認知を接地するという立場で、autopoiesis等の複数系譜が収斂する。**Bは「現在のMLLMに何が欠けているか」の記述**であって、将来AIが機能的等価物を持てるかについては著者自身が判断を保留している。**したがって本テーマの主張は「現時点でAIは身体経験を欠く」＋「生物学的身体を認知の基盤とみる有力な理論系譜がある」までで、「AIには永久に不可能」とは書かない。**
- 含意：これは**センサー追加で埋まる話ではなく、認知の構造の話**。ただし上記の通り、**"だからAIには永遠に無理" は本台帳の出典が支える範囲を超える**。

### ⚠️ ただし人間側にも不都合な事実（テーマ4への修正）

- **人間の嘘・欺瞞検出は約54%**（chanceをわずかに上回るのみ。Bond & DePaulo 2006, PSPR）。非言語手がかり自体（視線回避・まばたき・手の動き等）が診断的価値を欠くことは DePaulo et al. 2003, Psychological Bulletin が示す。**両論文はペイウォールだが、オープンアクセスの Levine 2021（Frontiers in Psychology, PMC8333997）で同じ主張を無料で読める**（下の台帳 E1/E2 参照）。
  - ※**2026-07-27訂正**：以前ここに「Levine 2021が**両方を引用**・確認」と書いていたが誤り。**Levine 2021の参考文献14件にDePaulo et al. 2003は入っていない**（引用しているのはBond & DePaulo **2006**／Hartwig & Bond 2011／Bond et al. 2015）。ただしLevine自身が該当の手がかり群を名指しして "lack diagnostic value" と明言しているので、**主張の無料での裏付けとしては成立する**（引用経路ではなく、独立した同趣旨の記述として使う）。
  - ※当初この2論文を混同していた点は数字の帰属確認で修正済み（2026-07-19）。
- **微表情トレーニングは効かない**：Jordan et al. (2019) の実験（90人）で、Ekman の METT 訓練群は偽訓練・無訓練群を上回らず、精度は偶然を下回った（全体 M=.46, 95%CI[.42,.50], p=.05／群間差なし F(2,87)=0.22, p=.80／ベイズ因子は「差なし」を約21:1で支持）。**皮肉なのは、訓練自体は機能していたこと**——微表情の識別能力は訓練で上がった（基準達成者 37.9%→72.4%）のに、嘘の見抜きは1つも改善しなかった。**2026-07-27：著者版全文（Huddersfield大リポジトリ）で3点とも人間確認済み。** 訓練が効いた群で示している点が効く——「訓練が失敗したから差が出なかった」という反論を封じている。
- **音声の嘘検出器は疑似科学**とする科学的レビュー。
- 含意：**「人間は現場で相手の嘘やためらいを"検出"できる」とは言えない**。テーマ4の「人間は非言語を読める」は、こう限定する必要がある——人間の強みは**検出精度ではなく、リアルタイムの関係調整**（相手の様子に合わせて間合い・話題・踏み込みを変え、信頼を築き、「言われなかったこと」を追加の問いにつなげる**行為**）。読み取った内容の真偽判定は人間も苦手。

## 分類（このテーマの判定表）

| 能力 | 判定 | 根拠 | なぜ |
|---|---|---|---|
| 物理的な現場に身を置き、五感で状況に接地する | **人間のみ**（原理的） | 身体化認知研究 | 身体・状況・必要の統一構造が認知の前提 |
| 自分の状態（疲労・違和感・不確かさ）の内的自覚 | **現状は人間のみ** | Kadambi 2026（現状記述） | 現在のMLLMは内部状態の持続的モデルを持たない。**ただし同論文は「AIに機能的等価物を持たせるべき」という提案であり、原理的不可能性は主張していない** |
| 非言語に合わせたリアルタイムの関係調整（間合い・踏み込み） | **人間優位** | 質的研究（T4） | 身体を伴う相互作用のループ |
| 非言語からの嘘・感情の"正確な検出" | **人間も苦手（54%）** — どちらの領域とも言えない | DePaulo 2003, METT研究 | 非言語手がかり自体が弱く不安定 |
| 複数モダリティの体系的記録・分析 | **AI/ツールが有利になりうる** | 自動解析研究（発展途上） | 網羅性・一貫性は機械の得意領域 |

**分類の結論（暫定）：** 「その場にいる」ことの価値は本物。ただし**「原理的にAIには不可能」とまでは本台帳の出典は言っていない**（→上記「『原理的』と言えるのはどこまでか」）。そしてその価値の中身は「人間は真実を見抜けるから」**ではなく**、①五感による状況接地、②信頼を作り相手の開示を引き出す身体的相互作用、③違和感という内的シグナル——にある。「見抜く」ではなく「引き出す・感じ取る・合わせる」。

## クロス分析への含意

1. **B軸の人間優位の言い方を修正する** — 「人間はためらいを読める」ではなく「人間は**その場の相互作用で開示を引き出し、違和感を感じ取れる**」。検出者ではなく**共鳴板**。この precision が、方法論の信頼性を守る（誇張した瞬間に疑似科学側に落ちる）。
2. **違和感は仮説であって判定ではない** — 現場で感じた「何かおかしい」は、クロス分析では**検証すべき仮説の種**として扱う（真偽判定に使わない）。これは既存の「断定しない・仮説として置く」ルールと一致。
3. **記録と分析はAIに任せてよい** — 現場の音声・映像の体系的な整理はむしろ機械が得意。人間は「その場」に集中する。

## まだわからない・要検証

- ✅【人間確認済 2026-07-27】**全7行を一次で確認完了**（下の台帳）。**種別の注意**：Aは意見コラム・Cは社説（どちらも証拠ではない）／**B は Neuron の Perspective**（Reviewではない）・**D は Biosystems の Review article**。**「原理的」を支えるのは実質D 1本**。**B・Dとも実はオープンアクセス**（当初「全てペイウォール」としていたのは誤り）。**E1/E2の原典（DePaulo 2003・Bond & DePaulo 2006）だけは依然ペイウォール未読**で、無料のLevine 2021が代役——ただしE1についてLevineは原典を引用しておらず「独立した同趣旨の記述」に留まる点は保持する。
- 「AIの感情認識が人間を超える」系の研究を追加で探す（今回の検索では直接比較が出なかった——ないと断定しない）。※Theme3で別途カバー済み（LEAS等）。

## 出典（**全7行✅人間確認済み・2026-07-27**）

| # | 主張の核 | 一次リンク | 状態 |
|---|---|---|---|
| A | LLMには身体がない＝身体的知識は人間-AIの本質的区別 | https://link.springer.com/article/10.1007/s00146-026-03000-1 （Twyman & O'Donnell, "A large language model has no body: embodied knowledge as a key distinction in human–AI interaction", *AI & SOCIETY* 41:5963-5965, 2026, doi:10.1007/s00146-026-03000-1）。**無料の公式共有リンク**→ https://rdcu.be/fwqBh （Springer SharedIt） | ✅**確認済み（2026-07-27）**。方向は一致——タイトル自体が主張そのもの。**内容は具体例による論証**（音楽家の耳トレーニング／サッカーの「ファーストタッチ」／身体的苦痛への共感）で、統計・実証データはゼロ。**種別は原文の編集部注記で確定**："Curmudgeon Corner is a short opinionated column..."＝査読論文ではなくオピニオン欄。**③整合＝△：主張の表明であって証拠ではない**——01-CのNature MI社説と同じ扱い。単独の根拠にせず、実質アンカーはB・D（**Bは Neuron の Perspective**。「原理的な限界」を支えるのはDの方） |
| B | 身体性は**内的身体**（内受容感覚・固有感覚・温度感覚・調節状態＝自分の内部状態の持続的モデル化）と**外的身体**（物理世界との相互作用）の2領域に分かれ、現在のMLLMは身体経験を欠く。とくに**内的身体はAI研究で手つかず** | https://doi.org/10.1016/j.neuron.2026.03.004 （Kadambi, Aziz-Zadeh, Damasio, Iacoboni & Narayanan, "Embodiment in multimodal large language models", **Neuron 114:1908-, 2026-06-03**, 種別＝**Perspective**, **CC BY 4.0 オープンアクセス**）。無料の別版→ arXiv https://arxiv.org/abs/2510.13845 | ✅**確認済み（2026-07-27・掲載版Neuron本体）**。経緯：2026-07-20に二次ニュース(TechXplore)から一次へ差替／2026-07-26にarXiv版を全文読了し主張を2点修正（内的身体の例に「疲労・不確かさ」と書いていたのは原著になし＝削除／「AIに欠ける2要素」は力点違いで、原著は "AI research has recently focused primarily on external embodiment via robotics and embodied agents" とし**欠けているのは内的身体**だと論じる）。**2026-07-27に掲載版で以下を確定**：<br>**訂正①：種別は「Review」ではなく "Perspective"**（Cell Pressの誌面表記）。査読誌の論考であって系統的レビューではない。<br>**訂正②：定義文の例示が掲載版でより厳密**——"(1) internal embodiment, or the internal states broadly construed that model internal dynamics and maintain homeostasis and internal control (e.g., **proprioception, interoception, thermoreception, and regulatory states**), and (2) external embodiment, incorporating interactions with the external world"。本文中の具体例（体温調節・ホルモン・血糖・水分バランス）は別途そのまま有効。<br>**⚠️最重要の発見：この論文は「AIには原理的に無理」とは言っていない。** 掲載版は明示的にこう限定する——"we explicitly operationalize internal embodiment in a **functional and non-phenomenological framing**" ／ "**our proposal remains agnostic about whether artificial systems similarly require such internal, subjective experiences**. We instead introduce the importance of internal **functional analogs** (or regulators) in artificial systems... **which need not require or replicate biological fidelity**"。**つまり本論はAIの改良提案であって、身体性がAIにとって原理的な壁だという主張ではない。**「原理的な限界」の根拠にこの行を使ってはいけない（その役割はD=Ziemkeが担う）。MLLM側の記述 "MLLMs lack any bodily experience..." は現状記述としては有効。<br>著者にA.Damasio（USC）＋Srini Narayanan（Google DeepMind）。IacoboniとNarayananが共同シニア |
| C | 身体は認知の構造の一部（intelligence is not computation abstracted from the body） | https://www.nature.com/articles/s42256-026-01239-3 （"From embodied intelligence to physical AI", *Nature Machine Intelligence* 8:491-492, 2026, doi:10.1038/s42256-026-01239-3）。ペイウォール・無料共有リンクなし（2026-07-27検索で未発見） | ✅**確認済み（2026-07-27）**。両主張とも原文一致："intelligence is not computation that can be abstracted from the body"／"the brain neither senses nor acts on the world except through the body"。**種別＝Editorial**（誌面に明記）。**両方とも社説自身の主張ではなく引用だった**——前者はBrooks, R. A., *Artif. Intell.* 47:139-159 (1991)（embodied AIの古典）、後者はBrunton & Tuthill, *The Transmitter* (2025)（COSYNE 2026での発言を紹介した記事）が出典。**③整合＝△：社説は主張の表明であって証拠ではない**——01-Aと同じ扱い。単独の根拠にせず、実質アンカーは引き続きB（Kadambi, Neuron査読Review）。**Brooks 1991は将来この主張の直接の柱にできる可能性あり**（古典的・被引用多数の一次論文） |
| D | 生きた身体（ホメオスタシス的自己調整）が身体化認知を接地する | https://www.sciencedirect.com/science/article/pii/S030326471630168X （Ziemke, "The body of knowledge: On the role of the living body in grounding embodied cognition", *Biosystems* 148:4-11, 2016, doi:10.1016/j.biosystems.2016.08.005, Review article）。**オープンアクセス**（CC BY-NC-ND、論文自体に明記）——**旧「SDペイウォール」の判定は誤りだった可能性が高い**（2026-07-25の自動チェックがボット検知の403をペイウォールと誤認したとみられる。Lucas 2014の死リンク誤判定と同型） | ✅**確認済み（2026-07-27）**。原文一致（要旨："the living body – and more specifically its homeostatic/allostatic self-regulation – plays in grounding both sensorimotor interactions and embodied cognitive processes"）。**種別＝Review article**（A・Cの意見コラム／社説とは違い、複数の理論的枠組み——autopoiesis(Maturana & Varela)・Christensen & Hookerの自律性理論・Bickhardの相互作用主義・Damasio/Panksepppの身体的情動理論——を横断的に統合した査読済みレビュー）。**③整合＝✓（据え置き・強化）**：A・Cと違い単なる意見の表明ではなく、複数の独立した理論的系譜が収斂する先として論証されている。**Theme1のもう一つの強いアンカー**（Bと並ぶ） |
| E1 | 非言語の欺瞞手がかりは弱い（視線回避・まばたき・手の動き等は診断的価値を欠く） | https://doi.org/10.1037/0033-2909.129.1.74 （DePaulo et al. 2003, Psych Bulletin 129(1):74-118／ペイウォール・**原典は未読**）。**無料で読める同趣旨の記述**→ https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ （Levine 2021, *Front. Psychol.* 12:642359, doi:10.3389/fpsyg.2021.642359, PMID 34366964） | ✅**確認済み（2026-07-27）**。**実在性を独立検証**：Crossref（Frontiers Media SA登録・参考文献14件）とPubMed/PMC（PMID 34366964／PMC8333997）が一致し、提供PDFの実物とも整合。捏造ではない。**原文一致**："The cues in question (gaze aversion, blinking, smiling, illustrators, hand movements, body movements, posture, and appearance) lack diagnostic value."<br>**⚠️訂正（2026-07-27）：旧記述「Levine 2021がDePaulo 2003を引用・確認」は誤り。参考文献14件にDePaulo et al. 2003は含まれない**（Levineが引くのはBond & DePaulo 2006／Hartwig & Bond 2011／Bond et al. 2015）。**したがってこの行は「原典を引用した確認」ではなく「独立した同趣旨の記述」として扱う**——主張の裏付けとしては成立するが、DePaulo 2003本体は依然として未読・ペイウォール。<br>**種別注記**：Levine 2021はFrontiersの **Opinion（意見論文）**。ただし当該の手がかり群の記述はメタ分析（Hartwig & Bond 2011等）を引いており、単なる私見ではない |
| E2 | 欺瞞判定の精度は平均54%・chanceをわずかに上回るのみ | https://doi.org/10.1207/s15327957pspr1003_2 （Bond & DePaulo 2006, PSPR 10(3):214-234／ペイウォール・**原典は未読**）。**無料で読める裏付け**→ https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ （Levine 2021） | ✅**確認済み（2026-07-27）**。E1と**バイト単位で同一のPDF**（SHA-256一致で照合）＝実在性の独立検証（Crossref／PubMed PMID 34366964）もE1と共通。**原文一致**："people are (a) slightly above chance accuracy overall, (b) truth-biased, and (c) more accurate at truths than lies... Findings to the contrary are refuted by literally hundreds of results (**Bond and DePaulo, 2006**)"／"Cue-based truth-lie discrimination is slightly better than chance (about d = + 0.4)"。<br>**E1との重要な違い：こちらは原典(Bond & DePaulo 2006)を実際に引用している**＝「引用による確認」として成立する（E1は独立した同趣旨の記述に留まる）。ただし原典 Bond & DePaulo 2006 本体は依然ペイウォール・未読。<br>**本プロジェクトに効く追加発見**：Levineは実験室外での実態をこう書く——研究協力者(confederate)による身元偽装では被験者はほぼ見抜けず "**Accuracy is near zero, not 54%**"。つまり**54%ですら実験室の設定に助けられた数字で、現実の検出力はさらに低い**＝「人間は検出者ではない」という我々の主張をむしろ強める |
| F | 微表情訓練(METT)は欺瞞検出を改善せず（90人・METT訓練群 vs 偽訓練群 vs 無訓練群、精度は偶然以下）。**微表情の識別能力自体は訓練で向上したのに、嘘の見抜きは改善しなかった** | https://doi.org/10.1002/jip.1532 （Jordan, Brimbal, Wallace, Kassin, Hartwig & Street, *J. Investigative Psychology and Offender Profiling* 16(3):222-235, 2019）。**無料全文＝著者版（Huddersfield大リポジトリ・31頁）**→ https://pure.hud.ac.uk/ws/files/17720891/accepted_manuscript.pdf | ✅**確認済み（2026-07-27）**。実在はCrossrefで独立確認（著者6名・16(3):222-235・2019-08-20・参考文献61件）、著者版全文（Huddersfield大リポジトリ・31頁・GREEN OA）と一致。経緯：2026-07-19に一次研究を特定・差し替え／2026-07-26に著者版を発見しプレスリリース依存を解消。**原文の数値（3点とも逐語確認）**：①全体精度 "slightly but significantly below the chance rate of 50%, (M = .46, 95% CI [.42, .50]), t(89) = -1.98, p = .05, d = 0.21"／②群間差なし "F(2, 87) = 0.22, p = .80, η2p = .01"（METT M=.46・偽訓練(IPT) M=.47・無訓練 M=.44）＋**ベイズ因子が「差なし」を約21:1で支持**＝帰無仮説の積極的支持／③**訓練自体は成功していた**——基準80%達成者が訓練前37.9%→訓練後**72.4%**、平均+11.66pt, t(28)=4.11, p<.001, dz=0.76。<br>**この行の価値**：「見抜く技術を身につけても見抜けるようにならない」ことを、**訓練が効いた群で**示している。訓練が失敗したから差が出なかった、という反論を封じる設計になっている。<br>※同論文p.3が Bond & DePaulo (2006) の54%を引用＝**台帳E2の帰属を裏づける無料の傍証**にもなる（著者のChris N.H. Streetは、E1/E2のLevine 2021の担当編集者と同一人物） |

*当初 F は liedetectortest.com という商用ブログを出典にしていた——一次情報ではないため差し替え済み（このプロジェクトの検証ルール違反を自己発見・修正した例）。*
