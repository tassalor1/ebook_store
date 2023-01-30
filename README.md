# ebook_store

E-Bookstore

This code is a simple e-bookstore program written in Python using SQLite.



Features

Creates a SQLite database ebookstore and table books if not exists
Inserts some books into the books table
Add a new book to the books table
Update a book in the books table
Delete a book in the books table
Search for a book in the books table



Usage

Connect to SQLite database ebookstore
Create the table books with the following columns: id (INTEGER PRIMARY KEY), title (TEXT), author (TEXT), category (Text), and qty (INTEGER)
Insert the books into the books table using the executemany method
Add a new book to the books table using the add_book function. It takes the user's input for the book id, title, author, category, and qty and inserts it into the books table. The user also has an option to view the newly added book
Update a book in the books table using the update_book function. It prompts the user to enter a book id and updates the book with the given id.



Requirements

Python 3.x
sqlite3 library installed
