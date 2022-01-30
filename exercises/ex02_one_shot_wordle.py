"""Excersize02- one shot wordle"""
"___730313338__" 
 
#  defining global variables:
guess: str = input("What is your 6-letter guess?")
i: int = 0
correct_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result: str = ""

# checking for length
while len(guess) != len(correct_word):
    guess: str = input("That was not" + str(len(correct_word)) + " letters! Try Again: ")   
        
# checking indices for correct characters / positions against correct word via loop
while i < len(correct_word):
    if guess[i] == correct_word[i]:
        result = result + GREEN_BOX
    else:
        secret_word: bool = False 
        j: int = 0
        while not secret_word and j < len(correct_word):
            if correct_word[j] == guess[i]:
                secret_word = True
            else:
                j += 1
                
        if secret_word:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX   
    i = i + 1

# printing input
print(result)
if guess == correct_word:
    print("Woo! You got it!") 
else: 
    print("Not quite. Play again soon!")    
