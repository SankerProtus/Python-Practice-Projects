import random
print("welcome to the number guessing game!".title())
print("I'm thinking about a number between 1 and 100.")
easy_attempts = 8
medium_attempts = 5
hard_attempts = 3
computer_guess = random.randint(1, 100)
# print(f"computer's guess is {computer_guess}")


def compare(c_guess, u_guess, turns):
    if c_guess > u_guess:
        print("Too low")
        return turns - 1
    elif c_guess < u_guess:
        print("Too high")
        return turns - 1
    else:
        print(f"You got it! The answer is {computer_guess}")


def level():
    game_level = input("Choose a difficulty: Type 'easy' or 'medium' or 'hard': ").lower()
    if game_level == "easy":
        return easy_attempts
    elif game_level == "medium":
        return medium_attempts
    elif game_level == "hard":
        return hard_attempts
    else:
        print("Invalid game level selected. Try again.")
        exit()


number_guess = level()
user_guess = 0
while computer_guess != user_guess:
    print(f"    You have {number_guess} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    number_guess = (compare(computer_guess, user_guess, number_guess))
    if number_guess == 0:
        print(f"    You've run out of live. Game over!!")
        exit()
