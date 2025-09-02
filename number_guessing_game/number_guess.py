from random import randint
from time import sleep, time

chances = 0
correct_number = randint(1, 100)
given_time = 0

def is_continue(user_choice):
        if user_choice == "y" or user_choice == "Y":
            print("I will think of a different number!")
            return True, randint(1, 100), False
        elif user_choice == "n" or user_choice == "N":
            print("Okay. It was nice meeting you.")
            exit(0)
        else:
            print("Hey, I said no hacking! >:(")
            exit(1)

print("""======== Welcome to the Number Guessing Game ========\n
Just guess the number correctly and you'll win a prize B)
I am thinking of a number between 1 - 100\n""")

sleep(2)

print("""======! Choose Difficulty !=======\n
1. Easy (15 chances)
2. Medium (10 chances)
3. Hard (7 chances)
4. Almost Impossible (3 chance)\n""")


difficulty = input("Choose Difficulty: ")
try:
    difficulty = int(difficulty)
except ValueError:
    print("Please no hack. GET OUT!")
    exit(1)

sleep(1)

match difficulty:
    case 1:
        chances = 15
        sleep(1)
        print("Easy? Baby.\n")
    case 2:
        chances = 10
        sleep(1)
        print("Alright. Medium should not be that hard.\n")
    case 3:
        chances = 7
        sleep(1)
        print("Hard huh. Good luck bro.\n")
    case 4:
        chances = 3
        sleep(1)
        print("Lmao. Let's see how lucky you are.\n")
    case _:
        chances = 0
        sleep(1)
        print("Invalid difficulty selected. Please choose 1, 2, 3, or 4.\n")
        exit(1)

continue_game = True
already_won = False

while continue_game:
    is_guessed = False
    user_guess = 0
    attempt = 0
    t0 = time()
    while not is_guessed and attempt < chances:
        user_guess = input("Enter a guess: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("No hacking bro >:(")
            exit(1)

        if user_guess != correct_number and user_guess < correct_number:
            attempt += 1
            print(f"Incorrect! The number is larger than {user_guess}.\n")
            print(f"You have {chances - attempt} chances left.")
        elif user_guess != correct_number and user_guess > correct_number:
            attempt +=1
            print(f"Incorrect! The number is smaller than {user_guess}.\n")
            print(f"You have {chances - attempt} chances left.")
        elif user_guess == correct_number and not already_won:
            with open("flag.txt", "r", encoding="utf-8") as flag:
                gift = flag.read()
            print(f"Correct! Here is a gift: {gift}\n")
            is_guessed = True
            t1 = time()
            already_won = True
        else:
            print("You won again and already got the flag.")
            is_guessed = True
            t1 = time()

    if is_guessed:
        print(f"Took you {t1 - t0:.2f} seconds to guess this time.\n")
        user_choice = input("Again? (y/n) ")
        continue_game, correct_number, is_guessed = is_continue(user_choice)
    else:
        print("You failed...\n")
        user_choice = input("Again? (y/n) ")
        continue_game, correct_number, is_guessed = is_continue(user_choice)

exit(0)