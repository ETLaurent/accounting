import sys
import os
import importlib

sys.path.insert(0, './banks')

def get_banks():
    files = [f for f in os.listdir('./banks') if f.endswith('.py')]
    banks = {}

    for file in files:
        bank_name = file[:-3] # Remove the '.py' extension
        banks[bank_name] = importlib.import_module(bank_name).expenses

    return banks

def get_expenses(selected_banks):
    banks = get_banks()
    expenses = {}

    for bank in selected_banks:
        if bank in banks:
            for expense, amount in banks[bank].items():
                if expense in expenses:
                    # If the expense already exists, add the amount
                    expenses[expense] += amount
                else:
                    expenses[expense] = amount

    return expenses
