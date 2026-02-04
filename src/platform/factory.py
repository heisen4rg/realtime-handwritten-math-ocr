import sys
from core.selector import ScreenRegionSelector

class _StubSelector(ScreenRegionSelector):
    def select(self):
        return (0, 0, 100, 100)

def get_selector() -> ScreenRegionSelector:
    if sys.platform == "darwin":
        return _StubSelector()
    elif sys.platform == "win32":
        return _StubSelector()
    else:
        return _StubSelector()