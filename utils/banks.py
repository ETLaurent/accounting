import sys
import os
import importlib
import math

from functools import reduce
from utils.string import dim, italic

# meh, this is a bit hacky,
# but it works... we get the banks from the banks directory
script_dir = os.path.dirname(os.path.realpath(__file__))
bank_dir = os.path.join(script_dir, '../banks')
sys.path.insert(0, bank_dir)


def get_banks():
    files = [f for f in os.listdir(bank_dir) if f.endswith('.py')]
    banks = {}

    for file in files:
        bank_name = file[:-3]  # Remove the '.py' extension
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
        "incomes": incomes,
    }


def process_transactions(
    expenses_or_incomes,
    paid_or_received,
    additional_amounts,
    get_transaction_message,
    get_total_message,
    get_remaining_message
):
    if additional_amounts:
        if not expenses_or_incomes:
            expenses_or_incomes = {}

        key = f"{italic('ADDITIONAL AMOUNT')} 💸"
        expenses_or_incomes[key] = sum(additional_amounts)

    for expense_or_income, amount in expenses_or_incomes.items():
        message = get_transaction_message(expense_or_income, amount)

        if expense_or_income in paid_or_received:
            print(f"    {dim(message)}")
        else:
            print(f"    {message}")

    print()

    if expenses_or_incomes and paid_or_received:
        total_paid_or_received = sum(
            map(
                lambda paid: math.ceil(expenses_or_incomes[paid]),
                paid_or_received
            )
        )
        print(f"    {get_total_message(total_paid_or_received)}")

        for expense_or_income in paid_or_received:
            expenses_or_incomes.pop(expense_or_income)

    total_remaining = reduce(
        lambda x,
        value: x + math.ceil(value),
        expenses_or_incomes.values(),
        0
    )
    print(f"    {get_remaining_message(total_remaining)}")

    return total_remaining
