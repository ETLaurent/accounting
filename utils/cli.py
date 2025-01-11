import argparse

from utils.banks import get_banks, get_transactions
from utils.currency import get_currencies

def get_args():
    banks = get_banks()
    banks_transactions = get_transactions(banks)
    currencies = get_currencies()

    # Process known arguments first for help message to
    # display all arguments correctly
    initial_args = parse_args(
        banks,
        banks_transactions,
        currencies
    )

    # Get transactions based on selected banks
    selected_banks_transactions = get_transactions(initial_args.banks)

    # Process arguments again, this time with the selected banks
    # in order to get the correct choices for the --paid and --received choices
    return parse_args(
        banks,
        selected_banks_transactions,
        currencies
    )

def parse_args(banks, transactions, currencies):
    parser = argparse.ArgumentParser(
        description='Determine the remaining balance after monthly transactions.'
    )

    parser.add_argument(
        '-a',
        '--banks',
        help='Specify which banks to include in the calculation.',
        nargs='+',
        default=list(banks),
        choices=list(banks)
    )

    parser.add_argument(
        '-p',
        '--paid',
        help='List of expenses that have already been paid.',
        nargs='*',
        default=[],
        choices=list(transactions["expenses"])
    )

    parser.add_argument(
        '-r',
        '--received',
        help='List of income sources that have already been received.',
        nargs='*',
        default=[],
        choices=list(transactions["incomes"])
    )

    parser.add_argument(
        '-b',
        '--current-balance',
        help='Current balance before transactions.',
        type=int,
        nargs='?'
    )

    parser.add_argument(
        '-c',
        '--currency',
        help=f'''Use a specific currency.
        Example: pass "€" or write "euro" to find the corresponding symbol among:
        {sorted(currencies.keys())}''',
        nargs='?',
        default='DOLLAR SIGN'
    )

    return parser.parse_args()
