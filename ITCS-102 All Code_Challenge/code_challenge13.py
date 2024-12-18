print("========== Numeric Diamond ==========")
for i in range(1, 8):
    for j in range(7,i,-1):
        print(" ",end=" ")
    for k in range(i,1,-1):
        print(k,end=" ")    
    for x in range(1,i+1):
        print(x,end=" ")
    print()

for i in range(6, 0,-1):
    for j in range(7,i,-1):
        print(" ",end=" ")
    for k in range(i,1,-1):
        print(k,end=" ")
    for x in range(1,i+1):
        print(x,end=" ")
    print()
print("=====================================")