# Creating log file to store every messages
import  logging as lg
lg.basicConfig(filename="Python_mini_project.log", level=lg.INFO, format="%(asctime)s $(name)s $(levelname)s %(message)s")

# Creating a class library
class Library:
    '''
    Docstring: This is a library class
    '''
    lg.info("We are inside the library class")
    def __init__(self, listOfBooks, libraryName):
        '''
        Init Docstring:
        It takes two arguments listOfBooks and libraryName
        '''
        lg.info("We are inside the init class ")
        self.listOfBooks = listOfBooks
        self.libraryName = libraryName
        self.lendDict = {}  # It is an empty dictinary.
        lg.info("The data entered by user is {},{} ".format(self.listOfBooks,self.libraryName))

    def displayBooks(self):
        '''
        Docstring:
        This function will return names of library
        '''
        try:
            print("We have following books in our library {}".format(self.libraryName))
            for book in self.listOfBooks:
                print(book)
        except Exception as e:
            print(e)

    def lendBook(self, user, book):
        '''
            Docstring:
            It takes two arguments user (name of user), book (name of book)
            This function will lend the book of library
        '''
        try:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print("Lender-Book database has been updated. You can take th book now")
            else:
                print("Book has been taken by {}".format(self.lendDict[book]))
            lg.info(f"The user has lend the book details are {self.lendDict.items()}")
        except Exception as e:
            print(e)

    def addBook(self, book):
        '''
            Docstring:
            It takes one arguments , book (name of book)
            This function will add the book of library
        '''
        try:
            self.listOfBooks.append(book)
            print("Book has been added to the book list")
            lg.info(f"The user has added a book {self.book}")
        except Exception as e:
            print(e)

    def returnBook(self, book):
        '''
            Docstring:
            It takes one arguments , book (name of book)
            This function will return the book in library
        '''
        try:
            self.lendDict.pop(book)
            lg.info(f"The user has returned the books {self.book}")
        except Exception as e:
            print(e)

    def __str__(self):
        return "This is a Library class"

def main():
    aman = Library(['Python', 'Rich Dad Poor Dad', 'data Structures and Algorithm', 'C++ Basics',
                    'Who moved my cheese'], "Aman Gupta")

    while True:
        try:
            print(f"Welcome to the {aman.libraryName} library.")
            print("1. Display Books")
            print("2. Lend a Book")
            print("3. Add a Book")
            print("4. Return a Book")
            choise = int(input("Enter your choises to continue :"))

            if choise == 1:
                aman.displayBooks()
            elif choise == 2:
                book = input("Enter the name of the book you want to lend :")
                user = input("Enter your name :")
                aman.lendBook(user, book)
            elif choise == 3:
                book = input("Enter the name of the book you want to add :")
                aman.addBook(book)
            elif choise == 4:
                book = input("Enter the name of the book you want to return :")
                aman.returnBook(book)
            else:
                print("Not a valid option")


            user_choise = ""
            while user_choise != 'q' and user_choise != 'c':
                user_choise = input("Press q to quit and c continue :")
                if user_choise == 'q':
                    exit()
                elif user_choise == 'c':
                    continue

        except Exception as e:
            print("You have enter invalid option error is",e)


if __name__ == '__main__':
    main()