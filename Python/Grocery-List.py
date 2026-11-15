items = [

]


def add_items(items):
    add = input("Enter item name: ").capitalize()
    if not add in items:
        while True:
            try:
                price = float(input("Enter price: "))
                if price > 0:
                    break
                else:
                    print("Price should be a positive number or greater than 0")
            except ValueError:
                print("Invalid input")
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    break
                else:
                    print("Quantity should be a positive number or greater than 0")
            except ValueError:
                print("Invalid input")
                        
        
        while True:
            print("===== CATEGORIES =====")
            print("(1)Fruits\n(2)Vegetable\n(3)Meat\n(4)Dairy\n(5)Beverages\n(6)Others\n")
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
                continue
            
            items.append(item)
            break
                       
    else:
        print("Item already exist")


def view(items):
    for item in items:
        print(f"Item: {item['Name']}")
        print(f"Quantity: {item['Quantity']}")
        print(f"Price: {item['Price']}")
        print(f"Category: {item['Category']}\n")

def update(items):
    while True:       
        find = input("Update item: ").capitalize()
        for item in items:
            if find in item['Name']:
                while True:
                    try:
                        price = float(input("Change price: "))
                        if price > 0:
                            item['Price'] = price
                            break
                        else:
                            print("Price should be positive or greater than 0")
                    except ValueError:
                        print("Invalid input")
                        
                while True:
                    try:
                        quantity = int(input("Change quantity: "))
                        if quantity > 0:
                            item['Quantity'] = quantity
                            break
                        else:
                            print("Price should be positive or greater than 0")
                            
                    except ValueError:
                        prin("Invalid input")
    
                while True: 
                    print("===== CATEGORIES =====")
                    print("(1)Fruits\n(2)Vegetable\n(3)Meat\n(4)Dairy\n(5)Beverages\n(6)Others\n")
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
                        continue 

                    return
                        
                        
            else:
                print("Item not found")
    
            
def remove(items):
    while True:
        rem = input("Remove item: ").capitalize()
        while True:
            for item in items:
                if rem in item['Name']:
                    if item['Name'] == rem:
                        items.remove(item)
                        print("Item has been removed")
                        return
                        
                else:
                    print("Item not found")
    
        
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
        
    
