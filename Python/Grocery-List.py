items = [

]


def add_items(items):
    while True:
        try:
            add = input("Enter item name: ").capitalize()
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            if not add in items:
                print("===== CATEGORIES =====")
                print("(1)Fruits\n(2)Vegetable\n(3)Meat\n(4)Dairy\n(5)Beverages\n(6)Others\n")
                while True:
                    category = input("Enter product category: ")
                    item = {
                        'Name': add,
                        'Quantity': quantity,
                        'Price': price,
                        'Category': {}
                    }
                    if category == "1":
                        item['Category'] = 'Fruits'
                    elif category == "2":
                        item['Category'] = 'Vegetable'
                    elif category == "3":
                        item['Category'] = 'Meat'
                    elif category == "4":
                        item['Category'] = 'Dairy'
                    elif category == "5":
                        item['Category'] = 'Beverages'
                    elif category == "6":
                        item['Category'] = 'Others'
                    else:
                        print("Invalid choice")
                    
                    
                    items.append(item)
                    break
        
            else:
                print("Item already exist")

        except ValueError:
            print("Invalid input. Try again")
            
def view(items):
    for item in items:
        print(f"Item: {item['Name']}")
        print(f"Quantitty: {item['Quantity']}")
        print(f"Price: {item['Price']}")
        print(f"Category: {item['Category']}")
    
def update(items):
    while True:
        try: 
            find = input("Update item: ").capitalize()
            for item in items:
                if find in item:
                    while True:
                        price = float(input("Change price: "))
                        item['Price'] = price
                        quantity = int(input("Change quantity: "))
                        item['Quantity'] = quantity
                        category = input("Change category: ")
                        if category == "1":
                            item['Category'] = 'Fruits'
                        elif category == "2":
                            item['Category'] = 'Vegetable'
                        elif category == "3":
                            item['Category'] = 'Meat'
                        elif category == "4":
                            item['Category'] = 'Dairy'
                        elif category == "5":
                            item['Category'] = 'Beverages'
                        elif category == "6":
                            item['Category'] = 'Others'
                        else:
                            print("Invalid choice")
                else:
                    print("Item not found")

        except ValueError:
            print("Invalid input")
    


    
def remove():
    pass 
def search():
    pass
def category_summary():
    pass
def calc_overall():
    pass


while True:
    print("===== GROCERY LIST SYSTEM =====")
    print("(1) Add Item")
    print("(2) View Items")
    print("(3) Update Item")
    print("(4) Remove Item")
    print("(5) Search Item")
    print("(6) Category Summary")
    print("(7) Calculate Overall Total")
    print("(8) Exit")

    choice = input("Enter your choice: ")

    if choice == "":
    elif choice == "":
    elif choice == "":    
    
