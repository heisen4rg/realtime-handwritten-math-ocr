from PIL import Image, ImageOps
import pytesseract

class OCREngine:
    def __init__(self):
        pass

    def run(self, image):
        # Convert to grayscale
        gray = ImageOps.grayscale(image)

        # Upscale image to improve OCR accuracy
        gray = gray.resize(
            (gray.width * 2, gray.height * 2),
            resample=Image.BICUBIC
        )

        # Debug information
        print("Image size:", gray.size, "mode:", gray.mode)

        # Run OCR with a suitable page segmentation mode
        text = pytesseract.image_to_string(
            gray,
            config="--psm 6"
        )

        return {
            "text": text.strip(),
            "confidence": None
        }