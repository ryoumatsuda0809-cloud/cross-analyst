# Theme 4: Trust & Disclosure — who gets the truth? / 信頼と自己開示 — 誰が本音を引き出せるか

**Status:** ⚠️ AI-verified, awaiting human verification of primary sources. Gathered 2026-07-19; **human side rebuilt 2026-07-20** (the depth claim retired; anchored on trust); claim-support audited 2026-07-26/27 — **A's "free full text" turned out to be a dead link** (abstract-level only now), **B (Pickard) is unverifiable at all** since the publisher withholds even the abstract, so it is demoted to supporting-only, **C's claim was rewritten** to match what the study actually measured (willingness to pick a disclosing statement, not depth), and **J gained a DOI and a free full text**.
**Verification note:** Per-row state is tagged `［depth｜claim-support｜human-check］` — see the [legend](README.md#状態ラベルの読み方2026-07-27-導入). Nothing here is ✅ yet: open the primary link and check before publishing. Rule: [the-fabricated-citation.md](../the-fabricated-citation.md).

---

## なぜ信頼と開示を調べるのか

クロス分析のB軸は「現場の生の声・本音」を集める工程だ。だが**本音は、集めようとして集まるものではない**。相手が話す気になって初めて出る。では「誰に対してなら人は本音を出すのか」——人間か、機械か。ここを検証しないと、「ヒアリングは人間の仕事」という分類が根拠を持たない。

テーマ3（共感）と同じく、**素朴な予想は裏切られる**。そして裏切られ方に、B軸を人間に置く本当の理由が隠れている。

## 何がわかったか（構図）

ここでも証拠は割れる。だが今回は「開示の"種類"」で割れる。

### 機械の方が引き出せる側 ── 「恥ずかしい事実」の開示

- **Lucas et al. 2014（Computers in Human Behavior）**：相手が「コンピュータだ」と信じた被験者は、評価される恐怖が下がり、自己開示が増えた。（テーマ3の反証として既出、ここが本拠地）
- **アバター vs 人間インタビュアー**：機微度の高い話題では、人間よりアバター相手の方が答えられたとされる（Pickard et al. 2016）。**ただしこの出典は本文も要旨も入手不能で③未確認のため、補助扱い**（2026-07-26）。同じ機構は次の項目（Croes・全文確認済み）が支える。
- **「判断されない安全地帯」**：人はチャットボットを、恥ずかしい・後ろめたい話を打ち明ける安全地帯とみなす。「コンピュータは社会的判断に必要な心を持たない」という認知が理由。
- **開示"意向"は同等という研究も**：Merwin et al. 2025（CHB:AH）——自己開示型の発言を選ぶ確率はAI相手と人間相手で同程度。**さらに、どちらの相手よりも「誰にも見せない」条件の方が有意に低い**（＝開示は privacy の問題というより、聞き手がいるかどうかの問題）。※測っているのは意向で、開示の量・深さではない。

**なぜ機械が勝つのか：** 恥の核心は「相手にどう思われるか」。相手が心を持たない（と信じられる）なら、評価の恐怖が消える。＝開示の障壁が"判断される恐怖"であるタイプの情報では、機械が有利。

### 人間の方が引き出せる側 ── 「信頼」と「具体の豊かさ」（"深さ"の人間優位は証拠が弱い）

**重要な立て直し（2026-07-20）：** 追加調査の結果、「人間の方が深く引き出す」という素朴な予想は**査読証拠にほとんど支持されない**ことが判明した。むしろ複数の査読研究は、AIが同等以上に"情報量・具体性"を引き出すと報告する（＝人間側主張への反証）：

- **Xiao et al. 2020（ACM TOCHI・実地N≈600）**：チャットボットの会話型調査は、通常のWeb調査より**エンゲージメントが高く、回答の質（情報量・関連性・具体性・明瞭さ＝Gricean Maxims）も有意に高い**。
- **Barari et al. 2025（N=1,800）**：AIの追い問いで開示は**より詳細で情報豊富**に（respondent experienceはわずかに低下）。
- **Wieland et al. 2026（HICSS・N=151）**：LLMの文脈的プロービングが**主題的豊かさ（thematic richness）と回答長を有意に増やした**。

では人間側に残る足場は何か。**"深さ"ではなく、実質的には「信頼」ただ一つ**だ：

- **信頼（trust）** — 判断の恐怖はAI相手で下がっても、**相手への信頼は人間の方が高い**（D=Croes et al. 2024）。恐怖の低さ≠信頼の高さ。これは"深く引き出す力"ではなく"関係の質"の話。

**注意：Cuevasは「人間の優位」ではなく「AIの限界」の研究：** ここでよく引きたくなる **Cuevas et al. 2023/25（Proc. ACM HCI・CSCW・N=399）** は独自の"richness"尺度で、LLMインタビュアーが既存指標では高品質でも**回答者固有の動機や個人的な事例をほとんど捉えられない**と実証した。だが**この研究の比較対照は定型質問ボットであって、人間インタビュアーではない**。したがって「人間の方が豊かに引き出せる」ことを示した研究は依然として存在せず、Cuevasが言えるのは「現在のAIには固有の具体を取りこぼす限界がある」までだ。**人間優位の証拠に数えてはいけない**（＝"人間側のアンカー"という言い方も本来は過大）。

なお ~~ラポール（信頼関係）が本音の前提~~ **【2026-07-19 撤回】**：裏付けに引いていた Rao 2026（*Qualitative Sociology*, OA）は実際には**逆向き**——ラポール前提を批判する論文（「ラポールは時に有害」「開示を駆動するのは参加の決断」）。引用ミスとして台帳Fに記録。「ラポール＝本音の前提」という通念自体が係争中であり、**人間有利の根拠には使わない**。

**なぜ人間が勝つのか（精密版）：** 深い本音の障壁は"判断の恐怖"だけではない。「この人になら話す価値がある」という**信頼**、ためらいを読んで踏み込む間合い、"言われなかったこと"に気づく身体的な察知——これらは関係と身体を伴う。**ただし「AIより深く引き出せる」という主張は現時点で査読証拠が支えていない**。人間の足場は「深さ」そのものより、**信頼**と**固有の具体の察知**にある。

## この割れ方が意味すること（分類の核）

テーマ3と全く同じ構造が現れた。**測っている"開示"が違う**。

| 開示の種類 | 誰が有利 | 根拠 | なぜ |
|---|---|---|---|
| 恥ずかしい/後ろめたい"事実"の開示 | **機械が有利になりうる** | Lucas14, アバター研究 | 障壁が"判断される恐怖"→心を持たぬ相手なら消える |
| 単純な個人情報の開示（量） | **同等** | ScienceDirect25 | どちらにも同程度出す |
| 回答の情報量・具体性・回答長（"質"の一般指標） | **AIが同等〜有利** | Xiao 2020 / Barari 2025 / Wieland 2026 | 追い問い・プロービングで機械が引き出す。「人間の方が深い」は支持されない |
| 固有の具体（固有の動機・個人的な事例＝richness） | **AIに限界あり（人間優位とは言えない）** | Cuevas et al. 2023/25（N=399・独自richness尺度） | 現在のLLMは高品質指標を満たしても固有の具体を取りこぼす。※対人間の直接比較ではない |
| ためらい・皮肉・トーン・"言われなかったこと"を読む | **人間**（※修正あり） | AI比較研究 | 非言語の察知は身体を伴う。**ただし Theme 1 の発見により限定：人間の強みは非言語からの"正確な検出"（欺瞞検出は54%とほぼ偶然）ではなく、リアルタイムの関係調整と追加の問いへの接続** → [01-embodiment.md](01-embodiment.md) |
| 相手への信頼そのもの | **人間** | 開示研究 | 恐怖の低さ≠信頼の高さ |

**分類の結論（更新）：** 「本音は人間にしか出さない」は不正確。**"恥ずかしい事実"はむしろ機械相手の方が出る**。そして立て直し後の重要な訂正——**"深く引き出す"ことも人間の専有ではない**：査読証拠はAIが同等以上に情報量・具体性を引き出すと示す。人間側に残るのは**「相手への信頼」と「固有の具体の察知」**であり、"言われなかったこと"を読む身体的察知（Theme 1）。開示の障壁が「判断の恐怖」か「信頼・関係」かで勝者が入れ替わる、という骨格は保つが、"深さ＝人間"という素朴な主張は捨てる。

> **【2026-07-20 立て直し完了】** 前回「人間側の証拠が最も薄い」としたテーマを再調査した。結論：**「人間の方が深く引き出す」は査読証拠に支持されない**——Xiao 2020（TOCHI, N≈600）/ Barari 2025（N=1,800）/ Wieland 2026（HICSS, N=151）はいずれもAIが同等以上に情報量・具体性・豊かさを引き出す。撤回したG（insightplatforms＝業界二次情報）は査読の一次 **Cuevas et al. 2023/25（Proc. ACM HCI, N=399）** に置換したが、その知見は「現在のLLMは"richness＝固有の具体"を取りこぼす」という**"AIの限界"**であって、人間の証明された優位ではない（比較対照は人間ではなく定型ボット）。**人間側の本当の足場は「深さ」ではなく「信頼」（D=Croes 2024）と「リアルタイムの関係調整」（Theme 1）**。この修正は [human-territory.md](../human-territory.md) の H7 に反映済み。

## クロス分析への含意（B軸を人間に置く、精密な理由）

テーマ3・4を合わせると、B軸が人間である理由が二段構えで言える：

1. **B軸の本質は"事実の収集"ではなく"意味の察知"** — 収集だけなら機械でもよい（恥ずかしい事実はむしろ機械が得意）。だがB軸で本当に価値があるのは「ためらいの奥・言われなかったこと・どの声が構造を支えるか」であり、それは信頼関係と身体的察知を要する＝人間。
2. **だから設計はハイブリッドが最適** — テーマ3の含意と一致：**匿名で恥ずかしい事実を出させる初期インテークはAI/ツール、深い本音と非言語を読む対面ヒアリングは人間**。これは「人間 vs AI」ではなく役割分担の精密化であり、Nacitの診断オペレーション（Drive の運用手順にある匿名フォーム→対面ヒアリングの二段構え）とも整合する。

## まだわからない・要検証（次にやること）

- ⚠️ 全一次リンクを人間が開いて確認（下の台帳）。特に **I（Barari 2025）の査読状態**と、**G（Cuevas）のCSCW掲載年・著者名綴り**、H/JのDOIを確定。
- ~~「深さ・本物さ」を定量化した研究をもっと探す~~ **【2026-07-20 完了】** Cuevas（richness尺度）＋反証群（Xiao/Barari/Wieland）で立て直し。結論：**"深さ＝人間"は査読証拠に支持されない**。人間側は「信頼」と「固有の具体の察知」に絞った。
- 非言語の察知（トーン・ためらい）は Theme 1（身体性）と重なる → そちらで深掘る。
- Lucas 2014：人間が一次リンクを開いて確認し✅化する（テーマ3から持ち越し）。※「一次PDFが sources にある」と書かれていたが **sources ディレクトリは存在しない**（deep-research出力の虚偽記述を2026-07-19削除）。SDはペイウォール——無料版探しはBと同時に。

## 出典（要・人間検証）

| # | 主張の核 | 一次リンク | 状態 |
|---|---|---|---|
| A | コンピュータと信じると評価恐怖↓・開示↑（本拠） | https://www.sciencedirect.com/science/article/abs/pii/S0747563214002647 （Lucas, Gratch, King & Morency, CHB 37:94-100, 2014, doi:10.1016/j.chb.2014.04.043）**／ペイウォール。無料で読めるのは要旨のみ**→ https://www.semanticscholar.org/paper/34e2cb7a4fef0651fb5c0a120c8e70ebab9f0749 | ⚠️**［要旨｜③✓｜人間確認:無料要旨のみ(全文は存在せず)］**（2026-07-19照合：Semantic Scholarで書誌・要旨確認。被引用849。**2026-07-26に要旨原文で4項目すべて再確認**——"participants who believed they were interacting with a computer reported lower fear of self-disclosure, lower impression management, displayed their sadness more intensely, and were rated by observers as more willing to disclose"＝③整合。**⚠️訂正：2026-07-25に記録した「CMU研究室に無料全文あり」は誤り（リンク切れ）**。2026-07-26に実取得を試みた結果、記事ページ・PDF直リンク（`wp-content/uploads/2017/09/2014_CHB_Lucas_It.pdf`）・USC ICTのPDFすべて **HTTP 404**、unpaywall も `is_oa: false`。**現時点で無料全文は存在しない**＝人間確認も要旨止まりになる） |
| B | 高機微な話題（機微度の高い項目）はアバター>人間で開示（判定されない＝ジャッジ回避が鍵） | https://www.sciencedirect.com/science/article/abs/pii/S0747563216305684 （Pickard, Roster & Chen, "Revealing sensitive information in personal interviews...", Computers in Human Behavior 65:23-30, 2016, doi:10.1016/j.chb.2016.08.004） | ⚠️**［書誌のみ｜③判定不能｜人間確認:不能］**（2026-07-19：**リンクPIIからDOIを推測して誤った書誌に飛んだのを検出**→Crossrefで正しい書誌を特定。著者=Pickard/Roster/Chen。方向（機微度高→アバター選好・ジャッジ回避が要因）は複数の二次記述で一致するが**本文・要旨原文は未読**。無料版は確定的に無し（Crossref/Semantic Scholar=abstractもOA PDFも無・ResearchGateはRequest PDF・PMC対象外）。当初主張の「民族/浮気/収入」の具体3項目は原文で要確認）／**③整合＝判定不能（2026-07-26）**：無料版の不在を3系統で再確認（unpaywall `is_oa:false`・OpenAlex `any_repository_has_fulltext:false`・Semantic Scholarは**出版社が要旨自体を非公開**にしている）。要旨さえ読めないため③（主張を支えるか）は原理的に確認できない。**→ 単独の根拠として使わない。同じ機構（ジャッジ回避）は D（Croes・全文確認済み）がカバーするので、Bは補助に留める。「民族/浮気/収入」の具体3項目は本文に書かない**（未確認のため） |
| C | **開示を選ぶ確率**はAI相手と人間相手で同程度（＋どちらの相手より「誰にも見せない」の方が有意に低い） | https://www.sciencedirect.com/science/article/pii/S2949882125000647 （**Merwin, Hagen, Keebler & Forbes**, "Self-disclosure to AI: People provide personal information to AI and humans equivalently", *Computers in Human Behavior: Artificial Humans* **vol.5, 2025**, doi:10.1016/j.chbah.2025.100180, CC BY）。**無料の公式抄録**→ https://doaj.org/article/211548cad3194147b8197577df32377f | ⚠️**［要旨(DOAJ公式)｜③✓(測定の言い換え要)｜人間確認:無料全文(機械は403)］**（2026-07-19：タイトル＝主張そのものを確認。SDが機械アクセスを拒むため本文未読。**2026-07-26：DOAJ APIで公式抄録を取得し書誌を確定（著者4名・DOI・vol.5）**。③整合＝**方向は✓だが測定の言い換えが必要**：デザインは「自己開示型の文 vs 事実型の文」の**強制選択**で、回答が①AIに分析される②人間の研究者に分析される③非公開、の3条件を比較。原文 "Choice for self-disclosure rates were similar for the AI and human researcher, but significantly lower when responses were kept private"。**測っているのは"開示的な発言を選ぶ確率"＝意向で、開示の量・深さではない**（タイトルの "provide personal information" は設計より広い）。**副産物として重要な発見**：非公開条件が最も低い＝人は「誰にも読まれない」より「相手がいる」方を選ぶ。またAIへの否定的態度が強い人は自己開示型を選びにくい（重回帰）） |
| D | チャットボットは恥ずかしい話の「安全地帯」（判断されない認知）・**ただし恐怖低下は開示量を増やさなかった** | https://academic.oup.com/iwc/article/36/5/279/7692197 （Croes, Antheunis, van der Lee & de Wit, "Digital Confessions", Interacting with Computers 36(5), 2024, CC BY-NC） | ⚠️**［全文｜③✓｜人間確認:OUP・機械403］**（2026-07-19：「判断されない」認知と評価恐怖↓を確認。**重要な限定：恐怖の低下は実際の親密な開示量を増やさず**——「機械有利」を弱める方向の内訳として追記） |
| E | ChatGPTへの健康情報開示は**機微度が高いほど意向が下がる**（N=216・反復測定） | https://www.tandfonline.com/doi/full/10.1080/10447318.2025.2499656 （Kelly, White, Kaye & Oviedo-Trespalacios, "Tapping into Key Drivers: Self-Disclosure in Sensitive Health Conversations with ChatGPT", IJHCI 41(24):15668-15678, 2025）／**無料版＝TU Delft機関リポジトリ: https://research.tudelft.nl/en/publications/tapping-into-key-drivers-self-disclosure-in-sensitive-health-conv/** | ⚠️**［要旨(原文照合)｜③✓｜人間確認:無料(ランディング200/PDF403)］**（2026-07-19：**主張を修正**——「機械なら機微情報も出す」ではなく「高機微ほど出さない」が実際の知見。2026-07-25：T&FはペイウォールだがTU Delftリポジトリに無料版あり。**2026-07-27：③整合を原文で確認＋PDF直リンクを取得**（https://research.tudelft.nl/files/245862763/Tapping_into_Key_Drivers_Self-Disclosure_in_Sensitive_Health_Conversations_with_ChatGPT.pdf ・**ただしPDF直リンクは機械アクセスで403。到達を確認できたのはランディングページ(200)まで**——人間のブラウザなら開ける可能性が高いが、私は本文PDFを取得できていない）。原文＝"A repeated measures ANOVA revealed participants were significantly more likely to provide their data when the information required low-disclosure than high-disclosure."（N=216・4つのビネット・反復測定）。書誌 41(24):15668-15678 も一致。**未記載だった第2の知見を追加**：身体的健康シナリオの方が精神的健康シナリオより開示意向が有意に高い＝**「機微度」は量だけでなく領域でも効く**） |
| F | **【引用ミス・撤回 2026-07-19】**当初「ラポールが本音の前提」の裏付けとして登録していたが、実際は**逆**——ラポール前提への批判（「ラポールは常に有益ではなく時に有害」「開示を駆動するのは参加の決断」）。**反証・限定として登録し直し** | https://link.springer.com/article/10.1007/s11133-025-09619-8 （Rao, "The Problem with Rapport in Interview-Based Studies", Qualitative Sociology 49:47-70, 2026, **オープンアクセス**） | ⚠️**［全文｜③✗撤回済(逆向き引用)｜人間確認:無料全文］**（2026-07-19：捏造引用事件と同型の「中身と逆向きの引用」をAI検証で検出。「ラポール＝本音の前提」の裏付けには**使用不可**） |
| G | 現在のLLMインタビュアーは高品質指標を満たしても"richness"（回答者固有の動機・個人的な事例）を取りこぼす（N=399・独自richness尺度） | https://arxiv.org/abs/2309.10187 （arXiv版＝無料全文）／原典 **Cuevas, Scurrell, Brown, Entenmann & Daepp**, "Collecting Qualitative Data at Scale with Large Language Models: A Case Study", Proc. ACM Hum.-Comput. Interact. 9(2), CSCW, article CSCW049, 2025, doi:10.1145/3710947 | ⚠️**［要旨(arXiv)｜③✓｜人間確認:無料全文(preprint版)］**（2026-07-20/**書誌確定2026-07-25**：撤回した旧G＝insightplatforms二次情報を査読一次に置換。要旨で「established metricsでは高品質だが、回答者固有の動機・個人的事例を捉えられずrichnessが低い」を確認。※比較対照は定型質問ボットで**人間インタビュアーとの直接対決ではない**＝「人間優位」の証明ではない。**掲載＝PACM HCI Vol.9 Issue2, 2025（arXiv版は2023 preprint）**）／**2026-07-27 ③確認＋書誌訂正**：③は整合（N=399・"rarely capture participants' specific motives or personalized examples"・richness＝"the extent to which responses capture the complexity and specificity of the social context"・**比較対照は "a baseline which employs hard-coded questions" ＝定型ボットで人間ではない**ことを原文で再確認）。**ただし著者順が誤っていたので訂正**：Crossref/arXivとも正しい順は **Cuevas → Scurrell → Brown → Entenmann → Daepp**（旧記載はBrownとScurrellが入れ替わっていた）。**姓も "Cuevas Villalba" ではなく "Cuevas"**（Crossref given=Alejandro / family=Cuevas。旧注記の「Cuevas VillalbaでWeb確定」は誤り） |
| H | チャットボットの会話型調査はWeb調査よりエンゲージ・回答品質（情報量/関連/具体/明瞭）が有意に高い（実地N≈600）＝**人間側"深さ"主張への反証** | 無料＝arXiv 1905.10700 ／ 原典 Xiao, Zhou, Liao, Mark, Chi, Chen, Yang, "Tell Me About Yourself: Using an AI-Powered Chatbot to Conduct Conversational Surveys with Open-ended Questions", ACM TOCHI 27(3), 2020, doi:10.1145/3381804 | ⚠️**［書誌フル＋要旨｜③✓｜人間確認:無料全文(preprint版)］**（2026-07-20：著者7名・巻号27(3)・DOI・年をACM＋複数ソースで確定。preprint=2019/1905.10700、TOCHI掲載=2020。Gricean Maximsで機械優位を要旨確認。被引用171。**プロセス注記：当初この書誌を"検証前に記憶で"記入→直後にWeb確認して一致。結果は正しかったが手順違反（LESSONS.md 2026-07-20と同型）**） |
| I | AIの追い問いで開示は詳細・情報豊富に（respondent experienceはわずか低下）（N=1,800）＝反証側 | https://arxiv.org/abs/2504.13908 （Barari et al., "AI-Assisted Conversational Interviewing: Effects on Data Quality and Respondent Experience", arXiv 2504.13908, 2025） | ⚠️**［要旨｜③✓｜人間確認:無料全文(未査読)］**（2026-07-25：**査読前プレプリントと確定**＝arXiv 2504.13908、査読誌掲載の形跡なし。方向は反証側で採るが、**未査読ゆえ本文で断定に使わない**。数値・本文はarXivで人間確認を）／**2026-07-27 ③再確認＝整合**：arXiv要旨で「回答はより詳細で情報量が多くなった一方、回答者体験はわずかに低下」の**両方向**を確認（N=1,800）。**査読誌掲載は今も確認できず**（最新版 2025-12）。**追加の注意**：著者はチャットボットの自動コーディング性能を "moderate"、かつ回答者の追従バイアスにより**偽陽性がやや増える**と報告している——AI面接の万能視には使えない |
| J | LLMの文脈的プロービングが主題的豊かさ・回答長を有意に増やす（N=151）＝反証側 | **Wieland, Leyh & Ahrens**（TU Munich）, "From Prompts to Probes: How Large Language Models Improve Response Quality in Open-Ended Survey Research", *Proc. 59th HICSS*, 2026, **doi:10.24251/HICSS.2026.565**。**無料全文（CC BY-NC-ND 4.0）**→ https://hdl.handle.net/10125/111964 | ⚠️**［全文｜③✓｜人間確認:無料全文］**（2026-07-20：HICSSは査読会議・DOI未特定だった。**2026-07-27：DOIと著者3名をCrossrefで確定し、ScholarSpaceの無料全文PDF（8頁）を読了**。③整合を確認。原文の数値：被験者間3群（N=151）で、平均語数 EG1 無プロービング 41.88 → EG2 非文脈的 75.02 → **EG3 文脈的 106.02**。F(2,148)=13.45, p<.001, η²=.15、Tukey HSDでEG3>EG2 (p=.036)・EG3>EG1 (p<.001)。主題数も同様に文脈的プロービングが最多（Kruskal–Wallis H(2)=45.12, p<.001）。**注意点**：測っているのは**語数と主題数**という量的指標で、開示の深さや正直さではない。また著者自身が「長文の外れ値は態度が極端な回答者に多い」と注記） |

*A〜H・Gは査読（GのCuevasは PACM HCI 2025）、J＝査読会議（HICSS）、**I＝査読前プレプリント（arXiv 2504.13908・2026-07-25確定）**。G〜Jは今回の立て直しで追加した"人間側 深さ主張への反証"群——**結論：「人間の方が深く引き出す」は査読証拠に支持されない**（ただしIは未査読なので補強材料の扱い）。全て人間がリンクを開いて確認し ⚠️→✅ に上げること。*
