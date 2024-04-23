import math
import random


# checks users have entered yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks the users response
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes or No!")


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


# checks for an integer between the inclusive numbers
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is entered
    if low is None and high is None:
        error = "Please enter an Integer!"

    # if the number needs to be more than an integer (rounds)
    elif low is not None and high is None:
        error = f"Please enter an Integer that is more than / equal to {low}"

    # if the number needs to between low & high
    else:
        error = f"Please enter an Integer that is between {low} and {high}"

    while True:
        response = input(question).lower()

        # check for infinite mode or exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return response
            else:
                return response

        except ValueError:
            print(error)


# calculate the maximum guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine Starts here

# Initialize game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("✨✨ Welcome to the Higher Lower Game ✨✨")

print()
want_instructions = yes_no("Do you want to read the instructions?: ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds? (Push <enter> for infinite mode): ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# asks user if they want to customise the number range
print()
default_params = yes_no("Would you like to use the default game parameters?: ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# allow user to choose the high / low number
else:
    low_num = int_check("Low Number?: ")
    high_num = int_check("High Number?: ", low=low_num + 1)

# calculate the maximum number of guesses
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n⭐⭐ Round {rounds_played + 1} (Infinite Mode) ⭐⭐"
    else:
        rounds_heading = f"\n⭐⭐ Round {rounds_played + 1} of {num_rounds} ⭐⭐"

    print(rounds_heading)

    # Round starts here
    # Set guesses used to zero at each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between the low and high number
    secret = random.randint(low_num, high_num)
    # print("Spoiler Alert", secret)

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess the number...
        print()
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check that they don't want to quit
        if guess == "xxx":
            # set end_game to use so that outer loop can be broken
            end_game = "yes"
            break

        # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You've already guessed {guess}!. You've used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

        # if guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        # add one to the number of guesses used
        guesses_used += 1

        # If there's one guess left,
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low, Please try a higher number. "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too high, Please try a lower number. "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")

        # when the secret number is guessed, output feedback
        elif guess == secret:
            if guesses_used == 1:
                feedback = "🎉🎉 Lucky! You got it on the first try. 🎉🎉"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it in {guesses_used} guesses."
            else:
                feedback = f"Well done! You guessed the secret number in {guesses_used} guesses."

        # if there are no guesses left!
        else:
            feedback = "😿😿 Sorry - You ran out of guesses. You lose this round 😿😿"
            guesses_used = guesses_allowed + 1

        # print feedback to user
        print(feedback)

        # Additional Feedback (warn user that they are running out of guesses)
        if guesses_used == guesses_allowed - 1:
            print("💣💣 Careful - You have one guess left! 💣💣")

    # Round ends here

    # if user has entered exit code, end game!!
    if end_game == "yes":
        break

    rounds_played += 1

    # Add round result to game history
    history_feedback = f"Round {rounds_played}: {feedback}"
    game_history.append(history_feedback)

    # add guesses to score list
    all_scores.append(guesses_used)

    # increase rounds if user is in infinite mode
    if mode == "Infinite":
        num_rounds += 1

# Game loop ends here

# check users have played at least one round before calculating statistics
if rounds_played > 0:
    # Game History / Statistics area

    # Calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output the statistics
    print("\n📊📊 Game Statistics 📊📊")
    print(f"Best: {best_score} | Worst: {worst_score} | Average: {average_score:.2f} ")
    print()

    # Display the game history on request
    see_history = yes_no("Do you want to see your game history?: ")
    if see_history == "yes":
        print()
        print("🎮🎮 Game History 🎮🎮")
        for item in game_history:
            print(item)

# End program if user hasn't played a round
else:
    print("😲😲 Oops - You chickened out! 😲😲")
