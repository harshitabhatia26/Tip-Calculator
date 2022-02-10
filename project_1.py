#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60



print("Welcome to the tip calculator!")
total = input("What was the total bill? ")
percent = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill?")

tip_amount = float(total)*(int(percent)/100)

final_tip = round( tip_amount, 2)

bill_final = float(total) + final_tip

split_amount = bill_final/int(people)

print(f"Each person should pay : {split_amount}")

input("Press ENTER to exit")

