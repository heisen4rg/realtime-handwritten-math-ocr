from PIL import ImageGrab
import time
import os

def capture_region(bbox):
    img = ImageGrab.grab(bbox=bbox)

    # save with timestamp so it never overwrites
    filename = f"capture_{int(time.time())}.png"
    path = os.path.join(os.getcwd(), filename)

    img.save(path)
    print(f"[OK] Screenshot saved to {path}")

    return img