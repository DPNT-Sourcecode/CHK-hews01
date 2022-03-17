import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    price_table = {
        "A": {"Price": 50, "Special Offers": [{'Units': 3, "Price": 130, 'PPU': 130/3}, {'Units': 5, "Price": 200, "PPU": 200/5}]},
        "B": {"Price": 30, "Special Offers": [{'Units': 2, "Price": 45, 'PPU': 45/2}]},
        "C": {"Price": 20},
        "D": {"Price": 15},
        "E": {"Price": 40}
    }

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
        sku_offers = sku_row.get('Special Offers')
        sku_counter = sku_count
        if sku_offers:
            while sku_counter != 0:
                sku_decrementer = 0
                current_ppu = math.inf
                for sku_offer in sku_offers:
                    sku_offer_units = sku_offer.get('Units')
                    sku_offer_price = sku_offer.get('Price')
                    sku_offer_ppu = sku_offer.get('PPU')

                    if sku_offer_ppu < current_ppu and sku_counter >= sku_offer_units:
                        sku_decrementer = sku_offer_units
                        total_price += sku_offer_price
                sku_counter -= sku_decrementer
                if not sku_decrementer:
                    total_price += sku_counter * unit_price
                    break
        else:
            total_price += unit_price * sku_count

    return total_price
