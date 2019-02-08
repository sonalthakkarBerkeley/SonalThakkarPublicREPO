from collections import defaultdict
from urllib.request import urlopen
import json
import io
import random

from EntertainmentPlay import EntertainmentPlay

class Entertainment_Movie():
    movie_dict = {}
    movie_list = "movie_list.json"

    def __init__(self):
        self.movie()

    # def shuffle_movie(self):
    #     return(random.shuffle(self.movies))

    def movie(self):
        # opening a movielist json file to diaplay the movies
        with open(Entertainment_Movie.movie_list) as handle:
            records = json.loads(handle.read())
        movs = records[0]['movie']
        # shuffling the movie selection
        movs = random.shuffle(movs)
        movs = records[0]['movie']
       # self.shuffle_movie(self.movs)

        i = 1
        for record in movs:
            print(str(i) + " Title: ", record["title"], "Release Year: ", record["year"], "Book Based On: ", record["book_based"])
            Entertainment_Movie.movie_dict[i] = (record["title"], record["year"], record["book_based"])
            i += 1
            if i > 10:
                break
        #calling the select movies again
        Entertainment_Movie.movie_replug(self)
        return None

    def movie_replug(self):
        #Not type casting to int means even if a number is entered it will be of type str
        user_input_movie_replug = input("Would you like to select one of the suggestions or go on? " +
                                       "(Enter number to select from above selection or 'Y' to go on: ")
        if user_input_movie_replug.upper() == 'Y':
            Entertainment_Movie.movie(self)
        #using a list comprehension since the entry can either be a num or letter
        elif user_input_movie_replug in (str(i) for i in list(range(1,11))):
            title, year, book_based = Entertainment_Movie.movie_dict[int(user_input_movie_replug)]
            fout = open("movielist", 'wt')
            fout.write("You movie selection and possible books you might find interesting based on your movie selection are as follows...\n\n")
            fout.write(("Title: "+ title + "\n" + "Year: " + year))
            fout.close()
            # Write JSON file
            try:
                to_unicode = unicode
            except NameError:
                to_unicode = str
            with io.open('movie_list2.json', 'w', encoding='utf8') as outfile:
                str_ = json.dumps(Entertainment_Movie.movie_dict[int(user_input_movie_replug)],
                                  indent=4, sort_keys=True,
                                  separators=(',', ': '), ensure_ascii=False)
                outfile.write(to_unicode(str_))
            et = EntertainmentPlay('Movie')
           # et.entertainment_play_main()
        elif type(user_input_movie_replug) != 'int' and user_input_movie_replug != 'Y' and user_input_movie_replug not in (str(i) for i in list(range(1,11))):
            user_input_movie_replug = input("Entry should be within 1-10 to be able to select from the above list. Or 'Y' to continue searching: ")
            if user_input_movie_replug.upper() == 'Y':
                Entertainment_Movie.movie(self)
            elif user_input_movie_replug in (str(i) for i in list(range(1,11))):
               # print (Entertainment_Book.book_dict[int(user_input_book_replug)])
                title, year, book_based = Entertainment_Movie.movie_dict[int(user_input_movie_replug)]
                fout = open("movielist", 'wt')
                fout.write("You movie selection and possible books you might find interesting based on your movie selection are as follows...\n\n")
                fout.write(("Title: "+ title + "\n" + "Year: " + year))
                fout.close()
                # Write JSON file
                try:
                    to_unicode = unicode
                except NameError:
                    to_unicode = str
                with io.open('movie_list2.json', 'w', encoding='utf8') as outfile:
                    str_ = json.dumps(Entertainment_Movie.movie_dict[int(user_input_movie_replug)],
                                      indent=4, sort_keys=True,
                                      separators=(',', ': '), ensure_ascii=False)
                    outfile.write(to_unicode(str_))
                et = EntertainmentPlay('Movie')
            else:
                print('Exiting from the program')
                exit()

        else:
            print('Exiting from the program')
            exit()

        return None
