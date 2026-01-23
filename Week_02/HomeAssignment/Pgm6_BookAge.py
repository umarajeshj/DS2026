import datetime
class Book:
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def get_age(self):
        current_year = datetime.datetime.now().year
        book_age = current_year - self.publication_year
        return book_age
    
book1 = Book("The White Tiger","AravindA",1980)
age = book1.get_age()
print("Book age : ",age)