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
                sku_offer_price = sku_offers.get(sku_count)
                if sku_offer_price:
                    total_price -= price * sku_count
                    total_price += sku_offer_price

        else:
            raise NotInPriceTable(skus)

    return total_price




