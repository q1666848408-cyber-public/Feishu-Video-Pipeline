"""
Gemini 2.5 Pro multi-modal client.
"""


class GeminiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def analyze_grid(self, grid_image: bytes, product_info: dict) -> dict:
        """Analyze 6-grid composition, return per-cell descriptions. [Not shown]"""
        pass

    async def generate_prompts(self, cells: list) -> list:
        """Cell descriptions → Seedance-compatible prompts. [Not shown]"""
        pass
