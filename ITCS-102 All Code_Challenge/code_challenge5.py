name = input("\n\t\t\t\t\tInput your name here --> ")

deposit = eval(input("\n\t\t\t\t\tPlease enter the amount you want to deposit: "))

libo = deposit % 1000
liboR = deposit // 1000

limaD = libo % 500
limaDR = libo // 500

dalawaD = limaD % 200
dalawaDR = limaD // 200

isaD = dalawaD % 100
isaDR = dalawaD // 100

fifty = isaD % 50
fiftyR = isaD // 50

bente = fifty % 20
benteR = fifty // 20

ten = bente % 10
tenR = bente // 10

sinko = ten % 5
sinkoR = ten // 5

piso = sinko % 5
pisoR = sinko // 5

print("\n\t\t\t\t\tGreetings" , name , ", the overall deposit input is: " )
print("\n\t\t\t\t\t" , liboR , "= 1000")
print("\n\t\t\t\t\t" , limaDR , "= 500")
print("\n\t\t\t\t\t" , dalawaDR , "= 200")
print("\n\t\t\t\t\t" , isaDR , "= 100")
print("\n\t\t\t\t\t" , fiftyR  , "= 50")
print("\n\t\t\t\t\t" , benteR , "= 20")
print("\n\t\t\t\t\t" , tenR , "= 10")
print("\n\t\t\t\t\t" , sinkoR , "= 5")
print("\n\t\t\t\t\t" , piso , "=1 \n\t\t\t\t\t\t By: Andrian C. Marino")