USERNAME = 'arish'
PASSWORD = 'pgc123'

def auth():
    max = 3
    i = 0
    while i < max:

        username = input("Enter your username ->")
        if not username == USERNAME:
            i+=1
            print(f"This Username does not exist. Please try again!\n{max-i} Attempts left")
            continue
            
        password = input("Enter your password ->")
        if not password == PASSWORD:
            i+=1
            print(f"Incorrect password. Please try again!\n{max-i} Attempts left")
            continue
        
        # At this point, authentication is done
        print("\nSuccessfully logged in!\n")
        return
    
    # Ar this point, the loop has terminated as max attempts have benn crossed
    print("Max attempts exceeded! You cannot log in now...")

auth()