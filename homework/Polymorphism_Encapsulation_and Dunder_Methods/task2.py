class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f"Library: <{self.name}, All books: {[b.name for b in self.books]}, All authors: {[a.name for a in self.authors]}>"

    def __str__(self):
        return self.name

    def new_book(self, name, year, author):
        added_book = Book(name, year, author)
        self.books.append(added_book)
        if author not in self.authors:
            self.authors.append(author)
        return added_book

    def group_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def group_by_year(self, year):
        return [b for b in self.books if b.year == year]


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)

    def __repr__(self):
        return f"Book: <{self.name}, {self.year}, {repr(self.author)}>"

    def __str__(self):
        return f"Title: {self.name}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author: <{self.name}, {self.country}, {self.birthday}, all books by this author: {[b.name for b in self.books]}>"

    def __str__(self):
        return f"Name: {self.name}"

"""I want to make an input function but i am uncertain to where they should be so 
it is directly in the code instead"""


bibliotek = Library("bibliotek")
author_ausfelt = Author("Ausfelt", "Sweden", "1986")
new_book = bibliotek.new_book("Spökjägaren", 2007, author_ausfelt)
new_second_book = bibliotek.new_book("Galoppkungen", 2012, author_ausfelt)

for book in bibliotek.group_by_author(author_ausfelt):
    print(book)
