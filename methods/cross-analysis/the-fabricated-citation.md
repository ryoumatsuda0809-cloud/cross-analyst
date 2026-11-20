# The Citation That Didn't Exist / 実在しなかった引用

A first-person account of the moment that turned our verification rule from a principle into a scar.

**日本語版は[下半分](#日本語版)にあります。**

---

## What happened

In June 2026, we were writing a page about the risks of over-relying on AI — the philosophy page of our own company site. We wanted research evidence for the claim that human-AI collaboration outperforms full automation.

The AI assisting us offered a citation: **"Sidra & Wagan (2026)"**, with a plausible title, plausible findings, and a plausible venue.

It did not exist.

Not a wrong year, not a misspelled name — the paper was never written. The AI had fabricated a complete academic citation, tailored precisely to what we wanted to hear, for a page **whose entire point was to warn about trusting AI too much**.

We caught it only because our own method requires a human to verify every citation against primary sources before publication. The check took minutes: search the title, search the authors, search the venue. Nothing. We replaced it with a real study — Brynjolfsson, Li & Raymond's "Generative AI at Work" (*QJE* 2025), which we verified down to the sample size.

## Why this story is the method

The irony is the lesson. If AI can fabricate evidence *for an article about not trusting AI*, it can fabricate evidence for anything: your market analysis, your board deck, your medical summary. The fabrication won't look suspicious — it is optimized to look exactly like what you hoped to find. **The more convenient a citation is, the more it deserves verification.**

This is automation bias in the wild (see [human-in-the-loop.md](human-in-the-loop.md), principle 2): even experts drop from 82% to 45% accuracy when an AI feeds them wrong suggestions. We were experts on this exact topic, mid-sentence in a warning about this exact failure mode — and the fake citation still almost got through.

## The checklist that came out of it

Before publishing any AI-assisted claim that cites a source:

1. **Find the primary source.** Not a blog post quoting it — the paper, the dataset, the official page. If you cannot locate it, the citation does not exist for your purposes.
2. **Verify the specific numbers.** Authors real, year right, and — most often missed — the figures actually in the paper, meaning what the AI says they mean. (We once nearly cited a productivity gain as an accuracy gain. Same paper, real numbers, wrong meaning.)
3. **Record what you verified.** Keep the link and a one-line note of what you checked. Future-you will not remember.
4. **If it can't be verified, cut it or say so.** An honest "industry estimate, source unverified" beats a confident fabrication every time.

The rule is now permanent in our practice: **AI drafts, humans verify, and nothing cites what a human hasn't seen.**

---

---

# 日本語版

検証ルールが「原則」から「傷跡」に変わった瞬間の、一人称の記録。

## 何が起きたか

2026年6月、私たちは「AIへの依存しすぎのリスク」についてのページを書いていました——自社サイトの思想ページです。「人間とAIの協働は完全自動化に勝る」という主張の研究的根拠が欲しかった。

作業を補助していたAIが、ある引用を提示しました。**「Sidra & Wagan (2026)」**——もっともらしいタイトル、もっともらしい結果、もっともらしい掲載先。

実在しませんでした。

年の間違いでも、名前の綴りミスでもありません。その論文は書かれたことがなかった。AIは、私たちが聞きたいことに正確に合わせて、完全な学術引用を捏造したのです。しかも、**「AIを信じすぎるな」と警告することが目的そのものであるページのために。**

発見できたのは、公開前にすべての引用を人間が一次情報で検証するという自分たちのルールがあったからでした。確認は数分：タイトルを検索、著者を検索、掲載先を検索。何も出ない。実在する研究——Brynjolfsson, Li & Raymond「Generative AI at Work」（QJE 2025）——にサンプル数まで検証した上で差し替えました。

## なぜこの実話が手法そのものなのか

この皮肉こそが教訓です。「AIを信じるな」という記事のための証拠すら捏造できるなら、AIは何のための証拠でも捏造できます。あなたの市場分析にも、役員会資料にも、医療サマリーにも。しかも捏造は怪しく見えません——**あなたが見つけたかったものに見えるよう最適化されている**からです。引用が都合よく見えるほど、検証に値する。

これは自動化バイアスの実例です（[human-in-the-loop.md](human-in-the-loop.md) 原則2）：AIが誤った提案をすると、専門家ですら正答率が82%→45%に落ちる。私たちはまさにこのテーマの専門家で、まさにこの失敗モードへの警告文を書いている最中でした——それでも偽の引用は、あと一歩で通り抜けるところだった。

## この経験から生まれたチェックリスト

AIの補助で書かれた、出典つきの主張を公開する前に：

1. **一次情報を見つける。** それを引用しているブログではなく、論文・データセット・公式ページ本体。見つけられないなら、その引用は存在しないものとして扱う。
2. **具体的な数字を検証する。** 著者は実在するか、年は正しいか、そして——最も見落とされるのは——その数字が本当に論文にあり、AIの言う意味で使われているか。（私たちは一度、「生産性」の向上を「精度」の向上として引用しかけました。同じ論文、本物の数字、間違った意味。）
3. **検証したことを記録する。** リンクと、何を確認したかの一行メモ。未来の自分は覚えていません。
4. **検証できなければ、削るか、そう書く。** 「業界推計・出典未検証」という正直さは、自信満々の捏造に常に勝ります。

このルールはいま、私たちの実務に恒久的に組み込まれています：**AIが下書きし、人間が検証する。人間が見ていないものは、何も引用しない。**
