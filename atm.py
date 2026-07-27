balance = 1000
pin=int(input("enter your pin: "))
user = input("Insert your card (yes/no): ")

if user.lower() == "yes":
    
    if pin == 1234:
        while True:
            print("Select mode : ")
            print("1. Withdraw Money")
            print("2. Check Balance")
            print("3. Deposit Money")
            print("4. Exit")
            
            choice = input("Please choose an option (1-4): ")
            
            if choice == '1':
                amt = int(input("Enter amount to withdraw: "))
                if amt > balance:
                    print("Insufficient balance.")
                elif amt <= 0:
                    print("Withdrawal amount must be positive.")
                else:
                    balance -= amt
                    print(f"Successfully withdrew ${amt}.")
                    print(f"Your current balance is: ${balance}")
            
            elif choice == '2':
                print(f"Your current balance is: ${balance}")
            
            elif choice == '3':
                amt = int(input("Enter amount to deposit: "))
                if amt > 0:
                    balance += amt
                    print(f"Successfully deposited ${amt}.")
                    print(f"Your current balance is: ${balance}")
                else:
                    print("Deposit amount must be positive.")
            
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break

            
            else:
                print("Invalid choice. Please try again.")
    
    elif pin==2345:
        while True:
            print("\nSelect mode of transaction:")
            print("1. Withdraw Money")
            print("2. Check Balance")
            print("3. Deposit Money")
            print("4. Exit")
            
            choice = input("Please choose an option (1-4): ")
            
            if choice == '1':
                amt = int(input("Enter amount to withdraw: "))
                if amt > balance:
                    print("Insufficient balance.")
                elif amt <= 0:
                    print("Withdrawal amount must be positive.")
                else:
                    balance -= amt
                    print(f"Successfully withdrew ${amt}.")
                    print(f"Your current balance is: ${balance}")
            
            elif choice == '2':
                print(f"Your current balance is: ${balance}")
            
            elif choice == '3':
                amt = int(input("Enter amount to deposit: "))
                if amt > 0:
                    balance += amt
                    print(f"Successfully deposited ${amt}.")
                    print(f"Your current balance is: ${balance}")
                else:
                    print("Deposit amount must be positive.")
            
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
    else:
        print("Invalid PIN.")
else:
    print("No card inserted.")