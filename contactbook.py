class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")

    def search_contact(self, search_key):
        if search_key in self.contacts:
            details = self.contacts[search_key]
            print(f"Name: {search_key}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
        else:
            print("Contact not found.")

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            print(f"Contact {name} updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print("Contact not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_key = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_key)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone, email, address)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
