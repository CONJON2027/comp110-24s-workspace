"""EX04 - List Utility Functions."""


def all(vals: list[int], number: int) -> bool:
    """Sees if they are the same."""
    if not vals:
        return False
    TorF = []
    for i in vals:
        TorF.append(i == number)
    count_true = 0
    for i in TorF:
        if i or len(vals) < 1:
            count_true += 1
    return count_true == len(vals)
    

def max(vals: list[int]) -> int:
    """Finds the Max."""
    if len(vals) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_val = vals[0]
    for i in vals[1:]:
        if i > max_val:
            max_val = i
    return max_val


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Evaluates if the lists are the same."""
    if not list1 and not list2:
        return True
    elif not list1 or not list2:
        return False

    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Puts list one and two together."""
    for i in list2:
        list1.append(i)
