import tkinter as tk
from PIL import ImageGrab, ImageTk, Image


class ScreenOverlay:
    def __init__(self):
        self.result_image = None
        self.done = False
        # Create ONE Tk root
        self.root = tk.Tk()
        self.root.withdraw()  # hide temporarily to query screen size

        # Query logical screen size (Tk coords)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Capture physical screen
        raw_screenshot = ImageGrab.grab()

        # Resize screenshot to match Tk logical resolution
        self.screenshot = raw_screenshot.resize(
            (screen_width, screen_height),
            resample=Image.Resampling.LANCZOS
        )

        # Configure root window
        self.root.deiconify()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.configure(cursor="crosshair")

        # Canvas for drawing
        self.canvas = tk.Canvas(
            self.root,
            width=screen_width,
            height=screen_height,
            highlightthickness=0
        )
        self.canvas.pack()

        # Selection state
        self.start_x = None
        self.start_y = None
        self.rect_id = None

        # IMPORTANT: keep PhotoImage as instance attribute
        self.tk_image = ImageTk.PhotoImage(self.screenshot)

        self.canvas.create_image(
            0, 0,
            anchor="nw",
            image=self.tk_image
        )

        # ESC to exit
        self.root.bind("<Escape>", self.on_escape)

        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def run(self):
        self.root.mainloop()
        self.root.destroy()
        return self.result_image

    def on_mouse_down(self, event):
        self.start_x = event.x
        self.start_y = event.y

        # Create rectangle once
        self.rect_id = self.canvas.create_rectangle(
            self.start_x, self.start_y,
            self.start_x, self.start_y,
            outline="red",
            width=2
        )

    def on_mouse_drag(self, event):
        if self.rect_id is None:
            return

        # Update rectangle as mouse moves
        self.canvas.coords(
            self.rect_id,
            self.start_x, self.start_y,
            event.x, event.y
        )

    def on_mouse_up(self, event):
        end_x, end_y = event.x, event.y

        x1 = min(self.start_x, end_x)
        y1 = min(self.start_y, end_y)
        x2 = max(self.start_x, end_x)
        y2 = max(self.start_y, end_y)

        # Ignore tiny or invalid selections
        if abs(x2 - x1) < 5 or abs(y2 - y1) < 5:
            self.result_image = None
        else:
            self.result_image = self.screenshot.crop((x1, y1, x2, y2))

        self.done = True
        self.root.quit()

    def on_escape(self, event=None):
        self.result_image = None
        self.done = True
        self.root.quit()