#Task 1: Create a class Book with attributes title and author.
#Then create two different objects from this class and print their details.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)

book1 = Book("1984", "George Orwell")
book2 = Book("The Alchemist", "Paulo Coelho")


# print(book1.title)
# print(book1.author)
# print()
# print(book2.title)
# print(book2.author)

book1.display_details()
print()
book2.display_details()







