"""Example of looping through all characters in a string."""

user_string: str = input("GIVE ME A STRING HOE ! ")

# the variable i is a common counter varaible name in programming, short for iteration. 

i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

print("youre done. youre done.")