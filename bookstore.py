import file_io
import re
import sys


def main():
    """ Main Function of the Program """

    if len(sys.argv) != 2:
        print("Invalid number of parameters") #command line parameters validation
        exit(0)

    book_filename = sys.argv[1] #name of the file is a command line parameter

    quit = False
    book_list = file_io.read_books(book_filename)
    while not quit:
        user_action = input("Add book (a), Delete book (d), View Book Summary (s), Search Book by Title (t),\
Search Book by Author (u), Search Book by Keyword (k), Quit (q)")

        try:
            if user_action == "a":  #adding a book to the bookstore
                title, author, isbn, year, description = file_io.get_book_info()
                if not file_io.does_isbn_exist(isbn, book_list):
                    book = {"Title": title, "Author": author, "Year": int(year), "ISBN": isbn, "Desc": description}
                    book_list.append(book)
                    file_io.write_books(book_list, book_filename)
                else:
                    print("Book already exists. Cannot add the book")
            
            elif user_action == "d": #deletes a book from the bookstore
                isbn = input("Enter ISBN:")
                if re.search("^\d{4,20}$", isbn) is None: #validates that ISBN is 4 to 20 digits (inclusive).
                    raise ValueError("Invalid ISBN")
                book_deleted = file_io.delete_book_by_isbn(isbn, book_list)
                if book_deleted:
                    print("Book with ISBN %s successfully deleted" % isbn)
                    file_io.write_books(book_list, book_filename)
                else:
                    print("Could not find book with ISBN %s" % isbn)
            
            elif user_action == "s": #view a book summary
                if len(book_list) > 0:
                    for book in book_list:
                        print("%s %s %d %s %s" % (book["Title"], book["Author"], book["Year"],
                                                  book["ISBN"], book["Desc"][:30])) #Only the first 30 characters of the description are displayed 
                else:
                    print("There are no books yet")
            
            elif user_action == "t": #searches book by title
                title = input("Enter title:")
                if re.search("^[A-Za-z0-9 ]+$", title) is None: #validates that tittle has letters (upper and lower case), digits and spaces. Must have at least one character
                                                                #Is case insensitive and allows partial matches
                    raise ValueError("Invalid Title Search Name")
                match_found = False
                for book in book_list:
                    if title.lower() in book["Title"].lower():
                        print("Match:\n %s\n %s\n %d\n %s\n %s\n" % (book["Title"], book["Author"], book["Year"],
                                                   book["ISBN"], book["Desc"]))

                        match_found = True
                if not match_found:
                    print("No matches found")
            
            elif user_action == "u": #searches book by author. 
                author = input("Enter author:")
                if re.search("^[A-Za-z ]+$", author) is None: #Validates that it has letters (upper and lower) and spaces. Must have at least one character.
                                                              #is case insensitive and allows partial matches
                    raise ValueError("Invalid Author Search Name")
                match_found = False
                for book in book_list:
                    if author.lower() in book["Author"].lower():
                        print("Match:\n %s\n %s\n %d\n %s\n %s\n" % (book["Title"], book["Author"], book["Year"],
                                                   book["ISBN"], book["Desc"]))

                        match_found = True
                if not match_found:
                    print("No matches found")
            
            elif user_action == "k": #searches book by keywords
                keyword = input("Enter keyword:")
                if re.search("^.{1,20}$", keyword) is None: #validates that it has any characters up to 20. Must have at least one character.
                                                            #is case insensitive and should allow partial matches
                    raise ValueError("Invalid Keyword Search Name. Must be between 1 and 20 characters")
                match_found = False
                for book in book_list:
                    if keyword.lower() in book["Title"].lower() or keyword.lower() in book["Desc"].lower():
                        print("Match:\n %s\n %s\n %d\n %s\n %s\n" % (book["Title"], book["Author"], book["Year"],
                                                   book["ISBN"], book["Desc"]))

                        match_found = True
                if not match_found:
                    print("No matches found")
            
            elif user_action == "q": #quits the program
                print("Quitting Program")
                quit = True
            else:
                print("Invalid Selection. Try Again.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
