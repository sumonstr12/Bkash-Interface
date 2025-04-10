import os
from Authentication import Authentication
from Action import Action

class Account:

    amount = Authentication.balance
    number = Authentication.number
    def __init__(self, account_no):
        self.account_no = account_no
    
    action = Action(amount)
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def send_money(self):
        self.action.send_money()


    def cash_out(self):
        self.action.cash_out()

    def make_payment(self):
        self.action.make_payment()

    def check_balance(self):
        print(f"Bkash--\nAcc No : {self.account_no}\nAmount: {self.amount}")
    
    def mobile_recharge(self):
        self.action.mobile_recharge()

    def other_services(self):
        self.action.other_services()