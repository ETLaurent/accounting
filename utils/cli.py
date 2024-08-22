import argparse
from banks import get_banks, get_expenses

def get_args():
    banks = get_banks()
    all_banks_expenses = get_expenses(banks)

    # Process known arguments first for help message to
    # display all arguments correctly
    initial_args = parse_args(banks, all_banks_expenses)

    # Get expenses based on selected banks
    selected_banks_expenses = get_expenses(initial_args.banks)

    # Process arguments again, this time with the selected banks
    # in order to get the correct choices for the --paid choices
    return parse_args(banks, selected_banks_expenses)

def parse_args(banks, banks_expenses):
    parser = argparse.ArgumentParser(
        description='What\'s left in my balance after monthly expenses?'
    )

    parser.add_argument(
        '-b',
        '--banks',
        help='which banks?',
        nargs='+',
        choices=list(banks),
        default=list(banks)
    )

    parser.add_argument(
        '-p',
        '--paid',
        help='expenses already paid',
        nargs='*',
        default=[],
        choices=list(banks_expenses)
    )

    parser.add_argument(
        '-c',
        '--current-balance',
        help='current balance before expenses',
        type=int,
        nargs='?'
    )

    return parser.parse_args()
