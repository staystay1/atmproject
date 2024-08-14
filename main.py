class ATM: #defining atm class
    def __init__(self, pin, balance):
        self.__pin = int(pin)
        self.__balance = balance
        self.__menu() #calling menu method.

    def __menu(self): #defining menu method.
        while True: 
            print('\n',"Welcome to the ATM!")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print("Your balance is:", self.__balance)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                self.__withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter deposit amount: "))
                self.__deposit(amount)
            elif choice == '4':
                self.__change_pin()
            elif choice == '5':
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please try again.")

    def __withdraw(self, amount): #deinfing withdraw method.
        if amount <= self.__balance: #checks if withdraw amount is greater or equal to balance method.
            self.__balance -= amount #sets new balance amount after removing the amount withdrawn.
            print("Withdrawal successful. New balance:", self.__balance)
        else:
            print("Insufficient funds. /n")

    def __deposit(self, amount): #defining deposit method.
        self.__balance += amount # sets new balance amount after adding the amount deposited.
        print("Deposit successful. New balance:", self.__balance)

    def __change_pin(self): #defining change pin method.
        old_pin = int(input("Enter your previous PIN: ")) #set variable "old_pin" to user input. Pin should be the value given when creating the atm object.
        if old_pin == self.__pin: #checks if old pin and the atm object pin match.
            new_pin = int(input("Enter new PIN: "))
            confirm_pin = int(input("Confirm new PIN: "))
            if new_pin == confirm_pin: #checks if user input for new pin and confirm pin match.
                self.__pin = new_pin
                print("PIN changed successfully. ")
            else:
                print("New PINS do not match. ")
        else:
            print("Previous PIN Incorrect. ")

atm = ATM(input("set a pin (4 digits): "), input("Set a balance amount: "))
