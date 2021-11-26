Library_Book_List=["One day morning", "A life of a girl", "A poor farmer"]

class library:
    def display_book(self):
        print(Library_Book_List)
    def lend_book(self):
        inp=input("Pls input your book name: ")
        if inp=="One day morning":
            print(Library_Book_List[0])
        elif inp=="A life of a girl":
            print(Library_Book_List[1])
        else:
            print(Library_Book_List[2])
        print("Thanks a lot for lending book from us!\npls return it on time")
    def add_book(self):
        inp1=input("Pls keep here: ")
        Library_Book_List.append(inp1)
        print("You successfully added a book!!!\nThank you for donet us a book! It will help other to get free book for devolop there knowledge.")
    def return_book(self):
        inp2=input("pls input your book that you want to return: ")
        import datetime
        def gettime():
            return datetime.datetime.now()
        f=open("returned book.txt", "a")
        f.write(inp2 + (str([gettime()])))
        f.close()
        print("Thank you for returning your book.")


Library=library()
print("Wellcome to our library!")
print("What you want? Display Book, Lend Book, Add Book Or return Book.")
library_input=int(input("pls input a number \n1 for Display Book\n2 for Lend Book\n3 for Add Book\n4 for return Book\nInput: "))

# print(Library.display_book())

if library_input==1:
    Library.display_book()
elif library_input==2:
    Library.lend_book()
elif library_input==3:
    Library.add_book()
elif library_input==4:
    Library.return_book()