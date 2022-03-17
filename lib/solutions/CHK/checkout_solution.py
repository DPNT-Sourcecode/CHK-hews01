from errors.CHK_R1_errors import NotAString, NotInPriceTable


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    price_table = {
        "A": {"Price": 50, "Special Offers": [{'Units': 3, "Price": 130}, {'Units': 5, "Price": 200}]},
        "B": {"Price": 30, "Special Offers": [{'Units': 2, "Price": 45}]},
        "C": {"Price": 20},
        "D": {"Price": 15},
        "E": {"Price": 40}
    }
    total_price = 0
    sku_collector = {}
    for sku in skus:
        sku_row = price_table.get(sku)
        if sku_row:
            if sku not in sku_collector.keys():
                sku_collector[sku] = 0
            sku_collector[sku] += 1
        else:
            return -1
    total_price = 0
    for sku in sku_collector.keys():
        sku_count = sku_collector[sku]
        unit_price = sku_row["Price"]
        total_price += unit_price * sku_count

        sku_offers = sku_row.get('Special Offers')

        #if sku_offers:
            #sku_offer_units = sku_offers.get('Units')
            #sku_offer_price = sku_offers.get('Price')

    return total_price


