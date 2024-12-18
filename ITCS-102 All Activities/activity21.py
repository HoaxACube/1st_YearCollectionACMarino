def act5():
    print(" Activity 5 \n")
    temp = int(input("Enter temperature in Fahrenheit: "))
    cel = (temp - 32) * 5 / 9
    cel_r = round(cel, 2)
    print(f"The conversion of {temp} degrees Fahrenhet is {cel_r} degrees celsius.\n")

def act7():
    print("Activity 7\n")
    miner = str(input("Enter you name: "))
    mined = str(input("Did you mine gold today (yes/no) : "))
    gold = 0
    if mined.lower() == "yes":
        gold += 1
        print("Your total mined today is {gold} gold")
    elif mined.lower() == "no":
        print("You havent mined a gold today")
    else:
        print("Invalid")

def act4():
    print("Activity 4 \n")
    number1 = eval(input("Put your first number here > "))
    number2 = eval(input("and your 2nd number here > "))

    add = number1 + number2
    subt = number1 - number2
    product = number1 * number2
    quotient = number1 / number2
    exponent = number1 ** number2
    remainder = number1 % number2
    fldivision = number1 // number2
    print("The sum of" , number1 , "and" , number2 , "is" , add)
    print("The difference of" , number1 , "and" , number2 , "is" , subt)
    print("The product of" , number1 , "and" , number2 , "is" , product)
    print("The quotient of" , number1 , "and" , number2 , "is" , quotient)
    print("The exponent by" , number2 , "is" , exponent)
    print("The remainder of" , number1 , "and" , number2 , "is" , remainder)

while True:
    select = input("Choose the option of Functions [1/2/3] type 'stop' if done: ")

    if select == "1":
        act5()
        continue
    elif select == "2":
        act7()
        continue
    elif select == "3":
        act4()
        continue
    elif select.lower() == "stop":
        print("System Stopped")
        break
    else:
        print("Invalid choice")