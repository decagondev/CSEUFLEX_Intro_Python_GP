class Category:

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __str__(self):
        return f"There are no products in {self.name}"