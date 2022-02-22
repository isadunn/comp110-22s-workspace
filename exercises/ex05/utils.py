"""Ex05- list utility functions."""
__author__ = "730313338"


def only_evens(xs: list[int]) -> list[int]:
    """Construct list of evens, inclusive."""
    result: list[int] = []
    j: int = 0
    while j < len(xs):
        if xs[j] % 2 == 0:
            result.append(xs[j])
        j += 1
    return result  


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Construct list of ints starting at start index and ending at end index, exclusive."""
    result: list[int] = []
    if start < 0: 
        start = 0 
    if end > len(xs):
        end = len(xs) 
    if len(xs) == 0 or start > len(xs) or end <= 0:
        return result       
    while start < end:
        result.append(xs[start])
        start += 1    
    return result     


def concat(first: list[int], second: list[int]) -> list[int]: 
    """Generates a new list from two."""
    result: list[int] = []
    for i in first: 
        result.append(i)
    for i in second:
        result.append(i)
    return result

    