"""Excersize03- Wordle."""
__author__ = "730313338"


# from exercises.ex02_one_shot_wordle import GREEN_BOX


def contains_char(secret: str, letter: str) -> bool:
    """searches for single ch guess found within secret word in loop.""" 
    i: int = 0
    assert len(letter) == 1
    while i < len(secret):
        if letter == secret[i]:
            return True
        # yellow
        i += 1     
    return False
    #  white


def emojified(guess: str, secret: str) -> str: 
    """compares guess to secret word ."""
    i: int = 0
    j: int = 0
    result: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    while j < len(secret):
        flag: bool = contains_char(secret, guess[i])
        if flag:
            if guess[i] == secret[i]:
                result += GREEN_BOX
            else:   
                result += YELLOW_BOX
        else: 
            result += WHITE_BOX
        i += 1
        j += 1
    return result


def input_guess(expected_length: int) -> str: 
    """prompts user for guess, keeps prompting until guess is right length."""
    guess: str = input("Enter a " + str(expected_length) + " character word: ")
    while(len(guess) != expected_length):
        guess: str = input("That wasn't " + str(expected_length) + " chars! Try again:")
    return guess


def main() -> None:
    GREEN_BOX: str = "\U0001F7E9"
    holder: str = GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX
    secret: str = "codes"
    i: int = 1
    while(i <= len(secret)):
        print("=== Turn " + str(i) + "/6 ===")
        guess: str = input_guess(len(secret))
        result: str = emojified(secret, guess)
        print(result)

        if result == holder:
            print("You won in " + str(i) + "/6 turns!")
            i = len(secret) + 1
        i += 1
    print("X/6- Sorry, try again tomorrow!")    
    

if __name__ == "__main__":
    main()    