import argparse
from banks import get_banks, get_expenses

def get_args():
    banks = get_banks()
    all_banks_expenses = get_expenses(banks)

    initial_parser = argparse.ArgumentParser(
        description='What\'s left in my balance after monthly expenses?'
    )

    initial_parser.add_argument(
        '-b',
        '--banks',
        help='which banks?',
        nargs='+',
        choices=list(banks),
        default=list(banks)
    )

    initial_parser.add_argument(
        '-p',
        '--paid',
        help='expenses already paid',
        nargs='*',
        default=[],
        choices=list(all_banks_expenses.keys())
    )

    initial_parser.add_argument(
        '-c',
        '--current-balance',
        help='current balance before expenses',
        type=int,
        nargs='?'
    )

    # Process known arguments first
    initial_args = initial_parser.parse_args()

    # Get expenses based on selected banks
    selected_banks_expenses = get_expenses(initial_args.banks)

    # Create a new parser and add all arguments
    final_parser = argparse.ArgumentParser(
        description='What\'s left in my balance after monthly expenses?'
    )

    final_parser.add_argument(
        '-b',
        '--banks',
        help='which banks?',
        nargs='+',
        choices=list(banks),
        default=list(banks)
    )

    final_parser.add_argument(
        '-p',
        '--paid',
        help='expenses already paid',
        nargs='*',
        default=[],
        choices=list(selected_banks_expenses.keys())
    )

    final_parser.add_argument(
        '-c',
        '--current-balance',
        help='current balance before expenses',
        type=int,
        nargs='?'
    )

    return final_parser.parse_args()
