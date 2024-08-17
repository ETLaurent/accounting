import sys
import os
import importlib
import argparse

def get_banks():
    files = [f for f in os.listdir('./banks') if f.endswith('.py')]
    banks = {}

    for file in files:
        bank_name = file[:-3]  # Remove the '.py' extension
        banks[bank_name] = importlib.import_module(bank_name).expenses

    return banks


def parse_arguments():
    available_banks = get_banks()
    print(list(available_banks))

    # Initial parsing to get the selected banks
    parser = argparse.ArgumentParser(
        description='What\'s left in my balance after monthly expenses?'
    )

    parser.add_argument(
        'balance',
        help='current balance (default: %(default)s)',
        type=int,
        nargs='?',
        default=0
    )

    parser.add_argument(
        '-b',
        '--banks',
        help='which bank? (default %(default)s)',
        nargs='+',
        default=list(available_banks)
    )

    # We need to parse once to get the banks argument
    args, remaining_args = parser.parse_known_args()

    # Initialize an empty dictionary to store the combined expenses
    selected_expenses = {}

    # Loop through the selected banks and add up expenses
    for bank in args.banks:
        if bank in available_banks:
            for expense, amount in available_banks[bank].items():
                if expense in selected_expenses:
                    selected_expenses[expense] += amount  # Add to existing expense
                else:
                    selected_expenses[expense] = amount  # Create new entry

    # Rebuild the parser with the updated `choices` for the `--paid` argument
    parser.add_argument(
        '-p',
        '--paid',
        help='expenses already paid',
        metavar='EXPENSE',
        nargs='*',
        default=[],
        choices=list(selected_expenses.keys())
    )

    # Parse again with the full set of arguments
    args = parser.parse_args(remaining_args)
    
    return args, selected_expenses
