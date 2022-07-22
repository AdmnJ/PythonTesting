#!/usr/bin/env python3

# This will take user input of how much they make in income in either yearly, monthly, semi-monthly, biweekly, weekly,
# or daily and then find their monthly income. (Super easy especially for the ones that enter monthly to start with)
# Then it will assign ask them what percentage of their monthly income they wish to budget for rent. Not only do
# many businesses limit who can sign leases based off of similar calculations, but it can help one to avoid
# many issues if they shoot for a lower percentage of their monthly income.


# Collect frequency of pay
while True:
    frequency = input('How often are you paid?\n Y: Yearly\n M: Monthly\n S: Semi-monthly\n B: Bi-weekly\n W: Weekly\n '
                      '(Y,M,S,B,W): ')
    frequency = frequency[0]  # Truncate to first letter
    frequency = frequency.strip().capitalize()  # Capitalize letter
    # Check to make sure input is either (Y,M,S,B,W)
    if frequency.strip().isalpha() and ((frequency == 'Y')
                                        or (frequency == 'M')
                                        or (frequency == 'S')
                                        or (frequency == 'B')
                                        or (frequency == 'W')):
        break  # Breaks while loop if input is acceptable
# Collect amount of pay
# Check amount is actual number
while True:
    pay = input('How much are you paid?\n'
                '$:')
    if (pay.strip().isdigit()) or (float(pay.strip()) % 1 > .01):  # added support for floating points
        pay = float(pay.strip())
        break
# Calculate monthly income
if frequency == 'Y':
    monthly = (pay/12)
else:
    if frequency == 'M':
        monthly = pay
    else:
        if frequency == 'S':
            monthly = (pay*2)
        else:
            if frequency == 'B':
                monthly = (pay*2.15)
            else:
                monthly = (pay*4.3)
# give approximate monthly income
print("$%.2f is your approximate monthly income." % monthly)
# Collect percentage of monthly they wish to budget for rent
while True:
    per = input('What percent of your monthly income would you like to budget for rent?\n'
                '%:')
    # checks to make sure input is either whole integer or floating point.
    if (per.strip().isdigit()) or (float(per.strip()) % 1 > .01):  # added support for floating points
        per = float(per.strip())  # converts  variable to float
        break
# If percentage stored in per is over 1, assume it is a whole percentage and divide by 100
if per > 1.0:
    per = (per/100)
full_per = (per*100)
# Calculate percentage for rental budget and subtract that from income to give rough estimate of monthly funds remaining
budget = (per*monthly)
remain = (monthly-budget)
# Give them their rental budget
print("You decided to budget %.0f-percent of your estimated monthly income for rent." % full_per)
print("Budget amount for monthly rent is $%.2f" % budget)
print("That leaves you with approximately just $%.2f remaining after rent each month" % remain)
