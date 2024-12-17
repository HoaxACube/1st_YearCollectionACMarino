print("Activity 17\n")
tabl = eval(input("Enter a number: "))
for x in range(1,11):
    for y in range(1, tabl + 1):
        print(f"\t {x} x {y} = {x*y} ",end="")
    print() 