items = []


def add_items(items):
    print("===== ADD ITEMS =====")
    add = input("Enter item name: ").capitalize()

    for item in items:
        if item['Name'] == add:
            print("Item already exists")
            return

    while True:
        try:
            price = float(input("Enter price: "))
            if price > 0:
                break
            print("Price should be greater than 0")
        except ValueError:
            print("Invalid input")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            print("Quantity should be greater than 0")
        except ValueError:
            print("Invalid input")

    while True:
        print("===== CATEGORIES =====")
        print("(1) Fruits\n(2) Vegetable\n(3) Meat\n(4) Dairy\n(5) Beverages\n(6) Others")

        category = input("Enter product category: ")

        categories = {
            "1": "Fruits",
            "2": "Vegetable",
            "3": "Meat",
            "4": "Dairy",
            "5": "Beverages",
            "6": "Others"
        }

        if category in categories:
            item = {
                'Name': add,
                'Quantity': quantity,
                'Price': price,
                'Category': categories[category]
            }

            items.append(item)
            print("Item added successfully!")
            return
        else:
            print("Invalid choice")


def view(items):
    print("===== VIEW ALL =====")
    if not items:
        print("No items available")
        return

    for item in items:
        print(f"Item: {item['Name']}")
        print(f"Quantity: {item['Quantity']}")
        print(f"Price: {item['Price']}")
        print(f"Category: {item['Category']}\n")


def update(items):
    print("===== UPDATE =====")
    find = input("Update item: ").capitalize()

    for item in items:
        if find == item['Name']:

            while True:
                try:
                    price = float(input("Change price: "))
                    if price > 0:
                        item['Price'] = price
                        break
                    print("Price should be greater than 0")
                except ValueError:
                    print("Invalid input")

            while True:
                try:
                    quantity = int(input("Change quantity: "))
                    if quantity > 0:
                        item['Quantity'] = quantity
                        break
                    print("Quantity should be greater than 0")
                except ValueError:
                    print("Invalid input")

            categories = {
                "1": "Fruits",
                "2": "Vegetable",
                "3": "Meat",
                "4": "Dairy",
                "5": "Beverages",
                "6": "Others"
            }

            while True:
                print("===== CATEGORIES =====")
                for key, value in categories.items():
                    print(f"({key}) {value}")

                category = input("Change category: ")

                if category in categories:
                    item['Category'] = categories[category]
                    print("Item updated successfully!")
                    return
                print("Invalid choice")

    print("Item not found")


def remove(items):
    print("===== REMOVE ITEMS =====")
    rem = input("Remove item: ").capitalize()

    for item in items:
        if rem == item['Name']:
            items.remove(item)
            print("Item has been removed")
            return

    print("Item not found")


def search(items):
    print("===== FIND ITEM =====")
    find = input("Search item: ").capitalize()

    for item in items:
        if find == item['Name']:
            print(f"Name: {item['Name']}")
            print(f"Price: {item['Price']}")
            print(f"Quantity: {item['Quantity']}")
            print(f"Category: {item['Category']}")
            return

    print("Item not found")


def category_summary(items):
    if not items:
        print("No items available")
        return

    summary = {}

    for item in items:
        category = item['Category']

        if category not in summary:
            summary[category] = 0

        summary[category] += 1

    print("===== CATEGORY SUMMARY =====")

    for category, count in summary.items():
        print(f"{category}: {count} item(s)")


def calc_overall(items):
    if not items:
        print("No items available")
        return

    total = 0

    for item in items:
        total += item['Price'] * item['Quantity']

    print(f"Overall inventory value: {total:.2f}")


while True:
    print("\n===== GROCERY LIST SYSTEM =====")
    print("(1) Add Item")
    print("(2) View Items")
    print("(3) Update Item")
    print("(4) Remove Item")
    print("(5) Search Item")
    print("(6) Category Summary")
    print("(7) Calculate Overall Total")
    print("(8) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_items(items)
    elif choice == "2":
        view(items)
    elif choice == "3":
        update(items)
    elif choice == "4":
        remove(items)
    elif choice == "5":
        search(items)
    elif choice == "6":
        category_summary(items)
    elif choice == "7":
        calc_overall(items)
    elif choice == "8":
        print("Program finished!")
        break
    else:
        print("Invalid choice. Try again")
