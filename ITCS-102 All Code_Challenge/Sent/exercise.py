for x in range(10, 0, -1):
    for y in range(1, 11 - x):
        print(" ", end="")
    for z in range(1, x + 1):
        print("*", end="")
    print()