#!/usr/bin/python3
import sys
from functools import reduce
import math  # Import the math module for rounding up

sys.path.insert(0, './banks')
sys.path.insert(0, './utils')

from cli import parse_arguments

args, expenses = parse_arguments()

print(f"expenses: {expenses}")
print()

# Remove already-paid expenses
for expense in args.paid:
    print(f"removing {expense} expense of {expenses[expense]}€")
    expenses.pop(expense)

if args.paid:
    print()

# Calculate total expenses and current balance
total_expenses = reduce(lambda x, value: x + value, expenses.values(), 0)
current_balance = reduce(lambda x, value: x - value, expenses.values(), args.balance)

# Round up the results
total_expenses = math.ceil(total_expenses)
current_balance = math.ceil(current_balance)

print(f"current balance: {args.balance}€")
print(f"expenses left: {total_expenses}€")
print()
print(f"balance: {current_balance}€")
