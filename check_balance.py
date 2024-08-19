#!/usr/bin/python3
import sys
import math
from functools import reduce

sys.path.insert(0, './utils')

from cli import parse_arguments

args, expenses = parse_arguments()

# Output expenses in a more readable way
print('expenses:')
for expense, amount in expenses.items():
    print(f"  {expense}: {math.ceil(amount)}€")

# Remove already-paid expenses
if args.paid:
    total_paid = sum(map(lambda paid: math.ceil(expenses[paid]), args.paid))
    print()
    print(f"removing paid expenses for a total of {total_paid}€:")
    for expense in args.paid:
        print(f"  {expense}: {math.ceil(expenses[expense])}€")
        expenses.pop(expense)

# Calculate total expenses and current balance
remaining_expenses = reduce(lambda x, value: x + math.ceil(value), expenses.values(), 0)

print()
print(f"remaining expenses: {remaining_expenses}€")

if args.current_balance:
    balance = reduce(lambda x, value: x - math.ceil(value), expenses.values(), args.current_balance)
    print(f"balance: {balance}€")

