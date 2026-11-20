# Research Log: What Only Humans Can Do / 調査記録：人間にしかできないこと

An ongoing, evidence-first research project mapping — in fine detail — what humans can do and feel that AI cannot, and honestly, where AI outperforms humans. This log feeds the classification that underpins the B-axis of [Cross-Analysis](../README.md).

**This is a living document.** Entries move from 🔍 to ✅ only after a human has checked the primary source.

**日本語の運用ルールは[下半分](#運用ルール日本語)にあります。**

---

## Rules

1. **Real papers only.** Every claim needs a primary source (the paper itself, not a blog about it). AI assistants fabricate citations — [we caught one ourselves](../the-fabricated-citation.md). **Where to look first: the [Source Registry](SOURCES.md)** — check Tier 1 (free full text) before searching; never cite Tier 3 (blogs).
2. **Counterevidence is mandatory.** For every "humans are better at X" claim, we actively search for studies showing the opposite. A classification built only on flattering evidence is fiction.
3. **Verification states:** 🔍 found, unverified → ⚠️ AI-verified (depth noted per entry: bibliographic / abstract / full text read) → ✅ human-verified against primary source. **AI verification never yields ✅, no matter how deep** — ✅ is reserved for a human opening the primary link and confirming. (Rule tightened 2026-07-19.)
4. **Precision over slogans.** "People only open up to humans" is false as stated; the truth is finer (see ledger: disclosure vs. felt empathy). We record the precise version.

## Themes

| # | Theme | Note file | Status |
|---|---|---|---|
| 1 | Embodied presence（身体でその場にいる） | `01-embodiment.md` | **✅ All 7 rows human-verified 2026-07-27 — first theme fully checked.** The checks changed the theme: **Kadambi (B) turns out to be agnostic about whether AI can acquire internal embodiment**, so the "in principle" framing now rests on Ziemke (D) — which itself turned out to be open access, not paywalled. E1's free source was also found not to cite the original it stood in for |
| 2 | Tacit knowledge（暗黙知） | `02-tacit-knowledge.md` | **✅ All 6 rows human-verified 2026-09-04 (A/B 2026-07-31) — second theme fully checked.** B was demoted 2026-07-27, so "AI can surface tacit knowledge" rests on Brynjolfsson alone; E's own genre turned out to be misrecorded (a teaching slide deck, not a working paper), which reinforces rather than changes its supplementary-only status |
| 3 | Empathy & feeling felt（共感・気持ちの受け皿） | `03-empathy.md` | ⚠️ AI-verified + **mechanism deep-research 2026-07-20** (110 agents, 25 claims adversarially verified: authenticity attribution confirmed strong; naive cost-signaling refuted; new choice-evaluation paradox found); awaiting human check |
| 4 | Trust & disclosure（信頼と自己開示 — 反証が濃い領域） | `04-trust-disclosure.md` | ⚠️ AI-verified + **human-side rebuilt 2026-07-20** ("deeper disclosure = human" retired); awaiting human check |
| 5 | Responsibility & judgment（責任・判断の引き受け） | `05-responsibility.md` | ⚠️ AI-verified (E swapped to Hohenstein & Jung 2020); awaiting human check |

Themes will be split further as research gets granular (e.g., #3 may split into cognitive/affective/motivational empathy).

## Human spot-check queue / 人間確認キュー

AIが確認済みの項目。**りょうまさんがリンクを開いて「確認すること」欄が本当に書いてあるか見たら、`☐`→`✅` にして、該当テーマ台帳のエントリも ✅ に上げる。** 上から順に潰せる。★＝主張の柱（優先）。
（最終更新 **2026-07-27**：③整合監査 第二〜四パスを反映＝①Kadambi/Jordan/Wenger/Wieland等を全文確認 ②Jordan・Wielandの無料全文を新規発見 ③Lucasの「無料全文」を撤回（死リンク）・Pickardを判定不能で補助へ降格 ④**03-Kは引用の向きが逆だったので訂正** ⑤**02-Bは全文確認で格下げ**（94.9%の指標定義・LLM模擬の被験者）⑥全39行に `［深度｜③｜人間確認］` ラベルを付与）

**リンク健全性チェック（最新＝2026-07-27・全面再実行）：** 台帳7ファイル内の**全57リンク**（重複除去後）にブラウザ相当のUAで実アクセスし、ステータスを実測。結果＝**到達可能 40（200/202）／機械アクセス拒否 17（403）／死リンク 0**。<br>※当初「59リンク」と記載していたが誤り（**URL抽出時に末尾のMarkdown強調記号 `**` を含めてしまい、同じURLを2本ぶん二重計上していた**。素のURLでは両方200＝Wharton版Dietvorst・TU Delft版Kelly）。2026-07-27に抽出を修正して再実測し、57本に訂正。
- **2026-07-25版の「取得できなかった6本は出版社ブロック」という判断は推測混じりで、うち1本（CMU/Lucas 2014）は実際には死リンクだった**（2026-07-26に発覚・該当リンクは撤去済み）。今回はその反省から**全リンクを実測**した。
- **403は「読めない」であって「存在しない」ではないが、「ブラウザなら読める」の証明でもない。** 17本の内訳＝ScienceDirect×6・T&F・OUP・ACM・MDPI・RSNA・SSRN・doi.org×2・DOAJ・Consensus・TU Delftの**PDF直リンク**。このうち**無料の代替経路が確保できているのは**：Jordan（→pure.hud.ac.uk・実測200）／Bond & DePaulo（→PMC8333997）／Merwin（→DOAJ **API** は通る。HTMLページのみ403）／Kelly（→TU Delftの**ランディングページ**は200。PDF直リンクは403）／Dratsch・Gerlich・Lee（既に✅人間確認済み）。
- **代替のないペイウォール＝Pickard・Yu・Croes(OUP)・Hohenstein(SD著者版)**。人間確認はここが機関アクセス頼みになる。**Ziemkeは2026-07-27に撤回**——SDの403はボット検知で、論文自体はCC BY-NC-NDのオープンアクセス（提供PDFで確認・✅化済み）。
- ※このチェックは「開ける・実在する」の事実確認のみ。**主張の裏付け（③）判断は含まない。** 過去の検証で著者名の誤り1件（Elkins→Elyoseph）も検出・訂正済み。

### 状態ラベルの読み方（2026-07-27 導入）

各テーマ台帳の「状態」欄は、**3つの軸**を `⚠️［深度｜③｜人間確認］` の形で表す。以前は「⚠️AI確認済み」等が7種類バラバラに使われ、注記には「全文読了」とあるのにラベルは「確認済み」だけ、といった不一致があったため統一した。

| 軸 | 取りうる値 |
|---|---|
| **深度**（AIがどこまで読んだか） | `書誌のみ` ／ `要旨` ／ `本文一部` ／ `全文` ／ `代替OA全文`（原典はペイウォールで、それを引用・確認しているOA文献を全文で読んだ） |
| **③**（主張を支えるか） | `✓` 整合 ／ `△` 限定つき（ジャンルが弱い・一部のみ・測定が主張より狭い） ／ `✗→訂正済` 不整合だったので直した ／ `判定不能` アクセスできず確認しようがない |
| **人間確認** | `無料全文` ／ `無料要旨のみ` ／ `無料代替あり` ／ `要機関アクセス` ／ `不能` |

**全39行の内訳（2026-09-04時点・02-C/D/E/Fの✅化を反映して手動再集計。行の状態を変えたら必ず数え直すこと）**

| 深度（AIがどこまで読んだか） | 行数 |
|---|---|
| 全文 | 13 |
| 要旨 | 12 |
| ✅ 人間確認済み | 13 |
| 代替OA全文（原典はペイウォール） | 0 |
| 書誌のみ | 1 |

| ③整合の判定 | 行数 | | 人間確認の道 | 行数 |
|---|---|---|---|---|
| ✓ 整合 | 22 | | 無料全文が読める | 19 |
| ✅ 人間確認済み | 13 | | ✅済み | 13 |
| △ 限定つき | 1 | | 無料だが機械403／要旨のみ | 4 |
| ✗→訂正済 | 2 | | 無料代替あり | 0 |
| 判定不能 | 1 | | 要機関アクセス | 2 |
| | | | 不能 | 1 |

**この表から読めること**：③としては22行が整合（△1・✗→訂正済2・判定不能1、別途✅13）。**人間確認の障害になるのは実質6行だけ**（要機関アクセス2＋機械403等4）で、**19行は無料全文が開くので、上から順に潰せば✅化は進む**。逆に `判定不能`(04-B Pickard) は、何をしても✅にできない行として切り分けておく。**✅化 進捗：13/39 — テーマ1・テーマ2が完了（全13行）**。**次はテーマ3〜5（未着手・0/26）**。

**読み替えの注意：`③✓` は「AIが原文と照合して主張を支えると判断した」までで、✅ではない。** ✅は人間が一次リンクを開いて確認したときだけ付く（このルールは変えない）。

### A. 無料で読める（優先度順・★＝柱）
| ✓ | リンク（無料全文） | 確認すること | 上げる先 |
|---|---|---|---|
| ✅ | https://rdcu.be/fwqBh （Twyman & O'Donnell, Springer SharedIt・確認済み2026-07-27） | ジャンル＝Curmudgeon Corner（オピニオン欄）。単独の根拠にはしない | Theme1 A（**✅済み**） |
| ✅ | 01-C（Nature Machine Intelligence社説・無料版なし・確認済み2026-07-27） | ジャンル＝Editorial。両主張とも社説自身ではなくBrooks 1991／Brunton & Tuthill 2025からの引用。単独の根拠にはしない | Theme1 C（**✅済み**） |
| ✅ | https://www.sciencedirect.com/science/article/pii/S030326471630168X （Ziemke 2016, *Biosystems*・**CC BY-NC-ND オープンアクセス**・確認済み2026-07-27） | 種別＝Review article（複数の理論的枠組みを統合）。旧「SDペイウォール」判定は誤りだった | Theme1 D（**✅済み**） |
| ✅ | ★ https://doi.org/10.1016/j.neuron.2026.03.004 （Kadambi et al.・掲載版NeuronはCC BYで無料／arXiv版 https://arxiv.org/abs/2510.13845 ・確認済み2026-07-27） | 種別＝**Perspective**（Reviewではない）。①内的身体＝固有感覚・内受容感覚・温度感覚・調節状態／外的身体＝外界との相互作用 ②"MLLMs lack any bodily experience" ③力点は「AI研究は外的身体に偏り、内的身体が手つかず」 ④**最重要：本論は "remains agnostic about whether artificial systems similarly require such internal, subjective experiences" と明記し、機能的等価物の実装を提案している＝「AIには原理的に無理」の根拠にはならない**（その役割はD=Ziemke） | Theme1 B（**✅済み**）・human-territory H3 |
| ✅ | ★ https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ （Levine 2021・**E1/E2とも確認済み2026-07-27**） | ①視線回避等は「診断的価値を欠く」（E1・原文一致）②「chanceをわずかに上回る・真実バイアス」（E2・Bond & DePaulo 2006を引用）。**注意：この論文はDePaulo 2003を引用していない**（参考文献14件に無し）＝**E1は「独立した同趣旨の記述」／E2は「引用による確認」**と性質が違う。種別はFrontiers **Opinion**。おまけ：実験室外では "Accuracy is near zero, not 54%" | Theme1 E1・E2（**✅済み**）・human-territory H8 |
| ☐ | ★ https://doi.org/10.3389/frai.2026.1800302 | 「権限は委任できるが道徳的責任は委任できない＝irreducibly human」「多くの手→answerableな役割の欠如」 | Theme5 A・human-territory H1 |
| ☐ | ★ https://pmc.ncbi.nlm.nih.gov/articles/PMC12872445/ （Wenger 2026） | 人間選好 57.1%(Study1)/62.1%(Study3)・**"AI empathy choice paradox" は著者の命名**・"the assumption that human empathy is perceived as more effortful is not supported"。**あわせて確認**：①労力自体は効いている（人間側で効果が強い）②25%はAIを選好 ③**比較対象の人間は関係のない他人（学部生RA）＝伴走関係との比較ではない**（著者が未解決と明記） | Theme3 H・human-territory H6 |
| ☐ | ★ https://www.nature.com/articles/s44271-024-00182-6 （Communications Psychology, OA） | AIが人間より思いやりと評価(d=0.73)・危機専門家超え・開示後も優位残存 | Theme3 C |
| ✅ | https://pure.hud.ac.uk/ws/files/17720891/accepted_manuscript.pdf （Jordan et al. 2019 METT・著者版31頁・**確認済み2026-07-27**） | 全体精度 M=.46（偶然50%を有意に下回る, p=.05）・群間差なし F(2,87)=0.22, p=.80・ベイズ因子≈21:1で「差なし」・**それでも微表情の識別自体は訓練で 37.9%→72.4% に向上**＝訓練が効いた群で示している点が強い | Theme1 F（**✅済み**）・human-territory H8（否定側） |
| ☐ | https://research.tudelft.nl/en/publications/tapping-into-key-drivers-self-disclosure-in-sensitive-health-conv/ （Kelly 2025・T&F版はペイウォール） | 機微度が高いほど開示意向が下がる（N=216） | Theme4 E |
| ☐ | https://arxiv.org/abs/1905.10700 （Xiao 2020・TOCHI版の無料preprint） | チャットボットの会話型調査がWeb調査よりGricean指標で有意に高品質 | Theme4 H |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC10148230/ （Ayers 2023） | 78.6%でAI選好・共感9.8倍・※AIが4倍長い交絡・評価者が共著者 | Theme3 B |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC12536877/ （Howcroft 2025メタ分析） | AI共感優位SMD 0.87・GPT-4のみ有意・全テキスト代理評価 | Theme3 D |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC12169703/ | OR=1.79/1.84・93.55%・識別45%（＝偶然水準） | Theme3 E |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC10254409/ | LEAS 85→98/100・「患者が"分かってもらえた"と感じるかは別」 | Theme3 F |
| ☐ | https://arxiv.org/abs/2602.17293 | 「認知・動機的共感で高評価／感情的共感は優位なし」（※プレプリント） | Theme3 G |
| ✅ | https://journals.openedition.org/philosophiascientiae/892 （確認済み2026-09-04・全文PDF） | 3分類の定義（関係的／身体的／集合的）を逐語照合。**あわせて発見**：論文自体の主眼はRTK（関係的）の名称・定義への批判で、「contingent」への改名を提案している | Theme2 C（**✅済み**） |
| ✅ | https://pmc.ncbi.nlm.nih.gov/articles/PMC12927663/ （確認済み2026-09-04・出版社PDF原本） | 「暗黙知の伝達には信頼と師弟の密な相互作用が不可欠」（※Editorial）4引用すべて逐語照合、訂正なし。**あわせて確認**：この論説は反AIではなく「AI/シミュレーションは有用な補助、ただし現行モデルは指導者を置き換えられない」が結論 | Theme2 D（**✅済み**） |
| ✅ | https://rakaposhi.eas.asu.edu/Polanyis-Revenge-CACM-Print.pdf （確認済み2026-09-04・著者公開PDF） | 「解釈可能性等の問題は暗黙知学習への一極集中に遡れる」 | Theme2 F（**✅済み**） |
| ✅ | https://arxiv.org/abs/2507.03811 （確認済み2026-07-31） | **格下げの根拠3点はすべて原文一致**：①94.9%＝「最終報告に**全カラム名**への言及があった実行の割合」（864回中820回）で知識の回収率ではない ②中身の再現度は **METEOR 0.17**（Coherence 2.65／Faithfulness 4.37、いずれも1〜5点のG-Eval）③「従業員」は**LLMで模擬**・配られる知識は**既存テーブル説明の断片**＝暗黙知の抽出をテストできていない ④著者全員 Kunumi 所属・同社助成。掲載＝IJCNN 2025（IEEE） | Theme2 B（**✅済み**） |
| ☐ | https://academic.oup.com/iwc/article/36/5/279/7692197 | 「判断されない」認知・評価恐怖↓・**ただし開示量は増えず** | Theme4 D |
| ☐ | https://link.springer.com/article/10.1007/s11133-025-09619-8 | ラポール前提への**批判**であること（＝当初の引用が逆向きだった確認） | Theme4 F |
| ☐ | https://arxiv.org/abs/2504.13908 （Barari・※査読前プレプリント） | AIの追い問いで開示が詳細・情報豊富に（UXはわずか低下、N=1,800）。**あわせて**：自動コーディングは "moderate"・追従バイアスで偽陽性増 | Theme4 I |
| ☐ | **NEW** https://hdl.handle.net/10125/111964 （Wieland et al. HICSS 2026・CC BY-NC-ND／2026-07-27に特定） | 語数 41.88→75.02→**106.02**（F(2,148)=13.45, p<.001, η²=.15）・主題数も文脈的プロービングが最多。**測っているのは語数と主題数＝量的指標で、開示の深さではない**点 | Theme4 J |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC9177159/ （Maasland "Blame the Machine?"） | 委譲差4.4pt・事前テスト−15.1pt・「嫌悪が非難回避に勝る」（※「機械エラーが厳しく裁かれる」はこの論文の知見**ではない**——誤帰属として除去済み） | Theme5 C |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC11153269/ | 「認識・制御条件はred herring」「many hands→answerableな役割の不在」 | Theme5 B |

### B. 無料版なし（機関アクセス／要旨止まり／著者連絡が必要）
これらはClaudeが無料版を探したが見つからなかった。優先度は本文の重みで判断を。
| ✓ | 出典 | 状況 | 上げる先 |
|---|---|---|---|
| ☐ | Rubin et al. 2025, *Nature Human Behaviour* (s41562-025-02247-w) | **柱だが**Nature本誌ペイウォール。要旨＋HBS要約で方向は確認済み、数値の本文確認が残る | Theme3 A・human-territory H6 |
| ☐ | Pickard, Roster & Chen 2016, *CHB* 65:23-30 | SDペイウォール・無料版なし。**2026-07-26に3系統で再確認（unpaywall `is_oa:false`／OpenAlex `any_repository_has_fulltext:false`／Semantic Scholarは出版社が要旨自体を非公開）＝要旨さえ読めず③判定不能。単独の根拠にせず補助扱い**（同じ機構はTheme4 Dが全文で支える） | Theme4 B |
| ☐ | **Lucas et al. 2014, *CHB* 37:94-100**（旧「CMUに無料全文あり」を撤回） | **2026-07-26：CMU記事ページ・CMUのPDF直リンク・USC ICTのPDFすべて404、unpaywall `is_oa:false`＝無料全文は現存しない。** 要旨は無料で読め、4項目（開示恐怖↓・印象管理↓・悲しみ表出↑・観察者評価の開示意欲↑）すべて原文で確認済み。人間確認も要旨止まりで可 | Theme4 A・human-territory A3 |

## Verified-citation ledger / 検証済み台帳

> **Note (synced 2026-07-20):** This is a *curated summary*. The per-theme files [`01`–`05`](.) carry the authoritative, most-recent status and full bibliographic detail — where they differ, **the detailed file wins**. Statuses below were reconciled against the detailed files on 2026-07-20; each ⚠️ notes which theme-file row (e.g. `04-B`) it mirrors.

| Claim（主張） | Source | Primary link | Status |
|---|---|---|---|
| **[HITL principle 2, 2026-07-31]** AI helps inside its capability frontier and *hurts* outside it, and the boundary is invisible — 758 BCG consultants: **+12.2% tasks / −25.1% time / >40% quality** inside the frontier (weakest performers +43%), but **19 percentage points less likely to be correct** on a task outside it | Dell'Acqua, McFowland III, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon & Lakhani, *Organization Science* (2026); orig. HBS WP 24-013 | https://doi.org/10.1287/orsc.2025.21838 （無料プレプリント: https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf ） | ✅ full text read 2026-07-31. Numbers verbatim. **Do not over-read:** the paper does **not** show that consultants who doubted or fact-checked AI performed better — "skeptical" appears 0 times and "verify" only once (unrelated). Its two success patterns, **Centaur** (dividing/delegating work between self and AI) and **Cyborg** (fully integrating and continually interacting), are patterns of *task division*, not of distrust. Supports a **structural** verification step because the frontier is invisible, not because skepticism was measured. **Now peer-reviewed** (Organization Science), no longer only a working paper |
| **[Method premise, 2026-07-31]** Combining two different kinds of evidence "produces more than the sum of its parts" and can yield conclusions neither method alone would reach — **the closest empirical precedent for the A×B collision, and it is quantitative×qualitative, NOT AI×human** | Moffatt, White, Mackintosh & Howel, *BMC Health Services Research* 6:28 (2006) | https://doi.org/10.1186/1472-6963-6-28 （OA・PMC1434735・PMID 16524479） | ✅ full text read 2026-07-31. Supports the collision premise; **but explicitly cuts against "the gap reveals the true cause"** — the authors advocate treating the datasets as complementary "rather than in competition for identifying the true version of events", say cross-validation "is not a viable option", and found their own conflict was an artifact: the standardised instruments never measured the dimension the interviews surfaced. Cited in [../README.md](../README.md) with those limits stated |
| Identical empathic messages are rated more empathic/authentic when attributed to a human; gap driven by *affective/motivational* empathy, not cognitive (9 studies, n>6,000) | Rubin et al., *Nature Human Behaviour* 2025 | https://www.nature.com/articles/s41562-025-02247-w | ⚠️ |
| People disclose *more* stigmatizing info when they believe the interviewer is a computer (lower fear of judgment) — **counterevidence** | Lucas, Gratch, King & Morency, *Computers in Human Behavior* 37 (2014) | https://www.sciencedirect.com/science/article/abs/pii/S0747563214002647 | ⚠️ AI-checked 2026-07-19 via Semantic Scholar (849 citations): lower fear of self-disclosure / lower impression management / more intense sadness display all confirmed in abstract |
| **[Trust/disclosure theme, 2026-07-19]** Highly sensitive topics disclosed more to avatars than humans (verify the ethnicity/cheating/income specifics) | Pickard, Roster & Chen, *Computers in Human Behavior* 65:23-30 (2016) | https://www.sciencedirect.com/science/article/abs/pii/S0747563216305684 | ⚠️ bib confirmed via Crossref (04-B); direction from secondary, abstract/full text not yet read — human check pending |
| People disclose personal info to AI and humans *equivalently* | *Computers in Human Behavior: Artificial Humans* 2025 | https://www.sciencedirect.com/science/article/pii/S2949882125000647 | ⚠️ title = the claim itself, confirmed (04-C); OA but machine-blocked — human check pending |
| Chatbots seen as non-judgmental "safe space" for embarrassing disclosure — **but lower fear did NOT increase intimate disclosure** | Croes, Antheunis, van der Lee & de Wit, *Interacting with Computers* 36(5) (2024) | https://academic.oup.com/iwc/article/36/5/279/7692197 | ⚠️ full text confirmed (04-D) — human check pending |
| ~~Rapport is prerequisite for honest depth~~ **RETRACTED / INVERTED 2026-07-20**: Rao 2026 actually *critiques* the rapport-as-prerequisite premise ("rapport can be harmful; disclosure is driven by the decision to participate"). Do **not** cite as a human advantage | Rao, *Qualitative Sociology* 49:47-70 (2026, OA) | https://link.springer.com/article/10.1007/s11133-025-09619-8 | ⚠️ inverted-citation caught (AI-checked) |
| **[Theme-4 rebuild 2026-07-20]** "Humans elicit *deeper* disclosure" is **NOT supported** — peer-reviewed evidence leans AI-favorable on informativeness (Xiao 2020 *TOCHI*; Barari 2025; Wieland 2026 *HICSS*). The nearest peer-reviewed finding is an AI *limitation*, not a human advantage: current LLM interviewers miss idiosyncratic specifics ("richness") — but its comparison arm is a scripted bot, **not** a human interviewer, so it does not show humans elicit more. Replaces the retracted industry secondary (insightplatforms) | Cuevas, Scurrell, Brown, Entenmann & Daepp, *Proc. ACM HCI* 9(2), CSCW049, 2025, doi:10.1145/3710947 — free: arXiv 2309.10187 (2023 preprint) | https://arxiv.org/abs/2309.10187 | ⚠️ AI-checked (abstract + arXiv); bib locked 2026-07-25 (PACM HCI vol 9, 2025) — awaiting human check |
| **[Tacit knowledge theme, 2026-07-19, human-verified 2026-09-04]** Collins' 3 types: relational (codifiable) / somatic (bodily) / collective (in practices) — key to resolving the Brynjolfsson conflict | Collins, *Tacit and Explicit Knowledge* (2010); free OA backing: Soler & Zwart, "Collins's Taxonomy of Tacit Knowledge", *Philosophia Scientiæ* 17-3 (2013), DOI 10.4000/philosophiascientiae.892 | https://journals.openedition.org/philosophiascientiae/892 | ✅ human-verified 2026-09-04 (full PDF). All 3 definitions confirmed verbatim (02-C). **Also found:** the paper's own thesis is a critique of the "relational" label itself — it argues only 2 of Collins's 5 RTK sub-cases are genuinely relational and proposes renaming RTK to "contingent tacit knowledge"; this ledger uses only the 3-way definitional split, not the renaming argument |
| **[Demoted 2026-07-27, confirmed 2026-07-31]** 94.9% is a per-run binary check that every column *name* got mentioned (820/864 runs) — not a recall rate, not real employees, not real organizational knowledge. Content fidelity is METEOR 0.17 / G-Eval Coherence 2.65 / Faithfulness 4.37 | Zuin, Mastelini, Loures & Veloso, *IJCNN 2025* (IEEE), doi:10.1109/IJCNN64981.2025.11227259 | https://arxiv.org/abs/2507.03811 | ✅ human-verified 2026-07-31 (full PDF, incl. tables). No longer cited as evidence that AI can extract tacit knowledge (02-B) |
| Tacit-knowledge transfer in medicine requires close mentor-learner interaction | Papadimos, Hsu & Pappada, "Insights From Michael Polanyi", *Cureus* 18(1):e102205 (2026), doi:10.7759/cureus.102205 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12927663/ | ✅ human-verified 2026-09-04 (publisher PDF). All 4 quotes re-confirmed verbatim, no corrections. Genre = Editorial; conclusion is "adjunct, not replacement" — not anti-AI (02-D) |
| Embodiment shapes cognition/meaning; text-only LLMs lack sensorimotor grounding — **Theme-1's strongest anchor** | Kadambi, Aziz-Zadeh, Damasio, Iacoboni & Narayanan, "Embodiment in multimodal LLMs", *Neuron* 114(11):1908-1921 (2026), peer-reviewed Review | https://doi.org/10.1016/j.neuron.2026.03.004 | ⚠️ AI abstract-confirmed (01-B) — human check pending |
| **[Embodiment theme, 2026-07-19]** LLMs lack a body; embodied knowledge is a key human-AI distinction | Twyman & O'Donnell, *AI & SOCIETY* 41:5963-5965 (2026) | https://link.springer.com/article/10.1007/s00146-026-03000-1 | ⚠️ identified (01-A); **genre = opinion/commentary column — weak** — human check pending |
| Body is part of cognition's structure, not peripheral (embodied intelligence) | *Nature Machine Intelligence* 8:491-492 (2026) | https://www.nature.com/articles/s42256-026-01239-3 | ⚠️ visible-text confirmed (01-C); **genre = Editorial**; paywalled — human check pending |
| Nonverbal cues to deception are weak/unreliable — **limits our own Theme-4 claim** | DePaulo et al. *Psychological Bulletin* 129(1) (2003) — **paywalled, still unread**; same claim stated independently in Levine 2021, *Frontiers in Psychology* (open access) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ | ✅ human-verified 2026-07-27. Levine 2021 states the listed cues "lack diagnostic value" verbatim; existence independently confirmed via Crossref + PubMed (PMID 34366964). **Correction 2026-07-27: Levine 2021 does NOT cite DePaulo 2003** (not among its 14 references) — it is an independent statement of the same claim, not a citation trail to the original. Genre: Frontiers Opinion. **Correction: the 54% figure belongs to Bond & DePaulo 2006, below** |
| Human lie-truth judgment accuracy ≈54%, only slightly above chance | Bond & DePaulo, *PSPR* 10(3) (2006) — **paywalled, still unread**; free confirmation: Levine 2021, *Frontiers in Psychology* (open access) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ | ⚠️ AI full-text check 2026-07-19/27: Levine 2021 **does cite Bond & DePaulo 2006** — "people are slightly above chance accuracy overall, truth-biased"; "cue-based truth-lie discrimination is slightly better than chance (about d = +0.4)". **Note for our own use:** Levine argues real-world accuracy is worse still — with research confederates, "Accuracy is near zero, not 54%" — so 54% is a lab-assisted ceiling, which strengthens rather than weakens our claim. Same PDF as E1, so this can be ✅ on request |
| **[Responsibility theme, 2026-07-19]** Agency can be delegated to AI; moral responsibility cannot — "irreducibly human"; gaps arise from institutional fragmentation | Radanliev, *Frontiers in AI* 9 (2026) | https://doi.org/10.3389/frai.2026.1800302 | ⚠️ AI-checked 2026-07-19: thesis and key passages confirmed against full text |
| People *may* delegate unpleasant decisions to algorithms for blame avoidance — but the effect is **weak & conditional**; algorithm aversion often dominates | Maasland & Weißmüller, "Blame the Machine?", *Frontiers in Psychology* 13 (2022), N=288 (DOI 10.3389/fpsyg.2022.779028 = PMC9177159, same paper) | https://pmc.ncbi.nlm.nih.gov/articles/PMC9177159/ | ⚠️ full text confirmed (05-C); the original "people prefer to delegate unpleasant decisions" was overstated — corrected — human check pending |
| Machine/algorithm errors judged more harshly than identical human errors (perfection expectation + negativity salience) | **origin** Dietvorst, Simmons & Massey 2015, *J. Exp. Psychol. General* 144:114-126 (free: Wharton PDF); **also summarized in** Maasland & Weißmüller 2022 | https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf | ⚠️ **CORRECTION 2026-07-25**: an earlier note here wrongly called this "no valid source." Verified: Dietvorst 2015 shows people lose confidence in algorithms faster than humans after the *same* error; Maasland's text explicitly states algorithm fallibility "triggers an asymmetrically larger negative response." Valid = 05-D — human check pending |
| Wrong AI suggestions collapse expert accuracy 82.3%→45.5% (automation bias, 27 radiologists) | Dratsch et al., *Radiology* 2023 | https://pubs.rsna.org/doi/full/10.1148/radiol.222176 | ✅ |
| AI assistance lifts productivity +14% (+34% for novices); mechanism is diffusing top performers' tacit knowledge | Brynjolfsson, Li & Raymond, *QJE* 2025 | https://www.nber.org/papers/w31161 | ✅ |
| Heavy AI use correlates negatively with critical thinking (n=666, cognitive offloading mediates) | Gerlich, *Societies* 2025 | https://www.mdpi.com/2075-4698/15/1/6 | ✅ |
| Higher trust in AI → less critical-thinking effort (319 knowledge workers, 936 examples) | Lee et al., *CHI* 2025 | https://dl.acm.org/doi/full/10.1145/3706598.3713778 | ✅ |
| Third-party evaluators rated AI responses *more* compassionate than expert humans — **counterevidence** | Ovsyannikova, Oldemburgo de Mello & Inzlicht, *Communications Psychology* 3:4 (2025) | https://www.nature.com/articles/s44271-024-00182-6 | ⚠️ AI-checked 2026-07-19: 4 preregistered studies N=556, Study1 d=0.73 (AI M=4.08 vs human M=3.50), beats crisis experts (S3: 4.08 vs 3.47; S4: 3.91 vs 3.41), persists when disclosed (blind B=0.83 / transparent B=0.38) — all confirmed |
| **[Empathy theme, 2026-07-19]** Identical messages rated more empathic when human-attributed; gap in affective/motivational, not cognitive (n=6,282) | Rubin, Li, Zimmerman, Ong, Goldenberg & Perry, *Nature Human Behaviour* 2025 | https://www.nature.com/articles/s41562-025-02247-w | ⚠️ AI-checked 2026-07-19: title/authors/9 studies/n=6,282/main finding all confirmed against abstract. Affective-vs-cognitive contrast "primarily driven by emotional sharing and care" — full-text check remains |
| Blinded evaluators preferred ChatGPT over physicians 78.6%; "empathetic" 9.8× — **counterevidence** (confound: AI 4× longer, raters were coauthors) | Ayers et al., *JAMA Internal Medicine* 2023 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10148230/ | ⚠️ AI-checked 2026-07-19: all figures confirmed against full text incl. coauthor-evaluator limitation |
| ‼️ **DUPLICATE** of the Ovsyannikova row above (same DOI `s44271-024-00182-6`) — merge on human pass | *Communications Psychology* 3:4 (2025) | https://www.nature.com/articles/s44271-024-00182-6 | ⚠️ see the ⚠️ Ovsyannikova row above (AI-checked) |
| Meta-analysis (15 studies, 13 pooled): AI empathy > human clinicians SMD 0.87 (GPT-4 sig, GPT-3.5 not); all text/proxy — **counterevidence** | Howcroft et al., *British Medical Bulletin* 2025 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12536877/ | ⚠️ AI-checked 2026-07-19: all figures and limitations confirmed against full text |
| Clinician blind eval: AI matched/exceeded experts on affective (OR 1.79)/motivational (OR 1.84) empathy; raters identified authorship at chance (45%) and preferred what they *believed* was expert-authored (93.55%) — **but actual AI authorship was also preferred (p=.002)**, so not belief-only | Internet Interventions 2025, doi:10.1016/j.invent.2025.100841 (= the ScienceDirect `S2214782925000429` paper) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12169703/ | ⚠️ PMC full text read (03-E); "belief alone drives it" was overstated — corrected — human check pending |
| ChatGPT scored above human norms on LEAS emotional awareness (85→98/100); authors caution this ≠ "feeling felt" | Elyoseph, Hadar-Shoval, Asraf & Lvovsky, *Frontiers in Psychology* 2023, doi:10.3389/fpsyg.2023.1199058 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10254409/ | ⚠️ PMC full text read (03-F); author name corrected Elkins→Elyoseph 2026-07-25 (link-checker catch) — human check pending |
| LLM relationship advice rated higher than human on cognitive/motivational empathy — **but no consistent advantage on *emotional* empathy** (supports the human-side classification) | Festor, Snels & Kleinberg, arXiv 2602.17293 (2026), CC BY 4.0 | https://arxiv.org/abs/2602.17293 | ⚠️ arXiv abstract confirmed (03-G); **unrefereed preprint — always flag when citing** — human check pending |
| **[Empathy mechanism rebuild, 2026-07-20]** Choice-evaluation paradox: people consistently prefer receiving empathy from a *human* (57–62% across 4 studies) even though AI's response is rated higher-quality and perceived as *more* effortful — cost-signaling alone doesn't explain the human preference; naive "humans pay more emotional cost" is refuted | Wenger, Cameron & Inzlicht, *Communications Psychology* (2026), PMC12872445 | https://pubmed.ncbi.nlm.nih.gov/41620574/ | ⚠️ AI-checked via deep-research adversarial verification (03-H), 110-agent run — human check pending |

✅ entries were verified during the Knacit philosophy-page project (June 2026) — see `DIAGNOSIS-ROADMAP.md` §8 (private) and [the-fabricated-citation.md](../the-fabricated-citation.md).

---

## 運用ルール（日本語）

**目的**：「人間にしかできない・感じられないこと」を、感覚論ではなく検証済みの研究で、細かく分類する。AIの方が優れている点も同じ厳密さで記録する（それが分類の信頼性を作る）。

**調査に使う道具（この環境に接続済み）**：
- **deep-research** — 検索を並列展開し、主張を敵対的に検証（反証探索）して出典つきレポートに合成する
- **Consensus** — 査読済み論文だけを対象にしたAI学術検索（実在しない論文が混ざらない）
- **PubMed** — 医学・心理学の一次情報データベース
- **WebSearch / WebFetch** — 論文本体ページを開いて数字を直接確認する用
- **Google Drive** — 過去に自分で調べた資料の参照元

**1テーマの回し方**：
1. deep-research か Consensus で広く当てる（賛成・反対の両方を集める）
2. 候補の主張を台帳に 🔍 で追加
3. 一次情報リンクを開き、著者・年・数字・数字の意味を確認 → ⚠️ / ✅ に昇格
4. テーマノート（`0X-*.md`）に「わかったこと／まだわからないこと／反証」を書く
5. commit & push（調査の過程自体が公開資産になる）

**最終アウトプット**：全テーマ完了後、`../human-territory.md`（人間の領域の分類完成版）に統合する。
