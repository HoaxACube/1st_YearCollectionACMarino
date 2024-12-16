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
for v in range(1,6):
    for w in range(1, v + 1):
        print("  ", end="")
    for x in range(6, w, -1):
        print("* ", end="")
    for y in range(6, v, -1):
        print("* ", end="")
    for z in range(1, v + 1):
        print("  ", end="")
    print("")

print("\n By: Andrian C. Marino")

