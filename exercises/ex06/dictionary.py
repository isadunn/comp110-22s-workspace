""""EX06- Dictionaries."""
___author__ = "730313338"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert a given dictionary."""
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in inverted_dict:
            raise KeyError("Key already assigned value.")
        inverted_dict[input_dict[key]] = key
    return(inverted_dict)


def favorite_color(colors_dict: dict[str, str]) -> str:
    """Determine what the most frequent favorite color is within a dictionary."""
    counter_dict: dict[str, int] = {}
    max: int = 0
    color: str = ""
    for key in colors_dict:
        if colors_dict[key] in counter_dict:
            store: int = counter_dict[colors_dict[key]]
            store += 1
            counter_dict[colors_dict[key]] = store
        else: 
            counter_dict[colors_dict[key]] = 1   
    for count in counter_dict: 
        if counter_dict[count] > max: 
            max = counter_dict[count]
            color = count    
    return(color) 


def count(input_list: list[str]) -> dict[str, int]:
    """Counter the number of items in a dictionary."""
    count_dict: dict[str, int] = {}
    value: int = 1
    for item in input_list: 
        if item in count_dict:
            count_dict[item] += 1 
        else:
            count_dict[item] = value 
    return(count_dict)