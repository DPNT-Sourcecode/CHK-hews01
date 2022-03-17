from errors.CHK_R1_errors import NotAString, NotInPriceTable


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        raise NotAString(skus)

    price_table = {
        "A": {"Price": 50, "Special Offers": {3: 30}},
        "B": {"Price": 30, "Special Offers": {2: 15}},
        "C": {"Price": 20},
        "D": {"Price": 15}
    }
    total_price = 0
    sku_collector = {}
    for sku in skus:
        sku_row = price_table.get(sku)
        if sku_row:
            if sku not in sku_collector.keys():
                sku_collector[sku] = 0

            sku_collector[sku] += 1
            price = sku_row["Price"]

            sku_offer = sku_row.get('Special Offers')
            if sku_offer:
                if sku_collector[sku] 



            total_price += price
        else:
            raise NotInPriceTable(skus)

    return total_price



