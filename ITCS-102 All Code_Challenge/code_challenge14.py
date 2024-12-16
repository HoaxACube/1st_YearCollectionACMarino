tuloy = True
a = 0
while tuloy == True:
    num = eval(input("Enter a number--->  "))
    if num == 0:
        print("Program Terminated")
        print(f"The total amount entered is {a}")
        break

    else:
        a += num
        continue
