
'''
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
'''

def get_skus():
    return {
        'A': {'price':50, 'offers': [{'amount': 3, 'price': 130}]},
        'B': {'price':30, 'offers': [{'amount': 2, 'price': 45}]},
        'C': {'price':20, 'offers': []},
        'D': {'price':15, 'offers': []}
    }


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(basket):
    skus = get_skus()

    if list(set(basket) - set(skus.keys())):
        return -1

    total_price = 0
    for (sku, options) in skus.iteritems():
        amount = basket.count(sku)
        for offer in options['offers']:
            while offer['amount'] <= amount:
                total_price += offer['price']
                amount -= offer['amount']

        total_price += amount * options['price']
    return total_price
