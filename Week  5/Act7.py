# Base class for library items
class LibraryItem:
    def __init__(self, title, author):
        self.__title = title   # private attribute
        self.__author = author # private attribute

    def display_details(self):
        # Returns basic info about the item
        return f"Title: {self.__title}, Author: {self.__author}"

# Subclass for books
class Book(LibraryItem):
    def display_details(self):
        # Override method to add Book label
        return f"Book {super().display_details()}"

# Subclass for magazines
class Magazine(LibraryItem):
    def __init__(self, title, author, frequency):
        super().__init__(title, author)
        self.__frequency = frequency # private attribute for magazines

    def display_details(self):
        # Override method to include issue frequency
        return f"Magazine {super().display_details()}, Frequency: {self.__frequency}"

# Library class to manage items
class Library:
    def __init__(self):
        self.__items = []  # private list to store items

    def add_item(self, item):
        self.__items.append(item)
        print(f"Added: {item.display_details()}")

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print(f"Removed: {item.display_details()}")
        else:
            print("Item not found.")

    def show_all_items(self):
        print("\nLibrary Items:")
        for item in self.__items:
            print(item.display_details())

# Main function to run the program
def main():
    library = Library()
    # Create some library items
    book = Book("Harry Potter", "J.K. Rowling")
    magazine = Magazine("Sunday Times", "Various", "Weekly")

    # Add items
    library.add_item(book)
    library.add_item(magazine)

    # Show all items
    library.show_all_items()

    # Remove a book
    library.remove_item(book)
    library.show_all_items()

if __name__ == "__main__":
    main()