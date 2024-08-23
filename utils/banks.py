import sys
import os
import importlib

# meh, this is a bit hacky,
# but it works... we get the banks from the banks directory
script_dir = os.path.dirname(os.path.realpath(__file__))
bank_dir = os.path.join(script_dir, '../banks')
sys.path.insert(0, bank_dir)

def get_banks():
    files = [f for f in os.listdir(bank_dir) if f.endswith('.py')]
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
