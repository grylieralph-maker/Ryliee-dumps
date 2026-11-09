import random
attempt = 5

random_num = random.randint(1,100)
print(5*"#","GUESS THE NUMBER","#"*5,"\n")
print("You only have 5 attempts")
while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess > 100 or guess < 1:
            print("\nInvalid guess! (1-100 only)\n")
        else:    
            if guess > random_num:
                print(f"\nYou guessed: {guess}\nToo high!")
                attempt -= 1
                if attempt > 0:
                    print(f"Attempts left: {attempt}\n")
                else: 
                    print("No attempts left. You lose!")
                    print(f"\nThe number is: {random_num}")
                    break
    
            elif guess < random_num:
                print(f"\nYou guessed: {guess}\nToo low!")
                attempt -= 1
                if attempt > 0:
                    print(f"Attempts left: {attempt}\n")
                else:
                    print("No attempts left. You lose!")
                    print(f"\nThe number is: {random_num}")
                    break
            else:
                print(f"\nYou Win. The number is: {random_num}")
                break
                

    except ValueError:
        print(f"\nInvalid guess! (whole numbers only)\n")
    