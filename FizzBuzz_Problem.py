n = int(input("enter a single Integer: "))

if (n % 3 == 0) and (n % 5 == 0):
    print("FizzBuzz")

elif (n % 3 == 0):
    print("Fizz")
elif (n % 5 == 0):
    print("Buzz")
else:
    print("Not a FizzBuzz Number.")