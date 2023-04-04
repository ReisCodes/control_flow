# Loops

list_data = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Reis",
        "money": "£0.05"},
    2: {"name": "Luke",
        "money": "£3.66"},
    3: {"name": "James",
        "money": "£1.14"}
}

# Basic Loop
# for num in list_data:
#    print(num * 2)

# Nested loops
"""
for data in embedded_list:
    for num in data:
        print(num)
"""
# Looping through dictionaries
"""
for value in dict_data.values():
    print(value)

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

for value in dict_data.values():
    print(value["money"])
"""

for num in list_data:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print("Ive gone to far")
    else:
        print("Too Soon!")

# While loop

# while loop manages a condition

x = 0

while x < 10:
    print(f"It's working  -> {x}")
    if x == 4:
        break
    x += 1    # Incrementer

# using while loops to verify user input

while True:
    age = input("What is your age? ")
    if age.isdigit() and 0 < int(age) < 117:
        break
    else:
        print("please provide your age in digits")

print(f"Your age is {age}")

