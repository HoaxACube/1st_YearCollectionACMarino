input("\n\t\t  __________________________________________________\n------------------|Hi User! This program will evaluate your number!|------------------\n\t\t  --------------------------------------------------\n Type anything to proceed . . . ")

num1 = eval(input("\n\t\t\t\t\t\t\t\tBy: Andrian C. Marino\n--------------------------------------------------------------------------------------\n\n\t\t Enter The First Number: "))
num2 = eval(input("\t\t Enter the Second Number: "))

answer1 = num1 + num2
answer2 = num1 - num2
answer3 = num1 * num2
answer4 = num1 / num2
answer5 = num1 ** num2
answer6 = num1 // num2
answer7 = num1 % num2

print( "\n\n\t -            The Sum of " , num1 , " and " , num2 , " is " , answer1 , "\n\t -     The Difference of " , num1 , " and " , num2 , " is " , answer2 , "\n\t -        The Product of " , num1 , " and " , num2 , " is " , answer3 , "\n\t -       The Quotient of " , num1 , " and " , num2 , " is " , answer4 , "\n\t -       The Exponent of " , num1 , "  by " , num2 , " is " , answer5 , "\n\t - The Floor Division of " , num1 , "  to " , num2 , " is " , answer6 , "\n\t -          Remainder of " , num1 , " and " , num2 , " is " , answer7 , "\n\n--------------------------------------------------------------------------------------")
