"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""


import csv
import os

FILE_NAME = "contacts.csv"
NAME = "Name"
PHONE = "Phone"
EMAIL = "Email"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([NAME, PHONE, EMAIL])
        
def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    
    
    #check for duplicates
    with open(FILE_NAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
           if row[NAME].lower() == name.lower():
               print("Contact name already exists")
               return
           
    with open(FILE_NAME, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added")
        
        
def view_contacts():
    with open(FILE_NAME, 'r', encoding="utf-8") as f: 
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 2:
            print("No contacts found")
            return
        
        print("\nYour contacts:\n")
        
        for row in rows[1:]:
            if len(row) >= 3:
                print(f"{row[0]} | {row[1]} | {row[2]}")
        print()
            
            
def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False
        
    with open(FILE_NAME, 'r', encoding="utf-8") as f: 
        reader = csv.DictReader(f)
        for row in reader:
            if term in row[NAME].lower():
                print(f"\n{row[NAME]} | {row[PHONE]} | {row[EMAIL]}")
                found = True
    if not found:
        print("No matching contact found")
        
        
        
        
def update_contact():
    term = input("Enter the name to update: ").strip().lower()
    updated = False
    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))


    for row in rows:
        if row[NAME].strip().lower() == term:
            print(f"\n Current contact: {row}")
            row[NAME] = input("Name: ").strip()
            row[PHONE] = input("Phone: ").strip()
            row[EMAIL] = input("Email: ").strip()
            updated = True
            break
    
    if updated:
        with open(FILE_NAME, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, [NAME, PHONE, EMAIL])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Contact updated successfully!")
    else:
        print("\n❌ Contact not found.")
            
            

def delete_contact():
    term = input("Enter the name to Delete: ").strip().lower()
    updated = False
    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))


    for row in rows:
        if row[NAME].strip().lower() == term:
            rows.remove(row)
            updated = True
            break
    
    if updated:
        with open(FILE_NAME, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, [NAME, PHONE, EMAIL])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Contact Deleted successfully!")
    else:
        print("\n❌ Contact not found.")
    
                 
    
    
def main():
    while True:
        print("\n Contact Book")
        print("1. Add Contact")
        print("2. View All Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")        
        print("6. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thanks for using our software")
            break
        else:
            print("Invalid choice of number")
        
           
if __name__ == "__main__":
    main()