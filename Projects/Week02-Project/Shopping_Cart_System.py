class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

class Cart:
    def __init__(self):
        self.items=[]

    # add item to cart
    def add_item(self, product):
        for item in self.items:
            if item["name"]==product.name:
                item["quantity"]+=1
                print("Quantity updated.")
                return

        self.items.append({
            "name": product.name,
            "price": product.price,
            "quantity": 1
        })
        print("Product added.")

    # view cart items
    def view_cart(self):
        if len(self.items)==0:
            print("Your cart is empty.")
        else:
            print("\nProducts added to cart are:")
            for index, item in enumerate(self.items):
                print(f"{index+1}. {item['name']} x{item['quantity']} - ${item['price']}")           
    
    # calculate total bill
    def total(self):
        if len(self.items)==0:
            print("Your cart is empty.")
            return
    
        total=0
        for item in self.items:
            total+=item["price"]*item["quantity"]
        print(f"Total bill: ${total}")

    
    # remove item from cart
    def remove_item(self):
        if len(self.items)==0:
            print("Your cart is empty.")
            return

        self.view_cart()

        try:
            item_number=int(input("Enter item number to remove: "))
        except ValueError:
            print("Invalid input!")
            return

        if 1<=item_number<=len(self.items):
            removed_item=self.items.pop(item_number-1)
            print(f"{removed_item['name']} removed from cart.")
        else:
            print("Invalid item number.") 

# predefined products
products={
    1: Product("Laptop", 999.99),
    2: Product("Smartphone", 499.99),
    3: Product("Tablet", 299.99),
    4: Product("Headphones", 199.99),
    5: Product("Smartwatch", 149.99)
}

# show these products
def show_products():
    print("\nAvailable Products:")
    for product_id, p in products.items():
        print(f"{product_id}. {p.name} - ${p.price}")

# add products to cart
cart = Cart()

# function to add products to cart
def add_to_cart():
    # handle invalid input
    try:
        product_id=int(input("Enter product ID to add: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    
    if product_id in products:
        product=products[product_id]

        cart.add_item(product)

    else:
        print("Invalid product id.")

# view cart
def view_cart():
    cart.view_cart()

# remove items from cart
def remove_from_cart():
    cart.remove_item()
    


# total bill
def total_bill():
    cart.total()



# call functions
# show_products()
# add_to_cart()
# view_cart()

# while loop to show all options
while True:
    print("\n=====Available Options=====")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove from Cart")
    print("5. Total Bill")
    print("6. Exit")

    choice=input("\nEnter your choice:")
    
    if choice=="1":
        show_products()

    elif choice=="2":
        add_to_cart()

    elif choice=="3":
        view_cart()

    elif choice=="4":
        remove_from_cart()

    elif choice=="5":
        total_bill()

    elif choice=="6":
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please try again.")

