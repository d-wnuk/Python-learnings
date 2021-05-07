#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
no_of_ppl = input("How many people to split the bill? ")

total_bill_int = float(total_bill)
tip_int = int(tip)
no_of_ppl_int = int(no_of_ppl)

sum = (total_bill_int + total_bill_int * (tip_int / 100)) / no_of_ppl_int
single_bill = round(sum, 2)

print(f"Each person should pay: ${single_bill}")