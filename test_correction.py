import unittest
import json
import os
from correction import clean_data, write_to_csv


class TestCleanData(unittest.TestCase):
    def setUp(self):
        with open('electronics_products.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.products = data['data']

    def test_clean_data(self):
        cleaned_products = clean_data(self.products)

        # Check if all products have 'stock' and 'warranty' fields
        for product in cleaned_products:
            self.assertIn('stock', product)
            self.assertIn('warranty', product)

        # Check if 'price' field is converted to float for products where it's a string
        for product in cleaned_products:
            if isinstance(product['price'], str):
                self.assertIsInstance(product['price'], float)

        # Check if 'extra_field' is removed from all products
        for product in cleaned_products:
            self.assertNotIn('extra_field', product)


class TestWriteToCSV(unittest.TestCase):
    def test_write_to_csv(self):
        products = [
            {"id": "1", "name": "Product 1", "category": "Appliances", "price": 320.46, "currency": "USD", "stock": 51, "description": "Description of product 1", "manufacturer": "CamTech", "warranty": "2 years"},
            {"id": "2", "name": "Product 2", "category": "Wearables", "price": 808.81, "currency": "USD", "stock": 127, "description": "Description of product 2", "manufacturer": "BrightLife", "warranty": "1 year"}
        ]
        write_to_csv(products, 'test.csv')

        # Check if CSV file is created
        self.assertTrue(os.path.exists('test.csv'))

        # Check if CSV file contains correct number of rows
        with open('test.csv', 'r', encoding='utf-8') as csvfile:
            csv_data = csvfile.readlines()
            self.assertEqual(len(csv_data), len(products) + 1)  # Add 1 for the header row

        # Clean up the test CSV file
        os.remove('test.csv')


if __name__ == '__main__':
    unittest.main()
