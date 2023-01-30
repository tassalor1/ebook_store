# Imports sqlite
import sqlite3

# Creates file
db = sqlite3.connect('ebookstore')

# Gets cursor object
cursor = db.cursor()

# Will insert titles
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, 
    author TEXT, category Text, qty INTEGER)
''')
print("Table Created!")
# Save changes
db.commit()

# List of books
book = [(3001, "A Tale of Two Cities", "Charles Dickens", "Fiction", 30),
        (3002,"Harry Potter and the Philosphers Stone", "J.K. Rowling", "Fiction", 40),
        (3003, "The Lion, the Witch and the Wardrobe", "C.S.Lewis", "Fiction", 25),
        (3004, "The Lord of the Rings", "J.R.R Tolkien", "Fiction", 37),
        (3005, "Alice in the Wonderland", "Lewis Carroll", "Fiction", 12),
        (3006, "Start with Why", "Simon Sinek", "Nonfiction", 43),
        (3007, "Atomic Habits", "James Clear", "Nonfiction", 28),
        (3008, "Meditations", "Marcus Aurelius", "Nonfiction", 67)]

# Inserts all values into rows
cursor.executemany('''INSERT INTO books(id, title, author, category, qty) 
VALUES(?,?,?,?,?)''', book)
print('All books added')
db.commit()


# Function to add book
def add_book():

    # Add book id
    while True:
        try:
            print("Input book details below")
            # Ask user to input book details
            user_add_id = int(input('''id of book:'''))
            break
        except ValueError:
            print("Please enter a vaild book id")

    # Add book title
    user_add_title = input("Title of book: ")

    # Add book author
    user_add_author = input("Author of book: ")

    # Add book category
    while True:
        try:
            user_add_category = input("Category of book (Fiction / NonFiction: ")
            # Checks to see if user entered desired input
            if user_add_category.lower() not in ('fiction', 'nonfiction'):
                raise ValueError
            break
        except ValueError:
            print("Please enter a vaild category")

    # Add book qty
    while True:
        try:
            # Asks for qty
            user_add_qty = int(input("qty of book: "))
            # Checks to see if book is below 0
            if user_add_qty <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a vaild qty")

    # Insert user inputs choice of book into books table
    cursor.execute('''
    INSERT INTO books VALUES(?,?,?,?,?)
    ''',(user_add_id, user_add_title, user_add_author, user_add_category, user_add_qty))

    # Error handling
    while True:
        try:
            # Ask user if they want to see recently added book
            user_view = input("Show recently added book? (y/n): ")

            # If users enters anything other than y / n raise error
            if user_view.lower() not in ('y', 'n'):
                    raise ValueError
            break
        except ValueError:
                print("Please enter y/n")

    while True:
            # If user enters y
            if user_view == 'y':
                    # Select recently added book by id from user input
                    cursor.execute('''
                    SELECT id, title, author, category, qty FROM books WHERE id=?
                    ''', (user_add_id,))
                    # Fetches the id
                    book = cursor.fetchone()
                    print(book)
                    break
            # If user enter n
            else:
                    print("Book Added!")
                    break
            db.commit()



# Function to update book
def update_book():

    # Select all ids
    cursor.execute("SELECT id FROM books")

    # Stores all ids in list and then for loops list
    # This is so we can check users input is in the book db
    all_ids = [i[0] for i in cursor.fetchall()]

    # Select all books
    cursor.execute('''SELECT * FROM books''')
    # Print to show user
    all_books = cursor.fetchall()
    for i in all_books:
        print("List of all current books in database")
        print(i)

    while True:
        # Ask user which book they would like to update
        user_update = input('''
id of book you would like to update?
or enter b to go back: ''')

        # If user want to go back to options menu
        if user_update == 'b':
            return
        try:
            # Convert to int for id number
            user_update = int(user_update)
            if user_update not in all_ids:
                raise ValueError
            break
        except ValueError:
            print("Please enter a vaild book id")

    # Select book from user input of which id they would like
    cursor.execute('''
    SELECT * FROM books WHERE id=?
    ''', (user_update,))
    # Fetches the id
    book = cursor.fetchone()
    print(book)

    # Will now ask user which section they would like to update
    while True:
        try:
            user_section = input('''
