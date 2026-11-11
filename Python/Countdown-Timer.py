import time

print(5*"#","COUNTDOWN TIMER","#"*5,"\n")
while True:
    try:
        start = int(input("Enter Countdown Duration: "))
        print("Countdown started!\n")
        for i in range(start,0, -1):
            print(i)
            time.sleep(1)
        
        print("Times up!")
    except ValueError:
        print("Invalid input. Please enter whole number.")