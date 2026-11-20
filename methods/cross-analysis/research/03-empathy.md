# Theme 3: Empathy — Is it really human territory? / 共感は本当に人間の領域か

**Status:** ⚠️ AI-verified (2026-07-19 citation check + **2026-07-20 mechanism deep-research**, 110 agents, 3-vote adversarial verification: 25 claims tested → 15 confirmed / 10 refuted), awaiting human verification of primary sources. **Claim-support audited 2026-07-27: K was cited backwards** — the paper found people judge a selfish decision-maker *more* responsible after following AI advice, the opposite of what this ledger said, and **the 3-vote deep-research had passed it 3-0**. J was narrowed to what it measured (helping intent toward a third party, not perceived empathy). H was confirmed in full, including the limit that its "human" comparison is a stranger, never someone the recipient has a relationship with.
**Verification note:** Per-row state is tagged `［depth｜claim-support｜human-check］` — see the [legend](README.md#状態ラベルの読み方2026-07-27-導入). Every claim is AI-checked against primary sources but **not yet human-verified**. Do not publish any figure until the primary link is opened and checked. This is exactly the rule from [the-fabricated-citation.md](../the-fabricated-citation.md).

---

## なぜ共感を調べるのか（分類の前提）

クロス分析のB軸（現場の声・気持ち）を「人間の領域」と置いた。その根拠として最初に思いつくのが「共感は人間にしかできない」だ。だが**この前提自体を検証しないと、分類が思い込みになる**。だから最初に共感を、しかも「人間有利」の証拠だけでなく「AIの方が共感的と評価された」反証も同じ厳しさで集めた。

結論を先に言うと——**「共感＝人間だけ」は、そのままでは成り立たない**。証拠は「共感を分解すると領域が分かれる」ことを示している。この分解こそが、分類の本体になる。

## 何がわかったか（構図）

証拠は真っ二つに割れている。割れ方に意味がある。

### AIが人間に匹敵／凌駕する側（テキスト・非同期・第三者評価）

- **医師 vs ChatGPT（JAMA Internal Medicine 2023）**：Redditの実際の患者質問195件で、盲検評価者はChatGPTの回答を78.6%で医師より好み、「共感的」評価は9.8倍。ただし著者自身が交絡を明記——**AIの回答は約4倍長く**（211語 vs 52語）、長さが共感と誤認された可能性、評価者が共著者、共感尺度が未検証。
- **思いやり（Nature系 2024, N=556）**：第三者評価で、AI(GPT-4)の回答が人間より「思いやりがある」と評価（Study 1で d=0.73）。**危機対応の専門家より**もAIが高評価（Study 3/4）。AIと明かしても優位は残った（縮んだが）。
- **メタ分析13研究（2025）**：AIチャットボットの共感評価は医療者より有意に高い（SMD 0.87）。ただしGPT-4は大きな優位（SMD 1.03）だがGPT-3.5は有意差なし＝**モデル性能で変わる**。限界：全てテキスト・代理評価者（実患者でない）・15研究中検証済み尺度は1つのみ・6研究が高バイアスリスク。
- **心理アドバイス盲検（ScienceDirect 2025）**：臨床家の盲検評価で、AIのアドバイスが感情的共感(OR=1.79)・動機的共感(OR=1.84)で専門家を上回った。認知的共感は同等。

### 人間が優位な側（帰属が既知・行動選択・「分かってもらえた」感）

- **Rubin et al.（Nature Human Behaviour 2025, 9実験 n=6,282）**：**全く同一の文章**でも「人間から」とラベルされた方が共感的・支持的と評価され、ポジティブ感情を多く引き出した。差は**感情的/動機的共感**（気持ちの共有・気にかけ）で生じ、認知的理解では生じない。行動選択でも人間を一貫して選好。
- **決定的なメカニズム（ScienceDirect 2025, 同研究の別面）**：評価を駆動したのは**実際の書き手ではなく「誰が書いたと信じたか」**。専門家作と信じたアドバイスへの選好は圧倒的（93.55%が信じた方を選好）。＝性能差ではなく**帰属・真正性**の効果。

## この割れ方が意味すること（分類の核）

矛盾ではない。**測っているものが違う**。整理すると：

| 共感の成分 | 判定 | 根拠 | なぜ |
|---|---|---|---|
| 認知的共感（状況を読む・理解する） | **AI同等〜優位**（テキスト） | JAMA23, ScienceDirect25 | 言語で表現できる理解は、AIの得意領域 |
| 感情的/動機的共感（テキスト表現・匿名） | **AIが高評価されうる** | Nature24, メタ分析25 | 丁寧・長文・定型の気遣いは書ける |
| 「分かってもらえた」感・真正性（書き手が既知） | **人間優位** | Rubin25 | AIと知るだけで感情的価値が下がる＝帰属効果 |
| 行動としての選好（どちらを選ぶか） | **人間を選ぶ**（※質の評価とは逆転） | Rubin25／Wenger26 | 感情的支えは人間から受けたい。**ただしAIの反応の方が"高品質"かつ"労力大"と評価されても選ばれない**＝評価と選択の乖離 |
| 「相手が労力を払った」という認知（コスト・シグナル） | **AIの方が高評価されうる**（素朴な人間優位説は反証） | Wenger26 | AIの反応の方が労力大と一貫して知覚される。それでも選択では人間が勝つ＝コスト知覚は選択を説明しない |
| 身体を伴う・実時間・実際の当事者 | **未解明**（確信度：低） | robotic embodiment研究（AI同士比較のみ） | 人間対AIの直接比較データが存在しない |

**分類の結論（暫定）：** 共感は「人間だけ」ではない。**書かれた共感の"質"はAIが匹敵・凌駕しうる**。だが**「本物だと感じられる／気持ちを分かち合ってもらえたと感じる」部分は、書き手がAIだと知られた瞬間に価値が落ちる**——これは性能ではなく帰属（誰が・どんなコストを払って）の問題。

## メカニズムの解明（2026-07-20 deep-research再検証・完了）

「なぜ帰属効果が起きるのか」を4つの仮説的メカニズム（真正性の帰属／コストのシグナル／身体性／責任）で直接検証する deep-research を実行した（110エージェント・25主張を3票で敵対的検証・15件生存/10件反証）。単なる「人間が勝つ/AIが勝つ」ではなく、**なぜ勝つ場合と負ける場合があるのか**が、査読研究から次のように解けた。

**結論（確定）：** メカニズム1・2（真正性の帰属／コスト・シグナル）は共感の文脈で**直接検証され、確信度highで決着**。メカニズム3・4（身体性／責任）は共感の文脈での直接証拠が乏しく、これ以上の追加deep-researchは行わない——代わりに他テーマの検証済み知見を**類推による代用**として下に接続する（直接証拠ではない旨を明記）。

### メカニズム1：真正性の帰属（authenticity attribution）—— 最も強く支持

- **信念そのものが評価を動かす**：Rubin et al. 2025の追加分析で、実験者が"AI"ラベルを貼らなくても、**参加者が自発的に「これはAIが手伝ったのでは」と疑っただけで**、"人間"ラベルの反応であっても共感評価が有意に低下した（t(571)=-6.13, p<.001）。ラベルではなく信念そのものが効くという、帰属効果の直接証拠。
- **効くのは感情的/動機的共感だけ**：この人間帰属プレミアムは共感の"種類"に依存する。認知的共感（状況理解・言語化）では差がほぼ消え、感情的・動機的共感（気にかける・支援する）でのみ実質的な差が残る——「なぜ勝つ場合と負ける場合があるのか」への直接的回答。

### メカニズム2：コスト・シグナル（cost signaling）—— 素朴な形は反証、しかし選択と評価が乖離するパラドックスを発見

**重要な新発見（当初の想定と逆）：** 「人間の方が感情的コストを払ってくれる」という素朴な前提は**反証された**。実際にはAIの反応の方が**「より多くの労力(effort)が注がれている」と一貫して知覚される**（4研究すべてで再現：Study1 b=-0.61, Study2 b=-0.78, Study3 b=-0.32, Study4 b=-0.23, いずれもp<.05）。

にもかかわらず——**選択と評価の乖離パラドックス**：4研究（N=152, 196, 195, 148/140）を通じて、参加者は人間からの共感を受け取ることを一貫して選好した（57.1%〜62.1%、すべてp<.001）にもかかわらず、実際に受け取った反応の質はAI生成の方が高く評価された（より高品質・より「聞いてもらえた」と感じる）。**評価軸（quality）と選択軸（preference）が乖離しており**、共感の人間性プレミアムは「認知」ではなく「選好・関係性への期待」に由来する可能性を示す。これは単純な「人間が勝つ/AIが勝つ」の枠組みそのものを超える発見。

なお、人間限定の文脈（AIとの比較なし）では、感情の言語化がコスト・シグナルとして信頼を媒介するという因果連鎖自体は6研究で一貫して支持される（Yu, Berg & Zlatev 2021）——ただしこれがAIに一般化するかは未検証で、類推の域を出ない。

### メカニズム3・4：身体性・責任 —— 共感文脈での直接証拠は薄い（追加調査は打ち切り、他テーマの知見を代用）

**共感を評価する場面に絞った人間対AIの直接検証は、この2つについては見つからなかった**（身体性で見つかったのはAI同士比較のみ・N=60、責任で見つかったのは助言追従の文脈で共感評価ではない）。これ以上、共感特化のdeep-researchを重ねても薄い証拠しか出ない可能性が高いと判断し、追加調査は打ち切る。

**代わりに、すでに検証済みの他テーマの一般理論を"類推による代用"として接続する**——**これは共感評価そのものを直接検証した証拠ではなく、隣接領域の確立した知見を借用した推論**であることを明記した上で：

- **身体性の代用**：Theme 1（身体性）で確認済みの一般知見——身体化認知は五感・疲労・違和感を伴う状況接地であり、テキストのみのLLMには構造的に欠けている（Kadambi et al., *Neuron* 2026／Ziemke 2016）。これを共感に当てはめれば、「相手が身体を持ち、実際に感じている」という接地が共感の"本物さ"の一部を支えている可能性は理論的に筋が通る。**ただしこれは一般理論の借用であり、共感評価における身体性の効果量を測った研究ではない。** → [01-embodiment.md](01-embodiment.md)
- **責任の代用**：Theme 5（責任）で確認済みの一般知見——道徳的責任は社会的地位であり機械に委譲すると消える（Radanliev 2026）、AIへの行為者性の帰属は人間側の責任知覚を弱める"moral crumple zone"として働く（Hohenstein & Jung 2020）。これを共感に当てはめれば、「相手が自分の言葉に対して責任を負う存在である」ことが共感の重みを支えている可能性は理論的に筋が通る。**ただしこれも一般理論の借用であり、共感を"受け取る"場面での責任効果を直接測った研究ではない。** → [05-responsibility.md](05-responsibility.md)

この2つは確信度lowのまま、**「共感特有の証拠」ではなく「隣接テーマの一般理論からの類推」として** human-territory.md に反映する。

## クロス分析への含意（なぜB軸が人間なのか、精密版）

素朴な「共感は人間だけ」ではなく、こう言える：

1. **現場ヒアリングは"書かれた共感"ではなく"実時間・身体を伴う信頼構築"** — そこにAIのデータは一件もない（全研究がテキスト・代理評価）。B軸が人間なのは「共感の文章が書けないから」ではなく、**本音の開示は"相手が本物の人間で、評価せず、責任を持つ"という帰属の上でしか起きないから**。
2. **むしろ反証（Lucas 2014ほか）を組み込むと強くなる** — 「恥ずかしい情報は機械相手の方が出やすい」なら、**初期の匿名アンケートはAI/ツール、本音を引き出す対面ヒアリングは人間**、と設計を分けられる。これは弱点ではなく分担の精密化。

## まだわからない・要検証（次にやること）

- ⚠️ **全て一次リンクを開いて数字を確認する**（下の台帳参照）。特にarXiv 2602.17293は査読前プレプリント、要注意。
- ~~「身体を伴う・実時間・実患者」文脈の共感研究を別途探す~~ **【2026-07-20 打ち切り・代用で決着】** 身体性・責任は共感文脈での直接比較研究が見つからず、追加のdeep-researchも打ち切った。Theme 1/Theme 5の一般理論を類推による代用として接続済み（上記メカニズム3・4節）。将来、共感評価に特化した直接研究が査読誌に出た場合のみ差し替える。
- Lucas 2014（開示）はTheme 4に送り、そこで深掘る。
- ~~メカニズム語彙の整理~~ **【2026-07-20 完了】** 真正性の帰属（強い）／コストのシグナル（素朴な形は反証・選択と評価の乖離パラドックスを発見）／身体性・責任（証拠薄い）に整理。
- 選択と評価の乖離パラドックス（人間を選ぶがAIを高く評価する）の心理的メカニズムは未解明——将来の関係性への期待、社会的望ましさなどの仮説が残る。

## 出典（要・人間検証）

| # | 主張の核 | 一次リンク | 状態 |
|---|---|---|---|
| A | 同一文章でも人間帰属の方が共感的（n=6,282, 差は感情/動機成分） | https://www.nature.com/articles/s41562-025-02247-w | ⚠️**［要旨｜③✓(本文精査残)｜人間確認:要機関アクセス］**（2026-07-19照合：著者・9研究・n=6,282・主結果を要旨で確認。感情/動機 vs 認知の対比は"emotional sharing and care が主因"まで確認、本文精査が残） |
| B | 医師 vs ChatGPT: 78.6%でAI選好・共感9.8倍（※4倍長い交絡） | https://pmc.ncbi.nlm.nih.gov/articles/PMC10148230/ | ⚠️**［全文｜③✓｜人間確認:無料全文］**（2026-07-19照合：Ayers et al., JAMA Internal Medicine 2023。195件/585評価/78.6% (CI 75.0-81.8)/45.1% vs 4.6%/211語 vs 52語/評価者が共著者である限界の明記、全て原文確認） |
| C | AIが人間より思いやりと評価（N=556, d=0.73, 危機専門家超え） | https://www.nature.com/articles/s44271-024-00182-6 | ⚠️**［全文(OA・全数値照合)｜③✓｜人間確認:無料全文］**（2026-07-19照合：Ovsyannikova, Oldemburgo de Mello & Inzlicht, Communications Psychology 3:4 (2025)。全数値一致確認） |
| D | メタ分析: AI共感優位 SMD 0.87（GPT-4のみ有意） | https://pmc.ncbi.nlm.nih.gov/articles/PMC12536877/ | ⚠️**［全文｜③✓｜人間確認:無料全文］**（2026-07-19照合：Howcroft et al., British Medical Bulletin 2025。15研究中13がメタ分析対象。SMD 0.87 (CI 0.54-1.20, P<.00001)/GPT-4 1.03有意・GPT-3.5 0.51非有意/全テキスト・代理評価・検証済み尺度1研究のみ・6研究が高バイアス、全て原文確認） |
| E | 臨床家盲検: AIが感情(OR=1.79)/動機的(OR=1.84)共感で専門家超え・専門家作と信じた方を93.55%が選好 | 無料全文: https://pmc.ncbi.nlm.nih.gov/articles/PMC12169703/ （Internet Interventions 2025, doi:10.1016/j.invent.2025.100841。ScienceDirect版と同一） | ⚠️**［全文｜③✓(訂正済)｜人間確認:無料全文］**（2026-07-19：PMC全文読了。OR/93.55%/識別45%＝偶然水準、全て本文確認。**ニュアンス修正**：盲検では実際の著者性も有意でAI作が選好(p=.002)——「実際は無関係で信念だけが駆動」は言い過ぎ。両効果が有意で、知覚された専門家帰属の効果が特に強い、が正確） |
| F | ChatGPTがLEAS(感情認識)で人間規範超え・但し「分かってもらえた感」とは別と著者が明言 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10254409/ （Elyoseph, Hadar-Shoval, Asraf & Lvovsky, "ChatGPT outperforms humans in emotional awareness evaluations", Front. Psychol. 2023, doi:10.3389/fpsyg.2023.1199058） | ⚠️**［全文｜③✓｜人間確認:無料全文］**（2026-07-19：PMC全文を読了。LEAS総合85→98/100で一般人口規範を有意超え・適合度9.7/10。著者が本文で「AIが相手の感情を"理解"できても患者が"分かってもらえた"と感じるかは別」と明言。主張と一致。**2026-07-25：リンク検証エージェントが著者名の誤り「Elkins」を検出→Web独立確認でElyosephに訂正**） |
| G | LLM恋愛相談が人間超え(認知/動機的共感)・**感情的共感は優位なし** ※プレプリント要注意 | https://arxiv.org/abs/2602.17293 （Festor, Snels & Kleinberg 2026, CC BY 4.0） | ⚠️**［要旨｜③✓｜人間確認:無料全文(プレプリント)］**（2026-07-19：arXiv原典で要旨確認。「総合品質・認知的共感・動機的共感で一貫して高評価／感情的共感に一貫した源泉優位なし」。後者は分類表の「感情的共感は人間側」をむしろ補強。**査読前プレプリント**である旨は引用時に必ず明記） |
| H | 選択と評価の乖離パラドックス：人間からの共感を選好(57.1〜62.1%)するが、AIの反応の方を高品質・労力大と評価する（コスト・シグナルの素朴な人間優位説は反証） | https://pubmed.ncbi.nlm.nih.gov/41620574/ （Wenger, Cameron & Inzlicht, "People choose to receive human empathy despite rating AI empathy higher", *Communications Psychology*, 2026, PMC12872445） | ⚠️**［全文｜③✓｜人間確認:無料全文］**（2026-07-20：deep-research内3票検証で3-0/2-1確認。原論文の学位論文版（ETDA, Penn State）はCloudflare Turnstileでアクセス不能だったため査読済み後継論文をPMC経由で採用。**2026-07-27：PMC全文を読了し③整合を確認**。doi:10.1038/s44271-025-00387-3。原文の数値：Study1で人間選好 **57.1%**, t(151)=5.37, p<.001／Study3で **62.1%**, t(194)=9.94, p<.001。**「乖離パラドックス」は著者自身の命名**——"We name this perplexing pattern of results in which people choose human empathy, but rate AI empathy as higher quality, the 'AI empathy choice paradox.'"。**コスト・シグナル素朴説の反証も原文が明言**："the assumption that human empathy is perceived as more effortful is not supported. We found that AI empathy was perceived as entailing more effort."。**ただし重要な補足4点**：①**労力そのものは効いている**——知覚労力は評価を予測し、その効果は人間側でより強い（交互作用 p<.001）＝「労力は無関係」ではなく「労力は効くが、人間の方が労力をかけていると見られていない」。②著者自身が「参加者はAIの労力を問う質問をカテゴリーエラーとして扱った可能性」と留保。③**選好は一枚岩でない**——25%（Study1/4）はAIを多く選んだ。④**本プロジェクトに直結する限界**：比較対象の人間は関係のない他人（学部生RA）。著者も "how does it compare to empathy from a human with whom the recipient has a relationship?" を未解決として挙げており、**伴走関係のある人間との比較ではない**） |
| I | 感情の言語化がコスト・シグナルとして信頼を媒介する（6研究・事前登録・査読済み）——ただし**人間限定の文脈で、AIへの一般化は未検証** | https://www.sciencedirect.com/science/article/abs/pii/S0749597821000194 （Yu, Berg & Zlatev, "Emotional acknowledgment: How verbalizing others' emotions fosters interpersonal trust", *Organizational Behavior and Human Decision Processes* **164:116-135**, 2021, **doi:10.1016/j.obhdp.2021.02.002**） | ⚠️**［要旨｜③✓｜人間確認:要機関アクセス］**（2026-07-20：deep-research内3票検証で確認（vote 3-0/2-1）。confidence=medium——AI比較なしのため類推止まり。**2026-07-27：Crossrefで書誌を確定しDOIを追加**（巻号頁は既存記載どおりで正しかった）。要旨原文で③整合を確認：Costly Signaling Theory に依拠し、6研究で「感情の言語化→コスト知覚の上昇→信頼の上昇」。効果は**肯定的感情より否定的感情で強い**（否定的感情を認める方がコストが高いと知覚されるため）。**無料版なし**（unpaywall `is_oa:false`）。**Hとの関係を必ず併記すること**：本行は「コストが信頼を生む」機構を人間同士で示すが、H（Wenger）は「AIの方が労力をかけていると知覚される」を示す。**この2行を並べると"人間はコストを払うから信頼される"という素朴な人間優位の推論は成立しない**） |
| J | 身体性の直接検証は乏しい：物理ロボット対音声チャットボット（AI同士比較・人間ベースラインなし、N=60）で、身体性も共感的口調も**第三者への援助意図**に有意差なし | https://arxiv.org/abs/2503.20518 （**Darwesh, Singh, Marian, Alexa, Hindriks & Baraka, "Exploring the Effect of Robotic Embodiment and Empathetic Tone of LLMs on Empathy Elicitation", Proc. Int. Conf. on Social Robotics (ICSR 2024), Springer**＝査読済み会議録。arXiv版＝無料全文） | ⚠️**［要旨(原文照合)｜③△(測定対象を訂正)｜人間確認:無料全文］**（2026-07-20：deep-research内3票検証で結果が割れていた（一部3-0、「身体性が知覚共感に無効」は0-3）。**2026-07-27：要旨原文で割れの理由が判明——測定対象の取り違え**。本研究の従属変数は**エージェントへの知覚共感ではなく、「架空の人物(Katie Banks)を助けるボランティア時間の申し出」＝第三者への共感の"喚起"**。原文＝"neither robotic embodiment nor empathetic tone significantly influenced participants' willingness to volunteer"。よって**「知覚共感に差なし」とは書けない**（未測定）→主張文を「第三者への援助意図」に限定して訂正。なお著者は "the LLM effectively simulated human empathy" とも述べており、**AIの共感表現が下手だったから差が出なかったのではない**点は押さえておく。書誌も追加（旧記載はarXiv htmlリンクのみで著者・掲載先が空欄だった）） |
| K | **【引用の向きを訂正 2026-07-27】** AIの助言に従った利己的決定者は、人間の助言に従った場合より**責任が重いと見なされる**（＝AIは非難を吸収しない）。ただし実際の懲罰量に助言源の差はなし——共感を"受け取る"場面の責任効果ではなく類推止まり | https://arxiv.org/abs/2507.19487 （**Leib, Köbis & Soraperra, "Does AI and human advice mitigate punishment for selfish behavior? An experiment on AI ethics from a psychological perspective", *Computers in Human Behavior*, 2025-10, doi:10.1016/j.chb.2025.108709**。arXiv版＝無料全文） | ⚠️**［要旨(原文照合)｜③✗→訂正済(向きが逆だった)｜人間確認:無料全文］**（2026-07-20：deep-research内3票検証で「確認」vote 3-0。**2026-07-27：arXivの要旨原文と照合したところ向きが逆だったことが判明し訂正**。原文＝"whereas selfish decision-makers were seen as **more** responsible when they followed **AI** compared to human advice, punishment between the two advice sources did not vary. Overall, behavior and advice content shape punishment, whereas the advice source does not."。旧記述「AIの助言に従うと責任帰属が下がる」は**主節が逆**だった（括弧内の「人間の助言者の方が肩代わり」だけが正しく、主節と矛盾していた）。**⚠️deep-researchの3票検証は、向きが逆の主張を"確認"として通していた**。**含意も反転する**：本研究は「AIを盾にすれば非難を逃れられる」説の**反証側**＝Theme5のW3(Maasland)・W4(moral crumple zone)と突き合わせるべき証拠。事前登録・金銭インセンティブ付き実験。CHB掲載をCrossrefで確定） |

*A〜Gは2026-07-19のdeep-research（敵対的検証は当時レート制限で未実行、その後個別にAI確認）。H〜Kは2026-07-20の再deep-research（110エージェント・3票敵対的検証込み）で追加。各リンクを人間が開いて確認し、確認できたものを ⚠️→✅ に上げること。*
