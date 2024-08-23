# Accounting

## Check how much is left after recurring expenses 💸

### Usage

```
usage: expenses [-h] [-b {a_bank,another_bank} [{a_bank,another_bank} ...]]
                [-p [{bank_fees,gym,newspaper,spotify,energy,mortgage,insurances} ...]]
                [-c [CURRENT_BALANCE]]

What's left in my balance after monthly expenses?

optional arguments:
  -h, --help            show this help message and exit
  -b {a_bank,another_bank} [{a_bank,another_bank} ...], --banks {a_bank,another_bank} [{a_bank,another_bank} ...]
                        which banks?
  -p [{bank_fees,gym,newspaper,spotify,energy,mortgage,insurances} ...], --paid [{bank_fees,gym,newspaper,spotify,energy,mortgage,insurances} ...]
                        expenses already paid
  -c [CURRENT_BALANCE], --current-balance [CURRENT_BALANCE]
                        current balance before expenses
```

### Examples

#### Check remaining expenses

- On every banks

```sh
./run.py # or:
./run.py --banks a_bank another_bank

# output:
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

- On "a_banks"

```sh
🏦 expenses:

bank_fees: 26€
gym: 50€
newspaper: 13€
spotify: 9€

💵 remaining expenses: 98€
```

- On "a_banks" minus expenses already paid

```sh
./run.py --banks a_bank --paid gym spotify

# output:
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

#### Check balance

- On every banks

```sh
./run.py --current-balance 1200 # or:
./run.py --current-balance 1200 --banks a_bank another_bank

# output:
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
./run.py --current-balance 1200 --banks another_bank

# output:
🏦 expenses:

bank_fees: 26€
energy: 80€
mortgage: 1200€
insurances: 97€

💰 current balance: 1200€
💵 remaining expenses: 1403€
😭 remaining balance: -203€
```

- On "another_banks" minus expenses already paid

```sh
./run.py --current-balance 1200 --banks another_bank --paid energy mortgage

# output:
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

- persist expenses, in order to add, remove and update them via the CLI
- add the possibility to configure the money sign
- add unit tests 🙄
