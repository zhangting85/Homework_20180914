def disprice(or_price):
    now_price = or_price - int(or_price / 80) * 20
    return now_price


def disprice2(or_price):
    now_price = or_price * 0.85
    return now_price


print(disprice(350))
print(disprice2(350))
