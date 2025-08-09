"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64
import os

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()
    
def decode(text):
    return base64.b64decode(text.encode()).decode()


def password_strength(password):
    lengeth = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special_char = any(c in "!@#$%^&*().,<>" for c in password)
    
    socre = sum([len(password) >= 8, has_upper, has_digit, has_special_char])
    
    return ["Weak", "Medium", "Strong", "Very Strong"][min(socre, 3)]



def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    strength = password_strength(password)
    
    line = f"{website}||{username}||{password}"
    encode_line = encode(line)
    
    with open(VAULT_FILE, 'a', encoding="utf-8") as f:
        f.write(encode_line + "\n")
        
    print("Credential saved")
    
    
def view_credintials():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return
    
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            hidden_password = "*" * len(password)
            
            print(f" {website} | {username} | {password}")
            
def update_credential():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return

    website_f = input("Enter the website to update credentials: ").strip().lower()

    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    found = False

    for line in lines:
        decoded = decode(line.strip())
        website, username, password = decoded.split("||")

        if website == website_f:
            new_password = input("Enter new password: ").strip()
            # new_username = input("Enter new username: ").strip()
            
            
            updated_line = f"{website}||{username}||{new_password}"
            updated_lines.append(encode(updated_line) + "\n")
            found = True
        else:
            updated_lines.append(line)

    if not found:
        print(f"No credentials found for '{website_f}'.")
        return

    # 🔁 Overwrite the file just once, outside the loop
    with open(VAULT_FILE, 'w', encoding="utf-8") as f:
        f.writelines(updated_lines)

    print("✅ Credentials updated successfully.")
      
                                

                
    
    
    
            
            
def main():
    while True:
        print("Credential Manager")
        print("1. Add Credential")
        print("2. View Credentials")
        print("3. Update password")
        print("4. Exit")
        
        choice = input("Enter Your choice: ")
        
        match choice:
            case "1":
                add_credential()
            case "2":
                view_credintials()
            case "3":
                update_credential()
            case "4":
                break
            case _:
                print("Invalid choice!")

if __name__ == "__main__":
    main()
            
            
    