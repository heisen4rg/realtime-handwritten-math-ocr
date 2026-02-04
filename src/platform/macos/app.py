import sys
from AppKit import (
    NSApplication,
    NSApp,
    NSWindow,
    NSWindowStyleMaskBorderless,
    NSScreen,
    NSBackingStoreBuffered,
    NSColor,
    NSEventMaskKeyDown,
    NSEvent,
)
from Foundation import NSObject
from Quartz import CGEventCreateKeyboardEvent, CGEventPost, kCGHIDEventTap
from src.platform.macos.window import ScreenshotView


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        self.window = self._create_fullscreen_window()

        view = ScreenshotView.alloc().initWithFrame_(
            self.window.contentView().bounds()
        )
        self.window.setContentView_(view)

        self.window.makeKeyAndOrderFront_(None)

        NSEvent.addLocalMonitorForEventsMatchingMask_handler_(
            NSEventMaskKeyDown, self._handle_key_event
        )

    def _create_fullscreen_window(self):
        screen = NSScreen.mainScreen()
        frame = screen.frame()

        window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            frame,
            NSWindowStyleMaskBorderless,
            NSBackingStoreBuffered,
            False,
        )

        window.setLevel_(NSScreenSaverWindowLevel := 1000)
        window.setOpaque_(False)
        window.setBackgroundColor_(NSColor.clearColor())
        window.setIgnoresMouseEvents_(False)
        window.setReleasedWhenClosed_(False)

        return window

    def _handle_key_event(self, event):
        # ESC key code = 53
        if event.keyCode() == 53:
            NSApp().terminate_(None)
            return None
        return event


def run_app():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)
    app.run()


if __name__ == "__main__":
    run_app()