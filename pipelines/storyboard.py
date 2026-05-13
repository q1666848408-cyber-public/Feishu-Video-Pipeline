"""
6-grid storyboard pipeline — Kalodata → Gemini → Seedance prompts.
"""

from typing import Dict


class StoryboardPipeline:
    def run(self, product_record: dict) -> Dict:
        """End-to-end: product info → 6-grid → Seedance prompts. [Not shown]"""
        pass

    def _strip_watermark(self, video_url: str) -> str:
        """Strip watermark from reference video. [Not shown]"""
        pass

    def _generate_grid(self, frames: list) -> bytes:
        """Compose 6 frames into single grid image. [Not shown]"""
        pass
