items = [
    
]
    

def add_items(items):
    add = input("Enter item name: ")
    if not add in items:
        print("===== CATEGORIES =====")
        print("(1)Fruits\n(2)Vegetable\n(3)Meat\n(4)Diary\n(5)Beverages\n(6)Others\n")
        category = input("Enter product category: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        item = {
            'Fruit': 
        }
        
    else: 
        print("Item already exist")

add_items(items)        