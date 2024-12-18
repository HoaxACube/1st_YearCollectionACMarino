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