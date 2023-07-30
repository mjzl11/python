def show_passwords():
    password = "123456789"
    
    userPassword = input("Input the password: ")
    
    if userPassword == password:
        passwords = ["password123", "987543", "123e345"]
        
        print("Password save:")
        for password in passwords:
            print(password)
    else:
        print("Wrong password")

show_passwords()