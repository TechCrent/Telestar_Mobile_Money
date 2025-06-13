#Transfer Money
#Buy Airtime and Bundles
#Allow Cash Out
#Check/Top up Wallet
#Initial Amount = GHS 1000
#4-digit MOMO PIN "7209"

# *150# for the main menu

def main():
    # Initial Wallet Balance
    balance = 1000
    # Default Pin
    pin = "7209"
    #Short Code Input
    code = input("Enter Short Code: ")
    #Changing Balance
    balance = main_menu(code,balance,pin)
    return

def main_menu(code,balance,pin):
    if code == "*150#":
        while True:
            print("Welcome to Telestar Mobile Money! Please select an option:")
            print("1. Transfer Money")
            print("2. Airtime and Bundles")
            print("3. Allow Cash Out")
            print("4. My Wallet")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                balance = transfer_money(balance)
            elif choice == "2":
                balance = buy_airtime_or_bundles(balance)
            elif choice == "3":
                balance = cash_out(balance, pin)
            elif choice == "4":
                balance = my_wallet(balance)
            else:
                print("Invalid Choice")

            again = input("Do you want to perform another operation? (yes/no): ").lower()
            if again != "yes" and again != "y":
                print("Thank you for using Telestar Mobile Money!")
                break
    else:
        print("Invalid Code")
    return balance


def transfer_money(balance):
    print("Transfer Money:")
    print("1. Telestar Network")
    print("2. Other Network")

    network_choice = input("Enter your transfer choice: ")

    if network_choice == "1":
        recipient_num = input("Enter the recipient's TeleStar phone number: ")

        if not(len(recipient_num) == 10 and recipient_num.startswith("059")):
            print("This Number Does Not Exist In The Telestar Network System")
            return balance

        transfer_amount = float(input("Enter the amount to transfer: "))
        # E-levy
        e_levy = transfer_amount * 0.01
        #Service Charge
        service_charge = transfer_amount * 0.005

        total_deduction = transfer_amount + e_levy + service_charge

        if total_deduction > balance:
            print("Insufficient balance")
            return balance

        new_balance = balance - total_deduction

        print(f'GHS{transfer_amount:.2f} has been sent successfully with an E-levy charge of GHS{e_levy}')
        print(f'The service charge is GHS{service_charge:.2f}.')
        print(f'New Balance: GHS{new_balance:.2f}')
        return new_balance


    elif network_choice == "2":
        recipient_num = input ("Enter the recipient's phone number: ")

        if not(len(recipient_num) == 10 and recipient_num.startswith(("050","026","023"))):
            print("This Number Does Not Exist In The Telestar Network System")
            return balance

        transfer_amount = float(input("Enter the amount to transfer"))
        #E-levy
        e_levy = transfer_amount * 0.01
        #Service Charge
        service_charge =transfer_amount * 0.075

        total_deduction = transfer_amount + e_levy + service_charge

        if total_deduction > balance:
            print("Insufficient Amount")
            return balance

        new_balance = balance - total_deduction

        print(f'GHS{transfer_amount:.2f} has been sent successfully with an E-levy charge of GHS{e_levy}')
        print(f'The service charge is GHS{service_charge:.2f}.')
        print(f'New Balance: GHS{new_balance:.2f}')

    else:
        print("Invalid network choice")
        return balance

    return new_balance


def buy_airtime_or_bundles(balance):
    print("Airtime and Bundles:")
    print("1. Buy Airtime")
    print("2. Buy Bundles")

    airtime_or_bundle = input("Enter your choice: ")

    if airtime_or_bundle == "1":
        airtime_amount = float(input("Enter the amount to purchase: "))

        if airtime_amount > balance:
            print("Insufficient Amount")
            return balance

        new_balance_2 = balance - airtime_amount

        print(f'GHS{airtime_amount:.2f} airtime has been successfully purchased')
        print(f"New balance: GHS{new_balance_2}")
        return new_balance_2

    elif airtime_or_bundle == "2":
        print("Bundles:")
        print("1. GHS 5(280 MB)")
        print("2. GHS 10(667 MB")
        print("3. GHS 100(10GB)")

        bundle_type = input("Choose your bundle type: ")

        if bundle_type == "1":

            if balance < 5:
                print("Insufficient Amount")
                return balance

            new_balance_2 = balance - 5

            print("280 MB Data Bundle successfully purchased")
            print(f"New balance: GHS{new_balance_2:.2f}")
            return new_balance_2

        elif bundle_type == "2":

            if balance < 10:
                print("Insufficient Amount")
                return balance

            new_balance_2 = balance - 10

            print("667 MB Data Bundle successfully purchased")
            print(f"New balance: GHS{new_balance_2:.2f}")
            return new_balance_2

        elif bundle_type == "3":

            if balance < 100:
                print("Insufficient Amount")
                return balance

            new_balance_2 = balance - 100

            print("10 GB Data Bundle successfully purchased")
            print(f"New balance: GHS{new_balance_2:.2f}")
            return new_balance_2

        else:
            print("Invalid Bundle Type Inputted")
            new_balance_2 = balance

    else:
        print("Invalid Choice")
        return balance

    return new_balance_2


def cash_out(balance, pin):
    print("Allow CashOUt:")
    print("1. Yes")
    print("2. No")
    allow_cashout = input("Enter your choice: ")

    if allow_cashout == "1":
        cashout_amount = float(input("Enter the amount to allow for Cash Out: "))

        user_pin = input("Enter your 4-digit PIN: ")

        if balance < cashout_amount:
            print("Insufficient Amount")
            return balance



        if user_pin == pin:
            new_balance_3 = balance - cashout_amount
            print("Cash Out Successfully allowed")
            print(f"New balance: GHS{new_balance_3:.2f}")
            return new_balance_3

        else:
            print("Incorrect Pin")
            new_balance_3 = balance


    elif allow_cashout == "2":
        print("Thank you for using Telestar Mobile Money!")
        return balance

    else:
        print("Invalid Input")
        return balance

    return new_balance_3

def my_wallet(balance):
    print("My Wallet:")
    print("1. Top Up Balance")
    print("2. Check Balance")

    wallet_choice = input("Enter your choice: ")

    if wallet_choice == "1":
        topup_amount = float(input("Enter amount to top up your balance: "))
        new_balance_4 = balance + topup_amount
        print(f"Balance top up is successful. New balance: GhS{new_balance_4}")
        return new_balance_4

    elif wallet_choice == "2":
        print(f"Your current balance is: GHS{balance}")
        return balance

    else:
        print("Invalid Choice")
        new_balance_4 = balance


main()
