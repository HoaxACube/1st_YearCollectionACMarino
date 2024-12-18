def option_one():
    print("Option 1 selected.")

def option_two():
    print("Option 2 selected.")

def exit_program():
    print("Exiting the program.")
    exit()


while True:
    import os
    print("\n--- Menu ---")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    
    choice = input("Select an option: ")

    
    if choice == "1":
        option_one()
        os.system('cls')
    elif choice == "2":
        option_two()
    elif choice == "3":
        exit_program()
    else:
        print("Invalid choice, try again.")
