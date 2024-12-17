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