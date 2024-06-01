import json
import csv


def clean_data(products):
    cleaned_products = []
    for product in products:
        product['stock'] = product.get('stock', 'N/A')
        product['warranty'] = product.get('warranty', 'N/A')

        if isinstance(product['price'], str):
            product['price'] = float(product['price'])

        del product['extra_field']

        cleaned_products.append(product)
    return cleaned_products


def write_to_csv(products, filename='electronics_products.csv'):
    fieldnames = products[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)


with open('electronics_products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    products = data['data']

cleaned_products = clean_data(products)

write_to_csv(cleaned_products)

print("CSV file generated successfully!")
