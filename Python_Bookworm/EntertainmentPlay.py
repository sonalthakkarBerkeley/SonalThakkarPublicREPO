import json
from urllib.request import urlopen
from BookwormException import BookwormException

class EntertainmentPlay():
    '''Class for Entertainment Play object
    This class will find matching movies for book selected'''

    movie_list = "movie_list.json"
    movie_list2 = "movie_list2.json"
    book_list = "book_list.json"
    book_data_loaded = ''
    movie_data_loaded = ''
    def __init__(self, mode_val):
        # Read JSON file
        with open(self.book_list) as book_data_file:
            EntertainmentPlay.book_data_loaded = json.load(book_data_file)
        #print(self.book_data_loaded[0])
        with open(self.movie_list) as movie_data_file:
            EntertainmentPlay.movie_data_loaded = json.load(movie_data_file)
        with open(self.movie_list2) as movie_data_file2:
            EntertainmentPlay.movie_data_loaded2 = json.load(movie_data_file2)
        self.mode_val = mode_val
        self.entertainment_play_main()


    def entertainment_play_main(self):
        try:
            if self.mode_val == 'Book':
                movs = EntertainmentPlay.movie_data_loaded[0]['movie']

                for record in movs:
                    if record["book_based"] == EntertainmentPlay.book_data_loaded[0]:
                        fout = open("booklist", 'at')
                        fout.write("\n\nThe following movies are based on your book selection. Maybe you would like to watch them \n")
                        fout.write(( "\n" +"Movie Title: "+ record["title"] + "\n" + "Release Year: " +record["year"]))
                        fout.close()

            elif self.mode_val == 'Movie':
                books = EntertainmentPlay.movie_data_loaded2[0]
                user_input_title = ''.join((books.split(' ')))
                urlis = "https://www.googleapis.com/books/v1/volumes?q=categories="+user_input_title+"*"+"'&maxResults=10"
                response = urlopen(urlis)
                rawData = response.read()#.decoding("utf-8")
                book_data = json.loads(rawData)
                #print(book_data)

                fout = open("movielist", 'at')
                fout.write("\n\nThe following books are related to your movie selection. Maybe you would like to read them \n")
                for item in book_data["items"]:
                    title = item["volumeInfo"].setdefault("title", "None")
                    authors = item["volumeInfo"].setdefault("authors", "None")
                    publishedDate = item["volumeInfo"].setdefault("publishedDate", "None")
                    description =  item["volumeInfo"].setdefault("description", "None")
                    fout.write(( "\n" +"Book Title: "+ title + "\n" + "Author: " + ','.join(authors) +  "\n" + "Description: " + description))
                    fout.write( "\n")
                fout.close()
            else:
                raise BookwormException

            EntertainmentPlay.entertainment_play_print(self)
        except BookwormException:
             print("Mode should be either Book or Movie")
        return None

    def entertainment_play_print(self):
        try:
            foutbook = open("booklist", 'rt')
            print(foutbook.read())
            foutbook.close()
            print("\n\n")
            foutmovie = open("movielist", 'rt')
            print(foutmovie.read())
            foutmovie.close()
        except BookwormException:
             print("Mode should be either Book or Movie")
        return None
