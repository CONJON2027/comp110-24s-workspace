"""Splitting a dictionary into two lists."""


__author__ = "730665579"


def get_keys(list: dict[str, int]) -> list[str]:
    """Spliting into list."""
    output = []
    for key in list:
        output.append(key)
    return output


def get_values(list: dict[str, int]) -> list[int]:
    """Spliting into list."""
    output = []
    for key in list:
        output.append(list[key])
    return output