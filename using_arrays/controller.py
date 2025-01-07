from model import Product
class ProductManagerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_product(self):
        name, quantite, amount = self.view.get_product_input()
        product = Product(name, quantite, amount)
        self.model.add_product(product)
        self.view.display_message("Product added successfully.")

    def view_products(self):
        products = self.model.get_products()
        self.view.display_products(products)

    def update_product(self):
        self.view_products()
        index = self.view.get_product_index()
        if 0 <= index < len(self.model.get_products()):
            print("Enter new details for the product (leave blank to keep current value):")
            name, quantite, amount = self.view.get_product_input()
            if self.model.update_product(index, name, quantite, amount):
                self.view.display_message("Product updated successfully.")
            else:
                self.view.display_message("Failed to update product.")
        else:
            self.view.display_message("Invalid product number.")

    def delete_product(self):
        self.view_products()
        index = self.view.get_product_index()
        if self.model.delete_product(index):
            self.view.display_message("Product deleted successfully.")
        else:
            self.view.display_message("Invalid product number.")
