#=====================================================
def cc1():
    print("\n\n\n\n\n\n\n\n\n \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b===========================\n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|  By: Andrian C. Marino  | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t    * \t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t  * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\b * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|      * * * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\b * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t  * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t    * \t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b===========================  \n\n\n\n\n\n\n\n\n\n\n")

#=====================================================
def cc2():
    name = input("\n\n\n\n\t\t Would you mind telling your name? Type here --> ")
    greet = input("\n\n\n\n\t\t Hi! "+ name + ", Select your greetings inside the object! (Hi/Hello) --> ")

    print("\n\n\n\n\n\n\n\n\n \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b===========================\n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|    Box: " + greet + ", USER!\t\b  | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t    * \t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|  for -   * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\b * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b|      * !" + name + "! * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\b * * * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t  * * * \t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t    * \t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b| \t\t\t | \n\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b===========================  \n\n\n\n\n\n\n\n\n\n\n")

#=====================================================
def cc():
    pass
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
    pass

#=====================================================
def cc12():
    pass

#=====================================================
def cc13():
    pass
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