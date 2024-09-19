import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario


    def test_list_of_more_three_prices(self):
        prices = [15,25,5,20]
        expected_discount = 5
        self.assertEqual(expected_discount,discount(prices))

    
    def test_empty_list(self): # an empty list should return 0 
        prices = []
        expected_discount = 0 
        self.assertEqual(expected_discount,discount(prices))

    
    def test_list_of_float(self):
        self.fail('finish this test')



if __name__ == '__main__':
    unittest.main()