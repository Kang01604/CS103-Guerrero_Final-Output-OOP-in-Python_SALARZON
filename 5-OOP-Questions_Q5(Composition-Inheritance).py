##############################################
# Q5: Composition Over Inheritance - Create a Book class with an Author class included within it.
##############################################
# This block illustrates composition and aggregation:
#   - Composition: A Book is composed of an Author (the Book "has an" Author).
#   - Aggregation: A Book aggregates Chapters (kept as a list).
#   - Nested Class: Chapter is defined within the Book class to logically group it.
#   - Encapsulation: Each class has clearly defined responsibilities and data members.
#
# This design shows how to build complex objects by composing simpler ones,
# thereby favoring flexible design over deep inheritance hierarchies.

class Author:
    def __init__(self, name):
        # The Author’s name is stored as a public attribute.
        self.name = name  

    def __str__(self):
        # Returns a string representation for the author.
        return f"Author: {self.name}"


class Book:
    # Nested Chapter class to represent individual chapters.
    class Chapter:
        def __init__(self, title, num_pages):
            self.title = title          # The chapter’s title.
            self.num_pages = num_pages  # The number of pages in the chapter.

        def __str__(self):
            # Returns a string showing the chapter title and its page count.
            return f"{self.title} ({self.num_pages} pages)"

    def __init__(self, title, author: Author, chapters=None):
        # Initialize the Book with a title and an Author object.
        self.title = title      
        self.author = author    # Composition: the Book directly includes an Author instance.
        # Aggregation: the Book holds a list of chapters.
        self.chapters = chapters if chapters is not None else []

    def add_chapter(self, chapter: 'Book.Chapter'):
        # Adds a chapter to the book’s chapter list.
        self.chapters.append(chapter)

    def __str__(self):
        # Provides a full description of the book including a numbered listing of chapters.
        chapter_details = "\n  ".join(
            f"Chapter {i + 1}: {chapter}" for i, chapter in enumerate(self.chapters)
        )
        return f"Book: {self.title}\n{self.author}\nChapters:\n  {chapter_details}"

# --- Q5 OUTPUT ---
print("Q5: Composition Over Inheritance: Create a Book class with a Author class")
print("    included within it, demonstrating composition over inheritance.")
print("___________________________________________________________________")
# Create an Author instance.
author = Author("Koyoharu Gotouge")
# Create a Book instance, here representing Volume 1 of a manga.
book = Book("Kimetsu no Yaiba: Volume 1", author)

# Add chapters to the book along with their page counts.
book.add_chapter(Book.Chapter("Cruelty", 55))
book.add_chapter(Book.Chapter("The Stranger", 25))
book.add_chapter(Book.Chapter("Return by Dawn", 23))
book.add_chapter(Book.Chapter("Tanjiro's Journal, Part One", 19))
book.add_chapter(Book.Chapter("Tanjiro's Journal, Part Two", 19))
book.add_chapter(Book.Chapter("A Mountain of Hands", 19))
book.add_chapter(Book.Chapter("Spirits of the Deceased", 21))

print(book)