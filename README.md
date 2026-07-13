# 金庸帮你起名字（jin-yong-name）

一个面向真实中文姓名的 Agent Skill。借鉴金庸先生的命名方法，为孩子起名、成人改名、兄弟姐妹或同辈命名提供少量、可解释、可长期使用的候选名字。

我一直觉得，金庸笔下很多名字的好，不靠生僻字，也不靠刻意营造武侠感。郭靖、杨康寄托家国记忆，木婉清有诗意却不过分雕琢，宁中则端正含蓄，程灵素从《灵枢》《素问》中自然取意。它们往往用字常见，却能把姓氏、音韵、文化出处、人物气质和人生期许连成一个整体：读起来顺，写出来稳，初看自然，细想又有余味。

「金庸帮你起名字」提取了金庸命名中的几种方法，包括浅字深用、姓名一体、典籍无痕、诗意留白、品格寄托和声韵气口，用来为真实生活中的孩子和成年人起名。它不会直接照搬金庸人物名，也不会把名字做成仙侠角色名或古风网名。

每个候选名字都要经过现实姓名标准检查：用字常见易认、全名连读顺口、声调有起伏、没有明显不良谐音、寓意正向、文化来源可靠、与姓氏适配，并且能自然用于证件、学校、职场和日常称呼。希望最后得到的名字，不只是一时好听，也能伴随一个人长期使用。

## 能做什么

- 新生儿、孩子起名
- 成人真实姓名优化或改名参考
- 兄弟姐妹、同辈姓名体系设计
- 根据姓氏、性别倾向、指定字和避用字定向起名
- 评价一个现有中文姓名，并给出更稳妥的替代方案

默认输出 3 个精选名和 2 个备选名。质量不足时宁可少给，不用弱名字凑数。

## 命名方法

- 浅字深用：使用常见字承载文化出处、人物气质和人生期许。
- 姓名一体：把姓与名作为一个整体判断，不把姓氏当作无关前缀。
- 典籍无痕：出处可靠，但名字表面自然，不生搬原句。
- 诗意留白：保留画面和余味，避免花月香露式堆砌。
- 品格寄托：表达清正、温厚、明达、坚韧等真实期许，不写成口号。
- 声韵气口：检查普通话声调、连读、谐音和日常称呼体验。

## 一键安装

适用于支持开放 Agent Skills 格式的 Codex、Claude Code、Cursor、Gemini CLI、GitHub Copilot、Cline、OpenCode 等工具。

### 自动识别本机 Agent

```bash
npx skills add linkaka93/jin-yong-name --skill jin-yong-name -g
```

运行后按提示选择要安装到的 Agent。

### 安装到 Codex

```bash
npx skills add linkaka93/jin-yong-name --skill jin-yong-name -g -a codex -y
```

### 安装到 Claude Code

```bash
npx skills add linkaka93/jin-yong-name --skill jin-yong-name -g -a claude-code -y
```

### 让 WorkBuddy 或其他 Agent 帮你安装

把下面这段话直接发给你的 Agent：

```text
请从 https://github.com/linkaka93/jin-yong-name/tree/main/skills/jin-yong-name 安装名为 jin-yong-name 的 Agent Skill。请复制完整 skill 目录，包括 SKILL.md、references、scripts、evals 和 agents，不要只复制 SKILL.md。安装后请检查 SKILL.md 的 name 为 jin-yong-name，并运行 evals/validate_skill_contract.py 验证。
```

如果所用工具支持“从 GitHub 导入 Skill”，直接粘贴仓库地址：

```text
https://github.com/linkaka93/jin-yong-name/tree/main/skills/jin-yong-name
```

## 使用方式

安装后，可以直接对 Agent 说：

```text
请用 jin-yong-name 帮我起一个真实可用的中文名字。
```

Skill 会先一次性确认六项信息：姓氏、性别倾向、名字字数、必须保留的字、避用字、主要命名维度。信息完整后再生成名字。

## 目录结构

```text
jin-yong-name/
├── README.md
├── LICENSE
└── skills/
    └── jin-yong-name/
        ├── SKILL.md        # 核心工作流与硬规则
        ├── agents/         # Agent 展示信息
        ├── references/     # 命名方法、文化素材、风险库和输出规范
        ├── scripts/        # 姓名质量机械检查
        └── evals/          # Skill 合同检查和测试用例
```

## 本地验证

```bash
python3 skills/jin-yong-name/evals/validate_skill_contract.py
```

通过时会显示：

```text
PASS: jin-yong-name contract is complete
```

## 使用边界

本 Skill 面向真实姓名，不用于网名、笔名、小说角色名、游戏 ID、品牌名或纯命理起名。它借鉴命名方法，不直接复用金庸人物全名，也不承诺八字、五行、运势或吉凶效果。

## 说明

这是一个非官方、独立制作的开源项目，与金庸先生遗产管理方、作品出版方及相关权利方无隶属或授权关系。“金庸”在本项目中用于说明所研究和借鉴的命名方法与审美来源。

## License

[MIT License](LICENSE)
