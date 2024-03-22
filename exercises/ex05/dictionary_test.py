"""EX05 - Dictionary Utility Functions Tests."""


__author__ = "730665579"


from exercises.ex05.dictionary import invert, count, favorite_color, alphabetizer, update_attendance


def test_invert_edge():
    """Edge case test for invert() function."""
    try:
        invert({"Alice": "Blue", "Bob": "Red", "Charlie": "Blue"})
    except KeyError:
        print("Edge case test passed for invert()")
    else:
        print("Edge case test failed for invert()")


def test_invert_normal_1():
    """Normal case 1 test for invert() function."""
    assert invert({"Alice": "Blue", "Bob": "Red", "Charlie": "Green"}) == {"Blue": "Alice", "Red": "Bob", "Green": "Charlie"}
    print("Normal case 1 test passed for invert()")


def test_invert_normal_2():
    """Normal case 2 test for invert() function."""
    assert invert({"John": "Yellow", "Doe": "Green", "Jane": "Red"}) == {"Yellow": "John", "Green": "Doe", "Red": "Jane"}
    print("Normal case 2 test passed for invert()")


def test_favorite_color_normal_1():
    """Normal case 1 test for favorite_color() function."""
    assert favorite_color({"Alice": "Blue", "Bob": "Red", "Charlie": "Blue"}) == "Blue"
    print("Normal case 1 test passed for favorite_color()")


def test_favorite_color_normal_2():
    """Normal case 2 test for favorite_color() function."""
    assert favorite_color({"John": "Green", "Doe": "Green", "Jane": "Red"}) == "Green"
    print("Normal case 2 test passed for favorite_color()")


def test_favorite_color_edge():
    """Edge case test for favorite_color() function."""
    assert favorite_color({}) == ""
    print("Edge case test passed for favorite_color()")


def test_alphabetizer_edge():
    """Edge case test for alphabetizer() function."""
    assert alphabetizer([]) == {}
    print("Edge case test passed for alphabetizer()")


def test_alphabetizer_normal_1():
    """Normal case 1 test for alphabetizer() function."""
    assert alphabetizer(["Apple", "Banana", "Apricot", "Cherry", "Avocado"]) == {'a': ['Apple', 'Apricot', 'Avocado'], 'b': ['Banana'], 'c': ['Cherry']}
    print("Normal case 1 test passed for alphabetizer()")


def test_alphabetizer_normal_2():
    """Normal case 2 test for alphabetizer() function."""
    assert alphabetizer(["Elephant", "Eagle", "Emu", "Giraffe"]) == {'e': ['Elephant', 'Eagle', 'Emu'], 'g': ['Giraffe']}
    print("Normal case 2 test passed for alphabetizer()")


def test_count_normal_1():
    """Normal case 1 test for count() function."""
    assert count(["apple", "banana", "apple", "cherry", "banana", "apple"]) == {"apple": 3, "banana": 2, "cherry": 1}
    print("Normal case 1 test passed for count()")


def test_count_normal_2():
    """Normal case 2 test for count() function."""
    assert count(["apple", "banana", "banana", "banana", "cherry", "cherry", "cherry"]) == {"apple": 1, "banana": 3, "cherry": 3}
    print("Normal case 2 test passed for count()")


def test_count_edge():
    """Edge case test for count() function."""
    assert count([]) == {}
    print("Edge case test passed for count()")


def test_update_attendance_normal_1():
    """Normal case 1 test for update_attendance() function."""
    attendance_dict = {"Monday": ["Alice", "Alice"], "Tuesday": ["Charlie"]}
    update_attendance(attendance_dict, "Monday", "David")
    assert attendance_dict == {"Monday": ["Alice", "Alice", "David"], "Tuesday": ["Charlie"]}
    print("Normal case 1 test passed for update_attendance()")


def test_update_attendance_normal_2():
    """Normal case 2 test for update_attendance() function."""
    attendance_dict = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
    update_attendance(attendance_dict, "Tuesday", "David")
    assert attendance_dict == {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie", "David"]}
    print("Normal case 2 test passed for update_attendance()")


def test_update_attendance_edge():
    """Edge case test for update_attendance() function."""
    attendance_dict = {}
    update_attendance(attendance_dict, "Monday", "Alice")
    assert attendance_dict == {"Monday": ["Alice"]}
    print("Edge case test passed for update_attendance()")