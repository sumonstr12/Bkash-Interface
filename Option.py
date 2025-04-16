from Account import Account
from Authentication import Authentication

filename = "./Data.txt"
class Option:

    count = 0
    account_no = 0

    def authentication(self):
        print("===== Welcome to Bkash =====")
        
        self.account_no = int(input("Enter account NO: "))
        acc = Authentication(self.account_no, filename)
        if acc.Authenticate():
            return True
        else:
            return False

    def option(self):
        self.count += 1
        if self.count == 4:
            exit()
        
        if self.authentication():
            print("Please select an option from the following list:")
            print("1. Send Money:\n2. Cash Out:\n3. Make Payment:\n4. Check Balance:\n5. Mobile Recharge:\n6. Other Services:")
        else:
            print("Wrong Pin/ Account No...")
            self.authentication()

        option = int(input("Enter your option: "))
        
        opt = Account(self.account_no)

        if option == 1:
            opt.send_money()
        elif option == 2:
            opt.cash_out()
        elif option == 3:
            opt.make_payment()
        elif option == 4:
            opt.check_balance()
        elif option == 5:
            opt.mobile_recharge()
        elif option == 6:
            opt.other_services()
        else:
            print("1. again try\n2. exit")
            a = int(input("Choose carefully- "))
            if a == 1:
                option()
            else:
                print("Exit successfully...")
                exit()
