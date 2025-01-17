#!/usr/bin/python3
import math

from utils.cli import get_args
from utils.banks import get_transactions, process_transactions
from utils.string import bold
from utils.currency import strip, get_price_fn, get_currency_emoji

args = get_args()

currency = strip(args.currency)
price = get_price_fn(args.currency)
currency_emoji = get_currency_emoji(args.currency)

transactions = get_transactions(args.banks)
expenses = transactions["expenses"]
incomes = transactions["incomes"]

remaining_expenses = 0
remaining_income = 0

if expenses or args.additional_expense_amounts:
    print(f"🔥 {bold('Expenses')} 🔥")
    print()
    remaining_expenses = process_transactions(
        expenses,
        args.paid,
        args.additional_expense_amounts,
        lambda expense, amount: f"📈 {expense}: -{price(math.ceil(amount))}",
        lambda paid: f"😇 total paid: {price(paid)}",
        lambda remaining: f"😒 total remaining: {bold('-')}{bold(price(remaining))}",
    )

if (expenses or args.additional_expense_amounts) and (incomes or args.additional_income_amounts):
    print()

if incomes or args.additional_income_amounts:
    print(f"💧 {bold('Income')} 💧")
    print()
    remaining_income = process_transactions(
        incomes,
        args.received,
        args.additional_income_amounts,
        lambda income, amount: f"📉 {income}: +{price(math.ceil(amount))}",
        lambda received: f"😈 total received: {price(received)}",
        lambda remaining: f"🥲 total remaining: {bold('+')}{bold(price(remaining))}",
    )

if args.current_balance or args.current_balance == 0:
    balance = args.current_balance - remaining_expenses + remaining_income
    minus_sign = "-" if balance < 0 else ""

    remaining_emoji = "🤑" if balance > 0 else "😭"

    remaining_expenses_message = f" -{price(remaining_expenses)}" if remaining_expenses else ""
    remaining_income_message = f" +{price(remaining_income)}" if remaining_income else ""
    calculation = f"{price(args.current_balance)}{remaining_expenses_message}{remaining_income_message}"

    print()
    print(f"⚖️ {bold('Balance')} ⚖️")
    print()
    print(f"    {currency_emoji} current: {bold(price(args.current_balance))}")
    print(f"    {remaining_emoji} remaining: {calculation} = {bold(minus_sign)}{bold(price(abs(balance)))}")
