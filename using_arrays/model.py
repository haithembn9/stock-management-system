class Product:
    def __init__(self, name, quantite, amount):
        self.name = name
        self.quantite = quantite
        self.amount = amount

    def __str__(self):
        return f"Name: {self.name}\nQuantite: {self.quantite}\nAmount: {self.amount}\nTotal Price: {self.get_total_price()}"

    def get_total_price(self):
        try:
            return float(self.quantite) * float(self.amount)
        except ValueError:
            return 0

class ProductModel:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'products'):  
            self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products

    def update_product(self, index, name=None, quantite=None, amount=None):
        if 0 <= index < len(self.products):
            if name:
                self.products[index].name = name
            if quantite:
                self.products[index].quantite = quantite
            if amount:
                self.products[index].amount = amount
            return True
        return False

    def delete_product(self, index):
        if 0 <= index < len(self.products):
            self.products.pop(index)
            return True
        return False
