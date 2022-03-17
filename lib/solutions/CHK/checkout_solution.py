

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        "A": {"Price": 50, "Special Offers": {3: 130}},
        "B": {"Price": 30, "Special Offers": {2: 45}},
        "C": {"Price": 20},
        "D": {"Price": 15}
    }

    sku_row = price_table.get(skus)
    if sku_row:
        price = sku_row["Price"]
        return price


