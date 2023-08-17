# Tip Calculator

Welcome to the Tip Calculator repository! This project is a part of my #PythonChallenge where I'm exploring and improving my Python programming skills. In this project, I've developed a simple yet handy Tip Calculator.

## Description

The Tip Calculator allows you to calculate the tip amount and the total bill after adding the tip. It's interactive and easy to use. You can input the total bill amount, the percentage of tip you'd like to give, and the number of people to split the bill among. The calculator then provides you with the amount each person should pay after splitting the bill.

## How to Use

1. Clone this repository to your local machine.
2. Run the `tip_calculator.py` file using a Python interpreter.
3. Follow the prompts to input the total bill amount, tip percentage, and number of people.

## Code Snippet

```python
# Calculate tip percentage
bill = input("What is the total bill? ")
tip = input("What percentage tip would you like to give? ")

# Calculate a tip for each person
tip_percent = int(tip) / 100
each_tip = float(bill) * float(tip_percent)

# Calculate the total bill amount
total_bill = float(each_tip) + float(bill)

# Split the bill per person
numbers_person = input("How many people to split the bill? ")
split_bill = total_bill / int(numbers_person)
rounds = round(split_bill, 2)

# Display the result
print(f"Each person should pay ${rounds}")
