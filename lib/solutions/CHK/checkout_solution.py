
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
def checkout(skus):
    for (sku, options) in get_skus().iteritems():


