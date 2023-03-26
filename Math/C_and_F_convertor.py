# Purpose: convert between Degree Celsius (c) to Degree Fahrenheit (f)
# Formular: 
#    f = c * 9 / 5 + 32
#    c = (f - 32) * 5 / 9
# Author: Yichen Zhao
# Date: 2023-03-06
# Version: 1.0

print("Please tell me what you want to convert to: (C or F)")

choice = input()

if choice == "c":
    f_degree = float(input("Please tell me the degree Fahrenheit:"))
    print("The degree Fahrenheit you input is ", f_degree)
    print("The converted degree Celsius is:", (f_degree - 32) * 5 / 9)
elif choice == "f":
    c_degree = float(input("Please tell me the degree Celsius:"))
    print("The degree Celsius you input is ", c_degree)
    print("The converted degree Fahrenheit is:", c_degree * 9 / 5 + 32)
else:
    print("Sorry, that's not a option, please try again.")