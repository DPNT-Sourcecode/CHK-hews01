import math


# noinspection PyUnusedLocal
# skus = unicode string

price_table = {
        "A": {"Price": 50, "Special Offers": [{'Units': 3, "Price": 130}, {'Units': 5, "Price": 200}]},
        "B": {"Price": 30, "Special Offers": [{'Units': 2, "Price": 45}]},
        "C": {"Price": 20},
        "D": {"Price": 15},
        "E": {"Price": 40, "Free Items": {'Units': 2, 'Item': "B"}},
        "F": {"Price": 10, "Free Items": {'Units': 3, 'Item': "F"}},
        'G': {"Price": 20},
        'H': {"Price": 10, "Special Offers": [{'Units': 5, "Price": 45}, {'Units': 10, "Price": 80}]},
        'I': {"Price": 35},
        'J': {"Price": 60},
        'K': {"Price": 70, "Special Offers": [{'Units': 2, "Price": 120}]},
        'L': {"Price": 90},
        'M': {"Price": 15},
        'N': {"Price": 40, "Free Items": {'Units': 3, 'Item': "M"}},
        'O': {"Price": 10},
        'P': {"Price": 50, "Special Offers": [{'Units': 5, "Price": 200}]},
        'Q': {"Price": 30, "Special Offers": [{'Units': 3, "Price": 80}]},
        'R': {"Price": 50, "Free Items": {'Units': 3, 'Item': "Q"}},
        'S': {"Price": 20},
        'T': {"Price": 20},
        'U': {"Price": 40, "Free Items": {'Units': 4, 'Item': "U"}},
        'V': {"Price": 50, "Special Offers": [{'Units': 2, "Price": 90}, {'Units': 3, "Price": 130}]},
        'W': {"Price": 20},
        'X': {"Price": 17},
        'Y': {"Price": 10},
        'Z': {"Price": 21},
    }


def checkout(skus):

    if not isinstance(skus, str):
        return -1

    sku_collector = {}
    for sku in skus:
        sku_row = price_table.get(sku)
        if sku_row:
            if sku not in sku_collector.keys():
                sku_collector[sku] = 0
            sku_collector[sku] += 1
        else:
            return -1

    for sku in sku_collector.keys():
        sku_count = sku_collector[sku]
        sku_row = price_table[sku]

        sku_free_items = sku_row.get('Free Items')
        sku_counter = sku_count
        if sku_free_items:
            sku_free_item_units = sku_free_items['Units']
            sku_free_item = sku_free_items['Item']

            if sku_free_item in sku_collector.keys():
                while sku_counter != 0:
                    if sku_counter - sku_free_item_units >= 0:
                        sku_counter -= sku_free_item_units
                        if sku_collector[sku_free_item] > 0:
                            sku_collector[sku_free_item] -= 1
                    else:
                        break

    total_price = 0
    for sku in sku_collector.keys():
        sku_count = sku_collector[sku]
        sku_row = price_table[sku]
        unit_price = sku_row["Price"]
        sku_offers = sku_row.get('Special Offers')
        sku_counter = sku_count
        if sku_offers:
            while sku_counter != 0:
                sku_decrementer = 0
                current_offer_price = 0
                current_ppu = math.inf
                for sku_offer in sku_offers:
                    sku_offer_units = sku_offer.get('Units')
                    sku_offer_price = sku_offer.get('Price')
                    sku_offer_ppu = sku_offer_price/sku_offer_units

                    if sku_offer_ppu < current_ppu and sku_counter >= sku_offer_units:
                        sku_decrementer = sku_offer_units
                        current_ppu = sku_offer_ppu
                        current_offer_price = sku_offer_price

                total_price += current_offer_price
                sku_counter -= sku_decrementer
                if not sku_decrementer:
                    total_price += sku_counter * unit_price
                    break
        else:
            total_price += unit_price * sku_count

    return total_price



