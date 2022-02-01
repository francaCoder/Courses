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


def summary(price=0, rate=10, tax=5):
    print("-"*30)
    print("VALUE'S SUMMARY".center(30))
    print("-"*30)
    print(f"Price → \t{coin(price)}")
    print(f"Double → \t{double(price, True)}")
    print(f"Half → \t{half(price, True)}")
    print(f"Increasing {rate}% → \t{increase(price, True)}")
    print(f"Decreasing {tax}% → \t{decrease(price, True)}")