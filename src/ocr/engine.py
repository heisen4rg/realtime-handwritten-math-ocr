from PIL import Image

class OCREngine:
    def __init__(self):
        pass

    def run(self, image: Image.Image) -> dict:
        """
        Input: PIL Image
        Output: dict with raw OCR results
        """
        return {
            "text": "",
            "confidence": None
        }