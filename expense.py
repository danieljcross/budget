class Expense:

    def __init__(self, name, value):
        self.name = name
        self.value = value

def getExpense(expenses, name):
    for expense in expenses:
        if expense.name is name:
            return expense