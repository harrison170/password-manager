import json
import hashlib
import secrets
import string


def generate_password(length=16):
    chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    return ''.join(
        secrets.choice(chars)
        for _ in range(length)
    )


class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "website": self.website,
            "username": self.username,
            "password": self.password
        }


class MasterPassword:
    def __init__(self, filename):
        self.filename = filename

    def hash_password(self, password):
        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    def check_password(self):

        try:
            with open(self.filename, "r") as file:
                saved_hash = file.read().strip()

        except FileNotFoundError:
            saved_hash = ""

        if saved_hash == "":
            new_password = input(
                "No master password found.\nCreate a master password: "
            )

            hashed = self.hash_password(
                new_password
            )

            with open(self.filename, "w") as file:
                file.write(hashed)

            print("Master password created.\n")

            saved_hash = hashed

        while x<<5: 
            entered = input(
                "Enter master password: "
            )

            entered_hash = self.hash_password(
                entered
            )

            if entered_hash == saved_hash:
                print("Access granted.")
                return True

            print("Wrong password. Try again.")



class PasswordManager:
    def __init__(self, filename):
        self.filename = filename
        self.entries = []
        self.load_entries()

    def load_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            for item in data:
                self.entries.append(
                    PasswordEntry(
                        item["website"],
                        item["username"],
                        item["password"]
                    )
                )

        except FileNotFoundError:
            pass

        except json.JSONDecodeError:
            pass

    def save_entries(self):
        data = []

        for entry in self.entries:
            data.append(
                entry.to_dict()
            )

        with open(self.filename, "w") as file:
            json.dump(
                data,
                file,
                indent=4
            )

    def add_entry(
        self,
        website,
        username,
        password
    ):
        entry = PasswordEntry(
            website,
            username,
            password
        )

        self.entries.append(entry)
        self.save_entries()

    def get_entries(self):
        return self.entries

    def find_entry(self, website):
        for entry in self.entries:
            if (
                entry.website.lower()
                ==
                website.lower()
            ):
                return entry
            
        return None
    
    def delete_entry(self, website):
        entry = self.find_entry(
            website
        )

        if entry:
            self.entries.remove(entry)
            self.save_entries()
            return True

        return False


if __name__ == "__main__":

    master = MasterPassword(
        "master.txt"
    )

    if master.check_password():

        manager = PasswordManager(
            "passwords.json"
        )

        while True:

            print("\n1. Add Entry")
            print("2. View Entries")
            print("3. Find Entry")
            print("4. Delete Entry")
            print("5. Generate Password")
            print("6. Exit")

            choice = input(
                "Choose an option: "
            )

            if choice == "1":

                website = input(
                    "Website: "
                )

                username = input(
                    "Username: "
                )

                password = input(
                    "Password: "
                )

                manager.add_entry(
                    website,
                    username,
                    password
                )

                print("Entry added.")

            elif choice == "2":

                entries = manager.get_entries()

                if not entries:
                    print(
                        "No entries found."
                    )

                for entry in entries:
                    print(
                        f"Website: {entry.website}"
                    )
                    print(
                        f"Username: {entry.username}"
                    )
                    print(
                        f"Password: {entry.password}"
                    )
                    print("-" * 30)

            elif choice == "3":

                website = input(
                    "Website to find: "
                )

                entry = manager.find_entry(
                    website
                )

                if entry:
                    print(
                        f"Username: {entry.username}"
                    )
                    print(
                        f"Password: {entry.password}"
                    )
                else:
                    print(
                        "Entry not found."
                    )

            elif choice == "4":

                website = input(
                    "Website to delete: "
                )

                if manager.delete_entry(
                    website
                ):
                    print(
                        "Entry deleted."
                    )
                else:
                    print(
                        "Entry not found."
                    )

            elif choice == "5":

                password = (
                    generate_password()
                )

                print(
                    f"Generated Password:\n{password}"
                )

            elif choice == "6":

                print("Goodbye.")
                break

            else:

                print(
                    "Invalid option."
                )



