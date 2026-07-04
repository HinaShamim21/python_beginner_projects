contacts = {}


def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print(f"{name} already exists! Use Update instead.")
        return
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"{name} added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return
    print(f"\nYou have {len(contacts)} contact(s):")
    for name, info in contacts.items():
        print(f"{name} -> Phone: {info['phone']}, Email: {info['email']}")


def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"{name} -> Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print("Contact found. Please enter the new details.")
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        contacts[name]["phone"] = new_phone
        contacts[name]["email"] = new_email
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")


# def load_sample_contacts(n=15):
#     """Auto-generates n fake contacts for quick testing."""
#     for i in range(1, n + 1):
#         name = f"Contact{i}"
#         contacts[name] = {
#             "phone": f"030012340{i:02d}",
#             "email": f"contact{i}@mail.com"
#         }
#     print(f"{n} sample contacts loaded for testing!")


def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Load 15 Sample Contacts (for testing)")
        print("7. Exit")

        choice = input("Choose an option: ")

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
        # elif choice == "6":
        #     load_sample_contacts()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()