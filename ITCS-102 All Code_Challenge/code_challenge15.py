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