#!/usr/bin/python3
import math

from utils.cli import get_args
from utils.banks import get_transactions, process_transactions

args = get_args()
transactions = get_transactions(args.banks)

expenses = transactions["expenses"]
incomes = transactions["incomes"]

currency_before = ""
currency_after = ""

remaining_expenses = 0
remaining_income = 0

if args.currency.startswith("_"):
    currency_after = args.currency.replace("_", "")
else:
    currency_before = args.currency

if expenses or args.additional_expense_amounts:
    print("🔥 Expenses 🔥")
    print()
    remaining_expenses = process_transactions(
        expenses,
        args.paid,
        args.additional_expense_amounts,
        lambda expense, amount: f"📈 {expense}: -{currency_before}{math.ceil(amount)}{currency_after}",
        lambda paid: f"😇 total paid: {currency_before}{paid}{currency_after}",
        lambda remaining: f"😒 total remaining: -{currency_before}{remaining}{currency_after}"
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
        lambda income, amount: f"📉 {income}: +{currency_before}{math.ceil(amount)}{currency_after}",
        lambda received: f"😈 total received: {currency_before}{received}{currency_after}",
        lambda remaining: f"🥲 total remaining: +{currency_before}{remaining}{currency_after}"
    )

if args.current_balance:
    balance = args.current_balance - remaining_expenses + remaining_income
    minus_sign = "-" if balance < 0 else ""

    currency_emojis = {
        "$":    "💵",
        "＄":   "💵",
        "﹩":   "💵",
        "€":    "💶",
        "₠":    "💶",
        "£":    "💷",
        "￡":   "💷",
        "¥":    "💴",
        "￥":   "💴"
    }

    current_emoji = currency_emojis.get(
        currency_before or currency_after,
        "💵"
    )
    remaining_emoji = "🤑" if balance > 0 else "😭"

    print()
    print("⚖️ Balance ⚖️")
    print()
    print(f"  {current_emoji} current: {currency_before}{args.current_balance}{currency_after}")
    print(
        f"  {remaining_emoji} remaining: {args.current_balance}"
        f"{f' - {remaining_expenses}' if remaining_expenses else ''}"
        f"{f' + {remaining_income}' if remaining_income else ''}"
        f" = {minus_sign}{currency_before}{abs(balance)}{currency_after}"
    )
