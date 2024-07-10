import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expected_stock = quote['stock']
      expected_bid_price = quote['top_bid']['price']
      expected_ask_price = quote['top_ask']['price']
      expected_price = (expected_bid_price + expected_ask_price) / 2
      
      self.assertEqual(getDataPoint(quote), (expected_stock, expected_bid_price, expected_ask_price, expected_price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expected_stock = quote['stock']
      expected_bid_price = quote['top_bid']['price']
      expected_ask_price = quote['top_ask']['price']
      expected_price = (expected_bid_price + expected_ask_price) / 2
      
      self.assertEqual(getDataPoint(quote), (expected_stock, expected_bid_price, expected_ask_price, expected_price))


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_withZeroPrices(self):
    quotes = [
      {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      expected_stock = quote['stock']
      expected_bid_price = quote['top_bid']['price']
      expected_ask_price = quote['top_ask']['price']
      expected_price = (expected_bid_price + expected_ask_price) / 2
        
      self.assertEqual(getDataPoint(quote), (expected_stock, expected_bid_price, expected_ask_price, expected_price))
  
  def test_getDataPoint_withNegativePrices(self):
    quotes = [
      {'top_ask': {'price': -121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    ]
    for quote in quotes:
      expected_stock = quote['stock']
      expected_bid_price = quote['top_bid']['price']
      expected_ask_price = quote['top_ask']['price']
      expected_price = (expected_bid_price + expected_ask_price) / 2
            
      self.assertEqual(getDataPoint(quote), (expected_stock, expected_bid_price, expected_ask_price, expected_price))
      
  def test_getRatio_normal(self):
    price_a = 120.0
    price_b = 100.0
    expected_ratio = 1.2
    
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)
    
  def test_getRatio_zeroDenominator(self):
    price_a = 120.0
    price_b = 0
    
    self.assertIsNone(getRatio(price_a, price_b))

  def test_getRatio_zeroNumerator(self):
    price_a = 0
    price_b = 100.0
    expected_ratio = 0.0
    
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)

  def test_getRatio_negativePrices(self):
    price_a = -120.0
    price_b = 100.0
    expected_ratio = -1.2
    
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)

if __name__ == '__main__':
    unittest.main()
