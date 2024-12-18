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