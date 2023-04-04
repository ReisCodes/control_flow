for i in range(10):
    print("Hello!")

list_names = []
for x in range(3):
    user_input = input("Whats your name? ")
    if user_input.isalpha():
        list_names.append(user_input)
    else:
        print("This is not a name!")

list_names_lower = []
for name in list_names:
    list_names_lower.append(name.lower())

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in values:
    if num % 2 == 0:
        print(f"This number, {num} is even")

number_sum = 0
for i in range(0, 101):
    number_sum += i

print(number_sum)

even_sum = 0
odd_sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(even_sum)
print(odd_sum)

user_numbers = []
user_numbers_sum = 0
while len(user_numbers) < 10:
    num_collected = input("Give me a number: ")
    if num_collected.isdigit():
        user_numbers.append(int(num_collected))
    else:
        print("This is not a number, try again")

for number in user_numbers:
    user_numbers_sum += number

print(user_numbers_sum / len(user_numbers))

x = 0
while x <= 300:
    x += 1
    if x % 10 == 0:
        print(x)

list_of_numbers = []
sum_of_even = 0
sum_of_odd = 0
while True:
    user_num = input("Give me a number: ")
    if int(user_num) == 0:
        for number in list_of_numbers:
            if number % 2 == 0:
                sum_of_even += number
            else:
                sum_of_odd += number
        print(f"The sum of your even numbers is: {sum_of_even}")
        print(f"The sum of your odd numbers is: {sum_of_odd}")
        break
    elif user_num.isdigit():
        list_of_numbers.append(int(user_num))
        print(list_of_numbers)
    else:
        print("This is not a number, please try again.")
