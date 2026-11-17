contacts = [] 
 
def add_contact(): 
    name = input("Enter name: ")     
    phone = input("Enter phone number: ")     
    email = input("Enter email: ") 
 
    contact = { 
        "name": name, 
        "phone": phone, 
        "email": email 
    } 
 
    contacts.append(contact)     
    print("Contact added successfully!") 
 
def search_contact(): 
    name = input("Enter name to search: ") 
 
    for contact in contacts:         
         if contact["name"].lower() == name.lower(): 
            print("Name:", contact["name"])             
            print("Phone:", contact["phone"])             
            print("Email:", contact["email"])             
            return 
 
    print("Contact not found!") 
 
def update_contact(): 
    name = input("Enter name to update: ") 
 
    for contact in contacts:         
        if contact["name"].lower() == name.lower(): 
            contact["phone"] = input("Enter new phone number: ") 
            contact["email"] = input("Enter new email: ")             
            print("Contact updated successfully!")             
            return 
 
    print("Contact not found!") 
 
def delete_contact(): 
    name = input("Enter name to delete: ") 
 
    for contact in contacts:         
        if contact["name"].lower() == name.lower(): 
            contacts.remove(contact)             
            print("Contact deleted successfully!")            
            return 
 
    print("Contact not found!") 
 
def display_contacts():     
    if not contacts: 
        print("No contacts available!")    
    else:         
        for contact in contacts: 
            print(contact) 
 
while True: 
    print("\n--- CONTACT BOOK ---")    
    print("1. Add Contact")    
    print("2. Search Contact")     
    print("3. Update Contact")     
    print("4. Delete Contact")    
    print("5. Display Contacts")     
    print("6. Exit") 
 
    choice = input("Enter your choice: ") 
 
    if choice == "1":         
        add_contact()    
    elif choice == "2":         
        search_contact()     
    elif choice == "3":         
        update_contact()    
    elif choice == "4":         
        delete_contact()     
    elif choice == "5":        
         display_contacts()     
    elif choice == "6": 
        print("Exiting Contact Book.")         
        break     
    else: 
        print("Invalid choice!") 
