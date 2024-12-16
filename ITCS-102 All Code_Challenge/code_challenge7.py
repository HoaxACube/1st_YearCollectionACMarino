name = input("Name: ")
age = eval(input("Age: "))

budget = 1000

chicken = 200
pork = 250
beef = 330

tax= 0.123

if age >= 60 and age <= 100:
    print(f"\n Greetings! {name}, \n Senior Discount Prices has been Activated")
elif age >= 100:
    print("Invalid Age")
else:
    print("\n You may now proceed \n")

isgrocery = input("Do you want to proceed for the grocery? [Yes/No]: ")