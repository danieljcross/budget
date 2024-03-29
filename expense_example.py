from expense import Expense, getExpense

# Example Usage:
# Here is some unchanged code made using without Expense:
        
fast_food_expense = 25
movie_night_expense = 50

print("Fast food expense: ", fast_food_expense)
print("Move night expense: ", movie_night_expense)

# Here is the same code refactored to use Expense objects:

expenses = []
expenses.append(Expense("Fast food expense", 25))
expenses.append(Expense("Move night expense", 50))

for expense in expenses:
    print(expense.name + ": " + str(expense.value))

# Here is an example showing how to retrive by name from an expenses array

fast_food = getExpense(expenses, "Fast food expense")
print("Fast food expense: " + str(fast_food.value))
