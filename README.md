# Accounting

## Calculate Remaining Balance After Monthly Transactions 💸

### Overview

This script calculates how much is left in your balance after deducting monthly expenses.

### Notes

> App is written in Python because it's wildly included by default in most of Linux and macOS systems.  
> It's also a good occasion for me to ~use~ learn Python (code isn't state-of-the-art, far from it).  
> It's a CLI usage, there is no web server, to keep it simple. However, persistence would be a good thing, and is the next milestone.

### Usage

```
usage: run.py [-h] [-c [CURRENCY]] [-a {a_bank,another_bank} [{a_bank,another_bank} ...]]
              [-p [{bank_fees,gym,newspaper,spotify,energy,mortgage,insurances} ...]]
              [-r [{salary,rent} ...]]
              [-e [ADDITIONAL_EXPENSE_AMOUNTS ...]]
              [-i [ADDITIONAL_INCOME_AMOUNTS ...]] [-b [CURRENT_BALANCE]]

Determine the remaining balance after monthly transactions.

optional arguments:
  -h, --help            show this help message and exit
  -c [CURRENCY], --currency [CURRENCY]
                        Currency symbol to show. Adding a leading underscore will place the symbol before the amount.
                        For instance, "_€" will print "foo: +10€" instead of "foo: +€10".
  -a {a_bank,another_bank} [{a_bank,another_bank} ...], --banks {a_bank,another_bank} [{a_bank,another_bank} ...]
                        Banks to use in the calculation.
  -p [{bank_fees,gym,newspaper,spotify,energy,mortgage,insurances} ...], --paid [{bank_fees,gym,newspaper,spotify,energy,mortgage,insurances} ...]
                        Expense names to be removed from the calculation.
  -r [{salary,rent} ...], --received [{salary,rent} ...]
                        Income names to be removed from the calculation.
  -e [ADDITIONAL_EXPENSE_AMOUNTS ...], --additional-expense-amounts [ADDITIONAL_EXPENSE_AMOUNTS ...]
                        Expense amounts to add to the calculation.
  -i [ADDITIONAL_INCOME_AMOUNTS ...], --additional-income-amounts [ADDITIONAL_INCOME_AMOUNTS ...]
                        Income amounts to add to the calculation.
  -b [CURRENT_BALANCE], --current-balance [CURRENT_BALANCE]
                        Current balance before calculation.
```

### Examples

> Note: ANSI terminals will support dim, bold and italic style which are not showed in the following examples.

#### Check Balance for a Specific Bank

```sh
./run.py --current-balance 1200 --banks a_bank --paid gym 
```

_Output:_

```
🔥 Expenses 🔥

    📈 bank_fees: -$26
    📈̶ ̶g̶y̶m̶:̶ ̶-̶$̶5̶0̶
    📈 newspaper: -$13
    📈 spotify: -$9

    😇 total paid: $50
    😒 total remaining: -$48

⚖️ Balance ⚖️

    💵 current: $1200
    🤑 remaining: $1200 -$48 = $1152
```

#### Show all Remaining Expenses and Income

```sh
./run.py --paid gym spotify --received rent
```

_Output:_

```
🔥 Expenses 🔥

    📈 bank_fees: -$51
    📈̶ ̶g̶y̶m̶:̶ ̶-̶$̶5̶0̶
    📈 newspaper: -$13
    📈̶ ̶s̶p̶o̶t̶i̶f̶y̶:̶ ̶-̶$̶9̶
    📈 energy: -$80
    📈 mortgage: -$1200
    📈 insurances: -$97

    😇 total paid: $59
    😒 total remaining: -$1441

💧 Income 💧

    📉 salary: +$2000
    📉̶ ̶r̶e̶n̶t̶:̶ ̶+̶$̶5̶5̶0̶

    😈 total received: $550
    🥲 total remaining: +$2000
```

#### Add additional Income and Expenses

```sh
./run.py --additional-expense-amounts 95 4 6 --additional-income-amounts 790 10
```

_Output:_

```
🔥 Expenses 🔥

    📈 bank_fees: -$51
    📈 gym: -$50
    📈 newspaper: -$13
    📈 spotify: -$9
    📈 energy: -$80
    📈 mortgage: -$1200
    📈 insurances: -$97
    📈 ADDITIONAL AMOUNT 💸: -$105

    😒 total remaining: -$1605

💧 Income 💧

    📉 salary: +$2000
    📉 rent: +$550
    📉 ADDITIONAL AMOUNT 💸: +$800

    🥲 total remaining: +$3350
```

#### Specify a Currency

```sh
./run.py --currency ₹
```

_Output:_

```
🔥 Expenses 🔥

    📈 bank_fees: -₹51
    📈 gym: -₹50
    📈 newspaper: -₹13
    📈 spotify: -₹9
    📈 energy: -₹80
    📈 mortgage: -₹1200
    📈 insurances: -₹97

    😒 total remaining: -₹1500

💧 Income 💧

    📉 salary: +₹2000
    📉 rent: +₹550

    🥲 total remaining: +₹2550
```

#### Specify a Trailing Currency

```sh
./run.py --currency _€
```

_Output:_

```
🔥 Expenses 🔥

    📈 bank_fees: -51€
    📈 gym: -50€
    📈 newspaper: -13€
    📈 spotify: -9€
    📈 energy: -80€
    📈 mortgage: -1200€
    📈 insurances: -97€

    😒 total remaining: -1500€

💧 Income 💧

    📉 salary: +2000€
    📉 rent: +550€

    🥲 total remaining: +2550€
```

#### Mix All the Things

```sh
./run.py \
    --currency _€ \
    --current-balance 1200 \
    --banks a_bank another_bank \
    --paid gym spotify \
    --received rent \
    --additional-expense-amounts 95 4 6 \
    --additional-income-amounts 790 10
```

_Output:_

```
🔥 Expenses 🔥

    📈 bank_fees: -51€
    📈̶ ̶g̶y̶m̶:̶ ̶-̶5̶0̶€̶
    📈 newspaper: -13€
    📈̶ ̶s̶p̶o̶t̶i̶f̶y̶:̶ ̶-̶9̶€̶
    📈 energy: -80€
    📈 mortgage: -1200€
    📈 insurances: -97€
    📈 ADDITIONAL AMOUNT 💸: -105€

    😇 total paid: 59€
    😒 total remaining: -1546€

💧 Income 💧

    📉 salary: +2000€
    📉̶ ̶r̶e̶n̶t̶:̶ ̶+̶5̶5̶0̶€̶
    📉 ADDITIONAL AMOUNT 💸: +800€

    😈 total received: 550€
    🥲 total remaining: +2800€

    ⚖️ Balance ⚖️

    💶 current: 1200€
    🤑 remaining: 1200 -$1546 +$2800 = 2454€
```

### TODO

- Persist expenses to allow adding, removing, and updating them via the CLI.
- Implement unit tests 🙄
- Publish package
- Add labels:

```py
incomes = {
    "bbr" = {
        "label": "BBR Salary",
        "amount": 3200.00
    }
}
```
