# we will save users name in a list of dectionary
# save current or active users that use ATM no

users = [{"Name" : "Ahmed", "Balance" : 1000, "PinCode" : 1111},
        {"Name" : "Reda", "Balance" : 2000, "PinCode" : 1112},
        {"Name" : "Yara", "Balance" : 3000, "PinCode" : 1113},
        {"Name" : "Yousra", "Balance" : 4000, "PinCode" : 1114},
        {"Name" : "Adham", "Balance" : 5000, "PinCode" : 1115},
        {"Name" : "Eslam", "Balance" : 6000, "PinCode" : 1116},
        {"Name" : "Layla", "Balance" : 7000, "PinCode" : 1117},
        {"Name" : "Sameh", "Balance" : 8000, "PinCode" : 1118},
        {"Name" : "Khaled", "Balance" : 9000, "PinCode" : 1119},
        {"Name" : "Lola", "Balance" : 1010, "PinCode" : 1121}]

#print(users) # to print all users
#print((users)[4]["Name"]) # to print name of the first user

import time  # to be used in load function

currentUser = {}
currentPin = 0

def load(t):
    for i in range(1, t):
        print("\rLoading" + "."*i, end="") #\r mean each time erase the line and print in the same line
        time.sleep(1)                      #*i thismean each time the string will increase by the same value
                                           # time.sleep (1) mean that the computer will wait for one second before go for next step in the loop

def intialScreen():
    load(5)
    global currentPin  # this mean that any value that will added to this variable in this function will be valid forthe whall program and other functions
    global currentUser     
    found = False  # if the user is ther this will be true and will open the next screen, if user is not there it will call Error screen
    print("\r***************************************************************")
    print("*                                                             *")
    print("*                                                             *")
    print("*                                                             *")
    print("*                Welcome to Python ATM                        *")
    print("*                Please enter your PIN                        *")
    currentPin =  int(input("                           ")) # as we defin the pincode as integer
    print("*                                                             *")
    print("*                                                             *")
    print("*                                                             *")
    print("***************************************************************")
    
    for user in users:
        if user["PinCode"] == currentPin:
            currentUser = user
            found = True
            
    if found: # this if shouldbe at the level of the function not the "for" no the above if
        selectScreen()
    else:
        errorScreen()
    
            
def errorScreen():
    load(2)
    print("\r***************************************************************")
    print("*                                                             *")
    print("*                                                             *")
    print("*                                                             *")
    print("*                Welcome to Python ATM                        *")
    print("*                Error: User not found                        *")
    print("*                   Please try again                          *")
    print("*                                                             *")
    print("*                                                             *")
    print("*                                                             *")
    print("***************************************************************")
    intialScreen()
    
def selectScreen():
    load(2)
    print("\r***************************************************************")
    print("*                                                             *")
    print("*                                                             *")
    print("*                Welcome to Python ATM                        *")
    print("*                Helo", currentUser['Name'],"                                *")
    print("*  1- Cash withdrawal                4- Bill Payment          *")
    print("*  2- Balance Inquiry                5- Settings              *")                                           
    print("*  3- Transfere                      6- Donate                *")                                         
    print("*     Please enter the number of required operation           *")
    print("*                                                             *")
    print("***************************************************************")
    op = int(input())
    if op == 1:
        cashWihdraw()
    elif op == 2:
        balaneInquiry()
    elif op == 3:
        transfer()
    elif op == 4:
        billPaymet()
    elif op == 5:
        setting()
    elif op == 6:
        donate()
    else:
        errorScreen()   
     
def cashWihdraw():
     global currentUser
     load(2)
     print("\r***************************************************************")
     print("*                                                             *")
     print("*                                                             *")
     print("*                                                             *")
     print("*                Welcome to Python ATM                        *")
     print("*                Helo", currentUser['Name'],"                                *")
     print("*           Please enter your required amount                 *")
     amount =            int(input("                     ")) 
     print("*                                                             *")
     print("*                                                             *")
     print("***************************************************************")
     if amount <= currentUser["Balance"]:
        currentUser["Balance"] = currentUser["Balance"] - amount
        print(" Please withdraw your cash")
        balaneInquiry()
     else:
        errorScreen()
     load(10)
     

def balaneInquiry():
     load(2)
     print("\r***************************************************************")
     print("*                                                             *")
     print("*                                                             *")
     print("*                                                             *")
     print("*                Welcome to Python ATM                        *")
     print("*                Helo", currentUser['Name'],"                                *")
     print("*           Your Balance is", currentUser['Balance'],"                                *")
     print("*                                                             *")
     print("*                                                             *")
     print("*                                                             *")
     print("***************************************************************")
     load(5)
     selectScreen()

def transfer():
    global currentUser
    load(2)
    print("\r***************************************************************")
    print("*                                                             *")
    print("*                                                             *")
    print("*                Welcome to Python ATM                        *")
    print("*                Helo", currentUser['Name'],"                                *")
    print("*           Please enter your required amount                 *")
    amount =            int(input("                     ")) 
    print("*           Please enter target account Name               *")
    name =                input("                     ")                                             
    print("*                                                             *")
    print("***************************************************************")
             
    if amount <= currentUser["Balance"]:
        for user in users:
            #if name == user["Name"]: # this can be the target account Pincode by using integer input and instedof user["Name"] by user["PinCode"]                user["Balance"] = user["Balance"] + amount
            if (name.lower() == user["Name"].lower()): # can avoid case sensitivety by useing, it is working
                user["Balance"] = user["Balance"] + amount
                currentUser["Balance"] = currentUser["Balance"] - amount
                print(" Transfer done succesfuly ")
        balaneInquiry()
    else:
        errorScreen()
    load(10)

def donate(): # same as transfer butmoney should go to charety 
    return

def setting():
    return

def billPaymet(): # same as transfer butmoney should go to company
    return

intialScreen()
