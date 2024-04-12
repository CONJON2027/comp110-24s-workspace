"""Challenge Question Number eight."""

from __future__ import annotations


class Point:
    """Class to make a new point."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """The innital x and y values."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scaling the points up by a factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creating a new point."""
        x: float = self.x * factor
        y: float = self.y * factor
        my_point: Point = Point(x, y)
        return my_point