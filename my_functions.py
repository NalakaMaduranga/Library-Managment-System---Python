from book import Book
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
    issued = input("Issued: y/Y")
    issued = (issued =="y" or issued == "Y")
    author = input("Author Name")
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

