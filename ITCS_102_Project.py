#=============/ PLAN 1: compilation of each activities \=============



#=====================================================
#||                   Activities                    ||
#=====================================================
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
#=====================================================
#||                 Code_Challenge                  ||
#=====================================================
def cc1():
    print("\n\n\n\n\n\n\n\n\n \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b===========================\n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|  By: Andrian C. Marino  | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t    * \t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t  * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\b * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|      * * * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\b * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t  * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t    * \t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b===========================  \n\n\n\n\n\n\n\n\n\n\n")

#=====================================================
def cc2():
    name = input("\n\n\n\n\t\t Would you mind telling your name? Type here --> ")
    greet = input("\n\n\n\n\t\t Hi! "+ name + ", Select your greetings inside the object! (Hi/Hello) --> ")

    print("\n\n\n\n\n\n\n\n\n \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b===========================\n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|    Box: " + greet + ", USER!\t\b  | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t    * \t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|  for -   * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\b * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|      * !" + name + "! * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\b * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t  * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t    * \t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b===========================  \n\n\n\n\n\n\n\n\n\n\n")

#=====================================================
def cc3():
    print("\n=== Welcome to the Biodata Form ===\n")

    full_name = input("Full Name: ")
    address = input("Address: ")
    birth_date = input("Date of Birth (MM/DD/YYYY): ")
    birth_place = input("Place of Birth: ")
    age = input("Age: ")
    gender = input("Gender: ")
    civil_status = input("Civil Status: ")
    nationality = input("Nationality: ")
    religion = input("Religion: ")
    weight = input("Weight (in kg): ")
    languages = input("Languages Known: ")

    print("\n--- Family Information ---")
    father_name = input("Father's Name: ")
    mother_name = input("Mother's Name: ")

    print("\n--- Academic & Contact Information ---")
    school_info = input("School/Department, Year & Section: ")
    occupation = input("Occupation: ")
    email = input("Email Address: ")
    mobile = input("Mobile Number: ")

    print("\n=========================================================")
    print("|                  BIODATA SUMMARY                      |")
    print("=========================================================")
    print(f"Name: \t\t\t{full_name}")
    print(f"Address:\t\t{address}")
    print(f"Date of Birth: \t\t{birth_date}")
    print(f"Place: \t\t\t{birth_place}")
    print(f"Age: \t\t\t{age}")
    print(f"Gender: \t\t{gender}")
    print(f"Civil Status: \t\t{civil_status}")
    print(f"Nationality: \t\t{nationality}")
    print(f"Religion: \t\t{religion}")
    print(f"Languages Known: \t{languages}")
    print(f"Father's Name: \t\t{father_name}")
    print(f"Mother's Name: \t\t{mother_name}")
    print(f"School:\t\t\t{school_info}")
    print(f"Occupation: \t\t{occupation}")
    print(f"Email: \t\t\t{email} | Mobile: {mobile}")
    print("=========================================================")
    print("\nThank you for completing the Biodata Form!")
#=====================================================
def cc4():
    input("\n\t\t  __________________________________________________\n------------------|Hi User! This program will evaluate your number!|------------------\n\t\t  --------------------------------------------------\n Type anything to proceed . . . ")

    num1 = eval(input("\n\t\t\t\t\t\t\t\tBy: Andrian C. Marino\n--------------------------------------------------------------------------------------\n\n\t\t Enter The First Number: "))
    num2 = eval(input("\t\t Enter the Second Number: "))

    answer1 = num1 + num2
    answer2 = num1 - num2
    answer3 = num1 * num2
    answer4 = num1 / num2
    answer5 = num1 ** num2
    answer6 = num1 // num2
    answer7 = num1 % num2

    print( "\n\n\t -            The Sum of " , num1 , " and " , num2 , " is " , answer1 , "\n\t -     The Difference of " , num1 , " and " , num2 , " is " , answer2 , "\n\t -        The Product of " , num1 , " and " , num2 , " is " , answer3 , "\n\t -       The Quotient of " , num1 , " and " , num2 , " is " , answer4 , "\n\t -       The Exponent of " , num1 , "  by " , num2 , " is " , answer5 , "\n\t - The Floor Division of " , num1 , "  to " , num2 , " is " , answer6 , "\n\t -          Remainder of " , num1 , " and " , num2 , " is " , answer7 , "\n\n--------------------------------------------------------------------------------------")

