# #f-String
# score = 0
# height = 1.8
# isWinning = True
# print(f"you score is {score}, your height is {height}, you are winning {isWinning}")


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the trip calculator!")

total = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split bill? "))

pay = (total / people) * (1 + tip / 100)

pay = "{:.2f}".format(pay)
print(f"Each person should pay: ${pay}")