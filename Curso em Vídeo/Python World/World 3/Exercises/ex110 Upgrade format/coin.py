def increase(price=0, rate=0, formatted=False):
    res = price + (price * rate / 100)
    return res if formatted is False else coin(price)


def decrease(price=0, rate=0, formatted=False):
    res = price - price * rate / 100
    return res if formatted is False else coin(price)


def double(price=0, formatted=False):
    res = price * 2
    return res if formatted is False else coin(price)


def half(price=0, formatted=False):
    res = price / 2
    return res if formatted is False else coin(price)


def coin(price=0, coin="R$"):
    return f"{coin}{price:.2f}".replace(".", ",")