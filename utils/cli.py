import argparse
from utils.banks import get_banks, get_transactions

def get_args():
    banks = get_banks()
    banks_transactions = get_transactions(banks)

    # Process known arguments first for help message to
    # display all arguments correctly
    initial_args = parse_args(
        banks,
        banks_transactions["expenses"],
        banks_transactions["incomes"]
    )

    # Get transactions based on selected banks
    selected_banks_transactions = get_transactions(initial_args.banks)

    # Process arguments again, this time with the selected banks
    # in order to get the correct choices for the --paid choices
    return parse_args(
        banks,
        selected_banks_transactions["expenses"],
        selected_banks_transactions["incomes"]
    )

def parse_args(banks, expenses, incomes):
    parser = argparse.ArgumentParser(
        description='Determine the remaining balance after monthly transactions.'
    )

    parser.add_argument(
        '-b',
        '--banks',
        help='Specify which banks to include in the calculation.',
        nargs='+',
        choices=list(banks),
        default=list(banks)
    )

    parser.add_argument(
        '-p',
        '--paid',
        help='List of expenses that have already been paid.',
        nargs='*',
        default=[],
        choices=list(expenses)
    )

    parser.add_argument(
        '-r',
        '--received',
        help='List of income sources that have already been received.',
        nargs='*',
        default=[],
        choices=list(incomes)
    )

    parser.add_argument(
        '-c',
        '--current-balance',
        help='Current balance before transactions.',
        type=int,
        nargs='?'
    )

    return parser.parse_args()
