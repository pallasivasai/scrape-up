import json


class AddressBook:
    """
    A class to manage an address book.

    Create an instance of `AddressBook` class
    ```python
    book = AddressBook()
    ```

    | Method                | Details                                                                                         |
    | --------------------- | ----------------------------------------------------------------------------------------------- |
    | `add_contact(name, phone, email)`    | Adds a new contact with the provided name, phone, and email.                    |
    | `delete_contact(name)`               | Deletes the contact with the provided name.                                     |
    | `update_contact(name, phone, email)` | Updates the contact details for the provided name.                               |
    | `get_contact(name)`                  | Retrieves the contact details for the provided name.                            |
    | `list_contacts()`                    | Returns a list of all contacts in the address book.                              |
    ---
    """

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        return f"Contact {name} added."

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"Contact {name} deleted."
        else:
            return f"Contact {name} not found."

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            return f"Contact {name} updated."
        else:
            return f"Contact {name} not found."

    def get_contact(self, name):
        return self.contacts.get(name, f"Contact {name} not found.")

    def list_contacts(self):
        return self.contacts
