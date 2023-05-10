import json
import os

class Phonebook:
    def __init__(self, name):
        self.name = name
        if os.path.isfile(f"{self.name}.json"):
            with open(f"{self.name}.json", "r") as f:
                self.contacts = json.load(f)
        else:
            self.contacts = []

    def add_contact(self, first_name, last_name, phone_number, city, state):
        contact = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "city": city,
            "state": state
        }
        self.contacts.append(contact)

    def search_by_first_name(self, first_name):
        results = []
        for contact in self.contacts:
            if contact["first_name"] == first_name:
                results.append(contact)
        return results

    def search_by_last_name(self, last_name):
        results = []
        for contact in self.contacts:
            if contact["last_name"] == last_name:
                results.append(contact)
        return results

    def search_by_full_name(self, full_name):
        results = []
        for contact in self.contacts:
            if f"{contact['first_name']} {contact['last_name']}" == full_name:
                results.append(contact)
        return results

    def search_by_phone_number(self, phone_number):
        results = []
        for contact in self.contacts:
            if contact["phone_number"] == phone_number:
                results.append(contact)
        return results

    def search_by_city_or_state(self, location):
        results = []
        for contact in self.contacts:
            if contact["city"] == location or contact["state"] == location:
                results.append(contact)
        return results

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if contact["phone_number"] == phone_number:
                self.contacts.remove(contact)
                return True
        return False

    def update_contact(self, phone_number, first_name=None, last_name=None, city=None, state=None):
        for contact in self.contacts:
            if contact["phone_number"] == phone_number:
                if first_name is not None:
                    contact["first_name"] = first_name
                if last_name is not None:
                    contact["last_name"] = last_name
                if city is not None:
                    contact["city"] = city
                if state is not None:
                    contact["state"] = state
                return True
        return False

    def save_to_file(self):
        with open(f"{self.name}.json", "w") as f:
            json.dump(self.contacts, f)

if __name__ == "__main__":
    phonebook = Phonebook("my_phonebook")

    while True:
        print("\nWelcome to the Phonebook application!")
        print("Please choose an option:")
        print("1. Add a new contact")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by phone number")
        print("6. Search by city or state")
        print("7. Delete a contact")
        print("8. Update a contact")
        print("9. Exit the program")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            phonebook.add_contact(first_name, last_name, phone_number, city, state)
            print("\nContact added successfully!")

        elif choice == "2":
            first_name = input("Enter first name to search: ")
            results = phonebook.search_by_first_name(first_name)
            if results:
                print(f"\nSearch results for '{first_name}':")
                for contact in results:
                    print(contact)
            else:
                print(f"\nNo contacts found with first name '{first_name}'.")

        elif choice == "3":
            last_name = input("Enter last name to search: ")
            results = phonebook.search_by_last_name(last_name)
            if results:
                print(f"\nSearch results for '{last_name}':")
                for contact in results:
                    print(contact)
            else:
                print(f"\nNo contacts found with last name '{last_name}'.")

        elif choice == "4":
            full_name = input("Enter full name to search: ")
            results = phonebook.search_by_full_name(full_name)
            if results:
                print(f"\nSearch results for '{full_name}':")
                for contact in results:
                    print(contact)
            else:
                print(f"\nNo contacts found with full name '{full_name}'.")

        elif choice == "5":
            phone_number = input("Enter phone number to search: ")
            results = phonebook.search_by_phone_number(phone_number)
            if results:
                print(f"\nSearch results for '{phone_number}':")
                for contact in results:
                    print(contact)
            else:
                print(f"\nNo contacts found with phone number '{phone_number}'.")

        elif choice == "6":
            location = input("Enter city or state to search: ")
            results = phonebook.search_by_city_or_state(location)
            if results:
                print(f"\nSearch results for '{location}':")
                for contact in results:
                    print(contact)
            else:
                print(f"\nNo contacts found in '{location}'.")

        elif choice == "7":
            phone_number = input("Enter phone number of contact to delete: ")
            if phonebook.delete_contact(phone_number):
                print(f"\nContact with phone number '{phone_number}' has been deleted.")
            else:
                print(f"\nNo contact found with phone number '{phone_number}'.")

        elif choice == "8":
            phone_number = input("Enter phone number of contact to update: ")
            first_name = input("Enter updated first name (leave blank if no change): ")
            last_name = input("Enter updated last name (leave blank if no change): ")
            city = input("Enter updated city (leave blank if no change): ")
            state = input("Enter updated state (leave blank if no change): ")
            if phonebook.update_contact(phone_number, first_name, last_name, city, state):
                print(f"\nContact with phone number '{phone_number}' has been updated.")
            else:
                print(f"\nNo contact found with phone number '{phone_number}'.")

        elif choice == "9":
            print("\nThank you for using the Phonebook application!")
            phonebook.save_to_file()
            break

        else:
            print("\nInvalid choice. Please try again.")
