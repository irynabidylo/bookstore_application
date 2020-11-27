Project: Creating a Bookstore Application that allows a user to: 
• Add a new book 
• Delete an existing book 
• View a listing of all books 
• Search a book by author, title or description

File "bookstore.py" – Main script for the bookstore. 
It takes one command line argument containing the filepath of the json file that stores the inventory of books. 

File "file_io" has following functions:
- read_books(book_filename), that takes in the filename, reads the books from the file and returns the list of books.
- write_books(book_list, book_filename), that takes in the list of books and writes them to file in json format.
- get_book_info(), that gets book info from the user and validates it.
- does_isbn_exist(isbn, book_list), that returns True is a book with the same ISBN already exists.
- delete_book_by_isbn(isbn, book_list), that deletes a book with the given ISBN, if it exists.

The inventory of books in the book store is stored in a .json file so the inventory of books is maintained even when the application is not running.

• The filepath is passed into the bookstore.py script on the command line. Command line arguments are validated.
• If the filepath does not exist, the script is still run but will display a warning message: “The bookstore database does not exist”.
• The .json file is read when the bookstore.py script is run. If the file exists, this populates the inventory of books in the script.
• The .json file is written with the latest book inventory whenever a book is added or deleted. If the file does not exist when a book is added, the file will be created.
• The .json file contains a list of dictionaries where each dictionary represents the book and has the following key/value pairs:
  - title
  - author
  - year
  - isbn
  - description
  
