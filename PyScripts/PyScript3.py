'''
PyScript 3 - 'Python ContactKeeper'
Author: Jay Bhatt

Desc: In this PyScript i'm using the dictionary for the store user contacts.
'''

from collections import OrderedDict

user = dict()

def storeContact() :
    status = input("Want to store new user contact press 'y', for existing user press 'n' :")
    name = input("Enter the name of user :")
    contact = input("Enter the contact number of user :")
    if(status=='y') :
        user[name] = [contact]
    elif(status=='n') :
        try :
            user[name].append(contact)
        except Exception as e:
            print('This user is not available in our record!!')

def retrieveContact() :
    status = input("Retrieve particular user contact number(s) press 'y', if you want to view all user contacts press 'n' :")
    if(status=='y') :
        name = input("Enter the name of user :")
        try :
            print(user[name])
        except Exception as e:
            print('This user is not available in our record!!')
        
    elif(status=='n') :
        print(user)

def manageContact() :  
    global user    
    user = dict(OrderedDict(sorted(user.items())))
    print("The contacts are arranged by sorting the dictionary !!")

while(1) :

    print("=======================================")
    print("Enter 1 to store contact number")
    print("Enter 2 to retrieve contact number")
    print("Enter 3 to manage contact number")
    print("Enter 0 to exit")
    print("=======================================")
    ch = int(input("Give your choice: "))

    if(ch==1) :
        storeContact()
    elif(ch==2) :
        retrieveContact()
    elif(ch==3) :
        manageContact()
        print(user)
    elif(ch==0) :
        exit()
    else :
        pass