# LinkedIn Search Terms — SDE & AI Engineering

> **Purpose**: searchable role titles when sourcing jobs.
> 很多好岗位用的不是 "Software Engineer" 这种标准 title，搜不到就漏了。
> 按"标准 / 专精 / 容易漏掉的高价值 title"分组，新公司可以加进去。

---

## SDE / Backend / Infra

### Standard titles
- Software Engineer / SWE
- Software Development Engineer / SDE / SDE I / SDE II
- Backend Engineer / Backend Developer
- Full Stack Engineer / Fullstack Developer
- Frontend Engineer / Web Engineer
- Mobile Engineer / iOS Engineer / Android Engineer

### Specialized
- Platform Engineer
- Infrastructure Engineer
- Site Reliability Engineer / SRE
- DevOps Engineer
- Distributed Systems Engineer
- Cloud Engineer
- Software Engineer in Test / SDET
- Embedded Engineer
- Data Engineer
- Analytics Engineer
- Game Engineer / Gameplay Engineer

### 容易漏掉的高价值 title (强烈建议加进搜索)
- **Forward Deployed Engineer / FDE** — Palantir 首创，Anthropic / OpenAI 也用。客户现场动手集成，薪资上限高
- **Solutions Engineer** — 在 Anthropic / OpenAI / Databricks 是动手的工程岗，不是 pre-sales
- **Founding Engineer** — 早期 startup，通常给大量 equity
- **Member of Technical Staff / MTS** — Anthropic / OpenAI / Mistral / Inflection 用的扁平 title，90% 工程岗叫这个
- **Technical Staff** — 同上
- **Applied Engineer** — OpenAI 用，product-facing engineering

---

## AI / ML Engineering

### Standard titles
- AI Engineer
- ML Engineer / Machine Learning Engineer
- Applied AI Engineer / Applied Scientist
- Research Engineer
- LLM Engineer / GenAI Engineer
- Deep Learning Engineer

### Specialized
- ML Research Engineer
- AI Research Engineer
- AI Infrastructure Engineer / ML Infra Engineer
- ML Platform Engineer
- MLOps Engineer
- Inference Engineer
- Foundation Model Engineer
- NLP Engineer
- Computer Vision Engineer
- Recommender Systems Engineer
- Search Engineer (经常是 ML-heavy)

### 容易漏掉的高价值 title
- **Forward Deployed Engineer (AI flavor)** — Anthropic / Palantir AI / OpenAI
- **Member of Technical Staff (AI focus)** — Anthropic / OpenAI 几乎所有工程 AI 岗都叫这个
- **Evaluation Engineer / Eval Engineer** — RLHF / alignment / 模型 eval，Anthropic / OpenAI
- **AI Solutions Engineer** — AI startup 的动手集成岗
- **AI Product Engineer**
- **Trust & Safety Engineer** — AI lab 经常是 ML-heavy
- **Alignment Engineer / Alignment Researcher** — Anthropic / OpenAI 专属
- **Prompt Engineer** — 2023-2024 hot，现在少了但还有

---

## Level / Recency 修饰词 (组合用)

### 经验级别
- "New Grad" / "University Grad"
- "Class of 2026" / "Class of 2025"
- "Intern" / "Summer 2026 Intern"
- "Entry Level" / "Junior"
- "L3" / "L4" (Google 风格)
- "SDE I" / "SDE II"
- "Early Career"

### Boolean 搜索示例 (直接粘进 LinkedIn 搜索框)

```
("Software Engineer" OR "SDE" OR "SWE") AND "New Grad"

("AI Engineer" OR "ML Engineer" OR "Member of Technical Staff") AND "New Grad"

"Forward Deployed Engineer"

("Founding Engineer" OR "Member of Technical Staff") AND ("AI" OR "LLM")

("Research Engineer" OR "Applied Scientist") AND ("New Grad" OR "Entry Level")
```

### LinkedIn 上有用的 filter
- Date posted: **Past 24 hours** / Past week
- Experience level: **Entry level** / **Internship**
- Company size: 1-50 / 51-200 (startup) / 1001-5000 (mid) / 10001+ (FAANG)
- Location: 具体城市 vs Remote 视情况

### URL 时间过滤参数 (拼到 LinkedIn URL 末尾)

| 参数 | 含义 |
|---|---|
| `f_TPR=r3600` | 过去 1 小时 |
| `f_TPR=r7200` | 过去 2 小时 |
| `f_TPR=r86400` | 过去 24 小时 |
| `f_TPR=r604800` | 过去 7 天 |
| `f_TPR=r2592000` | 过去 30 天 |
| `f_E=2` | Entry-level |
| `f_E=3` | Associate |
| `geoId=103644278` | United States |
| `geoId=102571732` | NYC metro |
| `geoId=102095887` | SF Bay Area |
| `f_WT=2` | Remote |

**例子 — 过去 2h 全美 NG SWE**:
```
https://www.linkedin.com/jobs/search/?keywords=software%20engineer%20new%20grad
&f_TPR=r7200&f_E=2&geoId=103644278
```

---

## 公司特定 title 习惯

| 公司 | Entry-level SDE 用什么 title |
|------|----------------------------|
| Google | Software Engineer (level 不写在 title 里), Engineering Intern |
| Meta | Software Engineer, Production Engineer (他们的 SRE) |
| Amazon | SDE I, SDE Intern |
| Microsoft | Software Engineer, Software Engineer II |
| Apple | Software Engineer, AIML - Engineer (AI 团队叫这个) |
| **Anthropic** | **Member of Technical Staff**, Forward Deployed Engineer, Research Engineer |
| **OpenAI** | **Member of Technical Staff**, Research Engineer, Applied Engineer, Forward Deployed Engineer |
| **Palantir** | **Forward Deployed Engineer**, Forward Deployed Software Engineer |
| Stripe | Software Engineer, Software Engineer New Grad |
| Databricks | Software Engineer, ML Engineer |
| Tesla | Software Engineer, Autopilot Software Engineer |
| Coinbase | Software Engineer, Crypto Engineer |
| Snowflake | Software Engineer, Cloud Engineer |
| Pinterest | Software Engineer |
| Roblox | Software Engineer |
| **Inflection / Mistral / xAI** | Member of Technical Staff |

---

## 工作流建议

把 5–10 个 LinkedIn 搜索 URL 存成浏览器书签，每个对应一个 role+location 组合。一次性打开就拿到当天结果。例:

- "Forward Deployed Engineer" past 24h, Bay Area
- "Member of Technical Staff" past 24h, US
- "AI Engineer New Grad" past 24h
- `("Software Engineer" OR "SDE") AND "New Grad"` past 24h, NYC
- "Software Engineering Intern" past 24h, Summer 2026

每天的流程:
1. 一次打开所有书签 (已经 filter 过 24h 内)
2. 感兴趣的岗位打开 JD tab
3. 把 JD URL 列表粘给 Claude → 批量出定制简历

---

## Other job sources (non-LinkedIn)

- **GitHub**: `SimplifyJobs/New-Grad-Positions`, `SimplifyJobs/Summer2026-Internships`, `Pitt-CSC/Summer-2026-Internships`. Updated daily by community.
- **Y Combinator**: `workatastartup.com` (need account for full filtering, but listings public)
- **Greenhouse / Lever / Ashby boards**: company careers pages mostly use these. Public JSON APIs available.
- **HackerNews "Who's Hiring"**: 1st of every month at news.ycombinator.com

---

*维护: 发现新的 title 就加进上面对应分组，作为 operator 的累积资产。*
