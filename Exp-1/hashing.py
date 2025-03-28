# 16.01.2025
# Validating passwords with SHA-256


import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_password(stored_password_hash, provided_password):
    return stored_password_hash == hash_password(provided_password)

# Example usage
if __name__ == "__main__":
    password = "mypassword"
    stored_password_hash = hash_password(password)    
    
    provided_password = input("Enter your password: ")
    print("Stored password hash  : ",stored_password_hash)
    print("Entered password hash : ",hashlib.sha256(provided_password.encode()).hexdigest())
    
    if validate_password(stored_password_hash, provided_password):
        print("Password is valid!")
    else:
        print("Invalid password.")