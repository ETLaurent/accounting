import sys
import os
import importlib
import argparse

sys.path.insert(0, './banks')

def get_banks():
    files = [f for f in os.listdir('./banks') if f.endswith('.py')]
    banks = {}

    for file in files:
        bank_name = file[:-3]  # Remove the '.py' extension
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

def parse_arguments():
    banks = get_banks()

    parser = argparse.ArgumentParser(
        description='What\'s left in my balance after monthly expenses?'
    )

    parser.add_argument(
        '-b',
        '--banks',
        help='which bank? (default: %(default)s)',
        nargs='+',
        default=list(banks)
    )

    # Process known arguments first
    args, remaining_args = parser.parse_known_args()

    # Calculate expenses based on selected banks
    expenses = get_expenses(args.banks)

    # Rebuild parser with the `--paid` argument
    parser.add_argument(
        '-p',
        '--paid',
        help='expenses already paid',
        metavar='EXPENSE',
        nargs='*',
        default=[],
        choices=list(expenses.keys())
    )

    parser.add_argument(
        '-c',
        '--current-balance',
        help='current balance before expenses',
        type=int,
        nargs='?'
    )

    # Parse the remaining arguments
    args = parser.parse_args(remaining_args)

    return args, expenses
