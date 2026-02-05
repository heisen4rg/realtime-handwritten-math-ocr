from src.ui.overlay_selector import ScreenOverlay
from src.ocr.engine import OCREngine


def main():
    # 1. Launch overlay and get cropped image
    overlay = ScreenOverlay()
    image = overlay.run()

    if image is None:
        print("No region selected.")
        return

    # 2. Run OCR
    engine = OCREngine()
    result = engine.run(image)

    # 3. Output result
    print("\n=== OCR RESULT ===")
    print(result["text"])


if __name__ == "__main__":
    main()