#!/usr/bin/python3

import sys
import argparse

from functools import reduce
from expenses import professional as professional_expenses, personal as personal_expenses

# --- CLI Arguments (not at the top in order to access expenses above for --paid argument choices)
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
        '-p',
        '--paid',
        help ='expenses already paid',
        metavar='EXPENSE',
        nargs='*',
        default=[],
        choices=professional_expenses.keys() if '--pro' in sys.argv else personal_expenses.keys()
)
parser.add_argument(
        '--pro',
        help ='use expenses for a professional bank account balance',
        action='store_true'
)
args = parser.parse_args()
# ---

# using professional or personal account
expenses = professional_expenses if args.pro else personal_expenses

print(f"expenses: {expenses}")
print()

# remove already-paid expenses
for expense in args.paid:
        print(f"removing {expense} expense of {expenses[expense]}€")
        expenses.pop(expense)

if args.paid:
        print()

total_expenses = reduce(lambda x, value:x + value, expenses.values(), 0)
current_balance = reduce(lambda x, value:x - value, expenses.values(), args.balance)

print(f"current balance: {args.balance}€")
print(f"expenses left: {total_expenses}€")
print()
print(f"balance: {current_balance}€")
