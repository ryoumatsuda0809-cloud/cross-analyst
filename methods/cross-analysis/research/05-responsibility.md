# Theme 5: Responsibility — who answers for the call? / 責任 — 誰がその判断を背負うのか

**Status:** ⚠️ AI-verified, awaiting human verification of primary sources. Gathered 2026-07-19; claim-support audited 2026-07-25/27 — all five rows support their claims, with two already weakened to match their sources (C's "people delegate the unpleasant decisions" and D's earlier misattribution). **Weigh the blame-shield reading of C/E against incoming counter-evidence from Theme 3 K (Leib et al. 2025): following AI advice made a selfish decision-maker look _more_ responsible, not less.**
**Verification note:** Per-row state is tagged `［depth｜claim-support｜human-check］` — see the [legend](README.md#状態ラベルの読み方2026-07-27-導入). Nothing here is ✅ yet: open the primary link before publishing. Rule: [the-fabricated-citation.md](../the-fabricated-citation.md).

---

## なぜ責任を調べるのか

3原則の第1は「決めるのは人間」。だがその根拠を「AIの判断は人間より劣るから」に置くと、モデルが賢くなるたびに土台が削れる。**AIの判断が人間と同等かそれ以上になっても崩れない理由**があるのか——それがこのテーマの問いだった。

**結論：ある。責任は「能力」ではなく「社会的な地位」であり、原理的に委譲できない。**

## 何がわかったか

### 責任の委譲は構造的に不可能（人間側の土台）

- **権限は移せるが、責任は移せない**：AIに意思決定の実行は委任できても、結果に対して**answerable（答えを負う）存在**は必ず残り、それは常に人間。
- **AIは道徳的行為者の要件を欠く**：道徳的自覚・省察・理解・動機・熟慮・判断——責任ある道徳的行為者性の基準を、現在の自律機械は満たさない。
- **責任のギャップ（accountability gap）**：AIが判断を駆動すると「機械の挙動を予見できなかったこと」に全責任を負える人間がいなくなる。責任が移るのではなく、**消える**。これが組織のガバナンス上の核心問題。
- **感情的な責任のメカニズムも作れない**：AIは失望できないし、約束を破って苦しむこともない。そして相手はそれを知っている——「この人は自分の判断に痛みを賭けている」という信頼の基盤が成立しない。

### ⚠️ 人間側の不都合な事実：人はAIを「責任の盾」に使う

- **解雇をアルゴリズムに委譲する傾向はあるが、弱く条件付き**（2026-07-19修正）：Maasland & Weißmüller 2022（N=288）では解雇と昇進の委譲率の差はわずか4.4ポイントで、アルゴリズムを事前テストできるかどうか（−15.1pt）の方がはるかに効いた。結論は「**アルゴリズム嫌悪が非難回避に勝る**」。つまり「AIを責任の盾にする」誘惑は実在するが、実験証拠は当初の記述より弱い——誇張しないこと。
- 機械のエラーは人間のエラーより**不釣り合いに負に知覚される**（機械は完璧という期待＋負の情報の顕著性。原典はDietvorst et al. 2015）。
- **擬似的な共感・意図の演出が、責任の誤帰属を招く**：AIが人間らしく振る舞うほど、人はAIに道徳的行為者性を誤って帰属し、**本来責任を負うべき人間（設計者・導入者）への監視が弱まる**。責任ギャップが放置される力学はこれ。

## 分類（このテーマの判定表）

| 要素 | 判定 | 根拠 | なぜ |
|---|---|---|---|
| 判断の結果に answerable であること | **人間のみ**（原理的） | 責任ギャップ研究 | 責任は能力でなく社会的地位。委譲すると消える |
| 道徳的自覚・省察・動機を伴う判断 | **人間のみ**（現時点で明確） | 道徳的行為者性研究 | 要件を満たす機械が存在しない |
| 「自分の判断に痛みを賭けている」という信頼の基盤 | **人間のみ** | 感情的責任の議論 | AIは失望も後悔もできず、相手もそれを知っている |
| 判断の実行・下準備・選択肢の生成 | **AIに委任可** | 委任研究 | 権限の委任と責任の委譲は別物 |
| （危険）責任逃れの盾としてのAI利用 | **人間の悪癖**（実験証拠は弱く条件付き） | 非難回避実験（Maasland & Weißmüller 2022） | 「AIが決めたので」— 分類ではなく警告として記録。誇張しない |

**分類の結論（暫定）：** 「決めるのは人間」の根拠は、AIの判断力の劣位**ではない**。①責任は委譲した瞬間に消える（誰も answerable でない判断は組織的に無価値）、②「痛みを賭けた判断」だけが信頼を生む、③AIを盾にする誘惑は実在し、それは判断の質ではなく**組織の誠実さ**を壊す。——モデルがどれだけ賢くなっても、この3つは変わらない。

## クロス分析への含意

1. **HITL原則の根拠が強化された** — 「AIに決めさせない」のは性能の問題ではなく構造の問題。診断で顧客に説明するとき「AIの精度が上がったら人間は不要では？」への答えがこれ：**答えを負える者だけが決められる**。
2. **「AIが決めたので」を診断の警告項目にできる** — 顧客組織がAI導入で責任の所在を曖昧にしていないか（解雇・評価・与信をAIの判断のせいにしていないか）は、それ自体が組織課題の兆候。B軸ヒアリングで拾うべきシグナル。
3. **Nacit自身の運用にも跳ね返る** — 診断レポートの結論は Nacit（人間）が署名して負う。「AIの分析によれば」を結論の主語にしない。

## まだわからない・要検証

- ⚠️【AI確認済 2026-07-19】責任ギャップ2本（A: Radanliev／B: Find the Gap）確認済み。Bは修正派である点を台帳に注記。人間確認待ち。
- ⚠️【AI確認済 2026-07-19】非難回避実験は全文確認→**主効果は弱く条件付き・嫌悪が支配**と判明、本文と台帳を修正済み。人間確認待ち。
- 「痛みを賭ける」系の議論は理論・エッセイ寄り——実証研究があるか追加調査。
- 法的責任（PL法・AI規制）の観点は今回未調査。実務では重要なので統合時に別枠で。

## 出典（要・人間検証）

| # | 主張の核 | 一次リンク | 状態 |
|---|---|---|---|
| A | 委任された行為者性と道徳的責任：権限は移せるが責任は移せない | https://doi.org/10.3389/frai.2026.1800302 | ⚠️**［全文｜③✓｜人間確認:無料全文］**（2026-07-19照合／2026-07-25全文再確認：Radanliev, "Delegated agency and moral responsibility in artificial intelligence", Frontiers in AI 9 (2026), Oxford/Alan Turing Institute。「道徳的責任は委任が進んでも irreducibly human」「責任は委任し設計した者に帰属し、実行の道具には帰属しない」を原文確認。補足：責任ギャップは機械の存在論でなく**制度の分断**から生じる、という精緻化あり。**この論文が支えるのは human-territory H1 のみ。H2（感情的コスト論）は支えない**） |
| B | 責任ギャップの精緻化：「認識・制御の欠如」説は的外れ（人間も同じ課題を持つ）。本当の問題は「多くの手」による行為者性の拡散で、**answerableな役割を占める人間がいなくなる**（脆弱性ギャップ） | https://pmc.ncbi.nlm.nih.gov/articles/PMC11153269/ （Vallor & Vierkant, "Find the Gap: AI, Responsible Agency and Vulnerability", Minds and Machines 2024, doi:10.1007/s11023-024-09674-0） | ⚠️**［全文｜③✓(精緻化版)｜人間確認:無料全文］**（2026-07-19：PMC全文で「red herring」「many hands／answerable」の該当箇所を確認。**注意：単純な「責任が消える」の裏付けではなく修正派**——だが「組織内でanswerableな者が不在になる」という我々の核心はむしろこの精緻化版が支える） |
| C | 非難回避：解雇をアルゴリズムに委譲する傾向は**あるが弱く条件付き**（差4.4pt・事前テスト機会に強く依存）。**アルゴリズム嫌悪が非難回避に勝る** | https://pmc.ncbi.nlm.nih.gov/articles/PMC9177159/ （Maasland & Weißmüller, "Blame the Machine?", Frontiers in Psychology 13, 2022, N=288, 2×2実験） | ⚠️**［全文｜③✓(過大主張を訂正済)｜人間確認:無料全文］**（2026-07-19：全文確認。**当初の「嫌な決定ほど委譲したがる」は言い過ぎ**——主効果は弱く、"Respondents' aversion to algorithms dominates blame avoidance by delegation" が結論。修正済み） |
| D | 機械のエラーは人間のエラーより不釣り合いに負に知覚される（機械=完璧という期待＋負の情報の顕著性） | 原典＝Dietvorst, Simmons & Massey 2015 (J. Exp. Psychol.: General 144:114-126, doi:10.1037/xge0000033)。**無料全文＝Wharton PDF: https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf** ／要約する裏付け→ https://pmc.ncbi.nlm.nih.gov/articles/PMC9177159/ | ⚠️**［全文｜③✓｜人間確認:無料全文］**（2026-07-19／**2026-07-25 ③整合を全文で再確認**：Dietvorst 2015＝「同じ誤りでも機械の方が早く信頼を失う」を確認（Wharton無料PDF特定）。Maasland本文も「アルゴリズムの誤りは非対称に大きい負の反応」「機械＝完璧の前提と矛盾」「負の情報が顕著」と明言＝機構まで一致。**注：READMEで一度"出典なし"と誤って削除しかけたが、有効な出典ありと訂正**） |
| E | AIへの行為者性の帰属が、人間側の責任知覚を弱める（AIが"moral crumple zone"として非難を吸収・転嫁） | https://www.sciencedirect.com/science/article/am/pii/S0747563219304029 （著者受理版=無料）／原典 Hohenstein & Jung, "AI as a moral crumple zone", Computers in Human Behavior 106:106190, 2020（オンライン2019）, doi:10.1016/j.chb.2019.106190 | ⚠️**［要旨｜③✓(やや一般化と自認)｜人間確認:SD著者版・機械403］**（2026-07-20：**弱い出典から差替**——当初の "When AI Agents Act" はIJRSI（略奪的とされる低質誌）掲載で使用中止。査読済みCHBの実験研究に置換。要旨で「AIが強制的エージェントと知覚され moral crumple zone として機能し、人間コミュニケーター間の責任を軽減」を確認。※原文は擬似"共感"ではなくAI媒介コミュニケーション文脈——「擬似共感が」の限定は本文で要確認、主張はやや一般化して記載） |

*【2026-07-20 更新】Eの旧出典（IJRSI掲載 "When AI Agents Act"）は低質誌のため使用中止し、査読済みCHBのHohenstein & Jung 2020（moral crumple zone）へ差替。A〜EすべてAI検証一巡（A/B/C/D=全文・要旨確認、E=要旨確認）。人間確認待ち。*
