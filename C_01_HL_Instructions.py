# checks users have entered yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes or No")


def instruction():
    print('''
✦✦✦ Instructions ✦✦✦

To begin with, choose the number of desired rounds, pressing <enter> for 
infinite mode.

Next, either customize the game parameters or choose the default option
(the secret number will be between 1 and 100).

Your goal is to guess the secret number without running out of guesses. 

Have fun!
    ''')


# Main routine
print("✨ Welcome to the Higher Lower Game ✨")

# loop for testing purposes
print()
want_instructions = yes_no("Do you want to read the instructions?: ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
