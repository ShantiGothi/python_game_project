class library:
    def __init__(self,listofbooks):
        self.books=listofbooks
    def display(self):
        print("books present in this ")
        for book in self.books:
            print("*"+book)
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued{bookname}.please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("sorry,this book is either not available or has already been issued to someone else.plase wait")
            return False
    def returnbook(self,bookname):
            self.books.append(bookname)
            print("thanks for returning this book! hope you enjoyed reading it.have a great day ahead")
class student:
    def requestbook(self):
        self.book=input("enter the name of the book you want tomorrow")
        return self.book
    def returnbook(self):
        self.book=input("enter the name of the book you want to return:")
        return self.book
#if __name__=="__main__":
centrallibrary=library(["algorithms","django","clrs","python notes"])
    #centrallibrary = library("sachin")
student=student()

while(True):
        welcomemsg='''\n =======welcome to central library====
        please choose an option:
        1.list all the books
        2.request a book
        3.add/return a book
        4.exit the library
        
        '''
        print(welcomemsg)
        a = int(input("enter the choice:"))
        if a==1:
            centrallibrary.display()
        elif a==2:
            centrallibrary.borrowbook(student.requestbook())
        elif a==3:
            centrallibrary.returnbook(student.returnbook())
        elif a==4:
            print("thanks for choosing central library. have a great day ahead:")
            exit()
        else:
            print("invalid choice:")

