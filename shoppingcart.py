class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self):
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        price = float(input("Enter item price: "))
        self.cart.append((name, quantity, price))
        print(f"Item '{name}' added to cart.")

    def remove_item(self):
        if self.cart:
            print("Cart Contents:")
            for i, item in enumerate(self.cart):
                print(f"{i+1}. {item[0]} x {item[1]} - ${item[2]*item[1]:.2f}")
            choice = int(input("Enter item number to remove: ")) - 1
            if 0 <= choice < len(self.cart):
                del self.cart[choice]
                print("Item removed from cart.")
            else:
                print("Invalid choice.")
        else:
            print("Cart is empty.")

    def display_cart(self):
        if self.cart:
            print("Cart Contents:")
            total_price = 0
            for item in self.cart:
                name, quantity, price = item
                item_price = quantity * price
                total_price += item_price
                print(f"{name} x {quantity} - ${item_price:.2f}")
            discount = self.apply_discount(total_price)
            total_price -= discount
            print(f"Subtotal: ${total_price + discount:.2f}")
            print(f"Discount: ${discount:.2f}")
            print(f"Total: ${total_price:.2f}")
        else:
            print("Cart is empty.")

    def apply_discount(self, total_price):
        if total_price > 100:
            return total_price * 0.1
        elif 50 <= total_price <= 100:
            return total_price * 0.05
        else:
            return 0

def main():
    cart = ShoppingCart()
    while True:
        print("\nShopping Cart System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Cart")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            cart.add_item()
        elif choice == 2:
            cart.remove_item()
        elif choice == 3:
            cart.display_cart()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()