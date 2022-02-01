def increase(price, rate):
    res = price + (price * rate / 100)
    return res


def decrease(price, rate):
    res = price - price * rate / 100
    return res


def double(price):
    res = price * 2
    return res


def half(price):
    res = price / 2
    return res