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


