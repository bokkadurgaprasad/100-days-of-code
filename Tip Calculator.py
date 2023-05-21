#print the salutation for the project
print("welcome to the tip calculator!")
#ask the total amount of bill       
bill = float(input("What was the total bill? $"))
#ask what percent of tip wanted to give
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#ask the no.of persons tom split the bill
people = int(input("How many eople to split the bill?"))
#calculate the percentage of tip
tip_as_percent = tip / 100
#multiply the tip percentage with the bill amont
total_tip_amount = bill * tip_as_percent
#Then add the tip amount to the total bill
total_bill = bill + total_tip_amount
#calculate the splitting amount for each person
bill_per_person = total_bill / people
#Round the bill amount to simply the amount
final_amount = round(bill_per_person, 2)
#Finally print the final amount
print(f"Each person should pay: ${final_amount} ")
