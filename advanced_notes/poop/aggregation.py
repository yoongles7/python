# Aggregation = represents a relationship where one object (the whole) 
#               contains refrences to one or more INDEPENDENT objects (the parts)
#               the objects can exist independently
#               "has-a" relationship

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []         # library containing book objects
        
    def add_books(self, book):
        self.books.append(book)
        
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]    

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("New York Public Library")

book1 = Book("Pride and Prejudice", "Jane Austen")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez")

print(library.name)

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

for book in library.list_books():
    print(book)