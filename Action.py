
from Authentication import Authentication
from FileHandling import FileHandling
# from Option import Option

filename1 = "small_project_with_ostad/Bkash interface/Data.txt"
filename2 = "small_project_with_ostad/Bkash interface/Details.txt"

class Action:

    pinp = Authentication.pin

    def __init__(self, amount):
        self.amount = amount

    obj1 = FileHandling(filename1)
    obj2 = FileHandling(filename2)

    def again_try(self):
        print("1. Again try\n2. exit")
        o = int(input("Choose Option--"))
        if o == 1:
            return True
        else:
            exit()


    def send_money(self):  
        num = input("Enter Reciever Bkash ACC no.: ")
        total = int(input("Enter Total Amount: "))
        pin = int(input("Enter PIN: "))
        if pin == self.pinp:
            self.amount = self.amount - total
            self.obj1.update_field("balance", self.amount)

            template = "Send {total} tk successfully to {num}\nAccount balance is {self.amount} tk"

            print(template.format(total=total, num=num))
            self.obj2.update_history(template, total=total, num=num)
            # self.opt.option()
        else:
            print(f"Failed to send money..")
            if self.again_try():
                self.send_money()

    def cash_out(self):
        agent_num = input("Enter Agent Number: ")
        total = int(input("Enter Amount"))
        pin = int(input("Enter PIN: "))
        if pin == self.pinp:
            self.amount = self.amount - total
            self.obj1.update_field("balance", self.amount)
            tem = "CashOut {total} tk successfully to {num}\nAccount balance is {self.amount} tk"
            print(tem.format(total=total, num=agent_num))
            self.obj2.update_history(tem, total=total, num=agent_num)
        else:
            print(f"Failed to Cashout..")
            if self.again_try():
                self.cash_out()


    def make_payment(self):
        mar_number = input("Enter Merchant Number: ")
        total = int(input("Enter Amount: "))
        invoice = input("Enter Invoice Number: ")
        pin = int(input("Enter PIN: "))
        if pin == self.pinp:
            self.amount = self.amount - total
            self.obj1.update_field("balance", self.amount)
            tem = "Payment of {total} tk successfully to {num} for invoice {invoice}\nAccount balance is {self.amount} tk"
            print(tem.format(total=total, num=mar_number, invoice=invoice))
            self.obj2.update_history(tem, total=total, num=mar_number, invoice=invoice)
        else:
            print("Payment Failed..")
            if self.again_try():
                self.make_payment()
    
    def mobile_recharge(self):
        number = input("Enter Mobile Number: ")
        total = int(input("Enter Amount: "))
        pin = int(input("Enter PIN: "))
        if pin == self.pinp:
            self.amount = self.amount - total
            self.obj1.update_field("balance", self.amount)
            tem = "Recharge {total} tk successfully to {num}\nAccount balance is {self.amount} tk"
            print(tem.format(total=total, num=number))
            self.obj2.update_history(tem, total=total, num=number)
        else:
            print("Recharge Failed..")
            if self.again_try():
                self.mobile_recharge()
    
    def check_balance(self):
        pin = int(input("Enter PIN: "))
        if pin == self.pinp:
            print(f"Your Balance is {self.amount} tk")
        else:
            print("Failed to check balance..")
            if self.again_try():
                self.check_balance()

    def other_services(self):
        print("1. Pay Bill\n2. Buy Package\n3. Buy Ticket\n4. Buy Product\n5. Change PIN")
        option = int(input("Choose an option: "))
        if option == 1:
            self.pay_bill()
        elif option == 2:
            self.buy_package()
        elif option == 3:
            self.buy_ticket()
        elif option == 4:
            self.buy_product()
        elif option == 5:
            self.change_pin()
        else:
            print("Invalid Option..")
            exit()

    def pay_bill(self):
        type_bill = {
            1: "Electricity",
            2: "Gas",
            3: "Water",
            4: "Internet",
            5: "Mobile"
        }
        print("Choose Bill Type:")
        print("1. Electricity\n2. Gas\n3. Water\n4. Internet\n5. Mobile")
        bill_type = type_bill.get(int(input("Enter Bill Type: ")), "Invalid Bill Type")
        if bill_type == "Invalid Bill Type":
            print("Invalid Option..")
            exit()
        total = int(input("Enter Amount: "))
        pin = int(input("Enter PIN: "))
        if pin == self.pinp:
            self.amount = self.amount - total
            self.obj1.update_field("balance", self.amount)
            tem = "Bill payment of {total} tk for {bill_type}\nAccount balance is {self.amount} tk"
            print(tem.format(total=total, bill_type=bill_type))
            self.obj2.update_history(tem, total=total, bill_type=bill_type)
        else:
            print("Bill Payment Failed..")
            if self.again_try():
                self.pay_bill()

    def buy_package(self):
        type_pak = {
            1: "daily package - 100 tk",
            2: "weekly package - 500 tk",
            3: "monthly package - 1500 tk",
            4: "yearly package - 5000 tk",
        }
        print("Choose Package Type:")
        for key, value in type_pak.items():
            print(f"{key}. {value}")
        package_type = type_pak.get(int(input("Enter Package Type: ")), "Invalid Package Type")
        total = int(input("Enter Amount: "))
        pin = int(input("Enter PIN: "))
        if pin == self.pinp:
            self.amount = self.amount - total
            self.obj1.update_field("balance", self.amount)
            tem = "Package {package_type} bought for {total} tk\nAccount balance is {self.amount} tk"
            print(tem.format(package_type=package_type, total=total))
            self.obj2.update_history(tem, package_type=package_type, total=total)
        else:
            print("Package Purchase Failed..")
            if self.again_try():
                self.buy_package()

    def buy_ticket(self):
        type_ticket = {
            1: "Movie",
            2: "Concert",
            3: "Event",
            4: "Theater",
        }
        print("Choose Ticket Type:")
        for key, value in type_ticket.items():
            print(f"{key}. {value}")
        ticket_type = type_ticket.get(int(input("Enter Ticket Type: ")), "Invalid Ticket Type")
        total = int(input("Enter Amount: "))
        pin = int(input("Enter PIN: "))
        if pin == self.pinp:
            self.amount = self.amount - total
            self.obj1.update_field("balance", self.amount)
            tem = "Ticket {ticket_type} bought for {total} tk\nAccount balance is {self.amount} tk"
            print(tem.format(ticket_type=ticket_type, total=total))
            self.obj2.update_history(tem, ticket_type=ticket_type, total=total)
        else:
            print("Ticket Purchase Failed..")
            if self.again_try():
                self.buy_ticket()

    def buy_product(self):
        product_name = input("Enter Product Name: ")
        total = int(input("Enter Amount: "))
        pin = int(input("Enter PIN: "))
        if pin == self.pinp:
            self.amount = self.amount - total
            self.obj1.update_field("balance", self.amount)
            tem = "Product {product_name} bought for {total} tk\nAccount balance is {self.amount} tk"
            print(tem.format(product_name=product_name, total=total))
            self.obj2.update_history(tem, product_name=product_name, total=total)
        else:
            print("Product Purchase Failed..")
            if self.again_try():
                self.buy_product()

    def change_pin(self):
        pin =  int(input("Enter Old Pin: "))
        pinNew = int(input("Enter New Pin(Must be 4 digits): "))
        if len(str(pinNew)) != 4:
            print("Pin must be 4 digits..")
            if self.again_try():
                self.change_pin()
        pinConfirm = int(input("Confirm New Pin: "))
        if pin == self.pinp and pinNew == pinConfirm:
            self.obj1.update_field("pin", pinNew)
        else:
            print("Unsuccessfull Operation...")
            if self.again_try():
                self.change_pin()
        print("Pin Changed Successfully...")
