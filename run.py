#!/usr/bin/python3
import math
from functools import reduce

from utils.cli import get_args
from utils.banks import get_transactions

args = get_args()
transactions = get_transactions(args.banks)

expenses = transactions["expenses"]
incomes = transactions["incomes"]

print('🏦 expenses:')
print()
for expense, amount in expenses.items():
    print(f"{expense}: {math.ceil(amount)}€")

# Remove already-paid expenses
if args.paid:
    total_paid = sum(map(lambda paid: math.ceil(expenses[paid]), args.paid))
    print()
    print(f"💸 removing paid expenses for a total of {total_paid}€:")
    print()

    for expense in args.paid:
        print(f"{expense}: {math.ceil(expenses[expense])}€")
        expenses.pop(expense)

# Calculate total expenses and current balance
remaining_expenses = reduce(lambda x, value: x + math.ceil(value), expenses.values(), 0)

print()
if args.current_balance:
    print(f"💰 current balance: {args.current_balance}€")

print(f"💵 remaining expenses: {remaining_expenses}€")

if args.current_balance:
    balance = reduce(lambda x, value: x - math.ceil(value), expenses.values(), args.current_balance)
    emoji = "🤑" if balance > 0 else "😭"
    print(f"{emoji} remaining balance: {balance}€")

