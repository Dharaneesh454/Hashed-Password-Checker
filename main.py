import bcrypt

# Simulated "stored" hashed password (this would be in your database)
def create_hashed_password(plain_password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_password.encode(), salt)

# Function to check if input matches stored hash
def verify_password(input_password: str, stored_hash: bytes) -> bool:
    return bcrypt.checkpw(input_password.encode(), stored_hash)

def main():
    # Step 1: Create a hashed password
    stored_hash = create_hashed_password("MySecurePassword123")
    print("Stored Hash (for demo):", stored_hash.decode())

    # Step 2: Get user input
    user_input = input("Enter your password: ")

    # Step 3: Verify
    if verify_password(user_input, stored_hash):
        print("✅ Password match! Access granted.")
    else:
        print("❌ Incorrect password! Access denied.")

if __name__ == "__main__":
    main()
