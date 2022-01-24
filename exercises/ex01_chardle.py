"""EX01 - Chardle- A cutte step toward Wordle."""
__author__ = "730313338"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must countain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + word)
instances = 0

if word[0] == single_character:
    instances = instances + 1
    print(single_character + " found at index 0") 
if word[1] == single_character:
    instances = instances + 1
    print(single_character + " found at index 1")
if word[2] == single_character:
    instances = instances + 1
    print(single_character + " found at index 2")
if word[3] == single_character:
    instances = instances + 1
    print(single_character + " found at index 3") 
if word[4] == single_character:
    instances = instances + 1
    print(single_character + " found at index 4")

if instances == 0:
    print(str("No instances of " + single_character + " found in " + word))
if instances == 1:
    print(str(instances) + " instance of " + single_character + " found in " + word)
else:
    print(str(instances) + " instances of " + single_character + " found in " + word)
