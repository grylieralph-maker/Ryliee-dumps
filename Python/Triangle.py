rows = int(input("Enter how many rows: "))

for i in range(1,rows+1):
    for spaces in range(rows-i):
        print(" ",end="")
    for astk in range(i*2-1):
        print("*",end="")
    print()    