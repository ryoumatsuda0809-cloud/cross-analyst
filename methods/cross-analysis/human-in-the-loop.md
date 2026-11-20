# Three Principles for Keeping Humans in the Loop / 人間を輪の中に残す3原則

The operating rules behind [Cross-Analysis](README.md). Each principle exists because of specific, peer-reviewed evidence — all citations below were verified against primary sources by a human. (That rule itself has a story: [the-fabricated-citation.md](the-fabricated-citation.md).)

**日本語版は[下半分](#日本語版)にあります。**

---

## 1. HITL — Humans decide

**Let AI suggest. Never let it decide.**

AI is a tool that spreads your best people's know-how across a whole team. In a study of 5,179 call-center workers, AI assistance lifted productivity by **14%** overall — and by **34%** for less-experienced workers. The gains came from AI diffusing the tacit knowledge of top performers, not from AI replacing anyone's judgment.

So we use that power — but AI's job ends at *suggesting*. The *decision* is made by a human.

> Brynjolfsson, E., Li, D., & Raymond, L. (2025). "Generative AI at Work." *Quarterly Journal of Economics*, 140(2). [NBER WP 31161](https://www.nber.org/papers/w31161) / [QJE](https://academic.oup.com/qje/article/140/2/889/7990658)
> Note: the 14% figure is *productivity*, not accuracy. We cite it as evidence that AI amplifies human judgment — not that HITL always improves accuracy.

## 2. Verification step — Always question the answer

**Never take AI output at face value. Build a human verification step physically into the process.**

Even seasoned experts get dragged down by wrong AI suggestions. In an experiment with 27 radiologists, when the AI suggested an incorrect classification, accuracy collapsed: inexperienced readers fell from 79.7% to **19.8%**, moderately experienced from 81.3% to **24.8%**, and even the most experienced from 82.3% to **45.5%**.

This is *automation bias* — humans over-trust automated systems, and expertise does not immunize you. The countermeasure is structural, not motivational: put a mandatory verification step between AI output and action.

> Dratsch, T., et al. (2023). "Automation Bias in Mammography: The Impact of Artificial Intelligence BI-RADS Suggestions on Reader Performance." *Radiology*, 307(4). [Primary source](https://pubs.rsna.org/doi/full/10.1148/radiol.222176)

**And the reason a verification step has to be structural: you cannot tell in advance when AI will help you or hurt you.** A preregistered field experiment with **758 Boston Consulting Group consultants** found that AI cuts both ways within the same job. On 18 realistic consulting tasks *inside* the frontier of what GPT-4 does well, consultants with AI completed **12.2% more tasks, 25.1% faster, at more than 40% higher quality** — and the weakest performers gained most (**+43%**, versus +17% for the strongest). But on one complex managerial task deliberately chosen to sit *outside* that frontier, consultants using AI were **19 percentage points less likely to reach the correct answer** than consultants working without it.

The authors call this boundary a **"jagged technological frontier"** — jagged because two tasks of seemingly similar difficulty can fall on opposite sides of it, and because the boundary is invisible from the inside. That is precisely why the countermeasure cannot be "be careful with hard tasks": you do not know which task was the hard one. It has to be a step in the process.

> Dell'Acqua, F., McFowland III, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F. & Lakhani, K. (2026). "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality." *Organization Science*. [doi:10.1287/orsc.2025.21838](https://doi.org/10.1287/orsc.2025.21838) — originally HBS Working Paper 24-013; free preprint: [SSRN 4573321](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf)

*Do not over-read this study.* It does **not** show that consultants who doubted or fact-checked the AI did better — the words "skeptical" and "verify" appear nowhere in that sense in the paper. The two successful patterns it identifies, **Centaurs** ("dividing and delegating their solution-creation activities to the AI or to themselves") and **Cyborgs** ("completely integrating their task flow with the AI and continually interacting with the technology"), are patterns of *dividing work*, not of *distrust*. What the study establishes is the jagged frontier and the 19-point drop beyond it. That is enough.

## 3. Room to think — Don't outsource your judgment

**Keep deliberate human thinking time built into the process.**

Reliance on AI correlates with weaker critical thinking. A study of 666 participants found a significant **negative correlation** between heavy AI-tool use and critical-thinking scores, mediated by cognitive offloading — and the effect was strongest in younger users. A separate study of 319 knowledge workers (936 real examples) found that the more people trusted AI, the less critical-thinking effort they invested, widening the room for over-dependence.

Convenience quietly hollows out judgment. So we preserve time where humans think without the machine — as a designed part of the process, not as nostalgia.

> Gerlich, M. (2025). "AI Tools in Society: Impacts on Cognitive Offloading and the Future of Critical Thinking." *Societies*, 15(1), 6. [Primary source](https://www.mdpi.com/2075-4698/15/1/6)
> Lee, H-P., et al. (2025). "The Impact of Generative AI on Critical Thinking." *CHI 2025* (Carnegie Mellon × Microsoft Research). [Primary source](https://dl.acm.org/doi/full/10.1145/3706598.3713778)

## The sequence matters

The three principles are ordered deliberately:

1. **Use AI** (humans decide) → 2. **but doubt it** (even experts get fooled) → 3. **and keep thinking** (long-term dependence erodes the skill you need for #1 and #2).

Affirm the tool, distrust the output, protect the thinker.

---

---

# 日本語版

[クロス分析](README.md) の背後にある運用原則。各原則は、査読済み研究という具体的な根拠の上に立っています。以下の引用はすべて**人間が一次情報で検証済み**です（そのルール自体の由来は [the-fabricated-citation.md](the-fabricated-citation.md) に）。

## 1. HITL ―「決めるのは、人間。」

**AIに提案はさせる。決定はさせない。**

AIは、優秀な人の知恵を組織全体へ広げる道具です。コールセンター5,179人の研究では、AI支援で生産性が全体で **+14%**、経験の浅い人では **+34%** 向上しました。効果の源泉は「トップ層の暗黙知をAIが波及させたこと」であり、AIが誰かの判断を置き換えたことではありません。

この力は使う。ただしAIの仕事は「提案」まで。「決定」は人間が下す。

> Brynjolfsson, Li & Raymond (2025) "Generative AI at Work" QJE 140(2)
> 注：+14%は「精度」ではなく「生産性」。HITLが常に精度を上げるという主張には使わない。

## 2. 検証ステップ ―「AIの答えに、ひと手間。」

**AIの出力を、そのまま信じない。人間の検証ステップを、プロセスに物理的に挟む。**

熟練の専門家ですら、AIの誤った提案に引きずられます。放射線科医27人の実験では、AIが誤った分類を提示すると正答率が激減：新人 79.7%→**19.8%**、中堅 81.3%→**24.8%**、熟練でも 82.3%→**45.5%**。

これが「自動化バイアス」——人は自動システムを過信し、専門性はその免疫になりません。対策は根性論ではなく構造です：AIの出力と行動の間に、必須の検証ステップを置く。

> Dratsch et al. (2023) "Automation Bias in Mammography" Radiology 307(4)

**そして、検証ステップが「構造」でなければならない理由がここにある——AIがいつ助けになり、いつ害になるかは事前に分からない。** **ボストン・コンサルティング・グループのコンサルタント758人**を対象とした事前登録済みのフィールド実験は、同じ職務の中でAIが両方向に働くことを示した。GPT-4が得意とする範囲の**内側**にある18の実務課題では、AI利用群は**課題処理量 +12.2%、所要時間 -25.1%、品質は40%超の向上**。しかも**成績下位層ほど伸びが大きい**（**+43%**、上位層は+17%）。ところが、その範囲の**外側**になるよう意図的に選ばれた1つの複雑な経営課題では、AI利用群は**正答に到達する確率が19パーセントポイント低かった**。

著者はこの境界を **"jagged technological frontier"（ギザギザの技術的フロンティア）** と呼ぶ。ギザギザなのは、**見た目の難易度が同じ2つの課題が境界の反対側に落ちうる**からであり、**内側からは境界が見えない**からだ。だから対策は「難しい課題では気をつける」ではありえない——**どれが難しい課題だったのかが分からない**のだから。工程の中の一手順にするしかない。

> Dell'Acqua, F., McFowland III, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F. & Lakhani, K. (2026). "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality." *Organization Science*. [doi:10.1287/orsc.2025.21838](https://doi.org/10.1287/orsc.2025.21838) — 初出はHBS Working Paper 24-013。無料のプレプリント：[SSRN 4573321](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf)

**この研究を読み過ぎないこと。** 本論は「**AIを疑い自分で検証したコンサルタントの成績が良かった**」ことを**示していない**（論文中に skeptical / verify はその意味では現れない）。示された2つの成功パターン——**Centaur**（"dividing and delegating their solution-creation activities to the AI or to themselves"＝仕事をAIと自分に分けて割り振る）と **Cyborg**（"completely integrating their task flow with the AI and continually interacting with the technology"＝工程をAIと融合させ絶えず対話する）——は、**仕事の分け方**の型であって、**不信の型ではない**。この研究が確立したのは「ギザギザのフロンティア」と「その外側での19ポイントの低下」である。それで十分に強い。

## 3. 思考の余白 ―「考える力を、明け渡さない。」

**人間が自力で考える時間を、仕組みとして残す。**

AI依存は思考力の低下と相関します。666人の研究では、AIツールの多用と批判的思考力の間に有意な**負の相関**（認知的オフロードが媒介、若年層ほど顕著）。知識労働者319人・実例936件の別研究では、AIへの信頼が高いほど批判的思考の労力が減り、過依存の余地が広がることが示されました。

便利さの裏で、判断力そのものが空洞化する。だから、機械なしで人間が考える時間を「設計として」残す。

> Gerlich (2025) Societies 15(1) ／ Lee et al. (2025) CHI 2025

## 並び順に意味がある

**① 使う**（決めるのは人間）→ **② でも疑う**（専門家すら騙される）→ **③ それでも考え続ける**（依存は①②に必要な力そのものを蝕む）。

道具を肯定し、出力を疑い、考える人を守る。
