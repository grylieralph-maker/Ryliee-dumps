products = {
    "P001": {"name": "Milk", "price": 50, "stock": 10},
    "P002": {"name": "Shirt", "price": 250, "stock": 5},
    "P003": {"name": "Bread", "price": 35, "stock": 20},
    "P004": {"name": "Rice", "price": 60, "stock": 0},
}


def view_product():
    print(14*"=", "PRODUCTS", "="*14)
    for key, value in products.items():
        print("ID:", key)
        print(f"Name: {value['name']}")
        print(f"Price: {value['price']}")
        print(f"Stock: {value['stock']}\n")


def sell_product():
    print(14*"=", "SELL", "="*14)
    while True:
        ID = input("Enter Product ID: ")
        if ID in products:
            while True:
                try:
                    sell = int(input("Enter Quantity: "))
                    if sell <= 0 or sell > products[ID]['stock']:
                        print("Insufficient or Invalid Amount")
                    else:
                        products[ID]['stock'] -= sell
                        print(f"Successfully sold {sell} {products[ID]['name']}")
                        print(f"Remaining Stocks: {products[ID]['stock']}\n")
                        return
                except ValueError:
                    print("Invalid Input")
        else:
            print("Product not found. Try again")


def restock():
    print(14*"=", "RESTOCK", "="*14)
    while True:
        ID = input("Enter Product ID: ")
        if ID in products:
            while True:
                try:
                    rstock = int(input("Enter Quantity: "))
                    if rstock > 0:
                        print("Previous Stock:", products[ID]['stock'])
                        products[ID]['stock'] += rstock
                        print(f"Successfully Restocked {products[ID]['name']}")
                        print(f"Added Stocks: {rstock}")
                        print(f"{products[ID]['name']} has {products[ID]['stock']} stocks now\n")
                        return
                    else:
                        print("Invalid Amount")
                except ValueError:
                    print("Invalid input")
        else:
            print("Product not found. Try again")


def search_item():
    print(14*"=", "SEARCH", "="*14)
    found = False
    while True:
        search = input("Enter Product Name: ").capitalize()
        for key, value in products.items():
            if search in products[key]['name']:
                found = True
                print("ID: ", key)
                print("Name: ", products[key]['name'])
                print("Price: ", products[key]['price'])
                print("Stock", products[key]['stock'],"\n") 
                return
        if not found:
            print("Product not found. Try again")


def report():
    lowest = None
    highest = None
    stotal = 0
    vtotal = 0

    for key, value in products.items():
        stotal += value['stock']
        vtotal += value['price'] * value['stock']

        if highest is None or value['stock'] > highest:
            highest = value['stock']
            high = value['name']

        if lowest is None or value['stock'] < lowest:
            lowest = value['stock']
            low = value['name']

    print(14*"=", "OVERALL REPORT", "=" * 14)
    print("Overall Stock Total:", stotal)
    print("Overall Products Total:", len(products))
    print("Overall Value Total:", vtotal)
    print("Highest Stock:", high, highest)
    print("Lowest Stock:", low, lowest,"\n")


while True:
    try:
        print(14*"=", "PRODUCT TRACKER", "="*14)
        print("(1) View Product\n(2) Sell\n(3) Restock\n(4) Search\n(5) Report\n(6) Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_product()
        elif choice == "2":
            sell_product()
        elif choice == "3":
            restock()
        elif choice == "4":
            search_item()
        elif choice == "5":
            report()
        elif choice == "6":
            print("Program Finished")
            break
        else:
            print("Invalid Choice")

    except ValueError:
        print("Invalid Input")