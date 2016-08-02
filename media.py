import re
import json

class Movie():     
	# keep track of all instances using a set     
	__instances = set()

	# class to store movie's info
	def __init__(self, movie_title, release_year, movie_storyline, poster_image, 
		trailer_youtube, star_rating):
		self.__class__.__instances.add(self)
		self.title = movie_title
		self.release_year = release_year
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.star_rating = star_rating

	# generates movie's youtube id from its url
	def trailer_youtube_id(self):
		youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.trailer_youtube_url)
		youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', 
			self.trailer_youtube_url)
		return youtube_id_match.group(0) if youtube_id_match else None

	@staticmethod
	# create movie instances from json file
	def import_json(file_name):
		with open(file_name, 'rt') as data_file:
			movie_data = json.load(data_file)

		for movie in movie_data:     
			Movie(movie['title'], movie['release_year'], movie['storyline'], 
				movie['poster_image_url'], movie['trailer_youtube_url'], movie['star_rating'])

	@classmethod
	# get a list of all instances of the class
	def list_movies(cls):
		return list(cls.__instances)