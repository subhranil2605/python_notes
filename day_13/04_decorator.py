# Plain function
# DRY - Don't Repeat Yourself


def checkout(prices):
    # logging
    print("calling checkout")
    total = sum(prices)
    print("checkout finished")
    return total


def price_with_tax(price, rate):
    # logging
    print("calling price_with_tax")
    total = round(price * (1 + rate), 2)
    print("price_with_tax finished")
    return total


print(checkout([100, 60, 78]))
print(price_with_tax(40.5, 0.18))
