import webbrowser
import os
import re
import media
from jinja2 import Environment, FileSystemLoader, Template

# tell jinja to use templates directory
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('main.html')

# open file for eriting 
output_file = open('fresh_tomatoes.html', 'w')

# create movie instances from json file
media.Movie.import_json('movies.json')

# get the list of all movie instances
movies = media.Movie.list_movies()

# Render template using our list of movies
rendered_page = template.render(movies=movies)

output_file.write(rendered_page)
output_file.close()

# display output file in a browser
url = os.path.abspath(output_file.name)
webbrowser.open('file://' + url, new=2)