#=====================================================
def cc5():
    name = input("\n\t\t\t\t\tInput your name here --> ")

    deposit = eval(input("\n\t\t\t\t\tPlease enter the amount you want to deposit: "))

    libo = deposit % 1000
    liboR = deposit // 1000

    limaD = libo % 500
    limaDR = libo // 500

    dalawaD = limaD % 200
    dalawaDR = limaD // 200

    isaD = dalawaD % 100
    isaDR = dalawaD // 100

    fifty = isaD % 50
    fiftyR = isaD // 50

    bente = fifty % 20
    benteR = fifty // 20

    ten = bente % 10
    tenR = bente // 10

    sinko = ten % 5
    sinkoR = ten // 5

    piso = sinko % 5
    pisoR = sinko // 5

    print("\n\t\t\t\t\tGreetings" , name , ", the overall deposit input is: " )
    print("\n\t\t\t\t\t" , liboR , "= 1000")
    print("\n\t\t\t\t\t" , limaDR , "= 500")
    print("\n\t\t\t\t\t" , dalawaDR , "= 200")
    print("\n\t\t\t\t\t" , isaDR , "= 100")
    print("\n\t\t\t\t\t" , fiftyR  , "= 50")
    print("\n\t\t\t\t\t" , benteR , "= 20")
    print("\n\t\t\t\t\t" , tenR , "= 10")
    print("\n\t\t\t\t\t" , sinkoR , "= 5")
    print("\n\t\t\t\t\t" , piso , "=1 \n\t\t\t\t\t\t By: Andrian C. Marino")
#=====================================================
def cc6():
    name = input("\n\t\t\t\t\t This program will evaluate whether you have passed the Course or not. \n\n\t\t\t\t\t Please enter your name to proceed...|  ")

    print("\n\t\t\t\t\t Good Luck," , name , "!")

    prelim = eval(input("\n\t\t\t\t\t\t\t\t\t\t By: Andrian C. Marino \n\n\t\t\t\t\t Input your Prelim Grade: "))
    midterm = eval(input("\n\t\t\t\t\t Input your Midterm Grade: "))
    semiF = eval(input("\n\t\t\t\t\t Input your Semi-Final Grade: "))
    final = eval(input("\n\t\t\t\t\t Input your Final Grade: "))
    quiz = eval(input("\n\t\t\t\t\t Input your Quiz Grade: "))
    project = eval(input("\n\t\t\t\t\t Input your Project Grade: "))

    finalg = (prelim * 0.15) + (midterm * 0.15) + (semiF * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)

    roundedFG = round(finalg, 0)

    print("\n\t\t\t\t\t GENERAL AVEGARE" , roundedFG)

    if finalg >= 75 and finalg <=100:
        print("\n\t\t\t\t\t Congatulations! You have passed the current Course!")

    elif finalg >= 0 and finalg <= 74:
        print("\n\t\t\t\t\t Unfortunately, you may have to do your best next time. You have failed")

    else:
        print("\n\t\t\t\t\t Invalid Input Results")

