

from sample_data import get_sample_products
from data_analyzer import DataAnalyzer

if __name__ == "__main__":
    products = get_sample_products()

    analyzer = DataAnalyzer()

    print("Analyzing data for PRICE sorting:\n")
    analysis = analyzer.analyze(products, "price")

    for key, value in analysis.items():
        print(f"{key}: {value}")
