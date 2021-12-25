import my_functions  #import module that created
import os
my_functions.print_options()
option = input()
books=[]
while option != 'X' and option !="x":
    #do stuff here
    if option == '1':
        books.append(my_functions.create_book()) 
        input("COMMAND EXECUTED..PRES ANY BUTTON TO CONTINUE")
    elif option == '2':
        my_functions.save_book(books)
    #asking for input again
    os.system("cls")
    my_functions.print_options()
    option = input()
        
