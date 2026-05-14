<div align="center">

# 📊 Feishu Video Pipeline

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Lark](https://img.shields.io/badge/Lark-Bitable-00D6B9?style=flat-square&logo=bytedance&logoColor=white)](https://open.feishu.cn)
[![Gemini](https://img.shields.io/badge/Gemini-2.5%20Pro-4285F4?style=flat-square&logo=google&logoColor=white)](https://deepmind.google/gemini)
[![Seedance](https://img.shields.io/badge/Seedance-2.0-FF6B35?style=flat-square)](https://www.volcengine.com)

**Feishu Bitable-driven TikTok video pipeline — Kalodata sourcing → Gemini multi-modal → 6-grid storyboard → Seedance 2.0 prompts**

> ⚠️ **Showcase Only** — ~15% skeleton. Production prompts & Feishu integration secrets not included.

</div>

---

## ✨ Overview

A Bitable-first refactor of the original n8n-based pipeline — replacing n8n with direct Flask APIs called by Feishu automations. Five Bitable tables × 16 automations drive the end-to-end loop from product discovery to Seedance-ready prompt assembly.

---

## 🏗️ Architecture

```
   Feishu Bitables (5)              Flask APIs (Singapore VPS)
  ┌────────────────────┐           ┌──────────────────────────┐
  │  · Products        │── HTTP ──►│  /api/feishu/select      │
  │  · Selling points  │           │  /api/feishu/analyze     │
  │  · Storyboards     │           │  /api/feishu/storyboard  │
  │  · Music           │           │  /api/feishu/music       │
  │  · TikTok stats    │           │  /api/feishu/stats       │
  └────────────────────┘           └────────────┬─────────────┘
                                                │
                              ┌─────────────────┴─────────────────┐
                              ▼                                   ▼
                    ┌──────────────────┐               ┌──────────────────┐
                    │  Kalodata API    │               │  Gemini 2.5 Pro  │
                    │  product source  │               │  multi-modal     │
                    └──────────────────┘               └────────┬─────────┘
                                                                │
                                                                ▼
                                                       Seedance prompts
                                                       (manual render)
```

---

## 📁 Structure

```
feishu-video-pipeline/
├── server.py                  # Flask entry
├── feishu_bitable.py          # Feishu Bitable client
├── pipelines/
│   └── storyboard.py          # 6-grid storyboard pipeline
├── platforms/
│   └── gemini.py              # Gemini multi-modal client
└── requirements.txt
```

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Web Server | Flask + Gunicorn |
| Hosting | Singapore VPS |
| Trigger | Feishu Bitable automation |
| LLM | Gemini 2.5 Pro (multi-modal) |
| Video | Seedance 2.0 (manual render) |

---

<div align="center">
<sub>Showcase version · Production prompts not included · For portfolio reference only</sub>
</div>
