

for numbers in range(1, 101):
    if numbers % 3 == 0:
        print("Fizz")
    if numbers % 5 == 0:
        print("Buzz")
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
