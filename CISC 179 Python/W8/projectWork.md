# Task A. Number Guesser (1-100)
```python
#Defining func & param
def guessNumber(low=1, high=100):
    print(f"Think of a number between {low} and {high}!\n")

    # step counter
    steps = 0

    # while loop to search for number guessed
    while low <= high:
        # incrementing step counter
        steps += 1
        # guess calculation
        guess = (low + high) // 2
        # User prompts for input
        print(f"Is your number greater (>), equal (=), or less (<) than {guess}?")
        answer = input("Please answer (<, =, >): ")

        # Validate the input
        if answer not in ['<', '=', '>']:
            print("Invalid input, please enter <, =, or >")
            continue

        # Process the answer
        if answer == '=':
            print("\nI have guessed it!")
            print(f"It took {steps} steps!")
            return
        elif answer == '>':
            low = guess + 1
        elif answer == '<':
            high = guess - 1

    # inconsistency handling
    print("The information you provided is inconsistent.")


# call function, can comment out to test bellow ranges
guessNumber()

# range modification for -10 and +10
guessNumber(-10, 10)

```
# Task B. Number (1-100) & Letter Guesser 
```python
#Defining func & param
def guessNumberOrCharacter(low=1, high=100):
    # user prompt for number of character
    choice = input("Enter 'n' if thinking of a number or 'c' if thinking of a character:  ").lower()

    # number guessing
    if choice == 'n':
        print(f"Think of a number between {low} and {high}!\n")

        steps = 0
        while low <= high:
            steps += 1
            guess = (low + high) // 2
            print(f"Is your number greater (>), equal (=), or less (<) than {guess}?")
            answer = input("Please answer (<, =, >): ")

            if answer not in ['<', '=', '>']:
                print("Invalid input, please enter <, =, or >")
                continue

            if answer == '=':
                print(f"\nI have guessed it!")
                print(f"It took {steps} steps!")
                return
            elif answer == '>':
                low = guess + 1
            elif answer == '<':
                high = guess - 1

        print("The information you provided is inconsistent.")

    # character guessing
    elif choice == 'c':
        print(f"Think of a character between A-Z or a-z!\n")

        # setting low and high ranges using ASCII values to handle lower and upper case characters
        low, high = ord('A'), ord('z')
        steps = 0
        guessChar = 'M'

        # binary search loop for characters
        while low <= high:
            steps += 1
            if steps == 1:
                guessChar = 'M'
            else:
                guess = (low + high) // 2
                # convert ASCII value back to a character
                guessChar = chr(guess)

            # user prompt for comparison
            print(f"Is your character after (>), equal (=), or before (<) than the letter {guessChar}?")
            answer = input("Please answer (<, =, >): ")

            # input validation
            if answer not in ['<', '=', '>']:
                print("Invalid input, please enter <, =, or >")
                continue

            # user input handling
            if answer == '=':
                print(f"\nI have guessed your character!")
                print(f"It took {steps} steps!")
                return
            # handling for smaller character
            elif answer == '>':
                low = ord(guessChar) + 1
            # handling for larger character
            elif answer == '<':
                high = ord(guessChar) - 1

        print("The information you provided is inconsistent.")

    else:
        print("Invalid choice! Please enter 'n' for number or 'c' for character.")
        return 
# Call the function
guessNumberOrCharacter()

```
