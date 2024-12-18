def act1():
    print("             Activity 1             __")
    print("**                                   |")
    print("*         |Typing test SCORE|         ")
    print("      5 Minutes Typing Test: Score    ")
    print("      44 WPM is with 93% ACCURACY    *")
    print("|__                                 **")

#=====================================================
def act2():
    print("Activity 2")
    name = input("Pease input a name ---->")
    print("Hello", name)

#=====================================================
def act3():
    input("\t\t We will be collecting your Biodata, please note that your information will be confidential and protected \n\n\t\t Type anything to proceed . . . ")

    name = input("----------------------- Fill up the form -----------------------\n\t Name:")
    mobile = input("\n\t Mobile No. : ")
    email = input("\n\t Email: ")
    gender = input("\n\t Gender: ")
    guardian = input("\n\t Guardian Name: ")
    siblings = input("\n\t Siblings Count: ")
    address = input("\n\t Address: ")
    birth = input("\n\t Date of Birth: ")
    age = input("\n\t Age: ")
    education = input("\n\t Education: ")
    course = input("\n\t Course Department: ")
    marital = input("\n\t Marital Status: ")
    religion = input("\n\t Religion: ")
    language = input("\n\t Language(s) Known: ")
    hobby = input("\n\t Hobbies: ")

    print("\n------------------------------- Here's the summary of your form -------------------------------\n\n\t\t" + "It is stated that your name is " + name + ". You can be contacted with this mobile number " + mobile + ". You'll be receiving emails at " + email + ". Your gender is " + gender + ". We can contact your guardian Mr/Ms." +  guardian + ". There are " +  siblings + " of your siblings. You live in " + address + ". Your education level is " +  education + ". You have chosen the course of " +  course + " Department. Your civil status is " +  marital + ". Your religion is " +  religion + ". You know the language(s) of " +  language + ". You like to do some " +  hobby + " as a hobby. " + "\n\n----------------------- Thanks for completing the form! Have a good day! -----------------------\n\t\t")

#=====================================================
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
    print("The floor division of" , number1 , "and" , number2 , "is" , fldivision, "\n" ,)

#=====================================================
def act5():
    print(" Activity 5 \n")
    temp = int(input("Enter temperature in Fahrenheit: "))
    cel = (temp - 32) * 5 / 9
    cel_r = round(cel, 2)
    print(f"The conversion of {temp} degrees Fahrenhet is {cel_r} degrees celsius.\n")

#=====================================================
def act6():
    print(" Activity 6 \n")

    x = eval(input("Put a number: "))
    print(x)
    x = x + 10
    print(x)
    x = x + 15
    print(x)
    x = x + 20
    print(x)
    x = x + 25


#=====================================================
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

#=====================================================
def act8():
    print("Activity 8\n")

    password= input("Enter Password: ") 
    if password.lower() == "hello":
        print("Password Entered, you may now proceed.")
    else:
        print("Invalid Password")

#=====================================================
def act9():
    print("Activity 9\n")

    age = eval(input("Enter your age: "))
    if age <= 1:
        print("You are a Toddler\n")
    elif age <= 8:
        print("You are a Pre-teen\n")
    elif age <= 14: 
        print("You are Teenager\n")
    elif age <= 19:
        print("You are in Early adulthood\n")
    elif age <= 32:
        print("You are in Mid adulthood\n")
    elif age <= 46:
        print("You are in Post adulthood\n")
    elif age <= 60:
        print("You are in your Senior\n")
    elif age >= 120:
        print("Exceeded age limit\n")
    else:
        print("Invalid syntax\n")

#=====================================================
def act10():
    print("ACTIVITY 10\n")

    dll = str(input("Are you a current student from DLL? (yes/no): "))
    if dll.lower() == "yes":
        print("\nWelcome to DLL BSIT scholarship\n")
        location = str(input("Are from Barangay 9 (yes/no): "))
        if location.lower() == "yes":
            print("Please fill up the additional information")
            year = str(input("What is your current year in DLL (f = freshmen)(p = sophomore)(j = Junior)(s = senior): "))
            if year.lower() == "f":
                print("Hi Freshmen")
            elif year.lower() == "p":
                print("Hi sophomore")
            elif year.lower() == "j":
                print("Hi junior")
            elif year.lower() == "s":
                print("Hi senior")
            else:
                print("Invalid choice")
            choice = str(input("Do you need scholarship (yes/no): "))
            if choice.lower() == "yes":
                print("You been granted a scholarship\n")
            else:
                print("You choose no (meaning you dont need scholarship\n)")
        else:
            print("Invalid location\n")
    else:
        print("Invalid choice in location\n")

#=====================================================
def act11():
    print("ACTIVITY 11 \n")

    for repeat in range (1,11):
        print("Hello World\n")

#=====================================================
def act12():
    print("\n Activity 12 \n")

    for x in range(10, 1, -1):
        print(f"{x}\n")

#=====================================================
def act13():
    print("Activity 13 \n")
    number = int(input("Enter any number: "))
    factorial = 1
    for factor in range(number, 0, -1):
        factorial *= factor 
        rounded = round(factorial, 2)
    print(f"The factorial of {rounded}\n")

#=====================================================
def act14():
    print("Activity 14\n")

    for x in range(1,11):
        print(x, end=" ")
        for y in range(1, 11):
            print("*", end = " ")
        print()


#=====================================================
def act15():
    print("Activity 15\n")

    for x in range(1,11, 5):
        print(x, end=" ")
        for y in range(1, 11):
            print("*", end = " ")
        print("\n")
        print()
#=====================================================
def act16():
    print("Activity 16\n")
    for x in range(1, 6):
        for y in range(1, x + 1):
            print("  ",end="")
        for z in range(6, y, -1):
            print("^ ",end="")
        for a in range(6, x, -1):
            print("* ",end="")
        for b in range(1, x + 1):
            print(" ",end="")
        print("")
    print()
#=====================================================
def act17():
    print("Activity 17\n")
    tabl = eval(input("Enter a number: "))
    for x in range(1,11):
        for y in range(1, tabl + 1):
            print(f"\t {x} x {y} = {x*y} ",end="")
        print() 
#=====================================================
def act18():
    print("Activity 18\n")
    tria = int(input("Enter a number: "))
    for a in range(1,5):
        for x in range(1,tria+1 ):
            for y in range(1, a + 1):
                print("*", end= " ")

            for z in range(5, a, -1):
                print(" ", end=" ")
        print()
#=====================================================
def act19():
    tuloy = True
    while tuloy == True:
        name = str(input("Will you give us your name? (yes/ no): "))
        if name.lower() == "no":
            print("program stopped\n")
            break
        else:
            continue
#=====================================================
def act20():
    print("Activity 20\n")
    tuloy = True
    num = 0
    while tuloy == True:
        question = str(input("Do you want to add triangles (yes/no): "))
        if question.lower() == "no":
            print("PROGRAM TERMINATED\n")
            break
        else:
            num += 1
            for a in range(1,5):
                for x in range(1, num+1 ):
                    for y in range(1, a + 1):
                            print("*", end= " ")
                            
                    for z in range(5, a, -1):
                            print(" ", end=" ")
                print()
        continue