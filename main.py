import os
import subprocess as sp

print("\t\t\t\t!! Welcome !!\n\n")

toContinue = True

while toContinue:
    print("""\t\t! Choose any number you want to do from the menu !

    1. Run a Command.

    """)

    menuSelected = int(input("Enter Your Choice: "))
    remoteIP = str

    if menuSelected == 1:
        print('''\nWhere do you want to run your Command?
        
        1. Remote System
        2. Local System
        ''')
        menuSelected = int(input("Enter Your Choice: "))

        if menuSelected == 1:
            userName = input("\nEnter User Name of Remote System: ")
            remoteIP = input("Enter Remote System IP Address: ")
            command = input("\nEnter Your Command: ")
            output = sp.getstatusoutput("ssh {}@{} {}".format(userName, remoteIP, command))
            print(output)
        
        elif menuSelected == 2:
            command = input("\nEnter Your Command: ")
            os.system(command)

    
    toContinue = input("...to continue press ENTER or type 'exit' to QUIT: ")
    if toContinue == 'exit':
        print("\n! Bye !")
        os._exit(0)
    else:
        toContinue = True