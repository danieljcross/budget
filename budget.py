'''
Expense Calculations
Author: Daniel Cross
Editors: Elf Fire Hydrant Group
'''
from expense import Expense, getExpense


'''
Spending:

Declare Lists
Input Amounts
Add Up Amounts
'''

# Declare Lists

spring_spending = []
summer_spending = []
fall_spending = []
w_break_spending = []
winter_spending = []
s_break_spending = []
spring_spending = []


# Input Amounts

# Summer
summer_spending.append(Expense("Rent", 700))
summer_spending.append(Expense("Food", 350))
summer_spending.append(Expense("Car", 300))

# Fall
fall_spending.append(Expense("Rent", 1300))
fall_spending.append(Expense("Food", 700))
fall_spending.append(Expense("Car", 550))
fall_spending.append(Expense("Tuition", 2500))

# Winter Break
w_break_spending.append(Expense("Rent", 100))
w_break_spending.append(Expense("Food", 250))
w_break_spending.append(Expense("Car", 150))

# Winter
winter_spending.append(Expense("Rent", 1300))
winter_spending.append(Expense("Food", 800))
winter_spending.append(Expense("Car", 350))
winter_spending.append(Expense("Tuition", 2500))

# Spring Break
s_break_spending.append(Expense("Rent", 100))
s_break_spending.append(Expense("Food", 50))

# Spring
spring_spending.append(Expense("Rent", 1300))
spring_spending.append(Expense("Food", 700))
spring_spending.append(Expense("Car", 550))
spring_spending.append(Expense("Tuition", 2500))


# Add Up Amounts

spring_spending_24 = 0
summer_spending_24 = 0
fall_spending_24 = 0
w_break_spending_24 = 0
winter_spending_25 = 0
s_break_spending_25 = 0
spring_spending_25 = 0

for Expense in spring_spending:
    spring_spending_24 += Expense.value

for Expense in summer_spending:
    summer_spending_24 += Expense.value

for Expense in fall_spending:
    fall_spending_24 += Expense.value

for Expense in w_break_spending:
    w_break_spending_24 += Expense.value

for Expense in winter_spending:
    winter_spending_25 += Expense.value

for Expense in s_break_spending:
    s_break_spending_25 += Expense.value

for Expense in spring_spending:
    spring_spending_25 += Expense.value


'''
Income
'''


# 400/paycheck, minus 200/semester for leeway
# Less in Summer and breaks for travel
spring_income_24 = 2500
summer_income_24 = 500
fall_income_24 = 2500
w_break_income_24 = 0
winter_income_25 = 2500
s_break_income_25 = 0
spring_income_25 = 2500


'''
Prints out entire budget through Spring 2025
'''


savings_now = 10000
after = savings_now

print('\n2024')
after = after - spring_spending_24 + spring_income_24
print(f'Spring Spending: ${spring_spending_24:,.0f}    Spring Income: ${spring_income_24:,.0f}    After: ${after:,.0f}')
after = after - summer_spending_24 + summer_income_24
print(f'Summer Spending: ${summer_spending_24:,.0f}    Summer Income: ${summer_income_24:,.0f}      After: ${after:,.0f}')
after = after - fall_spending_24 + fall_income_24
print(f'Fall Spending:   ${fall_spending_24:,.0f}    Fall Income:   ${fall_income_24:,.0f}    After: ${after:,.0f}')
after = after - w_break_spending_24 + w_break_income_24
print(f'W Break Spending:  ${w_break_spending_24:,.0f}    W Break Income: ${w_break_income_24:,.0f}       After: ${after:,.0f}')

print('\n2025')
after = after - winter_spending_25 + winter_income_25
print(f'Winter Spending: ${winter_spending_25:,.0f}    Winter Income: ${winter_income_25:,.0f}    After: ${after:,.0f}')
after = after - s_break_spending_25 + s_break_income_25
print(f'S Break Spending:  ${s_break_spending_25:,.0f}     S Break Income: ${s_break_income_25:,.0f}       After: ${after:,.0f}')
after = after - spring_spending_25 + spring_income_25
print(f'Spring Spending: ${spring_spending_25:,.0f}    Spring Income: ${spring_income_25:,.0f}    After: ${after:,.0f}\n')
total_income = spring_income_24 + summer_income_24 + fall_income_24 + w_break_income_24 + winter_income_25 + s_break_income_25 + spring_income_25
total_spending = spring_spending_24 + summer_spending_24 + fall_spending_24 + w_break_spending_24 + winter_spending_25 + s_break_spending_25 + spring_spending_25
print(f'Total Spending: ${total_spending:,.0f}    Total Income: ${total_income:,.0f}    After: ${after:,.0f}')
