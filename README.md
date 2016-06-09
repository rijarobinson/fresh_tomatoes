#Marija's Mass Lysteria (derived from Udacity's Movie Trailer Website project)

This web application is a modification of Udacity's Movie Trailer Website project for the Full Stack Programming Nanodegree.
The initial version displays a selection of Marija's favorite movies with release dates, descriptions, and movie posters. 
Clicking the movie posters brings up a linked YouTube video of the movie's trailer. Future expansions will include other lists, accessible by the drop-down menu at the right of the header.

##Modules & Libraries
media.py
entertainment_center.py
fresh_tomatoes.py


media.py contains the python code for the class "Movies". Imports webbrowser from standard library.
entertainment_center.py instantiates the movie objects, creates and array of the objects, and runs the open_movies_page function
contained in the fresh_tomatoes.py file. Imports fresh_tomatoes and media modules.
fresh_tomatoes.py contains the html formatting of the page as well as python scripting for the movie tiles and creation of the hmtl page (fresh_tomatoes.html). Imports webbrowser, os, and re modules.

##Using the Application
To run the application, place all files in the same folder, open entertainment_center.py and use the Run command to run the module. This should generate and open the fresh_tomatoes.html file in the web browser.

To customize the file, you can open the entertainment_center.py file in your favorite text editor and replace the movies with your own information, using links to provide the movie posters and trailer videos. Rename each movie instantiation variable to a relevant name and make sure you update the array at the bottom of the file to reflect the new variable names. Save the file and run to see your new web page. Change your page header and dropdown list in the fresh_tomatoes.py file. Re-run entertainment_center.py to generate the updated page.

Base files for this application were provided by Udacity (Udacity.com).  Additional instruction on programming python is available by signing up for a class on their site.

I welcome any feedback on this project at marija@springmail.com.