import random
nam=input("pls input Your username: ")
oo=["Talha", "Mahamud", "Rashid", "Rishan", "Kayes", "Zawad", "Khalid" "Anik","Rocky", "Alamin", "Sajol", "Dipto", "Durjoy", "Topu"]
pp=random.choice(list(oo))
Library_Book_List=["One day morning", "A life of a girl", "A poor farmer"]
class library:
    def display_book(self):
        print("We have this book:")
        for i in Library_Book_List:
            print(i)
    def lend_book(self):
        inp=input("Pls input your book name: ")
        if inp in Library_Book_List:
            if inp=="One day morning":
                print(Library_Book_List[0])
            elif inp=="A life of a girl":
                print(Library_Book_List[1])
            else:
                print(Library_Book_List[2])
            print("Thanks a lot for lending book from us!\npls return it on time")
        else:
            print(f"Sorry! this book is alredy lended by {pp}")
    def add_book(self):
        inp1=input("Pls keep here: ")
        Library_Book_List.append(inp1)
        print(Library_Book_List)
        print("You successfully added a book!!!\nThank you for donet us a book! It will help other to get free book for devolop there knowledge.")
    def return_book(self):
        inp2=input("pls input your book that you want to return: ")

        def getdate():
            import datetime
            return datetime.datetime.now()
        print(getdate())
        f=open("returned book.txt", "a")
        f.write(inp2 + (str(getdate())))
        f.close()
        print("Thank you for returning your book.")
Library=library()
print(f"Hi!{nam} welcome to Talha's library")
while True:
    print("What you want? Display Book, Lend Book, Add Book Or Return Book.")
    library_input = int(
        input("pls input a number \n1 for Display Book\n2 for Lend Book\n3 for Add Book\n4 for Return Book\nInput: "))
    if library_input==1:
        Library.display_book()
    elif library_input==2:
        Library.lend_book()
    elif library_input==3:
        Library.add_book()
    elif library_input==4:
        Library.return_book()
    num11 = input("Pls input 1 for continue or enter 2 for exit: ")
    if int(num11) == 1:
        continue
    elif int(num11)==2:
        break
