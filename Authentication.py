
class Authentication:
    def __init__(self, acc_no):
        self.__acc_no = acc_no
    

    __account_no = ''
    pin = 0
    balance = 0
    number = 0

    try:
        with open ('small_project_with_ostad/Bkash interface/Data.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(':', 1)
                if key.strip() == 'acc_no':
                    __account_no = int(value.strip())
                if key.strip() == 'pin':
                    pin = int(value.strip())
                if key.strip() == 'balance':
                    balance = int(value.strip())
                if key.strip() == 'number':
                    number = value.strip()


    except FileNotFoundError:
        print("Error: File Not Found")
    except Exception as e:
        print(f"Error Occured : {str(e)}")

    
    def Authenticate(self):
        if self.__account_no == self.__acc_no:
            passw  = int(input("Enter Pin: "))
            if self.pin == passw:
                return True
            else :
                return False
        else:
            print("Acount Not Found..")
