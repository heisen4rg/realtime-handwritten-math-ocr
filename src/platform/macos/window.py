from AppKit import NSView, NSImage
from Quartz import CGWindowListCreateImage, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from Foundation import NSMakeRect
from AppKit import NSGraphicsContext


class ScreenshotView(NSView):
    def initWithFrame_(self, frame):
        self = NSView.initWithFrame_(self, frame)
        if self is None:
            return None

        self.screenshot = self._capture_screen()
        return self

    def _capture_screen(self):
        # Capture the entire screen as a CGImage
        cg_image = CGWindowListCreateImage(
            NSMakeRect(0, 0, 0, 0),
            kCGWindowListOptionOnScreenOnly,
            kCGNullWindowID,
            0
        )

        # Convert CGImage to NSImage
        ns_image = NSImage.alloc().initWithCGImage_size_(cg_image, (0, 0))
        return ns_image

    def drawRect_(self, rect):
        if self.screenshot:
            self.screenshot.drawInRect_(self.bounds())