#=====================================================
def cc7():
    name = input("Name: ")
    age = int(input("Age: "))  
    budget = 1000
    chicken = 200
    pork = 250
    beef = 330
    tax = 0.123
    senior_discount = 0.2  

    if 60 <= age <= 100:
        print(f"\nGreetings! {name}, \nSenior Discount Prices have been Activated.")
        is_senior = True
    elif age > 100:
        print("Invalid Age.")
        exit()
    else:
        print("\nYou may now proceed.\n")
        is_senior = False

    is_grocery = input("Do you want to proceed for the grocery? [Yes/No]: ").strip().lower()

    if is_grocery != "yes":
        print("Exiting... Have a great day!")
        exit()

    print("\nItems Available:")
    print(f"1. Chicken - ₱{chicken}")
    print(f"2. Pork - ₱{pork}")
    print(f"3. Beef - ₱{beef}")

    total_bill = 0

    while True:
        choice = input("\nWhat would you like to buy? [1]Chicken [2]Pork [3]Beef or [0]Done: ")

        if choice == "1":
            price = chicken
        elif choice == "2":
            price = pork
        elif choice == "3":
            price = beef
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 0.")
            continue

        if is_senior:
            price -= price * senior_discount

        price_with_tax = price + (price * tax)

        if budget >= total_bill + price_with_tax:
            total_bill += price_with_tax
            print(f"Item added. Total Bill so far: ₱{total_bill:.2f}")
        else:
            print("Not enough budget for this item. Choose something else or type 'Done'.")


    print("\n======Grocery Receipt=======")
    print(f"Total Bill: ₱{total_bill:.2f}")
    print(f"Remaining Budget: ₱{budget - total_bill:.2f}")

    if total_bill > 0:
        print("Thank you for shopping with us!")
    else:
        print("No items purchased. Have a great day!")
        
#=====================================================
def cc8():
    odd = 0
    even = 0
    sum = 0

    for x in range(1,11):
        number = eval(input(f"Proceed with number ({x}): "))
        print(x, "=", number)
        sum += number
        if odd % 2 == 0:
            odd += number
        else:
            even += number

    print("\tTotal Odd: ", odd)
    print("\tTotal Even: ", even)
    print("\tTotal: ", sum, "\n\n By: Andrian C. Marino")
#=====================================================
def cc9():
    set = eval(input("Input Number: "))

    for x in range (set,0,-1):
        for y in range (set,x,-1):
            print("  ", end="")
        print("* " * x)
#=====================================================
def cc10():
    for a in range(1,6):
        for b in range(6, a, -1):
            print("  ", end="")
        for c in range(1, a + 1):
            print("* ", end="")
        for d in range(1, a + 1):
            print("* ", end="")
        for e in range(1, a, 1):
            print("  ", end="")
        print()
    for v in range(1,6):
        for w in range(1, v + 1):
            print("  ", end="")
        for x in range(6, w, -1):
            print("* ", end="")
        for y in range(6, v, -1):
            print("* ", end="")
        for z in range(1, v + 1):
            print("  ", end="")
        print("")

    print("\n By: Andrian C. Marino")

#=====================================================
def cc11():
    print("========== Diamond ==========")
    for x in range(1, 5):
        for y in range(4,x,-1):
            print(" ",end=" ")
        for z in range(1,x+1):
            print("^",end=" ")    
        for a in range(1,x):
            print("*",end=" ")
        print()

    for x in range(1, 4):
        for y in range(1,x+1):
            print(" ",end=" ")
        for z in range(4,x+1,-1):
            print("*",end=" ")
        for a in range(4,x,-1):
            print("^",end=" ")
        print()
    print("==============================")

#=====================================================
def cc12():
    for a in range(1,6):
        for b in range(6, a, -1):
            print("  ", end="")
        for c in range(1, a + 1):
            print("* ", end="")
        for d in range(1, a + 1):
            print("* ", end="")
        for e in range(1, a, 1):
            print("  ", end="")
        print()

    for x in range(5):
        print("        * * * *")
    print()




#=====================================================
def cc13():
    print("========== Numeric Diamond ==========")
    for i in range(1, 8):
        for j in range(7,i,-1):
            print(" ",end=" ")
        for k in range(i,1,-1):
            print(k,end=" ")    
        for x in range(1,i+1):
            print(x,end=" ")
        print()

    for i in range(6, 0,-1):
        for j in range(7,i,-1):
            print(" ",end=" ")
        for k in range(i,1,-1):
            print(k,end=" ")
        for x in range(1,i+1):
            print(x,end=" ")
        print()
    print("=====================================")
#=====================================================
def cc14():
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

#=====================================================
def cc15():
    import os

    tuloy = True
    no = 0
    while tuloy == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED (Andrian C. Marino)")
            break
            tuloy = False
        elif ask.lower() == "yes":
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        else:
            print("Please Choose [Yes/No]")
            continue

