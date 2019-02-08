from collections import defaultdict
from urllib.request import urlopen
import json

from Entertainment_Book import Entertainment_Book
from BookwormException import BookwormException
from Entertainment_Movie import Entertainment_Movie

class Entertainment():
    '''Class for Entertainment object'''
    mode = ('Book', 'Movie')
    def __init__(self):
        self.main()


    def entertainment_main(self, mode_val):
        self.mode_val = mode_val
        try:
            # depending on the user selection either the Book or the Movie class will get called
            if self.mode_val in Entertainment.mode:
                if self.mode_val == 'Book':
                    et = Entertainment_Book.book(self.mode_val)
                    return et
                elif self.mode_val == 'Movie':
                    et = Entertainment_Movie.movie(self.mode_val)
                    return et
                else:
                    raise BookwormException

        except BookwormException:
             print("Mode should be either Book or Movie")
             return None


    def main(self):
        user_input = ''
        fout = open("booklist", 'wt')
        fout.write("")
        fout.close()
        fout = open("movielist", 'wt')
        fout.write("")
        fout.close()
        while user_input.lower() != 'quit':
            user_input = input("Would you like to select a book or a movie? (Enter 'quit' to quit): ")
            if user_input.lower() == 'quit':
                print("Ending program. Thank you for using the Bookworm program!")
                break
            #Check to ensure only 1 word has been entered
            elif ' ' in user_input:
                print("Enter only 1 string")
                user_input = ''
            else:
                et = Entertainment.entertainment_main(self, user_input.title())

