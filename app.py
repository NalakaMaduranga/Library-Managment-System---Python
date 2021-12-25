import my_functions  #import module that created
import os
my_functions.print_options()
option = input()
books=[]
while option != 'X' and option !="x":
    #do stuff here
    if option == '1':
        books.append(my_functions.create_book()) 
      
    elif option == '2':
        my_functions.save_book(books)
    elif option =='3':
        books=my_functions.load_books()
    else:
        print("The given command not exists")
    input("press enter to continue")
    #asking for input again
    os.system("cls")
    my_functions.print_options()
    option = input()
        
