'''
Created on 3/08/2013

@author: luke
'''
from datetime import date, timedelta
from abc import *

class Library(object):
sadasfsdfsd
    def __init__(self):
        self._books = []
        
    @property
    def books_all(self):
        return self._books
    
    @property
    def books_out(self):
        return {book:(book.checked_out_to,book.checked_out[1]) for book in self._books if book.checked_out[0]} if len(self._books)>0 else False
    
    @property
    def books_in(self):
        return [book for book in self._books if not book.checked_out[0]] if len(self._books)>0 else False
    
    def _clear_data(self):
        """
        Reverts all dat ato expected data upon creation
        """
        self._books     = []
    
    def add_books(self,*args):
        """
        add a book or a bunch of books to the library
        catalogue 
        """
        def add_book(book):
            if isinstance(book,Book):
                self._books.append(book)
                
        for arg in args:
            # in case arg is iter of books
            if hasattr(arg,'__iter__'):
                for val in arg:
                    add_book(val)
            else: # presumably it's a book
                add_book(arg)
        return True
    
    def checkout(self,book,customer):
        if book.checked_out[0]:
            print("book is currently checked out to {0}".format(book.checked_out_to))
            return 0
        # set book status to out; date done in checked_out method of Book
        book.checked_out        = True
        book.checked_out_to     = customer
        # set overdue date
        book.checked_out_date   = date.today()
        return 1
        
    
    def checkin(self,book):
        """
        return the book
        """
        if book not in self._books:
            raise ValueError("book not part of library")
        if book not in self.books_out:
            raise ValueError("book is not currently out")
        book.checked_out        = False
        book.checked_out_to     = None
        book.checked_in_date    = date.today()
        book.checked_out_date   = None
        
class Book(object):
    
    def __init__(self,title,isbn,author,genre):
        for val in (title,isbn,author,genre):
            if not isinstance(val,str):
                raise TypeError("Expected str but received {0}".format(type(val)))
        self._title     = title
        if len(isbn)!= 13:
            raise AttributeError
        self._isbn              = isbn
        self._author            = author
        self._genre             = genre
        self._checked_out       = (False,)
        self._checked_out_to    = None
        self.checked_in_date    = date.today()
        self.checked_out_date   = None
        
    @property
    def title(self):
        return self._title
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def author(self):
        return self._author
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def checked_out(self):
        return self._checked_out
    
    @checked_out.setter
    def checked_out(self,res):
        if not isinstance(res,bool):
            raise TypeError("Expected boolean but recieved {0}".format(type(res)))
        self._checked_out   = (res,date.today())
        return 1
    
    @property
    def checked_out_to(self):
        return self._checked_out_to
    
    @checked_out_to.setter    
    def checked_out_to(self,person):
        self._checked_out_to = person
        
    @property
    def due_back(self):
        return self._checked_out[1]+timedelta(days=14) if self._checked_out[0] else False
        
    @property
    def overdue(self):
        return (date.today()==self._due_back)
    
    def __repr__(self):
        return ("{0}({title}-{author}-{genre}-{isbn})".format(
                self.__class__.__name__,title=self._title,
                author=self._author,genre=self._genre,isbn=self._isbn
                                                              ))
    
class ObjFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def get_object(self):
        return 0
    
    def __repr__(self):
        return "{0}-{1}".format(self.__class__.__name__, self._id)
        
class BookFactory(ObjFactory):
    
    def get_object(self, args):
        for (title,isbn,author,genre) in args:
            yield Book(title,isbn,author,genre)
            
        
                  
    
if __name__ == '__main__':
    pass
