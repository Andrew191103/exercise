amount_of_bill = int(input("Enter amount of bill:"))
number_of_people = int(input("Enter number of people:"))
amount_of_tips = int(input("Enter amount of tips:"))

Total_bill_per_person = amount_of_bill/number_of_people
Amount_of_tips_per_person = amount_of_bill*(amount_of_tips/100)

print("Bill and tips per person are", Total_bill_per_person, "And", Amount_of_tips_per_person, "USD")