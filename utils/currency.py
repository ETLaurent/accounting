import unicodedata

#  Returns { "DOLLAR SIGN": "$", ... }
def get_currencies():
    currencies = {}

    for codepoint in range(0x110000):
        char = chr(codepoint)
        if unicodedata.category(char) == "Sc":
            currencies[unicodedata.name(char)] = char

    return currencies

def get_currency(currency):
    currencies = get_currencies()

    if currency in currencies.keys():
        return currencies[currency]

    found = next(
        (
            currency_name
            for currency_name in sorted(currencies.keys())
            if currency.casefold() in currency_name.casefold()
        ),
        None
    )

    if found:
        return currencies[found]

    # If not found, simply use the given currency
    return currency
