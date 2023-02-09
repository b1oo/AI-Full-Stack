""" Here is an example of how to implement a program to manage a list of contacts stored in a CSV file using Python """

import csv

def read_contacts_from_file(file_path):
    contacts = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def write_contacts_to_file(file_path, contacts):
    with open(file_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'favorite fruit', 'favorite color'])
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

def main():
    file_path = 'contacts.csv'
    contacts = read_contacts_from_file(file_path)
    print('Contacts:')
    for contact in contacts:
        print(contact)

    new_contact = {
        'name': 'John Doe',
        'favorite fruit': 'apple',
        'favorite color': 'green'
    }
    contacts.append(new_contact)
    write_contacts_to_file(file_path, contacts)

    contacts = read_contacts_from_file(file_path)
    print('\nContacts after adding a new one:')
    for contact in contacts:
        print(contact)

if __name__ == '__main__':
    main()