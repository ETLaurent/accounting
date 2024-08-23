# Accounting

## Calculate Remaining Balance After Monthly Expenses 💸

### Overview

This script calculates how much is left in your balance after deducting monthly expenses. You can check expenses across multiple banks and exclude already paid expenses.

### Usage

```
usage: expenses [-h] [-b {a_bank,another_bank} [{a_bank,another_bank} ...]]
                [-p [{bank_fees,gym,newspaper,spotify,energy,mortgage,insurances} ...]]
                [-c [CURRENT_BALANCE]]

Determine the remaining balance after monthly expenses.

optional arguments:
  -h, --help            show this help message and exit
  -b {a_bank,another_bank} [{a_bank,another_bank} ...], --banks {a_bank,another_bank} [{a_bank,another_bank} ...]
                        Specify which banks to include in the calculation.
  -p [{bank_fees,gym,newspaper,spotify,energy,mortgage,insurances} ...], --paid [{bank_fees,gym,newspaper,spotify,energy,mortgage,insurances} ...]
                        List of expenses that have already been paid.
  -c [CURRENT_BALANCE], --current-balance [CURRENT_BALANCE]
                        Current balance before expenses.
```

### Examples

#### Check Remaining Expenses

- Across all banks

```sh
./run.py # or:
./run.py -b a_bank another_bank
./run.py --banks a_bank another_bank
```

_Output:_

```
🏦 expenses:

bank_fees: 51€
gym: 50€
newspaper: 13€
spotify: 9€
energy: 80€
mortgage: 1200€
insurances: 97€

💵 remaining expenses: 1500€
```

- On "a_bank"

```sh
./run.py -b a_bank
./run.py --banks a_bank
```

_Output:_

```
🏦 expenses:

bank_fees: 26€
gym: 50€
newspaper: 13€
spotify: 9€

💵 remaining expenses: 98€
```

- On "a_bank" minus paid expenses

```sh
./run.py -b a_bank -p gym spotify
./run.py --banks a_bank --paid gym spotify
```

_Output:_

```
🏦 expenses:

bank_fees: 26€
gym: 50€
newspaper: 13€
spotify: 9€

💸 removing paid expenses for a total of 59€:

gym: 50€
spotify: 9€

💵 remaining expenses: 39€
```

#### Check Balance After Expenses

- Across all banks

```sh
./run.py -c 1200
./run.py --current-balance 1200
```

_Output:_

```
🏦 expenses:

bank_fees: 51€
gym: 50€
newspaper: 13€
spotify: 9€
energy: 80€
mortgage: 1200€
insurances: 97€

💰 current balance: 1200€
💵 remaining expenses: 1500€
😭 remaining balance: -300€
```

- On "another_bank"

```sh
./run.py -c 1200 -b another_bank
./run.py --current-balance 1200 --banks another_bank
```

_Output:_

```
🏦 expenses:

bank_fees: 26€
energy: 80€
mortgage: 1200€
insurances: 97€

💰 current balance: 1200€
💵 remaining expenses: 1403€
😭 remaining balance: -203€
```

- On "another_bank" minus paid expenses

```sh
./run.py -c 1200 -b another_bank -p energy mortgage
./run.py --current-balance 1200 --banks another_bank --paid energy mortgage
```

_Output:_

```
🏦 expenses:

bank_fees: 26€
energy: 80€
mortgage: 1200€
insurances: 97€

💸 removing paid expenses for a total of 1280€:

energy: 80€
mortgage: 1200€

💰 current balance: 1200€
💵 remaining expenses: 123€
🤑 remaining balance: 1077€
```

### TODO

- Persist expenses to allow adding, removing, and updating them via the CLI.
- Add the option to configure the currency symbol.
- Implement unit tests 🙄
