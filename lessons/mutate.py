"""Mutating functions.""" 


__author__ = '730665579'


def manual_append(x: list[int], y: int) -> None:
    """Append."""
    x.append(y)


def double(x: list[int]) -> None:
    """Double."""
    count = 0
    while len(x) > count:
        x[count] *= 2
        count += 1
