import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


web_contents = requests.get(URL).text
soup = BeautifulSoup(web_contents, "html.parser")

movie_names = soup.find_all(name = "h3", class_="title")
movie_list = [f"{movie_names[i].text}" for i in range(len(movie_names)-1, 0,-1)]
top_movies = "\n".join(movie_list)

with open("100Day Python Bootcamp/Day 45 Web Scrapping/Starting Code - 100 movies to watch start/Top 100 Movies.txt", "w") as file:
    file.write(top_movies)