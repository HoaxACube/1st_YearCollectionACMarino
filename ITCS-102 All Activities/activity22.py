
names = []

while True:
    name = input("Enter a name ['done' to stop]: ")
    if name.lower() == "done":
        print(f"Here's your list of names : {names}")
        print(f"You have entered {len(names)} names!")
        break
    else:
        names.append(name)