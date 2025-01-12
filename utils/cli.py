import argparse

from utils.banks import get_banks, get_transactions

def get_args():
    banks = get_banks()
    banks_transactions = get_transactions(banks)

    # Process known arguments first for help message to
    # display all arguments correctly
    initial_args = parse_args(banks, banks_transactions)

    # Get transactions based on selected banks
    selected_banks_transactions = get_transactions(initial_args.banks)

    # Process arguments again, this time with the selected banks
    # in order to get the correct choices for the --paid and --received choices
    return parse_args(banks, selected_banks_transactions)

def parse_args(banks, transactions):
    parser = argparse.ArgumentParser(
        description="Determine the remaining balance after monthly transactions."
    )

    parser.add_argument(
        '-c',
        '--currency',
        help='Currency symbol (e.g "￥", "€"...). Adding a leading underscore will place the currency before the amounts (e.g specifying "_€" will print "foo: +10€" instead of "foo: +€10".',
        nargs='?',
        default='$'
    )

    parser.add_argument(
        '-a',
        '--banks',
        help="Banks to use in the calculation.",
        nargs='+',
        default=banks,
        choices=banks
    )

    parser.add_argument(
        '-p',
        '--paid',
        help="Expense names to be removed from the calculation.",
        nargs='*',
        default=[],
        choices=transactions["expenses"]
    )

    parser.add_argument(
        '-r',
        '--received',
        help="Income names to be removed from the calculation.",
        nargs='*',
        default=[],
        choices=transactions["incomes"]
    )

    parser.add_argument(
        '-e',
        '--additional-expense-amounts',
        help="Expense amounts to add to the calculation.",
        type=int,
        nargs="*",
        default=[]
    )

    parser.add_argument(
        '-i',
        '--additional-income-amounts',
        help="Income amounts to add to the calculation.",
        type=int,
        nargs="*",
        default=[]
    )

    parser.add_argument(
        '-b',
        '--current-balance',
        help="Current balance before calculation.",
        type=int,
        nargs='?'
    )

    return parser.parse_args()
