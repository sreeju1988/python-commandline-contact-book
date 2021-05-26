# show contact list

def showContact(contactList):

    if len(contactList) == 0:
        showMsg('###### Contact list empty ######')

    else:
        showMsg('My contact list')
        for contact in contactList:
            print(contact[0], "||", contact[1], '||', contact[2])
            print('------------------------------------------------')


# Add new contact


def addContact(contactList, name, phone_number, email):
    checkContact = searchContact(contactList, phone_number, email)
    if(checkContact[0]):
        showMsg('This phone number / email address already exist in our contact')
    else:
        contactList.append([name, phone_number, email])


# search in contact list


def searchContact(contactList, phone_number, email=''):

    for x in contactList:
        if len(phone_number) != '':
            if x[1] == phone_number:
                return [True, contactList.index(x)]
                break
        if len(email) != 0:
            if x[2] == email:
                return [True, contactList.index(x)]
                break
    return [False]

# delete contact


def deleteContact(contactList, phone_number):
    checkContact = searchContact(contactList, phone_number)
    if checkContact[0]:
        showMsg('Contact not found')
    else:
        showMsg('contact not found ==> '+phone_number)


# show message

def showMsg(message):
    print('-------------------------------------')

    print(message)

    print('-------------------------------------')
