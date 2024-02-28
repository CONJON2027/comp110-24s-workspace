"""Summing the elements of a list using different loops."""


__author__ = "730665579"


def w_sum(vals: list[float]) -> float:
    """Func 1."""
    index = 0
    number: float = 0.0
    while index < len(vals):
        number += vals[index] 
        index += 1
    return number


def f_sum(vals: list[float]) -> float:
    """Func 2."""
    number: float = 0.0
    for i in vals:
        number = i + number
    return number


def f_range_sum(vals: list[float]) -> float:
    """Func 1."""
    number: float = 0.0
    for i in range(0, len(vals)):
        number = vals[i] + number
    return number