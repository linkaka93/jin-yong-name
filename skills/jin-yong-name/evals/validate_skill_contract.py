#!/usr/bin/env python3
"""Static contract checks for the jin-yong-name skill."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def require(text: str, needle: str, label: str, issues: list[str]) -> None:
    if needle not in text:
        issues.append(f"missing {label}: {needle}")


def forbid(text: str, needle: str, label: str, issues: list[str]) -> None:
    if needle in text:
        issues.append(f"stale {label}: {needle}")


def main() -> int:
    issues: list[str] = []
    skill = read("SKILL.md")
    intake = read("references/08_交互与输出/01_五项信息收集.md")
    flow = read("references/08_交互与输出/02_默认生成流程.md")
    routing = read("references/09_需求路由与召回策略.md")
    cases = read("references/02_金庸方法/09_现实可用案例.md")
    caution = read("references/02_金庸方法/10_慎用与禁用案例.md")
    quality_script = read("scripts/name_quality_check.py")
    prompt = read("agents/openai.yaml")

    for text, label in ((skill, "SKILL"), (intake, "intake"), (flow, "flow")):
        require(text, "六项", f"{label} six-field gate", issues)
        require(text, "主要命名维度", f"{label} primary dimension", issues)

    menu = {
        "品格寄托": "杨铁心、穆念慈、刘正风",
        "典籍取字": "程灵素、张无忌、宁中则",
        "诗文取意": "木婉清、周芷若、李秋水",
        "姓名一体": "风清扬、木婉清、温仪",
        "风物成象": "霍青桐、阮星竹、邓百川",
        "浅字深用": "郭靖、刘正风、萧中慧",
        "纪念与家族体系": "郭靖 / 杨康、武敦儒 / 武修文、袁承志",
    }
    for dimension, examples in menu.items():
        require(intake, dimension, f"menu dimension {dimension}", issues)
        require(intake, examples, f"menu examples for {dimension}", issues)
        require(routing, dimension, f"routing dimension {dimension}", issues)
        support_count = len(re.findall(rf"(?:主要|次要)命名机制：[^\n]*{re.escape(dimension)}", cases))
        if support_count < 5:
            issues.append(f"dimension {dimension} has only {support_count} case supports; expected at least 5")

    require(intake, "自定义", "custom route", issues)
    require(intake, "一个主要方向", "single primary route", issues)
    require(intake, "一个辅助方向", "optional secondary route", issues)
    forbid(intake, "不挑，按姓氏默认", "default escape option", issues)

    card_count = len(re.findall(r"^### 案例 \d+：", cases, flags=re.MULTILINE))
    if card_count != 40:
        issues.append(f"expected 40 unified case cards, found {card_count}")
    card_blocks = re.split(r"(?=^### 案例 \d+：)", cases, flags=re.MULTILINE)[1:]
    card_fields = (
        "命名来历",
        "主要命名机制",
        "次要命名机制",
        "姓氏是否参与",
        "是否属于成对或家族体系",
        "可转化程度",
        "真人姓名风险",
        "是否允许在用户菜单中展示",
        "可借鉴部分",
        "禁止照搬部分",
    )
    for block in card_blocks:
        title = block.splitlines()[0]
        for field in card_fields:
            if f"- {field}：" not in block:
                issues.append(f"{title} missing field {field}")

    for name in ("杨康", "杨铁心", "郭啸天", "包惜弱", "黄蓉", "段誉", "令狐冲"):
        require(cases, name, f"expanded case {name}", issues)

    for name in ("林平之", "游坦之", "李莫愁", "向问天", "任我行", "谢烟客", "黄药师", "苗人凤", "刀白凤", "乔峰 / 萧峰"):
        require(caution, name, f"internal-only case {name}", issues)

    require(cases, "是否允许在用户菜单中展示", "case-card display field", issues)
    require(cases, "禁止照搬部分", "case-card prohibition field", issues)
    require(caution, "不得进入素材召回", "internal-only recall block", issues)

    require(quality_script, "本立谦修齐", "expanded safe-character cooling", issues)
    require(prompt, "主要命名维度", "updated default prompt", issues)

    if issues:
        print("FAIL")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("PASS: jin-yong-name contract is complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
