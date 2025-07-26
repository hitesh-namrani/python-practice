contacts=dict()
def addcontact():
    name=input("Give name : ")
    phone_number=input("Give phone number : ")
    contacts[name]=phone_number
    print(f"Contact {name} added sucessfully")
def viewcontacts():
    for name,phone_number in contacts.items():
        print(name+":"+phone_number)
def searchcontact():
    name=input("Give name of contact to be found : ")
    if name in contacts:
        print (name+":"+contacts[name])
    else:
        print("contact not found")
def deletecontact():
    name=input("Give name of contact to be deleted : ")
    if name in contacts:
        del contacts[name]
        print(f"contact of {name} deleted successfully")
    else:
        print("contact not found")
while True:
    operator=int(input("enter\n1: to add a contact\n2: to view all contacts\n3: to search for a contact\n4: to delete a contact\n5: to terminate the program (all data will be erased)\nenter here : "))
    if operator==1:
        addcontact()
    elif operator==2:
        viewcontacts()
    elif operator==3:
        searchcontact()
    elif operator==4:
        deletecontact()
    elif operator==5:
        break
    else:
        print("Give valid input")