"""Example of a function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))

# define a functin named containes 
#  two paramaters
# 1: needle- the string were searching for 
# 2: haystack - the list were searching through
# for each item in haystack 
#   test if it is equal to the needle 
#       if so, return true
#  after testing all items, return false, because not found
# returns true if needle in haystack, false otherwise


def contains(needle: str, haystack: list[str]) -> bool:
    """Searching for needle within haystack."""
    for item in haystack:
        if item == needle:
            return True 
    # i: int == 0 
    # while i < len(haystack)
    #     if i = needle:
    #         return True 
    #     else:
    #         i += 1
    return False


# in order to be able to run function as both a module and be able to call / import the functions in globals frame anywhere
if __name__ == "__main__":
    main()
else: 
    print(__name__)