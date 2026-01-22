cart = {}

def menu():
    print("\n--- Grocery Store Menu ---")
    print("1. Add items to cart")
    print("2. Remove item from cart")
    print("3. View total price")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-4): ")

    if choice not in ["1","2","3","4"]:
        print("Invalid Choice")
        continue

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart[item] = price
        print(f"{item} added to cart.")

    elif choice == "2":
        item = input("Enter item name to remove: ")
        if item in cart:
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            print("Item not found in cart.")

    elif choice == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            total = sum(cart.values())
            print("\nItems in cart: ")
            for item,price in cart.items():
                print(f"{item} : ₹{price}")
            print(f"Total Price: ₹{total}")

    elif choice == "4":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please try again.")