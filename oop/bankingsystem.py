from abc import ABC, abstractmethod

try:
    class Banking(ABC):
        def __init__(self, balance=10000):
            self.__balance = balance

        @abstractmethod
        def withdrawal_money(self):
            pass

        @abstractmethod
        def deposit_money(self):
            pass

        @abstractmethod
        def check_balance(self):
            pass

        @abstractmethod
        def transfer_money(self):
            pass

    class Withdraw(Banking):
        def __init__(self, balance=10000):
            super().__init__(balance)

        def withdrawal_money(self):
            for _ in range(3):
                try:
                    amount = float(input("Enter the amount of money you want to withdraw: "))
                    # Validate amount
                    if amount <= 0:
                        print(f"You entered {amount}, but the amount must be a positive number.")
                        continue
                    #sicnce there must remaing 
                    if amount < self._Banking__balance - 100: 
                        self._Banking__balance -= amount
                        print(f"Withdrawal successful! You withdrew {amount}.")
                        print(f"Your remaining balance is {self._Banking__balance}.")
                        break
                    elif amount == self._Banking__balance:
                        print("Your withdrawal amount is exactly equal to your balance.")
                        print("You must leave at least 100 in your account. Please try again.")
                    else:
                        print("Insufficient balance. Please enter an amount less than your existing balance.")
                except ValueError:
                    print("You entered an invalid input. Please enter a valid amount.")
            else:
                print("Too many attempts. Goodbye!")

        # Dummy implementations
        def deposit_money(self):
            pass

        def check_balance(self):
            pass

        def transfer_money(self):
            pass

    class Deposit(Banking):
        def __init__(self, balance=10000):
            super().__init__(balance)

        def deposit_money(self):
            try:
                amount = float(input("Enter your amount to deposit: ")) 
                # Validate amount
                if amount <= 0:
                    print(f"You entered {amount}, which is not a positive amount. Amount must be positive.")
                    return
                self._Banking__balance += amount
                print(f"You deposited {amount} amount successfully.")
                print(f"Your total balance is now {self._Banking__balance}.")
            except ValueError:
                print("You entered an invalid input. Please enter a valid amount.")

        # Dummy implementations
        def withdrawal_money(self):
            pass

        def check_balance(self):
            pass

        def transfer_money(self):
            pass

    class CheckBalance(Banking):
        def __init__(self, balance=10000):
            super().__init__(balance)

        def check_balance(self):
            print(f"Your current balance is {self._Banking__balance}.")

        # Dummy implementations
        def withdrawal_money(self):
            pass

        def deposit_money(self):
            pass

        def transfer_money(self):
            pass

    class Transfer(Banking):  
        def __init__(self, balance=10000):
            super().__init__(balance)

        def transfer_money(self):
            accepter_account = 1000202020
            accepter_name = "David"  

            for _ in range(3):
                try:
                    user_account = int(input("Enter the account number of the recipient: "))
                    user_name = input("Enter the name of the recipient: ")

                    if user_account == accepter_account and user_name == accepter_name:
                        transfer_amount = float(input("Enter the amount you want to transfer: "))

                        if transfer_amount <= self._Banking__balance - 100:
                            self._Banking__balance -= transfer_amount
                            print(f"You transferred {transfer_amount} Birr successfully to account number {user_account}.")
                            print(f"To name: {user_name}")
                            print(f"Your current balance is now {self._Banking__balance}.")
                            break
                        else:
                            print(f"You have insufficient balance to transfer {transfer_amount} Birr.")
                            print("Please enter a sufficient amount again.")
                    else:
                        print("Please enter the correct account number or user name.")
                except ValueError:
                    print("Invalid input. Please enter the correct input.")
            else:
                print("Too many attempts. Goodbye!")

        # Dummy implementations
        def withdrawal_money(self):
            pass

        def deposit_money(self):
            pass

        def check_balance(self):
            pass

    class Authenticate:
        def __init__(self, name="Abgel", account_no=100023456789):
            self._name = name
            self._account_no = account_no 

        def authenticate_user(self):
            for _ in range(3):
                user_name = input("Enter your name: ")
                if user_name == self._name:
                    try:
                        user_account = int(input("Enter your account number: "))
                        if user_account == self._account_no:
                            return True  # Return True upon successful authentication
                    except ValueError:
                        print("Invalid account number. Please try again.")
                    print("Enter your correct account number again.")
                else:
                    print("Please enter your name correctly.")
            return False  # Return False if all attempts fail

    # Objects
    authenticate = Authenticate()
    withdrawals = Withdraw()
    deposits = Deposit()
    check1 = CheckBalance()
    transfer1 = Transfer()

    # Function for menu
    def main_menu():
        while True:
            print("**===== Welcome to CBE =====**\n")
            print("==***** Main Menu *****==\n")
            print("-- Press 1: To Withdraw Money\n")
            print("-- Press 2: To Deposit Money\n")
            print("-- Press 3: To Check Balance\n")
            print("-- Press 4: To Transfer Money\n")
            print("-- Press 0: To Exit from the System\n")
            try:
                choice = int(input("Please Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            match choice:
                case 1:
                    if authenticate.authenticate_user():
                        withdrawals.withdrawal_money()
                case 2:
                    if authenticate.authenticate_user():
                        deposits.deposit_money()
                case 3:
                    if authenticate.authenticate_user():
                        check1.check_balance()
                case 4:
                    if authenticate.authenticate_user():
                        transfer1.transfer_money()
                case 0:
                    print("Thank you, dear customer. Goodbye! Have a nice time!")
                    break
                case _:
                    print("Invalid choice. Please select a valid option.")

    # Run the main menu
    main_menu()

except Exception as e:
    print(f"An error occurred because: {e}")
