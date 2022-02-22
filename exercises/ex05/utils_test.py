"""Ex05- testing list utility functions."""
__author__ = "730313338"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_two() -> None: 
    xs: list[int] = [1]
    assert only_evens(xs) == []


def test_only_evens_three() -> None: 
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_only_evens_four() -> None: 
    xs: list[int] = [10, 20, 30, 40, 50]
    assert only_evens(xs) == [10, 20, 30, 40, 50]    


def test_sub() -> None:
    xs: list[int] = []
    start: int = 0
    end: int = 2
    assert sub(xs, start, end) == []


def test_sub_two() -> None:
    xs: list[int] = [0, 1, 2, 3, 4, 5]
    start: int = 1
    end: int = 3
    assert sub(xs, start, end) == [1, 2]


def test_sub_three() -> None:
    xs: list[int] = [0, 1, 2, 3, 4]
    start: int = 1
    end: int = 7
    assert sub(xs, start, end) == [1, 2, 3, 4]


def test_sub_four() -> None: 
    xs: list[int] = [-3, -2, -1, 0, 1, 2, 3, 4]
    start: int = 1
    end: int = 4
    assert sub(xs, start, end) == [-2, -1, 0]


def test_concat() -> None:
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second) == []


def test_concat_two() -> None:
    first: list[int] = [1, 2, 3]
    second: list[int] = [1, 2, 3]
    assert concat(first, second) == [1, 2, 3, 1, 2, 3]


def test_concat_three() -> None:
    first: list[int] = []
    second: list[int] = [1, 2, 3]
    assert concat(first, second) == [1, 2, 3]


def test_concat_four() -> None:
    first: list[int] = [10, 20, 30]
    second: list[int] = []
    assert concat(first, second) == [10, 20, 30]