#=====================================================
def cc16():
    balance = 0
    def create_account(name, initial_deposit=0):
        global account_name, balance
        account_name = name
        balance = initial_deposit
        print(f"Account created for {account_name}. Initial deposit: PHP {balance}.")

    def deposit(amount):
        global balance
        balance += amount
        print(f"PHP {amount} deposited successfully.")
        denomination(amount)
        print(f"New balance: PHP {balance}.")

    def check_balance():
        global balance
        print(f"Current balance: PHP {balance}.")

    def withdraw(amount):
        global balance
        if amount > balance:
            print("Insufficient funds. Transaction failed.")
        else:
            balance -= amount
            print(f"PHP {amount} withdrawn successfully.")
            print(f"New balance: PHP {balance}.")

    def denomination(amount):
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        print(f"Breakdown of PHP {amount}:")
        for denom in denominations:
            count = amount // denom
            if count > 0:
                print(f"PHP {denom}: {count}")
            amount %= denom

    def exit_simulation():
        global Continue
        Continue = False
        print("Stopping Program. Thank you!")

    Continue = True

    while Continue:
        print("\n=== Bank Simulation === \t\t\t(Andrian C. Marino)")
        print("[1] Create Account")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Check Balance")
        print("[5] Exit")
        choose = input("Select an option: ")

        if choose == "1":
            print("\n--- Create Account ---")
            fullname = input("Enter your full name: ")
            while True:
                try:
                    amount = float(input("Enter initial deposit amount: "))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            create_account(fullname, amount)

        elif choose == "2":
            print("\n--- Deposit ---")
            while True:
                try:
                    amount = float(input("Enter deposit amount: "))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            deposit(amount)

        elif choose == "3":
            print("\n--- Withdraw ---")
            while True:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    break
                except ValueError:
                    print("Invalid or exceeded amount. Please enter a number.")
            withdraw(amount)

        elif choose == "4":
            print("\n--- Check Balance ---")
            check_balance()

        elif choose == "5":
            exit_simulation()

        else:
            print("Invalid option. Please try again.")
#=====================================================
import os
input("This program is recommended for full screen. Starting...... [Press Enter]: ")

usrname = input("Please input your name: ")
# os.system('cls')

#=============/ PLAN 2: MENU SETTINGS LOOKS(Animation) \=============

