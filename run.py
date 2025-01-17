#!/usr/bin/python3
import math

from utils.cli import get_args
from utils.banks import get_transactions, process_transactions
from utils.string import italic

args = get_args()
transactions = get_transactions(args.banks)

expenses = transactions["expenses"]
incomes = transactions["incomes"]

currency_before = ""
currency_after = ""

remaining_expenses = 0
remaining_income = 0

if args.currency:
    if args.currency.startswith("_"):
        currency_after = args.currency.replace("_", "")
    else:
        currency_before = args.currency


def price(amount):
    return f"{currency_before}{amount}{currency_after}"


if expenses or args.additional_expense_amounts:
    print("🔥 Expenses 🔥")
    print()
    remaining_expenses = process_transactions(
        expenses,
        args.paid,
        args.additional_expense_amounts,
        lambda expense, amount: f"📈 {expense}: -{price(math.ceil(amount))}",
        lambda paid: f"😇 total paid: {price(paid)}",
        lambda remaining: f"😒 total remaining: -{price(remaining)}",
    )

if (expenses or args.additional_expense_amounts) and (incomes or args.additional_income_amounts):
    print()

if incomes or args.additional_income_amounts:
    print("💧 Income 💧")
    print()
    remaining_income = process_transactions(
        incomes,
        args.received,
        args.additional_income_amounts,
        lambda income, amount: f"📉 {income}: +{price(math.ceil(amount))}",
        lambda received: f"😈 total received: {price(received)}",
        lambda remaining: f"🥲 total remaining: +{price(remaining)}",
    )

if args.current_balance or args.current_balance == 0:
    balance = args.current_balance - remaining_expenses + remaining_income
    minus_sign = "-" if balance < 0 else ""

    currency_emojis = {
        "$": "💵",
        "€": "💶",
        "£": "💷",
        "¥": "💴",
    }
    current_emoji = currency_emojis.get(currency_before or currency_after, "💵")
    remaining_emoji = "🤑" if balance > 0 else "😭"

    remaining_expenses_message = f" -{remaining_expenses}" if remaining_expenses else ""
    remaining_income_message = f" +{remaining_income}" if remaining_income else ""
    calculation = f"{args.current_balance}{remaining_expenses_message}{remaining_income_message}"

    print()
    print("⚖️ Balance ⚖️")
    print()
    print(f"    {current_emoji} current: {price(args.current_balance)}")
    print(f"    {remaining_emoji} remaining: {italic(calculation)} = {minus_sign}{price(abs(balance))}")
