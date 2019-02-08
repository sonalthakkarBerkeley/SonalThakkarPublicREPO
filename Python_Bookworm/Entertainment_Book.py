from collections import defaultdict
from urllib.request import urlopen
import json
import io
import numbers as np
#from urllib2 import urlopen

#from Entertainment import Entertainment
from EntertainmentPlay import EntertainmentPlay

class Entertainment_Book():
    '''Class for Entertainment Book object. This will create Book objects depending on user choices'''
    book_type_list = ('Fiction', 'Non-Fiction','fiction','non-fiction', 'Non-fiction')
    book_dict = {}
    def __init__(self, book_type):
        self.book_type = self.book_type
        self.book()

    def book(self):
        user_input_book = input("What kind of a book would you like to check out? You can select from Fiction or Non-Fiction: ")
        user_input_title = input("Would you like to enter a Title? If yes enter it: ")
        user_input_dt = input("Would you like to enter a Published Year? If yes enter it: ")
        publisher_counter = defaultdict(int)
        if ' ' in user_input_title:
            user_input_title = ''.join((user_input_title.split(' ')))
        #Checking if year entered is a number
        if user_input_dt != '' and user_input_dt not in list(np.arange(0,9)):
            #if str(int(float(user_input_dt))) != user_input_dt:
            print('You cannot enter a non-numberic/non null Published Date. Clearing it out and processing')
            user_input_dt = ''
        if user_input_book in Entertainment_Book.book_type_list:
            urlis = "https://www.googleapis.com/books/v1/volumes?q=categories="+user_input_book+"*"+user_input_title+"*"+user_input_dt+"'&maxResults=10"
            response = urlopen(urlis)
            rawData = response.read()#.decoding("utf-8")
            book_data = json.loads(rawData)

            for item in book_data["items"]:
                title = item["volumeInfo"].setdefault("title", "None")
                authors = item["volumeInfo"].setdefault("authors", "None")
                publishedDate = item["volumeInfo"].setdefault("publishedDate", "None")
                description =  item["volumeInfo"].setdefault("description", "None")
                publisher_counter[title, ','.join(authors), publishedDate, ','.join(description)] += 1

            i = 1
            for (title, authors, publishedDate, textSnippet), count in publisher_counter.items():
                print(i, (": Title: "+ title+ " , Author: "+ authors+ " , Published Date: "+ publishedDate), "\n")
                Entertainment_Book.book_dict[i] = (title, authors, publishedDate, description)
                i += 1

            Entertainment_Book.book_replug(publisher_counter)
        else:
            print("Entry should have been Fiction or Non-Fiction. Exiting Loop!")
            return publisher_counter

    def book_replug(self):
        #Not type casting to int means even if a number is entered it will be of type str
        user_input_book_replug = input("Would you like to select one of the suggestions or go on? " +
                                       "(Enter number to select from above selection or 'Y' to go on: ")
        if user_input_book_replug.upper() == 'Y':
            Entertainment_Book.book(self)
        #using a list comprehension since the entry can either be a num or letter
        elif user_input_book_replug in (str(i) for i in list(range(1,11))):
           # print (Entertainment_Book.book_dict[int(user_input_book_replug)])
            #unpacking the tuple to be able to feed into file
            title, authors, publishedDate, description = Entertainment_Book.book_dict[int(user_input_book_replug)]
            # creating a booklist file to diaplay to the user at the end
            fout = open("booklist", 'wt')
            fout.write ("You book selection and associated movie suggestions are as follows...\n\n")
            fout.write(("Title: "+ title + "\n" + "Author: " + authors + "\n"+ "Description: " + description))
            fout.close()
            # Write JSON file
            try:
                to_unicode = unicode
            except NameError:
                to_unicode = str
            with io.open('book_list.json', 'w', encoding='utf8') as outfile:
                str_ = json.dumps(Entertainment_Book.book_dict[int(user_input_book_replug)],
                                  indent=4, sort_keys=True,
                                  separators=(',', ': '), ensure_ascii=False)
                outfile.write(to_unicode(str_))
            et = EntertainmentPlay('Book')
        elif type(user_input_book_replug) != 'int' and user_input_book_replug != 'Y' and user_input_book_replug not in (str(i) for i in list(range(1,11))):
            user_input_book_replug = input("Entry should be within 1-10 to be able to select from the above list. Or 'Y' to continue searching: ")
            if user_input_book_replug.upper() == 'Y':
                Entertainment_Book.book(self)
            #using a list comprehension since the entry can either be a num or letter
            elif user_input_book_replug in (str(i) for i in list(range(1,11))):
               # print (Entertainment_Book.book_dict[int(user_input_book_replug)])
               #unpacking the tuple to be able to feed into file
                # creating a booklist file to diaplay to the user at the end
                title, authors, publishedDate, description = Entertainment_Book.book_dict[int(user_input_book_replug)]
                fout = open("booklist", 'wt')
                fout.write ("You book selection and associated movie suggestions are as follows...\n\n")
                fout.write(("Title: "+ title + "\n" + "Author: " + authors + "\n"+ "Description: " + description))
                fout.close()
                # Write JSON file
                # creating a booklist json file to use to to generate the associated movie selections
                try:
                    to_unicode = unicode
                except NameError:
                    to_unicode = str
                with io.open('book_list.json', 'w', encoding='utf8') as outfile:
                    str_ = json.dumps(Entertainment_Book.book_dict[int(user_input_book_replug)],
                                      indent=4, sort_keys=True,
                                      separators=(',', ': '), ensure_ascii=False)
                    outfile.write(to_unicode(str_))
                et = EntertainmentPlay('Book')
            else:
                print('Exiting from the program')
                exit()
        else:
            print('Exiting from the program')
            exit()

        return None
