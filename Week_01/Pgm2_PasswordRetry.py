password = "openAI123"

for retryAttempts in range(1,10):
    enterPassword = input("Enter password : ")
    if (password ==  enterPassword):
        print("Login Successful")
        break
    else:
        if(retryAttempts == 3):
            print("Account Locked")
            break