# Cross-Analysis / クロス分析

A diagnostic method that deliberately confronts two different kinds of evidence — **objective research & market data (A)** and **raw, first-hand field information (B)** — to surface the gap between the ideal and the reality, and to form a testable hypothesis about the root cause hiding beneath it.

Developed and used in practice by [Knacit](https://knacit.com), a hands-on business support company in Japan.

**日本語版は[下半分](#クロス分析日本語版)にあります。**

---

## The premise: AI should multiply perspectives, not replace judgment

Most AI adoption today runs in one direction: feed the problem to the model, take the answer. It's fast, and it's exactly how organizations end up with plausible-sounding conclusions nobody actually verified.

Cross-Analysis inverts this. The human's own viewpoint comes first; AI is used to *confront* that viewpoint with evidence — never to outsource the conclusion. AI is not an oracle. It is a tool for multiplying perspectives.

This isn't philosophy for its own sake. The evidence for keeping humans in the loop is concrete — see [human-in-the-loop.md](human-in-the-loop.md) for the verified research, and [the-fabricated-citation.md](the-fabricated-citation.md) for the time this method caught an AI-fabricated academic citation in our own work.

## The framework: A × B

| Source | What it is | What it alone misses |
|---|---|---|
| **A — Outside facts** | Research papers, market data, industry statistics | What is actually happening on the ground |
| **B — Field reality** | Interviews, direct observation, exceptions, unwritten rules | Whether the situation is normal, common, or an outlier |

Neither source is sufficient by itself:

- **A alone** produces generic consulting: "industry data says digitize." It fits every company, so it helps none.
- **B alone** produces anecdotes: vivid, but with no way to tell whether what you're seeing is a local quirk or a structural pattern.

The method is the **collision**: put a specific A next to a specific B and ask *why they don't line up*.

> Example: Industry data says digitization solves order-processing errors (A). But in this workshop, the real bottleneck is that only two veterans can read the smudged handwritten faxes and know what "urgent" actually means for each customer (B). The gap between A and B points at a candidate for the real problem: the judgment lives in two people's heads. No tool fixes that by itself — and now you know *why* every previous tool purchase failed.

## How to run it

1. **Collect A** — gather 1–3 pieces of objective, external evidence relevant to the problem. Research, statistics, benchmark data.
   **Verify every citation against primary sources before using it.** AI assistants fabricate plausible references; ours did. See [the-fabricated-citation.md](the-fabricated-citation.md).
2. **Collect B** — gather first-hand information: what people actually say, do, and work around. Keep original wording. The unwritten judgment calls ("what does *urgent* really mean here?") are the most valuable items.
3. **Confront** — place A and B side by side. Where do they contradict? Where does the general prescription (A) fail to explain the local reality (B)?
4. **Check the gap before you trust it** — a contradiction between A and B is not automatically a finding. First ask: are the two even measuring the same thing? Do they cover the same population, the same period, the same construct? In the closest published precedent (Moffatt et al. 2006, below), the quantitative and qualitative arms of the *same* study reached opposite conclusions — and the reason turned out to be that the standardised instruments simply never measured the dimension the interviews surfaced. A gap can be an artifact of A's instruments rather than a signal about the organization.
5. **Name the gap** — write one paragraph: what does this contradiction reveal that neither source shows alone?
6. **Form a hypothesis, not a verdict** — state the suspected root cause as a strong hypothesis to be tested *with* the people involved, not as a diagnosis delivered *to* them.

## Who does what — the division of labor

The two axes are not symmetric. This is the part most AI-driven analysis gets wrong.

| Step | Who | Why |
|---|---|---|
| Collect A (research, data) | **AI-assisted**, human verifies every source | Searching and summarizing is what AI is good at. Verification is non-negotiable. |
| Collect B (field voices, feelings) | **Human only** | People share what they really think only with someone they trust, in the room. AI cannot sit there, notice hesitation, or hear what was *not* said. |
| Classify B (which voice matters) | **Human only** | Deciding that "the two veterans can read smudged faxes" is a load-bearing fact — and that another comment is noise — takes context no transcript carries. |
| Confront A × B | Human decides, AI may suggest patterns | AI can propose "these two points seem to contradict." Only a human can judge what the contradiction *means* for this organization. |

In short: **A is where AI helps most; B is human territory end to end.** An analysis that lets AI collect and sort the field reality has already removed the human viewpoint the method depends on — whatever it produces, it is not Cross-Analysis.

Why these rules exist — with numbers — is in [human-in-the-loop.md](human-in-the-loop.md).

## What the evidence does and does not cover

Being straight about this matters more than making the method sound proven.

**What is evidenced.** That AI and humans reach *different* information is supported by peer-reviewed work — people disclose stigmatising facts more readily to a machine ([Lucas et al. 2014](https://doi.org/10.1016/j.chb.2014.04.043)), and identical words are felt as more empathic when attributed to a human ([Rubin et al. 2025](https://www.nature.com/articles/s41562-025-02247-w)). The full classification behind the A/B split, counterevidence included, is in [human-territory.md](human-territory.md).

**What is not evidenced.** *That putting A and B together yields the true root cause.* We know of no study testing that. The closest published precedent is not about AI and humans at all — it is mixed-methods research:

> **Moffatt, S., White, M., Mackintosh, J. & Howel, D. (2006).** "Using quantitative and qualitative data in health services research – what happens when mixed method findings conflict?" *BMC Health Services Research* 6:28. [doi:10.1186/1472-6963-6-28](https://doi.org/10.1186/1472-6963-6-28) — open access, PMC1434735.

In that study the quantitative arm (RCT, n=126) found no effect of welfare-rights advice while the qualitative arm (n=25) found wide-ranging benefit. The authors report that combining the two "produces more than the sum of its parts" and "led us to conclusions different from those that would have been drawn through relying on one or other method alone" — which is the closest empirical support the collision premise has.

**But read their caution, because it cuts against the naive version of this method.** They "advocate treating qualitative and quantitative datasets as complementary **rather than in competition for identifying the true version of events**", and state that combining methods for cross-validation "is not a viable option because it rests on the premise that both methods are examining the same research problem". In their case the conflict turned out to be an artifact: the standardised instruments never measured the dimension the interviews surfaced.

Two things follow. First, this is a **quantitative × qualitative** result, not an **AI × human** result — the analogy is ours, and it is an analogy. Second, it explains *why* gaps appear in a way that is more useful than "B reveals hidden truth": often **A's instruments are not measuring the local construct at all**. The industry data measures digitization; nobody measured whether anyone can read the faxes.

So the honest status of Cross-Analysis: a practice-derived method, with evidence for its parts, an analogy for its core, and a step-4 check to keep the analogy from becoming an excuse.

## What this method is not

- Not anti-AI. We use AI heavily — as a perspective multiplier, under human verification.
- Not a template for automating analysis. If you remove the human confrontation step, it stops being Cross-Analysis.
- Not finished. This document will evolve as our field practice does.

## Related

- [human-territory.md](human-territory.md) — the evidence-based classification of what only humans can do (and where AI wins) that underpins the A/B division of labor
- [human-in-the-loop.md](human-in-the-loop.md) — the three principles (humans decide / verify AI output / preserve room to think) and the peer-reviewed evidence behind each
- [the-fabricated-citation.md](the-fabricated-citation.md) — a first-person account of catching an AI-fabricated citation, and the checklist that came out of it
- [research/](research/) — the running research log and verified-citation ledger behind the classification

---

---

# クロス分析（日本語版）

性質の異なる2つの情報源——**〈A: 客観的な研究・市場データ〉**と**〈B: 現場の生々しい一次情報〉**——を意図的に突き合わせ、どちらか単独では見えない「理想と現実のギャップ」を浮かび上がらせ、**その奥にある真因の仮説**を立てる診断手法。

日本で伴走型の企業支援を行う [Knacit](https://knacit.com) が、実務の中で開発・使用している。

## 前提：AIは「答えを出す存在」ではなく「視点を増やす道具」

いまのAI活用の大半は一方通行です。問題を投げ、答えを受け取る。速い。そしてまさにそのやり方で、組織は「もっともらしいが誰も検証していない結論」を積み上げていきます。

クロス分析はこれを逆転させます。起点は人間自身の視点。AIはその視点に証拠を**突き合わせる**ために使い、結論を委ねるためには使わない。

これは思想のための思想ではありません。人間を輪の中に残すべき根拠は具体的な数字で存在します（[human-in-the-loop.md](human-in-the-loop.md)）。そして、この手法自体が私たち自身の仕事の中でAIの捏造引用を発見した実話が [the-fabricated-citation.md](the-fabricated-citation.md) にあります。

## フレームワーク：A × B

| 情報源 | 中身 | 単独では見えないもの |
|---|---|---|
| **A — 外の事実** | 研究論文・市場データ・業界統計 | 現場で実際に起きていること |
| **B — 現場の現実** | ヒアリング・観察・例外処理・暗黙のルール | 目の前の状況が普通なのか特殊なのか |

- **Aだけ**だと一般論のコンサルになります。「業界データによればデジタル化を」——どの会社にも当てはまる話は、どの会社も救いません。
- **Bだけ**だと逸話になります。生々しいが、それが構造的なパターンなのか局所的な癖なのか判別できません。

手法の核心は**衝突**です。具体的なAと具体的なBを並べ、「なぜ噛み合わないのか」を問う。

> 例：業界データは「受発注ミスはデジタル化で解決する」と言う（A）。しかしこの工場では、崩れた手書きFAXを読め、顧客ごとの「至急」の本当の意味を知っているのはベテラン2名だけ（B）。AとBのギャップが真の問題の**候補**を指す——判断が2人の頭の中にある。ツール単体では直らない。そして、過去のツール導入がなぜ失敗し続けたかも、これで説明がつく。

## 実行手順

1. **Aを集める** — 問題に関係する客観的な外部証拠を1〜3点。研究・統計・ベンチマーク。
   **使う前に、すべての出典を一次情報で検証する。** AIはもっともらしい参考文献を捏造します。私たちのAIも捏造しました（[the-fabricated-citation.md](the-fabricated-citation.md)）。
2. **Bを集める** — 一次情報。人々が実際に言っていること・やっていること・回避策。原文のまま残す。暗黙の判断（「ここでの『至急』の本当の意味は？」）が最も価値が高い。
3. **突き合わせる** — AとBを並べる。どこが矛盾するか。一般解（A）が現場の現実（B）を説明できないのはどこか。
4. **ギャップを信じる前に検算する** — AとBの矛盾は、それだけでは発見ではない。まず問う：**両者はそもそも同じものを測っているか**。対象・期間・構成概念は揃っているか。最も近い先行研究（下記 Moffatt et al. 2006）では、**同一研究の量的アームと質的アームが正反対の結論**に達したが、原因は「標準化された尺度が、インタビューに現れた次元をそもそも測っていなかった」ことだった。**ギャップは組織の実態ではなく、Aの計器の側の人工物かもしれない。**
5. **ギャップに名前をつける** — この矛盾は、単独の情報源では見えない何を明らかにしているか。1段落で書く。
6. **判決ではなく仮説を立てる** — 疑われる真因を「当事者と一緒に確かめる強い仮説」として置く。「診断結果の宣告」にしない。

## 誰が何をやるか ── 人間とAIの分担

2つの軸は対称ではありません。AI主導の分析が間違えるのは、たいていここです。

| 工程 | 担当 | 理由 |
|---|---|---|
| Aを集める（研究・データ） | **AI補助**＋人間が全出典を検証 | 検索と要約はAIの得意領域。検証は絶対に省かない。 |
| Bを集める（現場の声・気持ち） | **人間だけ** | 人は、信頼した相手にしか本音を話さない。AIは現場に座れないし、ためらいに気づけないし、「言われなかったこと」を聞けない。 |
| Bを分類する（どの声が重要か） | **人間だけ** | 「ベテラン2人は崩れたFAXを読める」が構造を支える事実で、別の発言はノイズだ——この仕分けには、文字起こしには残らない文脈が要る。 |
| A×Bを突き合わせる | 人間が判断（AIはパターン示唆まで） | 「この2点は矛盾していそうだ」まではAIが出せる。その矛盾がこの組織にとって**何を意味するか**を判断できるのは人間だけ。 |

要するに：**AはAIが最も役立つ場所、Bは端から端まで人間の領域。** 現場の現実の収集と仕分けをAIに任せた分析は、この手法が依って立つ「人間の視点」をその時点で失っている——何が出てきても、それはもうクロス分析ではありません。

このルールが存在する理由は、数字とともに [human-in-the-loop.md](human-in-the-loop.md) にあります。

## この手法の証拠はどこまであるか

「実証済みらしく見せる」より、ここを正直に書くことの方が大事だと考えている。

**証拠があること。** AIと人間で**取れる情報が違う**ことは査読研究に支持されている——恥ずかしい事実はむしろ機械相手に出やすく（[Lucas et al. 2014](https://doi.org/10.1016/j.chb.2014.04.043)）、同じ文面でも人間が書いたと思うと共感的に感じられる（[Rubin et al. 2025](https://www.nature.com/articles/s41562-025-02247-w)）。A/B分担の根拠と反証は [human-territory.md](human-territory.md) にある。

**証拠がないこと。** **「AとBを足すと真因が出る」ことを直接示した研究は、私たちの知る限り存在しない。** 最も近い先行研究はAI×人間の話ですらなく、混合研究法のものである：

> **Moffatt, S., White, M., Mackintosh, J. & Howel, D. (2006).** "Using quantitative and qualitative data in health services research – what happens when mixed method findings conflict?" *BMC Health Services Research* 6:28. [doi:10.1186/1472-6963-6-28](https://doi.org/10.1186/1472-6963-6-28) — オープンアクセス・PMC1434735

この研究では、量的アーム（RCT・n=126）が「福祉受給相談に効果なし」、質的アーム（n=25）が「広範な好影響あり」と**正反対の結論**に達した。著者は両者を統合すると "produces more than the sum of its parts"、"led us to conclusions different from those that would have been drawn through relying on one or other method alone" と述べており、**突き合わせの前提を支える実証としては現状これが最も近い**。

**ただし著者の釘刺しの方が重要で、これは本手法の素朴な理解を否定する。** 彼らは量的・質的データを "complementary **rather than in competition for identifying the true version of events**"（**どちらが真実かを競わせるのではなく相補的に**）扱うべきだとし、相互検証目的での統合は「両手法が同じ研究課題を検討しているという前提に立つので**成立しない**」と明言する。そして彼らのケースでは、**食い違いの正体は人工物**だった——標準化された尺度が、インタビューに現れた次元をそもそも測っていなかった。

ここから2つ言える。第一に、これは**量的×質的**の結果であって**AI×人間**の結果ではない。**類推は私たちが持ち込んだものであり、類推のままである。** 第二に、それでも「Bが隠れた真実を暴く」より有用な説明を与えてくれる——**多くの場合、Aの計器がその土地の構成概念を測っていない**のだ。業界データは「デジタル化」を測るが、「FAXを読める人がいるか」は誰も測っていない。

したがってクロス分析の正直な立ち位置はこうなる：**実践から生まれた手法であり、部品には証拠があり、中核は類推であり、手順4はその類推が言い訳に変わるのを防ぐための検算である。**

## この手法が「ではない」もの

- 反AIではない。私たちはAIを大量に使う——人間の検証の下で、視点を増やす道具として。
- 分析の自動化テンプレートではない。人間の突き合わせ工程を抜いたら、それはもうクロス分析ではない。
- 完成品ではない。現場の実践とともに、このドキュメントも更新されていく。
