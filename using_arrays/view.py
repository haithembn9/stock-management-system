class ProductManagerView:
    def display_products(self, products):
        if not products:
            print("No products available.")
        else:
            for i, product in enum(products):
                print(f"\nProduct #{i + 1}")
                print(product)

    def get_product_input(self):
        name = input("Enter product name: ")
        quantite = input("Enter product quantity: ")
        amount = input("Enter product amount: ")
        return name, quantite, amount

    def get_product_index(self):
        try:
            return int(input("Enter the product number: ")) - 1
        except ValueError:
            return -1

    def display_message(self, message):
        print(message)
