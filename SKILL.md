---
name: jin-yong-name
description: Use when the user wants a real Chinese personal name with Jin Yong-inspired naming methods, including newborn naming, adult renaming, sibling or generation naming, surname-based ideation, or Chinese name evaluation. Do NOT use for online handles, fictional characters, wuxia role names, brand names, or purely fortune-based naming.
---

# 金庸帮你起名字

## Core Positioning

Use this skill for real Chinese personal names, not online handles, pen names, fictional characters, game IDs, brand names, or wuxia role names.

The goal is not to make a name "sound like a Jin Yong character." The goal is to apply Jin Yong-style naming methods to real life. Every generated name must have a clear Jin Yong-style method behind it, not merely a generic traditional-culture explanation:

- Use common characters with depth.
- Treat surname and given name as one unit.
- Use cultural roots without showing off.
- Keep meaning positive but restrained.
- Prefer names that remain usable in documents, school, work, and family settings.
- Give the name a sense of personhood, structure, and aftertaste, rather than only being safe and correct.

Traditional culture material is the candidate source, not decorative backing. Final names should first draw core characters or wording direction from the supplied `06` material cards, then be converted through a Jin Yong-style method into a realistic personal name. If a candidate is only invented from general taste and later explained with generic meaning, do not output it.

The model example is 程灵素: take usable core characters from real source material such as 《黄帝内经》之《灵枢》《素问》, then combine them naturally with surname, sound, and real-name usability. Do not imitate the exact name; imitate the sourcing method.

Single north star: the user wants "Jin Yong feeling" in a real usable name. Specific style labels, cultural references, character pools, and output formats are subordinate to that. If references appear to conflict, prioritize: Jin Yong-style method > surname fit > real-life usability > user style preference > cultural source explanation.

## Reference Routing

Use progressive disclosure. Do not read every reference by default.

Always load first:

1. `references/01_起名定位与使用边界.md` for positioning and hard boundaries.
2. `references/08_交互与输出/00_交互索引.md` for the five-field intake, output format, and hard gate routing.
3. `references/09_需求路由与召回策略.md` for method routing and candidate-pool diversity.

For name generation, load only the relevant detail files:

- Surname fit: load `references/07_姓氏适配规则.md`.
- Jin Yong method details: start with `references/02_金庸方法/00_方法索引.md`, then load only the relevant method or case files.
- Cultural source material: start with `references/06_传统文化起名素材/00_素材目录与使用规则.md`, then read only the routed 06A-06F files. Final selected and backup names must be traceable to these loaded 06 files unless the user is only evaluating an existing name.
- Common-character usability: load `references/04_常用字白名单.md` after candidates exist, only as a usability check or replacement reference.

For filtering and quality control, load as needed in this order:

- Banned/risky characters: `references/05A_禁用字与风险字库.md`
- Homophone and pronunciation risks: `references/05B_谐音风险库.md`
- Final quality standard: `references/03_好名字评判标准.md`
- Mandatory output gate: apply `references/08_交互与输出/02_默认生成流程.md` and `references/08_交互与输出/08_禁止输出与标准模板.md` before showing any name.

Do not load the entire 06 material library by default. Use targeted search or read only the relevant folders/files based on the route and candidate direction.

If available, use `scripts/name_quality_check.py` to check tone-pattern, repeated ending characters, repeated structure hints, and high-frequency safe-character overload before final output. The script is a hard-rule aid, not a replacement for judgment.

## Workflow

1. Collect the six naming inputs（六项硬信息）in one message whenever possible.
   - Surname.
   - Gender tendency: boy, girl, or neutral.
   - Name length preference: one-character given name, two-character given name, or no preference.
   - Required character(s), if any.
   - Avoided character(s), if any.
   - Primary naming dimension（主要命名维度）, with at most one optional secondary dimension. The user may instead provide a custom feeling or reference name.
   - Ask with the fixed method-based menu from `08_交互与输出/01_五项信息收集.md`. Do not replace it with gender-based or abstract mood menus.

2. If surname is missing, ask for surname first.

3. If gender tendency is missing, ask whether the name should be boy, girl, or neutral.

4. If any of the six naming inputs are missing, ask for the missing items together using the standard six-field form in `08_交互与输出/01_五项信息收集.md`. Missing a primary naming dimension is a hard stop. "直接起"、"你决定"、"不挑" do not satisfy this field.

5. Treat a clear user-provided method, feeling, or reference name as the sixth field. Map it to one primary naming dimension and, only when useful, one secondary dimension. Analyze the reference name's method; never copy the full name or make a one-character substitution.

6. Do not ask by default for birth date, birth hour, Five Elements, zodiac, stroke fortune, or parent-surname fusion.
   - If the user provides these, treat them only as soft preferences.
   - Never promise luck, fate improvement, or fortune effects.

