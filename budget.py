'''
Expense Calculations
Author: Daniel Cross
Editors: Elf Fire Hydrant Group
'''
from expense import Expense

# Individual Spending

# 1000 rent, 100 parking pass
spring_rent_24 = 1300
summer_rent_24 = 700
fall_rent_24 = 1300
w_break_rent_24 = 100
winter_rent_25 = 1300
s_break_rent_25 = 100
spring_rent_25 = 1300

# 50 a week
spring_food_24 = 700
summer_food_24 = 350
fall_food_24 = 700
w_break_food_24 = 250
winter_food_25 = 800
s_break_food_25 = 50
spring_food_25 = 700

# 50 every 2 weeks, 300 every 6 months for insurance (fall and spring), 125 extra for summer
spring_car_24 = 550
summer_car_24 = 300
fall_car_24 = 550
w_break_car_24 = 150
winter_car_25 = 350
s_break_car_25 = 0
spring_car_25 = 550

# Quarter Grant applied fall 24 and winter 25, internship only spring 25
spring_tuition_24 = 2500
summer_tuition_24 = 0
fall_tuition_24 = 2500
w_break_tuition_24 = 0
winter_tuition_25 = 2500
s_break_tuition_25 = 0
spring_tuition_25 = 2500

# Spending by Semester
spring_spending_24 = spring_car_24 + spring_food_24 + spring_tuition_24 + spring_rent_24
summer_spending_24 = summer_car_24 + summer_food_24 + summer_rent_24 + summer_tuition_24
fall_spending_24 = fall_car_24 + fall_food_24 + fall_tuition_24 + fall_rent_24
w_break_spending_24 = w_break_car_24 + w_break_food_24 + w_break_rent_24 + w_break_tuition_24
winter_spending_25 = winter_tuition_25 + winter_rent_25 + winter_car_25 + winter_food_25
s_break_spending_25 = s_break_car_25 + s_break_food_25 + s_break_rent_25 + s_break_tuition_25
spring_spending_25 = spring_car_25 + spring_food_25 + spring_tuition_25 + spring_rent_25


'''
Income Calculations
'''


# Income by Semester

# 400/paycheck, minus 200/semester for leeway
# Less in Summer and breaks for travel
spring_income_24 = 2500
summer_income_24 = 500
fall_income_24 = 2500
w_break_income_24 = 0
winter_income_25 = 2500
s_break_income_25 = 0
spring_income_25 = 2500


# Function to calculate new semester incomes

# Take 20% off (tax & tithing) * hrs/wk * $/hr * 14 (wks per semester)
# Rounds to the nearest hundred
def new_income_semester(hpw, dph):
    return round(.8 * hpw * dph * 14, -2)

# Change incomes by hrs/wk and $/hr

# hpw = hours per week, dph = dollars per hour
hpw = 0
dph = 0

if hpw != 0 and dph != 0:
    spring_income_24 = new_income_semester(hpw, dph)
    summer_income_24 = new_income_semester(hpw, dph) / 2
    fall_income_24 = new_income_semester(hpw, dph)
    winter_income_25 = new_income_semester(hpw, dph)
    spring_income_25 = new_income_semester(hpw, dph)
    summer_income_25 = new_income_semester(hpw, dph) / 2


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
