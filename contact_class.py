class contactClass:

    # show message
    def showMsg(self, message):
        print(' ')
        print('-------------------------------------')

        print(message)

        print('-------------------------------------')

    # intro screen
    def firstScreen(self):
        # welcome msg and input
        userInput = int(input("""
        1) Add contact
        2) List contacts(display all items)
        3) Remove contact(delete by phone no)
        4) Quit
        Input: """))

        return userInput

    # show contact list

    def showContact(self, contactList):
        if len(contactList) == 0:
            self.showMsg('###### Contact list empty ######')

        else:
            self.showMsg('My contact list')
            for contact in contactList:
                print(contact[0], "||", contact[1], '||', contact[2])
                print('------------------------------------------------')

    # Add new contact

    def addContact(self, contactList, name, phone_number, email):
        contactList.append([name, phone_number, email])

    # search in contact list

    def searchPhone(self, contactList, phone_number):

        for x in contactList:
            if len(phone_number) != '':
                if x[1] == phone_number:
                    return [True, contactList.index(x)]
                    break

        return [False]

    def searchEmail(self, contactList, email):
        for x in contactList:
            if len(email) != 0:
                if x[2] == email:
                    return [True, contactList.index(x)]
                break
        return [False]

    # delete contact

    def deleteContact(self, contactList, phone_number):
        checkContact = self.searchPhone(contactList, phone_number)
        if checkContact[0]:
            confirm = input(""" 
                Are you sure want to delete this contact ?
                
                    1 ==> Yes
                    2 ==> No
                    Input: """)

            if confirm == '1':
                del contactList[checkContact[1]]
                self.showMsg('Contact deleted sucessfully')
            else:
                self.showMsg('Your request cancelled !')

        else:
            self.showMsg('contact not found ==> '+phone_number)

    # validate
    def validateInput(self, contactList, input, value):
        if len(value) == 0:
            self.showMsg(input + ' requied')
            if(input == 'Name'):
                self.askName()
            elif(input == 'Phone'):
                self.askPhone()
            elif(input == 'Email'):
                self.askEmail()

    # ask name

    def askName(self):
        return input('Enter name: ')

    # ask Phone
    def askPhone(self):
        return input('Enter phone: ')

    # ask Email
    def askEmail(self):
        return input('Enter email id: ')
