balance = 10000
def withdraw(balance,amount):
  if balance < amount or amount <= 0:
    print("Invalid amount\n")
    return balance
  else:
    return balance - amount

def deposit(balance, amount):
  if amount <=0:
    print("Invalid amount")
    return balance
  else:    
    return balance + amount
      
def view_balance(balance):
    print(f"Balance: {balance:,.2f}")

while True:
  print("==========ATM==========\n")
  print("(1)WITHDRAW\n(2)DEPOSIT\n(3)VIEW BALANCE\n(4)EXIT\n")
  
  try:
    choice = input("Enter your choice: ")      
    if choice == "1":
      amount = float(input("Enter the amount: "))
      balance = withdraw(balance, amount)
          
    elif choice == "2":
        amount = float(input("Enter the amount: "))
        balance = deposit(balance, amount)
        
    elif choice == "3":
        view_balance(balance)
         
    elif choice == "4":
        print("Thankyou, Come again!")   
        break
        
    else:
        print("Invalid input! try again")
        
  except ValueError:
    print("Invalid input")
    