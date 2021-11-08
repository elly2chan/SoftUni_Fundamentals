phonebook = {}

while True:
    new_contact = input()

    if new_contact.isnumeric():
        break

    contact = new_contact.split('-')
    contact_name = contact[0]
    contact_number = contact[1]
    phonebook[contact_name] = contact_number

number_of_searched_contacts = int(new_contact)
for name in range(number_of_searched_contacts):
    searched_contact = input()
    if searched_contact in phonebook:
        print(f'{searched_contact} -> {phonebook[searched_contact]}')
    else:
        print(f'Contact {searched_contact} does not exist.')