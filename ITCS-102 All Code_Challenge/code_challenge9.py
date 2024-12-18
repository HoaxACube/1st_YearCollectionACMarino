for a in range(1,6):
    for b in range(6, a, -1):
        print("  ", end="")
    for c in range(1, a + 1):
        print("* ", end="")
    for d in range(1, a + 1):
        print("* ", end="")
    for e in range(1, a, 1):
        print("  ", end="")
    print()