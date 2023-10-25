#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Oct/20/2023
# This program generates a random number between 0 and 9 and tells the user if they guessed correctly or not. It also verifies that the user input is valid with a Try Catch.
import random


def main():
    # Declaring my variable for the random number generated by my program.
    random_number = random.randint(0, 9)

    # Getting input from the user as a string.
    user_guess_as_string = input("Enter an integer between 0 & 9: ")

    # Initiating Try Catch.
    try:
        # Converting the user input into an integer.
        user_guess_as_integer = int(user_guess_as_string)
        # If statement for the user guessing correctly.
        if user_guess_as_integer == random_number:
            print("You guessed correctly! The number was {}.".format(random_number))
        # Else statement for the user guessing wrong.
        else:
            print(
                "You guessed incorrectly.The correct number was {}. Please try again.".format(
                    random_number
                )
            )
    # Exception for if the user does not enter a valid integer.
    except:
        print("{} is not a valid integer.".format(user_guess_as_string))
    # Appreciative message for playing my program.
    finally:
        print("Thanks for playing my program!")


if __name__ == "__main__":
    main()
