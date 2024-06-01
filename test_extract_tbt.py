import unittest
import json
import os
from extract_tbt_new import extract_tbt_values_from_json


class TestExtractTBTValues(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            "id": "1",
            "name": "Product 1",
            "category": "Appliances",
            "price": "TBT:320.46",
            "currency": "USD",
            "stock": 51,
            "description": "Description of product 1",
            "manufacturer": "CamTech",
            "warranty": "2 years",
            "extra_field": "Extra value 1"
        }

    def test_extract_tbt_values_from_json(self):
        test_file = 'test.json'
        with open(test_file, 'w', encoding='utf-8') as file:
            json.dump(self.test_data, file, indent=4)

        tbt_values = extract_tbt_values_from_json(test_file)
        expected_result = {
            'test.json': {'': {'price': '320.46'}}
        }
        self.assertEqual(tbt_values, expected_result)

        os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
