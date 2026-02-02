from pynput import mouse
from src.system.screen_capture import capture_region

start_pos = None
end_pos = None

def normalize_bbox(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    left   = int(min(x1, x2))
    right  = int(max(x1, x2))
    top    = int(min(y1, y2))
    bottom = int(max(y1, y2))

    return (left, top, right, bottom)

def on_click(x, y, button, pressed):
    global start_pos, end_pos

    if pressed:
        start_pos = (x, y)
        print(f"Mouse down at {start_pos}")
    else:
        end_pos = (x, y)
        print(f"Mouse up at {end_pos}")

        bbox = normalize_bbox(start_pos, end_pos)
        print("Normalized bbox:", bbox)

        img = capture_region(bbox)
        img.show()

        return False


with mouse.Listener(on_click=on_click) as listener:
    listener.join()

