set = eval(input("Input Number: "))

for x in range (set,0,-1):
    for y in range (set,x,-1):
        print("  ", end="")
    print("* " * x)