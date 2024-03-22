"""EX05 - Dictionary Utility Functions."""


__author__ = "730665579"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverting Dict."""
    inverted_dict: dict[str, str] = {}
    for key in dictionary:
        value = dictionary[key]
        if value in inverted_dict:
            raise KeyError("Duplicate value found when inverting dictionary")
        inverted_dict[value] = key
    return inverted_dict
        

def favorite_color(dictionary: dict[str, str]) -> str:
    """Finding fav color."""
    color_count = {}
    for name in dictionary:
        color = dictionary[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_count = 0
    most_popular_color = None
    for color in color_count:
        count = color_count[color]
        if count > max_count or (count == max_count and most_popular_color is None):
            most_popular_color = color
            max_count = count
    
    return most_popular_color


def count(values_list: list[str]) -> dict[str, list[str]]:
    """Counting vals."""
    count_dict = {}
    for item in values_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def update_attendance(attendance_dict, day_of_week, student):
    if day_of_week in attendance_dict:
        attendance_dict[day_of_week].append(student)
    else:
        attendance_dict[day_of_week] = [student]