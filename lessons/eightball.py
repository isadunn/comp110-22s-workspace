"""A magic 8 ball orcal of truth about the future."""

from random import randint

input("Ask a yes or no question: ")

response: int = randint(0, 3)

# if response == 0: 
#     print("Yes, definitiely!!!!!")
# else:
#     if response == 1: 
#         print("looking hopeful. ")
#     else:
#         if response == 2: 
#             print("Ask again later") 
#         else:
#             print("No way. Not a chance. ")

if response == 0:
    print("yes, definitely!!")
elif response == 1:
    print("looking hopeful")
elif response == 2: 
    print("ask again later")
else: 
    print("no way")
