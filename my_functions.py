from book import Book
import json


#print options
def print_options():
    print("Press the specific Button")
    print("1- Create a new book")
    print("2-Save book locally")
    print("3-load book from disk")
    print("4-issue book")
    print("5-return a book")
    print("6-update a book")
    print("7-show all book")
    print("8-Find book by id")

def input_book_info():
    id=input("ID: ")
    name=input("Name: ")
    descdription =input("Description: ")
    isbn = input("ISBN: ")
    page_count = int(input("Page count: "))
    issued = input("Issued: y/Y: ")
    issued = (issued =="y" or issued == "Y")
    author = input("Author Name: ")
    year = int(input("Year: "))
    return{
        'id': id,
        'name':name,
        'description':descdription,
        'isbn':isbn,
        'page_count':page_count,
        'issued':issued,
        'author':author,
        'year':year
    }

    

#create book function
def create_book():
    print("Please ENter your information")
    book_input = input_book_info()
    book = Book(book_input['id'],book_input['name'],book_input['description'],book_input['isbn'],book_input['page_count'],
    book_input['issued'],book_input['author'],book_input['year'])
    print(book.to_dict())
    return book 

#defining save book
def save_book(books):
    json_books=[]
    for books in books:
        json_books.append(books.to_dict())
    try:
        file=open("books.dat","w")
        file.write(json.dumps(json_books,indent=4))
    except:
        print("Error in saving books")

#defining function to load books
def load_books():
    try:
        file=open("books.dat","r")
        loaded_books=json.loads(file.read())
        books=[]
        for book in loaded_books:
            new_obj=Book(book['id'],book['name'],book['description'],book['isbn'],book['page_count'],
    book['issued'],book['author'],book['year'])
            books.append(new_obj)
        print("Successfully loaded books")
        return books
    except:
        print("The file dosent exists or error occur during loading")

#defining function to find book
def find_book(books,id):
    for index,book in enumerate(books):
        if book.id==id:
            return index
        return None

 #issue book
def issue_book(books):
    id = input("Enter the id of the book")
    index=find_book(books,id)
    if index != None:
        books[index].issued = True
        print("book updated")
    else:
        print("Could not find the book")

#return book
def return_book(books):
    id = input("Enter the id of the book want to return")
    index=find_book(books,id)
    if index != None:
        books[index].issued = True
        print("book returned")
    else:
        print("Could not find the book")