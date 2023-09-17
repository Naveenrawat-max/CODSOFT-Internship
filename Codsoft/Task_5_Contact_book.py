contact_book = {}


def add_contact():
    """Allow users to add new contacts with their details."""
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")

    contact_book[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"{name} has been added to the contact book.")


def view_contact_list():
    """Display a list of all saved contacts with names and phone numbers."""
    print("\nContact List:")
    for name, contact_info in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {contact_info['Phone']}")
        print(f"Email: {contact_info['Email']}")
        print(f"Address: {contact_info['Address']}")
        print("-" * 20)


def search_contact():
    """Implement a search function to find contacts by name or phone number."""
    search_term = input("Enter the name or phone number to search for: ")

    for name, contact_info in contact_book.items():
        if search_term in name or search_term == contact_info['Phone']:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {contact_info['Phone']}")
            print(f"Email: {contact_info['Email']}")
            print(f"Address: {contact_info['Address']}")
            return

    print("Contact not found.")


def update_contact():
    """Enable users to update contact details."""
    name = input("Enter the name of the contact you want to update: ")

    if name in contact_book:
        print("Current Contact Information:")
        view_contact_details(name)

        phone = input(
            "Enter the new phone number (press Enter to keep current): ")
        email = input("Enter the new email (press Enter to keep current): ")
        address = input(
            "Enter the new address (press Enter to keep current): ")

        if phone:
            contact_book[name]["Phone"] = phone
        if email:
            contact_book[name]["Email"] = email
        if address:
            contact_book[name]["Address"] = address

        print("Contact information updated.")
        view_contact_details(name)
    else:
        print("Contact not found.")


def delete_contact():
    """Provide an option to delete a contact."""
    name = input("Enter the name of the contact you want to delete: ")

    if name in contact_book:
        del contact_book[name]
        print(f"{name} has been deleted from the contact book.")
    else:
        print("Contact not found.")


def view_contact_details(name):
    """Display the details of a specific contact."""
    contact_info = contact_book[name]
    print(f"Name: {name}")
    print(f"Phone: {contact_info['Phone']}")
    print(f"Email: {contact_info['Email']}")
    print(f"Address: {contact_info['Address']}")


def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thanks For Using This Contact Book, Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-6).")


if __name__ == "__main__":
    main()
