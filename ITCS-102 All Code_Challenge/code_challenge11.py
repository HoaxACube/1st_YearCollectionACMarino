
print("========== Diamond ==========")
for x in range(1, 5):
    for y in range(4,x,-1):
        print(" ",end=" ")
    for z in range(1,x+1):
        print("^",end=" ")    
    for a in range(1,x):
        print("*",end=" ")
    print()

for x in range(1, 4):
    for y in range(1,x+1):
        print(" ",end=" ")
    for z in range(4,x+1,-1):
        print("*",end=" ")
    for a in range(4,x,-1):
        print("^",end=" ")
    print()
print("==============================")