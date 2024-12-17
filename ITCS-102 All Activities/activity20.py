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