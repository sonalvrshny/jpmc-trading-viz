import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      top_bid_price = quote['top_bid']['price']
      top_ask_price = quote['top_ask']['price']
      self.assertEqual(getDataPoint(quote), (quote['stock'], top_bid_price, top_ask_price, (top_ask_price + top_bid_price)/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      top_bid_price = quote['top_bid']['price']
      top_ask_price = quote['top_ask']['price']
      self.assertEqual(getDataPoint(quote), (quote['stock'], top_bid_price, top_ask_price, (top_ask_price + top_bid_price)/2))



  def test_getRatio(self):
    prices = [
      (0,1), (20,0), (30,10)
    ]

    for price in prices:
      if price[1] == 0:
        ratio = None
      else:
        ratio = price[0]/price[1]

      self.assertEqual(getRatio(price[0], price[1]), ratio)


if __name__ == '__main__':
    unittest.main()
