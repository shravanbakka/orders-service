def total(items):
    return sum(i["price"] * i["qty"] for i in items)


def apply_discount(amount, pct):
    return amount * (1 - pct / 100)
