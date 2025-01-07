from model import ProductModel, Product
from view import ProductManagerView
from controller import ProductManagerController

if __name__ == "__main__":
    model = ProductModel()
    view = ProductManagerView()
    controller = ProductManagerController(model, view)

    while True:
        print("\nProduct Manager")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            controller.add_product()
        elif choice == "2":
            controller.view_products()
        elif choice == "3":
            controller.update_product()
        elif choice == "4":
            controller.delete_product()
        elif choice == "5":
            print("Exiting Product Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
