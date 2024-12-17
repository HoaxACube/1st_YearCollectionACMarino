print("Activity 13 \n")
number = int(input("Enter any number: "))
factorial = 1
for factor in range(number, 0, -1):
    factorial *= factor 
    rounded = round(factorial, 2)
print(f"The factorial of {rounded}\n")