print("""

Welcome to ATM application

1. To be able to see How much Money you got in your bank account.

2. Inserting Money into your bank account.

3. press 3 to quit the programme.




""")

Account_ID = "alpay"
Acoount_Password = "123456"
Account_Limit = 1500
Amount = 0
token = 3



while True:

    Account_ID_Bank = input(print("Please enter your account ID:"))
    Account_password_bank = input(print("Please enter your account password:"))

    if(Account_ID != Account_ID_Bank and Acoount_Password == Account_password_bank ):
        print("You entered wrong ID")

    elif(Account_ID == Account_ID_Bank and Acoount_Password != Account_password_bank ):
        print("You entered wrong password")

    elif(Account_ID != Account_ID_Bank and Acoount_Password != Account_password_bank ):
        print("You entered wrong ID and password")
        token -= 1

        print("You have only {} right to enter after that.".format(token))

        if (token == 0):

            print("You cannot enter any longer.")
            break

    else:

        print("You entered to the system successfully.")

        while True:

            transaction_id = int(input(print("What type of transaction you would like to do 1: Learn amount of money in your Acc 2:Insert Money 3:Quit the transaction")))

            if(transaction_id == 1):

                print("Money in your bank account: {}".format(Account_Limit))

            elif(transaction_id == 2):

                Amount = int(input(print("Insert the amount of money to your account:")))

                Account_Limit = Account_Limit + Amount

                print("Amount of the money in your account is :{}".format(Account_Limit))

                Answer = str(input(print("Would you like to continue the process? If yes, please type Yes/No")))

                if(Answer == "No"):
                    print("Transaction is being closed. You are out of the account")
                    break

                else:
                    continue

            elif(transaction_id == 3):

                print("Transaction is being closed. You are out of the account")
                break

            else:
                continue