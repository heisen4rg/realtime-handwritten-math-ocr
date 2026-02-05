from PIL import Image, ImageOps
import pytesseract


class OCREngine:
    """
    OCR engine wrapper around Tesseract with basic preprocessing.
    """

    def __init__(self, scale_factor=2, psm=6):
        self.scale_factor = scale_factor
        self.psm = psm

    def run(self, image):
        """
        Run OCR on a PIL Image and return extracted text.
        """
        try:
            # 1. Convert to grayscale
            gray = ImageOps.grayscale(image)

            # 2. Upscale image to improve OCR accuracy
            gray = gray.resize(
                (
                    gray.width * self.scale_factor,
                    gray.height * self.scale_factor,
                ),
                resample=Image.BICUBIC,
            )

            # Debug information
            print("Image size:", gray.size, "mode:", gray.mode)

            # 3. Run OCR
            text = pytesseract.image_to_string(
                gray,
                config=f"--psm {self.psm}",
            )

            return {
                "text": text.strip(),
                "confidence": None,
            }

        except Exception as e:
            return {
                "text": "",
                "confidence": None,
                "error": str(e),
            }