#introduction
def sc1():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("           _____________                           _____________         ||")
    print("            ===========                             ===========            ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                    ==                                     ")
    print("                                             111111                        ")
    print("                                                  1                        ")
    print("                                  e e e          1                         ")
    print("                                e       e       1                          ")
    print("||                              e       e      111111                      ")
    print("||                                e e e                                   +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc2():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("           _____________                           _____________         ||")
    print("            ===========                             ===========            ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                    ==                                     ")
    print("                                              0000000000                   ")
    print("                                                      0                    ")
    print("                                  e e e             0                      ")
    print("                                e       e         0                        ")
    print("||                                e e e          000000000                 ")
    print("||                                                                        +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc3():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("            eeeee                           eeeee                        ||")
    print("                 eee                     eee                               ")
    print("                    ee                 ee                                  ")
    print("                 eee                     eee                               ")
    print("            eeeee                           eeeee                          ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("                      WW      WW      WW                                   ")
    print("||                  WW  WW  WW  WW  WW  WW  WW                             ")
    print("||                WW      WW      WW      WW                              +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc4():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("                       eeeee                           eeeee             ||")
    print("                            eee                     eee                    ")
    print("                               ee                 ee                       ")
    print("                            eee                     eee                    ")
    print("                       eeeee                           eeeee               ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                 WW      WW      WW                        ")
    print("||                             WW  WW  WW  WW  WW  WW  WW                  ")
    print("||                           WW      WW      WW      WW                   +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc5():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("            ######################################################         ")
    print("                                                                           ")
    print("           ######################################################          ")
    print("                                                                           ")
    print("            ######################################################         ")
    print("                                                                           ")
    print("           ######################################################          ")
    print("                                                                           ")
    print("            ######################################################         ")
    print("||                                                                         ")
    print("||         ######################################################         +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc6():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("            ______________________________________________________         ")
    print("                                                                           ")
    print("           ______________________________________________________          ")
    print("                                                                           ")
    print("            ______________________________________________________         ")
    print("                                                                           ")
    print("           ______________________________________________________          ")
    print("                                                                           ")
    print("            ______________________________________________________         ")
    print("||                                                                         ")
    print("||         ______________________________________________________         +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc7():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("                                                                           ")
    print("                ---                                        ---             ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                     --                                    ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("                            ----           ----                            ")
    print("||                                                                         ")
    print("||                                                                        +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc8():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("           0000000000000                        0000000000000              ")
    print("         00             00                     00             00           ")
    print("        0   WWWWWWWWWWW   0                   0   WWWWWWWWWWW   0          ")
    print("        0   WWWWWWWWWWW   0                   0   WWWWWWWWWWW   0          ")
    print("         00             00                     00             00           ")
    print("           0000000000000                         0000000000000             ")
    print("                                   ===                                     ")
    print("                                                                           ")
    print("                               _ 0 0 0 0 _                                 ")
    print("||                            0           0           < A User! >          ")
    print("||                             0         0                                +")
    print("||                               0 0 0 0                                 ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc9():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                AAA                              AAA                    ||")
    print("                AA AA                            AA AA                     ")
    print("               AA   AA                          AA   AA                    ")
    print("              AA     AA                        AA     AA                   ")
    print("             AA       AA                      AA       AA                  ")
    print("                                                                           ")
    print("                                 ===                                       ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                      < Welcome! >         ")
    print("||                      ^||||||||||||||||||||^                             ")
    print("||                                                                        +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc10():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("           ############      ############       ############               ")
    print("            ##########        ##########         ##########                ")
    print("            ##########        ##########         ##########                ")
    print("            ##########        ##########         ##########                ")
    print("             ########          ########           ########                 ")
    print("             ########          ########           ########                 ")
    print("             ########          ########           ########                 ")
    print("             ########          ########           ########                 ")
    print("                                                                           ")
    print("||             ####              ####                ####                  ")
    print("||            ######            #######             ######                +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc11():
    print("++++                                                             ==========")
    print("++                                                                       ||")
    print("+                                                                        ||")
    print("            ######################################################         ")
    print("                                                                           ")
    print("           ######################################################          ")
    print("                                                                           ")
    print("            ######################################################         ")
    print("                                                                           ")
    print("           ######################################################          ")
    print("                                                                           ")
    print("            ######################################################         ")
    print("||                                                                         ")
    print("||         ######################################################         +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc12():
    print("++++                                                             ==========")
    print(f"++                       GREETINGS!! *{usrname}*                          ")
    print("+                                                                          ")
    print("                   ||||||||||||||||||||||||||||||||||||                    ")
    print("                                                                           ")
    print("   ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||      ")
    print("                                                                           ")
    print("                       |||||||||||||||||||||||||||||                       ")
    print("                                                                           ")
    print("      ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||       ")
    print("                                                                           ")
    print("      |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||          ")
    print("||                                                                         ")
    print("||                                                                        +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc13():
    print("++++                                                             ==========")
    print(f"++                       GREETINGS!! *{usrname}*                          ")
    print("+                                                                          ")
    print("                   Welcome to this interactive program!                    ")
    print("                                                                           ")
    print("   ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||      ")
    print("                                                                           ")
    print("                       |||||||||||||||||||||||||||||                       ")
    print("                                                                           ")
    print("      ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||       ")
    print("                                                                           ")
    print("      |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||          ")
    print("||                                                                         ")
    print("||                                                                        +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc14():
    print("++++                                                             ==========")
    print(f"++                       GREETINGS!! *{usrname}*                          ")
    print("+                                                                          ")
    print("                   Welcome to this interactive program!                    ")
    print("                                                                           ")
    print("       This program allows you to engage in various program that is-       ")
    print("                                                                           ")
    print("                       made by my owner [Andrian]..                       ")
    print("                                                                           ")
    print("      ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||       ")
    print("                                                                           ")
    print("      |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||          ")
    print("||                                                                         ")
    print("||                                                                        +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")

def sc15():
    print("++++                                                             ==========")
    print(f"++                       GREETINGS!! *{usrname}*                          ")
    print("+                                                                          ")
    print("                   Welcome to this interactive program!                    ")
    print("                                                                           ")
    print("       This program allows you to engage in various program that is-       ")
    print("                                                                           ")
    print("                       made by my owner [Andrian]..                       ")
    print("                                                                           ")
    print("      Feel Free to choose from the options and enjoy the experience.       ")
    print("                                                                           ")
    print("      |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||          ")
    print("||                                                                         ")
    print("||                                                                        +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")


def sc16():
    print("++++                                                             ==========")
    print(f"++                       GREETINGS!! *{usrname}*                          ")
    print("+                                                                          ")
    print("                   Welcome to this interactive program!                    ")
    print("                                                                           ")
    print("       This program allows you to engage in various program that is-       ")
    print("                                                                           ")
    print("                       made by my owner [Andrian]..                        ")
    print("                                                                           ")
    print("      Feel Free to choose from the options and enjoy the experience.       ")
    print("                                                                           ")
    print("       Please Follow the instructions carefully as provided. ENJOY!        ")
    print("||                                                                         ")
    print("||                                                                        +")
    print("||                                                                       ++")
    print("==========     type anything to continue... [Enter]                    ++++")



os.system('cls')
input("[-.-]  <--- Wake him up (type anything to continue 1/3)")

os.system('cls')
input("[-_-] <--- Wake him up (type anything to continue 2/3)")

os.system('cls')
input("[-.-]  <--- Wake him up (type anything to continue 3/3)")

os.system('cls')
sc1()
input()

os.system('cls')
sc2()
input()

os.system('cls')
sc1()
input()

os.system('cls')
sc2()
input()

os.system('cls')
sc3()
input()

os.system('cls')
sc4()
input()

os.system('cls')
sc3()
input()

os.system('cls')
sc4()
input()

os.system('cls')
sc7()
input()

os.system('cls')
sc10()
input()

os.system('cls')
sc8()
input()

os.system('cls')
sc9()
input()

os.system('cls')
sc11()
input()

os.system('cls')
sc6()
input() 

os.system('cls')
sc12()
input() 

os.system('cls')
sc13()
input() 

os.system('cls')
sc14()
input() 

os.system('cls')
sc15()
input() 

os.system('cls')
sc16()
input()
os.system('cls')


#=============/ PLAN 2: functions of commands \=============
while True:
    print("++++                                                             ==========")
    print("++                          ===============                              ||")
    print("+                              Main Menu                                 ||")
    print("                            ===============                                ")
    print("                                                                           ")
    print("                        Activities | Code Challenges                       ")
    print("                 [1]              |               [2]                      ")
    print("     Activities contains          |     Code Challenges contains some      ")
    print("    several basics and the        |    of the most beginner level of       ")
    print("    fundamental applications of   |    understanding my owner 'Andrian'    ")
    print("    the codes that is mostly      |    had to face.                        ")
    print("    used by python users.         |     He did his best to finish each     ")
    print("||   Thanks to my owner's         |    one of them. Hopefully he can       ")
    print("||  professor. He can grasp most  |    improve the way he codes and it    +")
    print("||  of these topics.              |    applications in python            ++")
    print("==========     Choose which one you'd like to explore [1/2]            ++++")
    print("                    To let me rest again do [hibernate]                    \n\n\n\n")
    mainmenu = input("Input Here: ")
    

    if mainmenu == "1":
        while True:
            print("++++                                                             ==========")
            print("++                            < ACTIVITIES >                             ||")
            print("+                                                                        ||")
            print("Activity[1]: Typing Test Score         Activity[11]: Print 'Hello World'   ")
            print("Activity[2]: Greeting with Name        Activity[12]: Countdown from 10     ")
            print("Activity[3]: Biodata Collection        Activity[13]: Factorial Calculation ")
            print("Activity[4]: Basic Math Ops            Activity[14]: Star Patterns         ")
            print("Activity[5]: Fahrenheit to Celsius     Activity[15]: Incremental Patterns  ")
            print("Activity[6]: Incremental Numbers       Activity[16]: Pyramid Pattern       ")
            print("Activity[7]: Gold Mining Tracker       Activity[17]: Multiplication Table  ")
            print("Activity[8]: Password Checker          Activity[18]: Star Triangle         ")
            print("Activity[9]: Age Categorization        Activity[19]: Name Input Loop       ")
            print("Activity[10]: Scholarship Check        Activity[20]: Triangle Patterns     ")
            print("                                                                           ")
            print("                           Activity[0]: Exit                               ")
            print("||                                                                         ")
            print("||                                                                        +")
            print("||                                                                       ++")
            print("==========     Choose the corresponding number                         ++++\n\n\n\n")
            choice = int(input("\nEnter your choice: "))
        
            if choice == 0:
                print("Exiting the program. Goodbye!")
                break
            elif choice == 1:
                act1()
            elif choice == 2:
                act2()
            elif choice == 3:
                act3()
            elif choice == 4:
                act4()
            elif choice == 5:
                act5()
            elif choice == 6:
                act6()
            elif choice == 7:
                act7()
            elif choice == 8:
                act8()
            elif choice == 9:
                act9()
            elif choice == 10:
                act10()
            elif choice == 11:
                act11()
            elif choice == 12:
                act12()
            elif choice == 13:
                act13()
            elif choice == 14:
                act14()
            elif choice == 15:
                act15()
            elif choice == 16:
                act16()
            elif choice == 17:
                act17()
            elif choice == 18:
                act18()
            elif choice == 19:
                act19()
            elif choice == 20:
                act20()
            else:
                print("Invalid choice. Please choose a valid option.")
            print("Invalid input. Please enter a number.")

    elif mainmenu == "2":
        while True:
            print("++++                                                             ==========")
            print("++                          < Code Challenges >                          ||")
            print("+                                                                        ||")
            print("Activity[1]: Greetings Animation     Activity[9]: Reverse Pyramid          ")
            print("Activity[2]: Greeting Box           Activity[10]: Star Pyramid             ")
            print("Activity[3]: Biodata Form           Activity[11]: Diamond Shape            ")
            print("Activity[4]: Arithmetic Operations  Activity[12]: Star Pyramid with Base   ")
            print("Activity[5]: Deposit Denommination  Activity[13]: Numeric Diamond          ")
            print("Activity[6]: Course Evaluation      Activity[14]: Summation Until Zero     ")
            print("Activity[7]: Grocery Calculator     Activity[15]: Repeated Triangle Pattern")
            print("Activity[8]: Odd and Even Calc..    Activity[16]: Bank Account Manager     ")
            print("                                                                           ")
            print("                         Activity[0]: Exit Program                         ")
            print("||                                                                         ")
            print("||                                                                        +")
            print("||                                                                       ++")
            print("==========     Choose the corresponding number                         ++++\n\n\n\n\n")  

            choice = input("Select an option by number: ")

            if choice == "1":
                cc1()
            elif choice == "2":
                cc2()
            elif choice == "3":
                cc3()
            elif choice == "4":
                cc4()
            elif choice == "5":
                cc5()
            elif choice == "6":
                cc6()
            elif choice == "7":
                cc7()
            elif choice == "8":
                cc8()
            elif choice == "9":
                cc9()
            elif choice == "10":
                cc10()
            elif choice == "11":
                cc11()
            elif choice == "12":
                cc12()
            elif choice == "13":
                cc13()
            elif choice == "14":
                cc14()
            elif choice == "15":
                cc15()
            elif choice == "16":
                cc16()
            elif choice == "0":
                print("Exiting Program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    
    elif mainmenu.lower() == "hibernate":
        os.system('cls')
        print("Thank you! LIGHTS OUT! [^_^]/-\n\nBest Regards From: Andrian C. Marino")
        break
    else:
        os.system('cls')
        print("Please Choose Properly")
        continue

#=============/ PLAN 3: ERROR/Bug Testing(my notes and comments) \=============

#MY GITHUB ACCOUNT: https://github.com/HoaxACube

#I've plan to animate the intro, although my original plan was a clock, it was too time consuming that I've scrap the idea

#There's several errors on the menu but thankfully it's too easy to detect.

#I've had trouble using github at first but then I think I've adapted to it fairly well

#I've used several references of codes credits to: Ragudo, Orte, Terrence, Elumba

#Did well under pressure(I was cramming lol)