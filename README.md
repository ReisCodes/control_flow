## Control Flow Task 1

```python
user_age = input('''How old are you?
: ''')

if user_age.isalpha() is True:
    print("This is not a number please try again.")
elif int(user_age) > 117 or int(user_age) < 1:
    print("This Age is not within range.")
elif int(user_age) >= 18:
    print("You old enough to watch the all the movies you like!")
elif int(user_age) >= 15:
    print("You are only allowed to watch movies rated U, PG, 12 and 15.")
elif int(user_age) >= 12:
    print("You are only allowed to watch movies rated U, PG, and 12.")
else:
    print("Parental Guidance is advised but you are allowed to watch movies rated U and PG.")
```

When creating a better movie rantings program, using the `.isalpha()` method helps to identify if the user
has used any characters in their input to make them input again.

Casting the user input to `int` data type enables us to use comparison operators 
to determine the users age to display the correct message.

## Control flow task 2
#### Program 1

Within this program using the modulo operator helps us determine if the user input is odd or even
to display them the correct message.

```python
if user_number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")
```

#### Program 2

importing the random module meant we could randomize the number the user tries to guess each time we
run the program `import random`, `number_to_guess = random.randint(1, 20)`.
When creating the actual control using if statements within if statements meant the whole
program could be consolidated into one, also using breaking when the correct answer was given.

Below is the first if statement that shows the logic behind the rest of the program:  

```python
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
```

#### Program 3
Combining a `for` loop with an `if` statement, enables us to iterate through the numbers from 1-100,
again using the modulo operator can check if the number is divisible by 3, 5 or both and 
display the relevant message. 

```python
for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```