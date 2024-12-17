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