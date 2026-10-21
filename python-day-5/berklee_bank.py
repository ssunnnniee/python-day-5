bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}

def authenticate_user(database):

    '''
    Task: Ask for username and Pin until they match
    Name: check_user_fake_or_real
    Input: username, pin 
    Side Effects: N/A
    Return: N/A
    '''
    print("Welcome message")
    
    while True:
        username = input("Priya")
        pin = input("4821")

        username = input("Carlos")
        pin = input("1092")

        username = input("Amira")
        pin = input("0000")

        username = input("Jordan")
        pin = input("9999")

        
        
        if username in database and database[username]["pin"] == pin:
            print("Login successful. Welcome, {username}!")
            return username
        else:
            print("Username and pin doesn't match or not exist. Try Again")


def check_balance(database, username):

    '''
    Task: Display the current balance for the given user.
    Name: check_balance.
    Input: dict, username.
    Side Effects: N/A
    Return: N/A
    '''

if True:
            username = input("Priya")
            balance = 100
    
            username = input("Carlos")
            balance = 300
            
            username = input("Amira")
            balance = 0
      
            username = input("Jordan")
            balance = 7788
            
            print( "User's Balance")
            print("Your current balance is: $user's balance")


def deposit_money(database, username):

    '''
    Task: Ask for a deposit amount and add it to the user's account.
    Name: add_money.
    Input: dict, username
    Side Effects: N/A
    Return: N/A
    '''        
    
       

    
