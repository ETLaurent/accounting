import argparse
from banks import get_banks, get_expenses

def get_args():
    banks = get_banks()

    initial_parser = argparse.ArgumentParser(
        description='What\'s left in my balance after monthly expenses?'
    )

    initial_parser.add_argument(
        '-b',
        '--banks',
        help='which bank? (default: %(default)s)',
        nargs='+',
        default=list(banks)
    )

    # Process known arguments first
    initial_args, unknown_args = initial_parser.parse_known_args()

    # Calculate expenses based on selected banks
    expenses = get_expenses(initial_args.banks)

    # Create a new parser and add all arguments
    final_parser = argparse.ArgumentParser(
        description='What\'s left in my balance after monthly expenses?'
    )

    final_parser.add_argument(
        '-b',
        '--banks',
        help='which bank? (default: %(default)s)',
        nargs='+',
        default=initial_args.banks
    )

    final_parser.add_argument(
        '-p',
        '--paid',
        help='expenses already paid',
        metavar='EXPENSE',
        nargs='*',
        default=[],
        choices=list(expenses.keys())
    )

    final_parser.add_argument(
        '-c',
        '--current-balance',
        help='current balance before expenses',
        type=int,
        nargs='?'
    )

    # Parse the remaining arguments with the final parser
    final_args = final_parser.parse_args(unknown_args)

    return final_args
