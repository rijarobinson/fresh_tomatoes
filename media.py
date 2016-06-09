# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    #triple quotes specifies the text as __doc__ pre-defined class variable, which provides
    #documentation on the class when called. needs to be before any custom variables
    #in the code??


    VALID_RATINGS = ["G","PG","PG-13","R"]
    #VALID_RATINGS is a Class Variable. This particular one is a constant, which
    #means it will probably not change, and Google style guide recommends all caps
    #for these variable names
    

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release = release_date
        self.storyline = movie_storyline

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)     
        

        #Class
        #Instance
        #Constructor
        #Self
        #Instance Variable
        #Instance method
