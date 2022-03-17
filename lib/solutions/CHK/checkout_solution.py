from errors.CHK_R1_errors import NotAString, NotInPriceTable


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        raise NotAString(skus)

    price_table = {
        "A": {"Price": 50, "Special Offers": {3: 130}},
        "B": {"Price": 30, "Special Offers": {2: 45}},
        "C": {"Price": 20},
        "D": {"Price": 15}
    }
    total_price = 0
    for sku in skus:
        sku_row = price_table.get(sku)
        if sku_row:
            price = sku_row["Price"]
            total_price += price
        else:
            raise NotInPriceTable(skus)

    return total_price


