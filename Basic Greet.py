#Project Title
    print("\nProject Title: Basic Greet")
    
    # Functions for the Project
    def greet(usrName, birthDate):
        return print("\nYour name is " + usrName + ' and you were born on ' + birthDate + '. ' + 'Nice to meet you!\n')

    #User-Program Interaction
    userName = str()
    userBday = str()

    userName = input('\nWhat is your name?\n')
    userBday = input('\nWhen were you born?\n')
    
    greet(userName, userBday)