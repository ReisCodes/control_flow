import random

user_number = int(input('''Give me a number, ANY number!
 : '''))

if user_number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")

number_to_guess = random.randint(1, 20)


user_guess = int(input('''Guess the number i have chosen between 1-20!
: '''))

if user_guess > 20 or user_guess < 1:
    print("This number is not between 1-20! try again")
    user_guess = int(input(": "))
    if user_guess > 20 or user_guess < 1:
        print("This number is not between 1-20! try again")
        user_guess = int(input(": "))
        if user_guess == number_to_guess:
            print("Well done you got it right!")
        else:
            print("Unlucky maybe next time!")
    elif user_guess > number_to_guess:
        print("you guessed a little high try again!")
        user_guess = int(input(": "))
        if user_guess == number_to_guess:
            print("Well done you got it right!")
        else:
            print("Unlucky maybe next time!")
    elif user_guess < number_to_guess:
        print("you guessed a little low try again!")
        user_guess = int(input(": "))
        if user_guess == number_to_guess:
            print("Well done you got it right!")
        else:
            print("Unlucky maybe next time!")
    elif user_guess == number_to_guess:
        print("Well done! you got it right!")
elif user_guess > number_to_guess:
    print("you guessed a little high try again!")
    user_guess = int(input(": "))
    if user_guess > 20 or user_guess < 1:
        print("This number is not between 1-20! try again")
        user_guess = int(input(": "))
        if user_guess == number_to_guess:
            print("Well done you got it right!")
        else:
            print("Unlucky maybe next time!")
    elif user_guess > number_to_guess:
        print("you guessed a little high try again!")
        user_guess = int(input(": "))
        if user_guess == number_to_guess:
            print("Well done you got it right!")
        else:
            print("Unlucky maybe next time!")
    elif user_guess < number_to_guess:
        print("you guessed a little low try again!")
        user_guess = int(input(": "))
        if user_guess == number_to_guess:
            print("Well done you got it right!")
        else:
            print("Unlucky maybe next time!")
    elif user_guess == number_to_guess:
        print("Well done! you got it right!")
elif user_guess < number_to_guess:
    print("you guessed a little low try again!")
    user_guess = int(input(": "))
    if user_guess > 20 or user_guess < 1:
        print("This number is not between 1-20! try again")
        user_guess = int(input(": "))
        if user_guess == number_to_guess:
            print("Well done you got it right!")
        else:
            print("Unlucky maybe next time!")
    elif user_guess > number_to_guess:
        print("you guessed a little high try again!")
        user_guess = int(input(": "))
        if user_guess == number_to_guess:
            print("Well done you got it right!")
        else:
            print("Unlucky maybe next time!")
    elif user_guess < number_to_guess:
        print("you guessed a little low try again!")
        user_guess = int(input(": "))
        if user_guess == number_to_guess:
            print("Well done you got it right!")
        else:
            print("Unlucky maybe next time!")
    elif user_guess == number_to_guess:
        print("Well done! you got it right!")
elif user_guess == number_to_guess:
    print("Well done! you got it right!")

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
