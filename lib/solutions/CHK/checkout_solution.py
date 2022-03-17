from errors.CHK_R1_errors import NotAString, NotInPriceTable


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    price_table = {
        "A": {"Price": 50, "Special Offers": {'Units': 3, "Price": 130}},
        "B": {"Price": 30, "Special Offers": {'Units': 2, "Price": 45}},
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
            sku_count = sku_collector[sku]

            price = sku_row["Price"]
            total_price += price

            sku_offers = sku_row.get('Special Offers')
            if sku_offers:
                sku_offer_units = sku_offers.get('Units')
                sku_offer_price = sku_offers.get('Price')
                if sku_count % sku_offer_units == 0:
                    total_price -= price * sku_offer_units
                    total_price += sku_offer_price
        else:
            return -1

    return total_price





