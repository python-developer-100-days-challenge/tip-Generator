#Day 2 of my #PythonChallenge: Project 2 - Tip Generator 💰

#🔢 Interactive prompts for bill, tip percentage, and number of people.
#🧮 Calculating tips and splitting bills like a pro!

# Calculate tip percentage
bill = input("What is the total bill? ")
tip = input("What percentage tip would you like to give? ")

# Calculate tip for each person
tip_percent = int(tip) / 100
each_tip = float(bill) * float(tip_percent)

# Calculate total bill amount
total_bill = float(each_tip) + float(bill)

# Split the bill per person
numbers_person = input("How many people to split the bill? ")
split_bill = total_bill / int(numbers_person)
rounds = round(split_bill, 2)

# Display the result
print(f"Each person should pay ${rounds}")

#Transforming code into practical solutions! 🚀🐍💻 #CodingJourney #Day2