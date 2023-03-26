number1 = int(input("please input the original number: "))
number2 = int(input("please input the number for checking: "))

if (number1 % number2 == 0):
    print(number1, "can be fully divided by", number2, "directly!")
    print(number1, "/", number2, "=", int(number1/number2))
    print("\U0001F602")
else:
    print(number1, "cannot be fully divided by", number2, "directly!")
    print(number1, "/", number2, "=", number1//number2, "*", number2, "+", number1%number2)
    print("\U0001F62A")