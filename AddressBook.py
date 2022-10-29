# process of taking input, file or memory stream into an object: deserialization into person object to later serialize data into a file if need to persist it


import os


class Person:
    def __init__(self, first, last, age, phone_number, email):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number
        self.email = email

    def full_name(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        return f"{self.first} {self.last} | {self.age} | {self.phone_number} | {self.email}"


contacts = list()

if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:
        csv_list = f.readlines()
        for contact_line in csv_list:
            contact_data = contact_line.rstrip().split(",")
            contact = Person(contact_data[0],
                             contact_data[1],
                             contact_data[2],
                             contact_data[3],
                             contact_data[4])
            contacts.append(contact)

users_input = ""


print("Welcome to the address book program")

while users_input != "q":
    print("Available options")
    print("1 - Enter a contact")
    print("2 - Display contacts")
    print("3 - Find contact")
    print("q - quit program")
    users_input = input("Select option: ")

    if users_input == "1":
        print("Enter your contact's information")

        first_name = input("First name: ")
        last_name = input("Last name: ")
        age = input("Age: ")
        phone_number = input("Phone number: ")
        email = input("Email: ")

        our_contact = Person(first_name, last_name, age, phone_number, email)
        contacts.append(our_contact)
        print("Thank you we have received your contacts information")
    elif users_input == "2":
        for contact in contacts:
            print(contact)
        input("Contacts displayed. Hit enter to continue.")
    elif users_input == "3":
        to_lookup = input("Enter contact's name to lookup\n")
        for contact in contacts:
            if to_lookup in contact.full_name():
                print(contact)
    elif users_input.lower() == "q":
        break

with open("contacts.csv", "w") as f:
    for contact in contacts:
        f.write(
            f"{contact.first},{contact.last},{contact.age},{contact.phone_number},{contact.email}\n")

print("Thank you for using the address book")
