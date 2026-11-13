items = [
    
]
    

def add_items(items):
    add = input("Enter item name: ")
    if not add in items:
        
        print("===== CATEGORIES =====")
        print("(1)Fruits\n(2)Vegetable\n(3)Meat\n(4)Dairy\n(5)Beverages\n(6)Others\n")
        
        category = input("Enter product category: ")
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
            
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        
        items.append(item)
        
    else: 
        print("Item already exist")

add_items(items)

print(items)