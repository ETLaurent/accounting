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
        banks[bank_name] = importlib.import_module(bank_name)

    return banks

def get_transactions(selected_banks):
    banks = get_banks()

    expenses = {}
    incomes = {}

    # if the expense/income already exists, add up the amount
    for bank_name in selected_banks:
        if bank_name in banks:
            bank = banks[bank_name]

            bank_expenses = getattr(bank, "expenses", {})
            bank_incomes = getattr(bank, "incomes", {})

            for expense, amount in bank_expenses.items():
                expenses[expense] = expenses.get(expense, 0) + amount

            for income, amount in bank_incomes.items():
                incomes[income] = incomes.get(income, 0) + amount

    return {
        "expenses": expenses,
        "incomes": incomes
    }
