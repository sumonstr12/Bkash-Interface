account_no = ''
password = ''
balance = 0

try:
    with open ('small_project_with_ostad/Bkash interface/Data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(':', 1)
            if key.strip() == 'acc_no':
                acc_no = int(value.strip())
            if key.strip() == 'password':
                password = str(value.strip())
            if key.strip() == 'balance':
                balance = value.strip()
    
        print(f"Balance: {balance}\nAcc_no: {acc_no}")
        print(type(acc_no))


except FileNotFoundError:
    print("Error: File Not Found")
except Exception as e:
    print(f"Error Occured : {str(e)}")