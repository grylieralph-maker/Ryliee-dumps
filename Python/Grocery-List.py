items = [

]


def add_items(items):
    while True:
        try:
            add = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            if not add in items:
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


    
def update():
    pass
def remove():
    pass 
def search():
    pass
def category_summary():
    pass
def calc_overall():
    pass

add_items(items)
view(items)
