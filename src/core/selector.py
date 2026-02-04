from typing import Tuple

BBox = Tuple[int, int, int, int]

class ScreenRegionSelector:
    def select(self) -> BBox:
        """
        Launches an interactive selection UI and blocks
        until the user completes the selection.

        Returns:
            (x1, y1, x2, y2) in absolute screen coordinates
        """
        raise NotImplementedError