7. Generate internally using this order:
   - Judge surname type and risk with `07`.
   - Route the request with `09` so the selected primary naming dimension controls the main method, reference files, source pool, composition pattern, and rejection rules. The secondary dimension may supplement but must not receive equal weight.
   - Choose at least three methods from `02_金庸方法`: surname linkage, shallow words with deep use, hidden classics, poetic restraint, imagery, virtue/personality, or sound/rhythm.
   - Before forming names, load the routed 06 files and extract source-backed core characters, imagery, personality directions, two-source relationships, or short wording directions. These are the seed pool, not finished names.
   - Generate a broad internal candidate pool from the 06 seed pool before filtering. Do not invent names from abstract taste, then look for an explanation afterward. Do not let a user-provided style label collapse the pool into one repetitive word cluster.
   - Apply the high-frequency safe-character cooling rule in `09`: do not let `本、立、谦、修、齐、景、行、允、衡、和、知、远、明、守、安、正、诚、言` or similar safe words dominate the final list across turns.
   - Use 06 as the default candidate source, and always convert it back into a Jin Yong-style real-name method.
   - Use `04` after candidate formation to check common-character usability or find a safer replacement. Do not use it as the first-round idea generator.
   - Filter candidates through `05A` and `05B`.
   - Apply final quality control with `03` after risk filtering.
   - Run or mentally apply `scripts/name_quality_check.py` before final output when candidates can be represented with tone sequences.
   - Apply the pre-output hard gate from `08_交互与输出`: five inputs complete, tone sequence passes, ping-ze balance passes, pronunciation passes, real-name feel passes, web-novel/pen-name feel absent, and final list has structural variety.
   - Keep only candidates with a clear Jin Yong-style method and real-life usability.

8. Output according to `08_交互与输出/04_精选名输出模板.md` and `08_交互与输出/05_备选名输出模板.md`.
   - Default to 3 selected names plus 2 backup names.
   - Do not output large candidate lists.
   - If quality is insufficient, give fewer rather than forcing weak names.

## Hard Rules

- Do not directly reuse full Jin Yong character names.
- Do not create names that feel like xianxia, web-novel, game ID, or ancient-style social handle names.
- Do not create names that feel like internet-fiction heroines, pen names, Xiaohongshu-style aesthetic names, or "clean/cold literary" handles even when every single character is individually safe.
- Do not output generic traditional-culture names that lack a Jin Yong-style method.
- Do not output names that cannot point to a specific loaded 06 source file, source item, or clearly named 06 material direction.
- Do not treat the 06 material-card "seed" words or listed two-character phrases as finished candidate names. Two-character phrases in 06 are recall and transformation hints unless they independently pass surname fit, tone movement, real-name feel, and Jin Yong-style method checks.
- Do not output "safe but made-up" combinations such as generic `文 + 序`, `维 + 清`, `修 + 言` unless the exact combination or both core characters have a clear 06 source relationship and pass surname fit.
- Do not output a batch where all selected names have the same structure, such as all "virtue + distance" or all "clear + peaceful" names.
- Do not output three-syllable full names with all three syllables in the same tone: 111, 222, 333, or 444. This includes cases like `luó chéng huái` = 222. Do not waive this for cultural source quality.
- Do not let a three-syllable full name pass selected-name quality control only because it avoids exact same-tone triples. If all three syllables are level tones, such as `2-1-2`, `2-2-1`, or `1-2-1`, optimize it or downgrade it; selected names should have real tone movement or ping-ze balance.
- Do not use banned or high-risk characters from `05A`.
- Do not use names with obvious vulgar, insulting, disease/disaster, poverty/failure, or awkward homophones from `05B`.
- Do not fabricate classics, titles, original quotes, or sources.
- Do not present risky names to the user as selected names.
- Do not hide serious issues; if a user insists on a risky character or sound, explain cleanly and offer safer replacements.

## Output Standard

For selected names, include:

- Name
- Pronunciation
- Source or meaning
- Surname fit
- Real-life usability assessment

For backup names, keep the explanation shorter.

Keep the final result clean. Do not show the full internal scoring or full filtering process unless the user asks for analysis.

## Handling Special Requests

- If the user asks for "more Jin Yong / more wuxia / more jianghu", lower the intensity into a real-name-safe version.
- If the user asks for "八字 / 五行 / 生肖", acknowledge it as a preference but continue to prioritize real-name usability.
- If the user gives a fixed character, still check `05A`, `05B`, and surname fit.
- If the user asks only to evaluate an existing name, use `03`, `05A`, `05B`, and `07` first, then optionally suggest cleaner alternatives.
