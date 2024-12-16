odd = 0
even = 0
sum = 0

for x in range(1,11):
    number = eval(input(f"Proceed with number ({x}): "))
    print(x, "=", number)
    sum += number
    if odd % 2 == 0:
        odd += number
    else:
        even += number

print("\tTotal Odd: ", odd)
print("\tTotal Even: ", even)
print("\tTotal: ", sum, "\n\n By: Andrian C. Marino")