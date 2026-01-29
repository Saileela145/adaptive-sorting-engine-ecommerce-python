

from sample_data import get_sample_products

if __name__ == "__main__":
    products = get_sample_products()

    print("Product list:")
    for product in products:
        print(product)
