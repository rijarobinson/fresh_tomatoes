# Lesson 3.4: Make Classes                                                      |80 characters
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

contact = media.Movie("Contact",
                        "A woman volunteers for a mission to the unknown "
                        "and is thoroughly moved by what she finds there."
                        "Story outlined by Carl Sagan and Ann Druyan, based "
                        "on the novel by Carl Sagen.",
                        "http://fr.web.img6.acsta.net/medias/nmedia/18/83/99/25/19721074.jpg", #NOQA
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "Jul 11, 1997")

axe_murderer = media.Movie("So I Married an Axe Murderer",
                     "A man finally finds his one and only...and "
                     "finds she has a secret past that he may not "
                     "be able to overlook.",
                     "http://moviefiles.alphacoders.com/400/poster-4008.jpg", #NOQA
                     "https://www.youtube.com/watch?v=yto08I_IiAg",
                     "Jul 30, 1993")

what_dreams = media.Movie("What Dreams May Come",
                          "After he dies in a car crash, a man searches heaven "
                          "and hell for his beloved wife.",
                          "http://www.upsem.edu/theologyandfilm/wp-content/uploads/2013/07/What-Dreams-May-Come-poster.jpg", #NOQA
                          "https://www.youtube.com/watch?v=TPZpQsEFcKI",
                          "Oct 2, 1998")

gentlemen_prefer_blondes = media.Movie("Gentlemen Prefer Blondes",
                                        "Singers Lorelei Lee and Dorothy Shaw "
                                        "travel to Paris, pursued by a private "
                                        "detective hired by the disapproving "
                                        "father of Lorelei's fiance to keep "
                                        "an eye on her, as well as a rich, enamored "
                                        "old man and many other doting admirers.",
                                        "http://images2.fanpop.com/image/photos/10800000/Gentlemen-Prefer-Blondes-Poster-gentlemen-prefer-blondes-10896389-665-1024.jpg", #NOQA
                                        "https://www.youtube.com/watch?v=ur9GKLl8v4U", #NOQA
                                        "Jul 15, 1953")

edward_scissorhands = media.Movie("Edward Scissorhands",
                                  "A gentle man created from body parts by a mad "
                                  "scientist with scissors for hands is "
                                  "brought into a new community after living "
                                  "in isolation.",
                                  "http://img12.deviantart.net/dd40/i/2010/249/c/0/edward_scissorhands_poster_by_dark_spawn-d2d8mwe.jpg", #NOQA
                                  "https://www.youtube.com/watch?v=PubEgTsP-Kc",
                                  "Dec 7, 1990")

pleasantville = media.Movie("Pleasantville",
                            "A community discovers that seeing the no-so-pleasant "
                            "side of life results in a rich experience.",
                            "http://www.dvdsreleasedates.com/posters/800/P/Pleasantville-movie-poster.jpg", #NOQA
                            "https://www.youtube.com/watch?v=Q-4pnXcqyt0",
                            "Oct 23, 1998")

#create a movie array
movies = [pleasantville, what_dreams,
          gentlemen_prefer_blondes, edward_scissorhands,
          contact, axe_murderer]
#run open_movie_pages function within the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
