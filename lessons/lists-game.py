"""Examples of using lists in a sample 'game'."""


from random import randint 

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)    

# remove an ittem from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# sum the values of our rolls
i: int = 0
sum: int = 0 
while i < len(rolls):
    sum = sum + rolls[i]
    i += 1

print(f"Total Score: {sum}")

# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# rolls.append(randint (1,6))
# print(rolls)

# # access an indivual item 
# print(rolls[0])

# # access the length of a list (number of items)
# print(len(rolls))

# # access last item of a list 
# # print(rolls[len(rolls) -1])
# last_index: int = len(rolls) - 1
# print(rolls[last_index])