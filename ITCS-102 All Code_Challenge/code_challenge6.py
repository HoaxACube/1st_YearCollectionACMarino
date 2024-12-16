name = input("\n\t\t\t\t\t This program will evaluate whether you have passed the Course or not. \n\n\t\t\t\t\t Please enter your name to proceed...|  ")

print("\n\t\t\t\t\t Good Luck," , name , "!")

prelim = eval(input("\n\t\t\t\t\t\t\t\t\t\t By: Andrian C. Marino \n\n\t\t\t\t\t Input your Prelim Grade: "))
midterm = eval(input("\n\t\t\t\t\t Input your Midterm Grade: "))
semiF = eval(input("\n\t\t\t\t\t Input your Semi-Final Grade: "))
final = eval(input("\n\t\t\t\t\t Input your Final Grade: "))
quiz = eval(input("\n\t\t\t\t\t Input your Quiz Grade: "))
project = eval(input("\n\t\t\t\t\t Input your Project Grade: "))

finalg = (prelim * 0.15) + (midterm * 0.15) + (semiF * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)

roundedFG = round(finalg, 0)

print("\n\t\t\t\t\t GENERAL AVEGARE" , roundedFG)

if finalg >= 75 and finalg <=100:
	print("\n\t\t\t\t\t Congatulations! You have passed the current Course!")

elif finalg >= 0 and finalg <= 74:
	print("\n\t\t\t\t\t Unfortunately, you may have to do your best next time. You have failed")

else:
	print("\n\t\t\t\t\t Invalid Input Results")
