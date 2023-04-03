# if, elif and else

"""
age = 19

if age > 18:
    print("You are the correct age to buy a ticket for this movie")
elif age < 18:
    print("Sorry, you are not old enough to buy a ticket of this movie")
"""

film_rating = "Reis"

if film_rating.lower() == "universal":
    print("All ages can watch this movie")
elif film_rating.lower() == "pg":
    print("Parental guidance recommended")
elif film_rating.lower() == "12":
    print("You must be at least 12 to watch this movie!")
elif film_rating.lower() == "15":
    print("You must be at least 15 to watch this movie!")
elif film_rating.lower() == "18":
    print("You must be at least 18 to watch this movie!")
else:
    print("This is not a correct rating please use universal, pg, 12, 15 or 18")


