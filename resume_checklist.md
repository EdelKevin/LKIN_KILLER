# 北美 CS 学生简历 Checklist

> **Scope**: 3year/Entry/New Grad/Intern SWE/SDE applications in North America. Does NOT apply to applicants with US work history or those job-hunting in China.
> **Source**: Public Xiaohongshu (小红书) account `2sumtech`.

---

## 简历核⼼原则

- ✅ 用 Claude，不用 ChatGPT
- ✅ 简历不需要 100% 合理；缺点不要写
- ✅ 不要用 Overleaf / Canva 模板（机筛不友好）
- ✅ 不同岗位不同版本：backend / frontend / fullstack / PM / AI / ML
- ✅ JD 上所有 grep-able 技能都要在简历中有覆盖（候选人面试前自行补齐掌握，见 master_prompt Strategy C）
- ✅ 第一个看简历的是 recruiter，不懂技术 → 提供 business context，不是纯技术细节
- ✅ 用 recruiter 能理解的语言描述 impact

## 简历格式要求

- ✅ Gmail / Yahoo 邮箱，不用 QQ
- ✅ 邮箱、LinkedIn、GitHub profile 名字一致，slug 一致（e.g. `/annalisde`）
- ✅ 毕业时间必须写，不能写 "present"
- ✅ GPA：< 3.5 不写；小数位一致（3.6/4.0 或 3.67/4.00，不能混）
- ✅ **Header location 按 JD 填 city/state**（表示可到岗地点，便于通过 recruiter 地域筛选；仅限 header，过往工作地点为硬事实不可改）
- ✅ 文件 PDF，命名 `姓名+Resume`
- ✅ **Section 标题首字母大写**（`Education` NOT `EDUCATION`）
- ✅ 写完整 LinkedIn URL，不用 hyperlink（HR 可能打印）
- ✅ 如持有永久工作许可（Green Card / Citizen），名字下面单独一行加粗注明，如 `No Sponsorship Needed`；具体身份以 `profile/` 中的候选人信息为准
- ✅ 删除 hobby

## 不要做

- ❌ 时间 gap 不主动提及
- ❌ 换专业等缺点不主动提及
- ❌ 工作时间不能 overlap（e.g. 5/2025-8/2025 vs 7/2025-10/2025 ❌）

## 重点突出

- ✅ Awards/Publications/Certificates 单独成 section 放前面（如有）
- ✅ Skills section 放最后（仅为过机筛）
- ✅ 工作经历充分呈现、量化到位，不轻描淡写
- ✅ 每个 bullet 格式：**用了啥（tech）+ 干了啥（feature）+ 实现了啥（business impact / 数字量化）**
- ✅ 数字量化（统一 ≤40% 提升；>25% 必须在同一 bullet 内点出 mechanism，如 `−35% p95 via Redis cache`）
  - 减少 X 损失 / 提高 X 效率
  - 减少 X 内存 / 提高 X 搜索效率
  - 节省 / 赚取具体金额
  - X 用户使用量
  - ❌ 裸数字 `10x` / `100x` / `1000x`（无来源 = 编造红旗）
- ✅ 每行体现 action, value, tech-readiness

## 不要写

- ❌ 所有 coursework
- ❌ 形容词堆砌的 summary（proactive / innovative）
- ❌ 技术罗列的 summary（已有 Skills section）
- ❌ Summary 超过 3 行 → 删除超出部分
- ⚠️ Summary 可选；写则 ≤2 行、无形容词堆砌、无技术罗列

## LinkedIn

- ✅ 自我介绍加 "willing to relocate"
- ✅ 自我介绍：拒绝形容词堆砌、技术堆砌，一切用数字说话
- ✅ 连接数 ≥ 500
- ✅ 真实照片（微笑、干净背景、非合照）
- ✅ 定期 post / repost
- ✅ 购买 Premium 显示认真态度

## 工作经历描述（核心 writing rules）

- ✅ 至少一个工作经历且 location 在美国
- ✅ 每个经历严格 **3** 个 bullets（与 `profile/style_profile.md` Structure fingerprint 一致，不可扩展）
- ❌ 工作经历下面不要再列出几个不同 project 然后 sub-describe
- ✅ 每个 bullet ≤ 3 行，超过就拆分
- ✅ 全部过去时，时态一致
- ✅ 删除 "the" / "an" 等冠词
- ✅ 只对技能和数字加粗（除非跟 JD 一致需要 bold 别的）
- ✅ 突出工程相关经历，不写无关专业背景
- ✅ 同学 review 并提问 → 用解释补充简历
- ✅ AI 检查语法、时态、句式

### 动词规则

**WHITELIST（3year/Entry/New Grad/Intern 优先用）**:
`developed, implemented, built, created, optimized, enhanced, integrated, deployed`

**SENIOR BLACKLIST（永远不用 — 即使 3-year SWE 也显得虚）**:
`architected`

**CONDITIONAL（受限使用）**:
- `led` —— 仅限明确的小范围对象，如 `led migration of X`, `led 2-person spike`；**禁** `led team of N`（N≥5）
- `designed` —— 仅限 feature / API / 数据模型层面；**禁** 用于 system architecture / platform 级宣称

**WEAK BLACKLIST（永远不用）**:
`worked with, learnt, studied, assisted, helped, experienced, familiar with, knowledge of`

**Other observations**:
- 删除 ChatGPT 生成的 `<summary>: <details>` 冒号格式
- 美国工作不写 remote，写具体 City, State
- 每个工作下面不要单独一行写 tech stack（乱且没用）
- 每个工作下面不要单独一行介绍公司业务（融进第一条 bullet）

## 面试准备

- ✅ 5 个 mock interview：2 个 mock 别人（学描述）、3 个 mock 自己（练表达）
- ✅ 环境整洁，光线充足，看清脸
- ✅ 清洁眼镜，头发不遮脸
- ❌ 不在车、咖啡馆、图书馆工作区、户外
- ✅ 女生化淡妆

## 时间线

- ✅ 有 refer 找 refer；开岗第一天没 refer → 直接投
- ✅ 开岗就申请（FAANG NG 收 1000+ 申请）

## 后端程序员 (backend SWE) ATS 必须有

- ✅ RESTful API (with language + framework)
- ✅ 数据库
- ✅ Cloud
- ✅ AI / ML
- ✅ Agile workflow
- ✅ Unit test coverage 90%
- ✅ CI/CD
- ✅ Docker
- ✅ K8s

**加分**:
- ✅ Kafka
- ✅ Cache (Redis)
