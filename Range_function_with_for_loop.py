# Range function with for loop

for number in range (1, 101, ):
    print(number)


# The Gauss Challenge
total = 0
for number in range (1, 101):
    total += number
print(total)


for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)