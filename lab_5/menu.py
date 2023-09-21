"""
A menu - you need to add the database and fill in the functions. 
"""
from record_db import Records


def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input("Enter your choice: ")
        if choice == "1":
            display_all_records()
        elif choice == "2":
            search_by_name()
        elif choice == "3":
            add_new_record()
        elif choice == "4":
            edit_existing_record()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            break
        else:
            print("Not a valid selection, please try again")


def display_all_records():
    print("todo display all records")
    records = Records.display_all_Records()
    for record in records:
        print(record)


def search_by_name():
    name = input("Enter name: ")
    records = Records.search_by_name(name)
    if records:
        for record in records:
            print(record)
    else:
        print("No records found for that name.")


def add_new_record():
    name = input("Enter name: ")
    existing_records = Records.search_by_name(name)

    if existing_records:
        print("A record with that name already exists!")
        return

    country = input("Enter country: ")
    catches = input("Enter catches: ")

    Records.add_record(name, country, catches)
    print("Record added!")


def edit_existing_record():
    name = input("Enter name of the record to edit: ")
    existing_record = Records.search_by_name(name)

    if not existing_record:
        print("No record found with that name.")
        return

    country = input("Enter new country: ")
    catches = input("Enter new catches: ")

    Records.edit_existing_record(name, country, catches)
    print("Record updated!")


def delete_record():
    name = input("Enter name of the record to delete: ")
    existing_record = Records.search_by_name(name)

    if not existing_record:
        print("No record found with that name.")
        return
    Records.delete_record(name)
    print("Record deleted!")


if __name__ == "__main__":
    main()