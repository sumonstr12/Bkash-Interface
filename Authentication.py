

# filename = "./Data.txt"
class Authentication:
    def __init__(self, acc_no=None, filename=None):
        self.__acc_no = acc_no
        self.filename = filename

    __account_no = ''
    pin = 0
    balance = 0
    number = 0

    def data_function(self):
        data = {}
        try:
            with open (self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    key, value = line.strip().split(':', 1)
                    data[key.strip()] = (value.strip())
                return data


        except FileNotFoundError:
            print("Error: File Not Found")
        except Exception as e:
            print(f"Error Occured : {str(e)}")

    
    def Authenticate(self):
        data = self.data_function()
        if int(data["acc_no"]) == self.__acc_no:
            passw  = int(input("Enter Pin: "))
            if int(data["pin"]) == passw:
                return True
            else :
                return False
        else:
            print("Acount Not Found..")
