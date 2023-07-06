# Accounting

## Check balance after expenses left

### Usage

```
usage: check_balance.py [-h] [-p [EXPENSE ...]] [--pro] [balance]

What's left in my balance after monthly expenses?

positional arguments:
  balance                                 current balance (default: 0)

optional arguments:
  -h, --help                              show this help message and exit
  -p [EXPENSE ...], --paid [EXPENSE ...]  expenses already paid
  --pro                                   pro expenses
```

### Examples

```sh
# check current balance of 123 after monthly expenses
./check_balance.py 123

# output:
expenses: {'rent': 850, 'insurance': 60, 'spotify': 10}

current balance: 123€
expenses left: 920€

balance: -797€
```

```sh
# check current balance of 321 after monthly professional expenses
./check_balance.py 321 --pro

# output:
expenses: {'bank': 10, 'internet': 30}

current balance: 321€
expenses left: 40€

balance: 281€
```

```sh
# check current balance of 123 after monthly expenses
# minus expenses already paid
./check_balance.py 123 --paid rent spotify

# output:
expenses: {'rent': 850, 'insurance': 60, 'spotify': 10}

removing rent expense of 850€
removing spotify expense of 10€

current balance: 123€
expenses left: 60€

balance: 63€
```

```sh
# check current balance of 321 after monthly professional expenses
# minus expenses already paid
./check_balance.py 321 --pro -p internet

# output:
expenses: {'bank': 10, 'internet': 30}

removing internet expense of 30€

current balance: 321€
expenses left: 10€

balance: 311€
```

```sh
# check current balance of 0 after monthly expenses
./check_balance.py

# output:
expenses: {'rent': 850, 'insurance': 60, 'spotify': 10}

current balance: 0€
expenses left: 920€

balance: -920€
```

```sh
# check current balance of 0 after monthly pro expenses
./check_balance.py --pro

# output:
expenses: {'bank': 10, 'internet': 30}

current balance: 0€
expenses left: 40€

balance: -40€
```

```sh
# check current balance of 0 after monthly pro expenses
# minus expenses already paid
./check_balance.py --pro --paid bank

# output:
expenses: {'bank': 10, 'internet': 30}

removing bank expense of 10€

current balance: 0€
expenses left: 30€

balance: -30€
```

### TODO

- persist expenses, in order to add, remove and update them via the CLI
- add the possibility to configure the money sign