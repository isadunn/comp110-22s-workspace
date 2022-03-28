"""Dictionary related utility functions."""

__author__ = "730313338"

# Define your functions below
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


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with a speicfic subset."""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = column_table[column]
    return result 


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Prorduce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in first: 
        result[column] = first[column]
    for column in second: 
        if column in result: 
            result[column] += second[column]
        else: 
            result[column] = second[column]    
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