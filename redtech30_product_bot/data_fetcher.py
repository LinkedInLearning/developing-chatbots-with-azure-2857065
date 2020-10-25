import pandas as pd

PRODUCT_PATH = "data/products.csv"


class ProductDataFetcher:
    def __init__(self):
        self.dataframe = pd.read_csv(PRODUCT_PATH)

    def get_product(self, name):
        name = name.lower()
        return self.dataframe[self.dataframe["Product"].str.contains(name, case=False)]

    def get_product_info(self, name):
        return self.get_product(name)["Description"].iloc[0]

    def get_price(self, name):
        return self.get_product(name)["Price"].iloc[0]

    def list_products(self, category):
        category = category.lower()
        return self.dataframe[self.dataframe["Category"].str.contains(category, case=False)]
