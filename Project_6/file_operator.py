# PR-6 File Operator

import datetime
import os


class JournalManager:

    FILE_NAME = "journal.txt"

    
    # Add a New Entry
    def add_entry(self):
        try:
            entry = input("Enter your journal entry:\n").strip()

            if not entry:
                print("Journal entry cannot be empty!")
                return

            time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

            print(time)

            with open(self.FILE_NAME, "a") as file:
                file.write(f"\n[{time}]\n")
                file.write(entry + "\n")

            print("\nYour entry has been successfully added!")

        except PermissionError:
            print("Permission denied! Cannot write to the file.")

        except Exception as e:
            print("Error:", e)


    # View All Entries
    def view_entries(self):

        try:
            with open(self.FILE_NAME, "r") as file:
                content = file.read()

                if content.strip():
                    print("\n===== All Journal Entries =====")
                    print(content)

                else:
                    print("\nJournal is empty!\n")

        except FileNotFoundError:
            print("Journal file not found.")

        except PermissionError:
            print("Permission denied! Cannot read the file.")

        except Exception as e:
            print("Error while reading entries:", e)


    # Search Entry
    def search_entry(self):

        keyword = input("\nEnter keyword or date for search: ").strip()

        if not keyword:
            print("Please enter a keyword or date.")
            return

        try:
            with open(self.FILE_NAME, "r") as file:
                content = file.read()

            entries = content.split("\n\n")
            found = False

            print("\n===== Search Result =====")

            for entry in entries:

                if keyword.lower() in entry.lower():
                    print(entry)
                    found = True

            if not found:
                print("No matching journal entry found.")

        except FileNotFoundError:
            print("Journal file not found.")

        except PermissionError:
            print("Permission denied! Cannot read the file.")

        except Exception as e:
            print("Error while searching:", e)


    # Delete All Entries
    def delete_entries(self):

        try:
            confirmation = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()

            if confirmation == "yes":

                if os.path.exists(self.FILE_NAME):

                    os.remove(self.FILE_NAME)

                    print("All journal entries deleted successfully!")

                else:
                    print("Journal file does not exist.")

            elif confirmation == "no":
                print("Your journal entries are safe.")

            else:
                print("Please enter only 'yes' or 'no'.")

        except FileNotFoundError:
            print("Journal file not found.")

        except PermissionError:
            print("Permission denied! Cannot delete the file.")

        except Exception as e:
            print("Error while deleting:", e)


    # Create Journal File
    def create_file(self):

        try:
            # 'x' mode = create a new file
            with open(self.FILE_NAME, "x") as file:
                file.write("")

            print("Journal file created successfully!")

        except FileExistsError:
            print("Journal file already exists.")

        except PermissionError:
            print("Permission denied! Cannot create the file.")

        except Exception as e:
            print("Error while creating file:", e)


    # Clear All Entries
    def clear_entries(self):

        try:

            if not os.path.exists(self.FILE_NAME):
                print("Journal file does not exist.")
                return

            confirmation = input("\nDo you want to clear all entries? (yes/no): ").strip().lower()

            if confirmation == "yes":

                with open(self.FILE_NAME, "w") as file:
                    file.write("")

                print("All journal entries cleared successfully!")

            elif confirmation == "no":
                print("Your journal entries are safe.")

            else:
                print("Please enter only 'yes' or 'no'.")

        except FileNotFoundError:
            print("Journal file not found.")

        except PermissionError:
            print("Permission denied! Cannot modify the file.")

        except Exception as e:
            print("Error while clearing entries:", e)


# Main Menu

my_journal = JournalManager()

while True:

    print("\n===== Welcome to Personal Journal Manager =====")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Create Journal File")
    print("6. Clear All Entries")
    print("7. Exit")

    choice = input("\nEnter your choice: ").strip()


    if choice == "1":
        my_journal.add_entry()

    elif choice == "2":
        my_journal.view_entries()

    elif choice == "3":
        my_journal.search_entry()

    elif choice == "4":
        my_journal.delete_entries()

    elif choice == "5":
        my_journal.create_file()

    elif choice == "6":
        my_journal.clear_entries()

    elif choice == "7":
        print("Thank you for using Personal Journal Manager!")
        break

    else:
        print("Invalid input. Please select a valid option.")
