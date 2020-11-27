import json
import os
import re


def read_books(book_filename):
    """ Takes in the filename, reads the books from the file and returns the list of books """
    book_list = []
    if os.path.isfile(book_filename):
        book_file = open(book_filename)
        book_data = book_file.read()
        book_file.close()
        book_list = json.loads(book_data)
    else:
        print("The %s database does not exist" % book_filename)
    return book_list


def write_books(book_list, book_filename):
    """ Takes in the list of books and writes them to file in json format """
    book_file = open(book_filename, "w")
    bookstore_json = json.dumps(book_list, indent=4)
    book_file.write(bookstore_json)
    book_file.close()


def does_isbn_exist(isbn, book_list):
    """ Returns True is a book with the same ISBN already exists """
    for book in book_list:
        if book["ISBN"] == isbn:
            return True
    return False


def delete_book_by_isbn(isbn, book_list):
    """ Deletes a book with the given ISBN, if it exists """
    book_deleted = False
    for book in book_list:
        if book["ISBN"] == isbn:
            book_list.remove(book)
            book_deleted = True
            break
    return book_deleted


def get_book_info():
    """ Gets book info from the user and validates it """

    title = input("Title:")
    if re.search("^[A-Za-z0-9 ]+$", title) is None:
        raise ValueError("Invalid Title")
    author = input("Author:")
    if re.search("^[A-Za-z ]+$", author) is None:
        raise ValueError("Invalid Author")
    isbn = input("ISBN:")
    if re.search("^\d{4,20}$", isbn) is None:
        raise ValueError("Invalid ISBN. Must be between 4 and 20 digits")
    year = input("Year:")
    if re.search("^\d{4}$", year) is None:
        raise ValueError("Invalid Year. Must be 4 digits only")
    if int(year) < 1900:
        raise ValueError("Year cannot be less than 1900")
    description = input("Description:")
    if re.search("^.{,256}$", description) is None:
        raise ValueError("Description must be up to 256 characters long")
    return title, author, isbn, year, description



