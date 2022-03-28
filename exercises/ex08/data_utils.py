"""Dictionary related utility functions for EX08."""

__author__ = "730313338"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read and entire CSV of data into a list of rows, reach row represented as a dict."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)
    
    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result   


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]: 
    """Visualize first few rows of data."""
    result: dict[str, list[str]] = {} 
    for column in column_table: 
        values: list[str] = []
        i: int = 0
        if N >= len(column_table[column]): 
            values = column_table[column]
        else:
            while i < N: 
                values.append(column_table[column][i])
                i += 1    
        result[column] = values
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]: 
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result    


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result    


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with a speicfic subset."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = column_table[column]
    return result     


def count(values: list[str]) -> dict[str, int]:
    """Produce a dict where each key is unique value in given list, assosicated with the count."""
    result: dict[str, int] = {}
    for item in values: 
        if item in result: 
            result[item] += 1 
        else: 
            result[item] = 1 
    return result


def helper(prior_exp: list[str], difficulty: list[str]) -> None:
    """Produce a list where each item is a student who answered a speficic level of experince, then find the average."""
    i: int = 0 
    none: int = 0
    some: int = 0
    average_none: float = 0.0
    average_some: float = 0.0
    while i < len(prior_exp): 
        if prior_exp[i] == "None to less than one month!":
            none += 1
            average_none += int(difficulty[i])
        else: 
            some += 1
            average_some += int(difficulty[i])
        i += 1
    print(f"Students with no prior experience: {none}.")
    print(f"Students with some prior experince: {some}.") 
    average_none /= none
    average_some /= some
    print(f"Averaged percieved difficulty for students with no prior experience: {average_none}.")
    print(f"Averaged percieved difficulty for students with some prior experience: {average_some}.")
    return None