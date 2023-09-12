import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quotes in quotes:
        self.assertEqual(getDataPoint(quotes),(quotes['stock'],quotes['top_bid']['price'],quotes['top_ask']['price'],(quotes['top_bid']['price']+quotes['top_ask']['price'])/2))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quotes in quotes:
      self.assertEqual(getDataPoint(quotes),(quotes['stock'],quotes['top_bid']['price'],quotes['top_ask']['price'],(quotes['top_bid']['price'] + quotes['top_ask']['price'])/2 ))


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_missingData (self):
    quote = {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'id': '0.109974697771'}
    with self.assertRaises(KeyError):
      getDataPoint(quote)

  # def test_getDataPoint_missingType (self):
  #   quote = {'top_ask': {'price': 'string', 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': '120.48', 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
  #   with self.assertRaises(TypeError):
  #     getDataPoint(quote)

  def test_getDataPoint_negativePrice (self):
    quote = {'top_ask': {'price': -100, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -200, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
   # with self.assertRaises(TypeError):
    result = getDataPoint(quote)
    print(result)

  def test_getDataPoint_zeroPrice(self):
    quote = {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453','top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    # with self.assertRaises(TypeError):
    result = getDataPoint(quote)
    print(result)
    stock, bid_price, ask_price, price = getDataPoint(quote)

    print(getRatio(price,price))
    self.assertEqual(getRatio(price,price),None)



if __name__ == '__main__':
    unittest.main()
