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
    code = input("Enter: ")
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
                balance = my_wallet(balance, pin)
            else:
                print("Invalid Choice")

            again = input("Do you want to perform another operation? (yes/no): ").lower()
            if again != "yes":
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
        recipient_num = input("Enter the recipient's TeleStar phone number")
        transfer_amount = float(input("Enter the amount to transfer: "))
        # E-levy
        e_levy = transfer_amount * 0.01
        #Service Charge
        service_charge = transfer_amount * 0.005

        new_balance = balance - (transfer_amount + e_levy + service_charge)

        print(f'GHS{transfer_amount:.2f} has been sent successfuly with an E-levy charge of GHS{e_levy}')
        print(f'The service charge is GHS{service_charge:.2f}.')
        print(f'New Balance: GHS{new_balance:.2f}')

    elif network_choice == "2":
        recipient_num = input ("Enter the recipient's phone number")
        transfer_amount = float(input("Enter the amount to transfer"))
        #E-levy
        e_levy = transfer_amount * 0.01
        #Service Charge
        service_charge =transfer_amount * 0.075

        new_balance = balance - (transfer_amount + e_levy + service_charge)

        print(f'GHS{transfer_amount:.2f} has been sent successfuly with an E-levy charge of GHS{e_levy}')
        print(f'The service charge is GHS{service_charge:.2f}.')
        print(f'New Balance: GHS{new_balance:.2f}')
    else:
        print("Invalid network choice")
        return balance

    return new_balance



def buy_airtime_or_bundles(balance):
    pass

def cash_out(balance, pin):
    pass

def my_wallet(balance, pin):
    pass

main()

'''
def main_menu
if main_menu == "*150#":
    print("Welcome to Telestar Mobile Money! Please select an option:")
    print("1. Transfer Money")
    print("2. Airtime and Bundles")
    print("3. Allow Cash Out")
    print("4. My Wallet")
    wind1 = input("Enter Your Choice: ")
    if wind1 == "1":#Transfer Money
        print("Transfer Money:")
        print("1. TeleStar Network")
        print("2. Other Network")
        wind2 = input("Enter Your Choice:")
        if wind2 == "1":#Telestr phone No
            pass
        elif wind2 == "2":#Other phone No
            pass
    elif wind1 == "2":#Airtime and Bundles
        pass
    elif wind1 == "3":#Allow Cash Out
        pass
    elif wind1 == "4":#My Wallet
        pass
'''