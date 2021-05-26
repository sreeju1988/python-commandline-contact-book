from contact_class import *
# Define a function to welcome the user and provide options on how the phonebook works


def firstScreen():
    # Create an entry variable using the input function and multiple line strings format
    userInput = int(input("""
    1) Add contact
    2) List contacts(display all items)
    3) Remove contact(delete by phone no)
    4) Quit
    Input: """))

# Close the function
    return userInput

# Define a function Phonebook


def contactBook():
    # initiate an empty contact dictionary to store values
    contactList = []
    contactList.append(['s', '9', '9'])
  # initiate a while loop to continuously run the phonebook program
    while True:
        # call welcome function.
        # Set entry variable to welcome function
        userInput = firstScreen()

        # Create conditions for  decision making for any option entered by the user
        if userInput == 1:

            name = input('Enter name: ')
            phone_number = input('Enter phone: ')
            email = input('Enter email id: ')
            addContact(contactList, name, phone_number, email)

        elif userInput == 2:
            showContact(contactList)
        elif userInput == 3:
            phone_number = input('Enter the phone number you wish to delete: ')
            deleteContact(contactList, phone_number)
            # for x in contactList:
            #     if x[1] == phone_nuber:
            #         position = contactList.index(x)
            #         del contactList[position]
            #         print("contact deleted successfully")
            #     else:
            #         print('contact not found ==>', phone_nuber)
        elif userInput == 4:
            showMsg('Thanks for using contact book!')
            break


contactBook()
