#!/usr/bin/python3
import unicodedata
import math
from functools import reduce

from utils.cli import get_args
from utils.banks import get_transactions
from utils.string import strikethrough
from utils.currency import get_currency

def print_transactions(
    transactions,
    paid_or_received,
    get_transaction_message,
    get_total_message,
    get_remaining_message
):
    for transaction, amount in transactions.items():
        message = get_transaction_message(transaction, amount)

        if transaction in paid_or_received:
            print(f"  {strikethrough(message)}")
        else:
            print(f"  {message}")

    print()

    if transactions and paid_or_received:
        total_paid_or_received = sum(map(lambda paid: math.ceil(transactions[paid]), paid_or_received))
        print(f"  {get_total_message(total_paid_or_received)}")

        for transaction in paid_or_received:
            transactions.pop(transaction)

    total_remaining = reduce(lambda x, value: x + math.ceil(value), transactions.values(), 0)
    print(f"  {get_remaining_message(total_remaining)}")


args = get_args()
transactions = get_transactions(args.banks)

expenses = transactions["expenses"]
incomes = transactions["incomes"]

currency_before = ""
currency_after = ""

if args.currency:
    if args.currency.startswith("_"):
        currency_after = get_currency(args.currency.replace("_", ""))
    else:
        currency_before = get_currency(args.currency)

if expenses:
    print("🔥 Expenses 🔥")
    print()
    print_transactions(
        expenses,
        args.paid,
        lambda expense, amount: f"📈 {expense}: -{currency_before}{math.ceil(amount)}{currency_after}",
        lambda total_paid: f"😇 total paid: {currency_before}{total_paid}{currency_after}",
        lambda total_remaining: f"😒 total remaining: -{currency_before}{total_remaining}{currency_after}"
    )

if expenses and incomes:
    print()

if incomes:
    print("💧 Income 💧")
    print()
    print_transactions(
        incomes,
        args.received,
        lambda income, amount: f"📉 {income}: +{currency_before}{math.ceil(amount)}{currency_after}",
        lambda total_received: f"😈 total received: {currency_before}{total_received}{currency_after}",
        lambda total_remaining: f"🥲 total remaining: +{currency_before}{total_remaining}{currency_after}"
    )

if args.current_balance:
    balance = reduce(
        lambda x,
        value: x + math.ceil(value),
        incomes.values(),
        reduce(
            lambda x,
            value: x - math.ceil(value),
            expenses.values(),
            args.current_balance
        )
    )
    emoji = "🤑" if balance > 0 else "😭"
    print()
    print("⚖️ Balance ⚖️")
    print()
    print(f"  💸 current: {currency_before}{args.current_balance}{currency_after}")
    print(f"  {emoji} remaining: {currency_before}{balance}{currency_after}")

