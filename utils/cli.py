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
        description='Determine the remaining balance after monthly transactions.',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '-c',
        '--currency',
        help=f'''Specify a currency symbol or provide a name to get the corresponding symbol (e.g "￥" or "yen").
Adding a leading underscore will place the currency before the amounts (e.g providing "_euro" will print "foo: +10€" instead of "foo: +€10".
Below is a list of supported currency names. A partial name (such as "yen") will be matched to one from that list.
If the given currency cannot be matched, it will be used as-is.
{sorted(currencies.keys())}''',
        nargs='?',
        default='DOLLAR SIGN'
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

    return parser.parse_args()
