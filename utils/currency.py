def strip(currency):
    return (currency or "").replace("_", "")


def get_price_fn(currency):
    if not currency:
        return lambda amount: amount

    if currency.startswith("_"):
        return lambda amount: f"{amount}{strip(currency)}"

    return lambda amount: f"{strip(currency)}{amount}"


def get_currency_emoji(currency):
    currency_emojis = {
        "$": "💵",
        "€": "💶",
        "£": "💷",
        "¥": "💴",
    }

    return currency_emojis.get(strip(currency), "💵")
