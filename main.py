# import contact class
from contact_class import *

contact = contactClass()


def contactBook():
    # An empty contactList to store contact
    contactList = []

    while True:

        userInput = contact.firstScreen()

        if userInput == 1:
            while True:
                name = input('Enter name: ')
                # check for name not empty
                if len(name) != 0:
                    break
                else:
                    contact.showMsg('Name required')
            while True:
                phone_number = input('Enter phone: ')
                phoneCount = len(phone_number)

                # check for phone not empty
                if phoneCount == 0:
                    contact.showMsg('Phone required')
                else:
                    checkPhone = contact.searchPhone(contactList, phone_number)
                    # check for phone number already exist / not
                    if checkPhone[0]:
                        contact.showMsg('This phone number already exist')
                    if checkPhone[0] == False:
                        break

            while True:
                email = input('Enter email: ')
                emailCount = len(email)
                # check for email not empty
                if emailCount == 0:
                    contact.showMsg('Email required')
                else:
                    checkEmail = contact.searchEmail(contactList, email)
                    # check for email already exist / not
                    if checkEmail[0] == False:
                        break
            # add entries to contact array
            contact.addContact(contactList, name, phone_number, email)

        elif userInput == 2:
            contact.showContact(contactList)
        elif userInput == 3:
            phone_number = input('Enter the phone number you wish to delete: ')
            # delete selected contact form array
            contact.deleteContact(contactList, phone_number)

        elif userInput == 4:
            contact.showMsg('Thanks for using contact book!')

            break
        else:
            contact.showMsg('Invalid entry, Please try agin')


contactBook()
