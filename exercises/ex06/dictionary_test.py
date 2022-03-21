"""Test EX06- Dictionaries."""
___author___ = "730313338"


from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Test invert one time with an empty dict."""
    input_dict: dict[str, str] = {}
    assert invert(input_dict) == {}


def test_invert_two() -> None:
    """Test invert a second time with a normal dict."""
    input_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(input_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_three() -> None:
    """Test invert a third time with a dict."""
    input_dict: dict[str, str] = {'dog': 'hair', 'cat': 'fur', 'fish': 'scales'}
    assert invert(input_dict) == {'hair': 'dog', 'fur': 'cat', 'scales': 'fish'}


def test_favorite_color() -> None:
    """Test favorite color with an empty dict."""
    color_dict: dict[str, str] = {}
    assert favorite_color(color_dict) == ""


def test_favorite_color_two() -> None:
    """Test favorite color with a normal dict."""
    color_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(color_dict) == "blue"


def test_favorite_color_three() -> None:
    """Test favorite color where all colors appear only once."""
    color_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "green"}
    assert favorite_color(color_dict) == "yellow"


def test_count() -> None:
    """Test count with an empty list."""
    input_list: list[str] = ""
    assert count(input_list) == {}


def test_count_two() -> None:
    """Test count with no repeats."""
    input_list: list[str] = "cat", "dog", "bird"
    assert count(input_list) == {"cat": 1, "dog": 1, "bird": 1}


def test_count_three() -> None:
    """Test count with repeat keys."""
    input_list: list[str] = "cat", "dog", "dog"
    assert count(input_list) == {"cat": 1, "dog": 2}