Which section of the book record would you like to update? (title, author, category, qty) : ''')
            # If users enters anything other than specified sections raise error
            if user_section not in ('title', 'author', 'category', 'qty'):
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid section")

    while True:
        # User wants to update title
        if user_section == 'title':

            new_title = input("Enter new title: ")

            cursor.execute('''
            UPDATE books SET title=? WHERE id=?
            ''', (new_title, user_update,))

        # User wants to update author
        elif user_section == 'author':

            new_author = input("Enter new author: ")

            cursor.execute('''
            UPDATE books SET author=? WHERE id=?
            ''', (new_author, user_update,))

        # User wants to update category
        elif user_section == 'category':

            new_category = input("Enter new category: ")

            cursor.execute('''
            UPDATE books SET category=? WHERE id=?
            ''', (new_category, user_update,))

        # User wants to update category
        elif user_section == 'qty':

            new_qty = input("Enter new category: ")

            # Updates qty for chosen book
            cursor.execute('''
                        UPDATE books SET qty=? WHERE id=?
                        ''', (new_qty, user_update,))

        # Selects book they have chosen to update to print info
        cursor.execute('''
        SELECT * FROM books WHERE id=?
        ''', (user_update,))
        # Fetches the id
        updated_book = cursor.fetchone()
        print(f"Updated book {updated_book}")
        break


# Function to delete book
def delete_book():

    # Select all ids
    cursor.execute("SELECT id FROM books")

    # Stores all ids in list and then for loops list
    # This is so we can check users input is in the book db
    all_ids = [i[0] for i in cursor.fetchall()]

    # Select all books
    cursor.execute('''SELECT * FROM books''')
    # Print to show user
    all_books = cursor.fetchall()
    for i in all_books:
        print("List of all current books in database")
        print(i)

    while True:
        # Ask user which book they would like to delete
        user_delete = input('''
id of the book would you like to delete
or enter b to go back: ''')
        # If user wants to go back to options menu
        if user_delete == 'b':
            return
        try:
            # Convert to int for id
            user_delete = int(user_delete)
            # Checks if the id they entered is in the list of ids
            if user_delete not in all_ids:
                raise ValueError
            break
        except ValueError:
            print("Please enter a vaild book id")


    # Select book from user input of which id they would like
    cursor.execute('''
        SELECT * FROM books WHERE id=?
        ''', (user_delete,))
    # Fetches the id
    book = cursor.fetchone()

    # Delete chosen book
    cursor.execute('''
    DELETE FROM books
    WHERE id=?
    ''', (user_delete,))
    print(f"{book} has been deleted")
    db.commit()



# Function for searching books
def search_books():

    # Select all ids
    cursor.execute("SELECT id FROM books")

    # Stores all ids in list and then for loops list
    # This is so we can check users input is in the book db
    all_ids = [i[0] for i in cursor.fetchall()]

    # Select all books
    cursor.execute('''SELECT * FROM books''')
    # Print to show user
    all_books = cursor.fetchall()
    for i in all_books:
        print("List of all current books in database")
        print(i)

    while True:
        # Asks user which book they want to search for
        user_search = input('''
Enter the id of the book
or enter b to go back: ''')

        # User enters b send to options menu
        if user_search == 'b':
            return
        try:
            # Convert user search to int if not b
            user_search = int(user_search)
            # Checks if id user entered is in id list
            if user_search not in (all_ids):
                raise ValueError
            break
        except ValueError:
            print("Please enter a vaild book id")

    # Select book from user input of which id they would like
    cursor.execute('''
        SELECT * FROM books WHERE id=?
        ''', (user_search,))

    # Fetches the id
    book = cursor.fetchone()
    print(f"{book} has been selected")
    db.commit()


# Function for exit
def exit():
    if menu == '0':
        print('Goodbye!!!')
    quit()


while True:
    try:
        # Options menu
        menu = str(input('''
-------------------------------------
 Enter the number you would like:
 1. Add new book
 2. Update a books information
 3. Delete a book
 4. Search for a book
 0. Exit
 Enter number here: '''))
        # Checks that user input is correct
        if menu not in ('1', '2', '3', '4', '0'):
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    # If statement for menu options
    if int(menu) == 1:
        add_book()
    elif int(menu) == 2:
        update_book()
    elif int(menu) == 3:
        delete_book()
    elif int(menu) == 4:
        search_books()
    else:
        exit()



