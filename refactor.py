from forex_python.converter import CurrencyRates, CurrencyCodes


def convert(convertFrom, convertTo, amount):
    c = CurrencyRates()
    s = CurrencyCodes()

    convertFrom = convertFrom.upper()
    convertTo = convertTo.upper()
    if float(amount) <= 0:
        amount = 0.0
    else:
        amount = float(amount)

    symbol = s.get_symbol(convertTo)

    result = f'{symbol}{round(c.convert(convertFrom, convertTo, amount), 2)}'

    return result
