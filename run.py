#!/usr/bin/python3
import unicodedata
import math
from functools import reduce

from utils.cli import get_args
from utils.banks import get_transactions, process_transactions
from utils.string import strikethrough
from utils.currency import get_currency

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
    process_transactions(
        expenses,
        args.paid,
        args.additional_expense_amounts,
        lambda expense, amount: f"📈 {expense}: -{currency_before}{math.ceil(amount)}{currency_after}",
        lambda paid: f"😇 total paid: {currency_before}{paid}{currency_after}",
        lambda remaining: f"😒 total remaining: -{currency_before}{remaining}{currency_after}"
    )

if expenses and incomes:
    print()

if incomes:
    print("💧 Income 💧")
    print()
    process_transactions(
        incomes,
        args.received,
        args.additional_income_amounts,
        lambda income, amount: f"📉 {income}: +{currency_before}{math.ceil(amount)}{currency_after}",
        lambda received: f"😈 total received: {currency_before}{received}{currency_after}",
        lambda remaining: f"🥲 total remaining: +{currency_before}{remaining}{currency_after}"
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

    current_emoji_map = {
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

    current_emoji = current_emoji_map[currency_before or currency_after]
    remaining_emoji = "🤑" if balance > 0 else "😭"

    print()
    print("⚖️ Balance ⚖️")
    print()
    print(f"  {current_emoji} current: {currency_before}{args.current_balance}{currency_after}")
    print(f"  {remaining_emoji} remaining: {currency_before}{balance}{currency_after}")

