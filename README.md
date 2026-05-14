# Feishu-Video-Pipeline

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

> **Showcase** — ~15% skeleton. Core implementation not included.

Feishu Bitable automation across 5 linked sheets, processing 16 rows per run. Pulls product data from Kalodata, runs Gemini multimodal analysis, generates 6-grid storyboards, removes watermarks from reference clips, and writes Seedance prompts back to Bitable.

## Stack

- Python, Flask
- Google Gemini API
- Feishu (Lark) Bitable API
- Kalodata API
- Seedance 2.0
- FFmpeg (watermark removal)

## Pipeline

```
Bitable trigger (5 sheets, 16 rows/run)
    └── Kalodata: fetch product metadata
         └── Gemini: multimodal video + image analysis
              └── 6-grid storyboard builder
                   └── FFmpeg: strip watermarks from reference clips
                        └── Seedance prompt writer
                             └── Write results back to Bitable
```

## Usage

```bash
pip install -r requirements.txt
cp .env.example .env

# Run one full batch
python pipeline.py --batch-size 16

# Process a single Bitable row by record ID
python pipeline.py --record rec_abc123

# Start as a webhook server
python app.py
```

## Structure

```
Feishu-Video-Pipeline/
├── app.py               # Flask webhook entry
├── pipeline.py          # batch processing logic
├── storyboard.py        # 6-grid storyboard generator
├── watermark.py         # FFmpeg watermark removal
├── seedance.py          # Seedance prompt builder
├── kalodata_client.py
├── feishu_client.py
└── .env.example
```

## Sheet Schema

Each of the 5 Bitable sheets maps to a production stage. The pipeline reads from stage N and writes outputs to stage N+1, keeping the full audit trail in Bitable.
