from bs4 import BeautifulSoup

# with open("100Day Python Bootcamp/Day 45 Web Scrapping/website.html") as web_file:
#     contents = web_file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)


import requests
website_link = "https://news.ycombinator.com"

response = requests.get(website_link)
vc_web_page = response.text

soup = BeautifulSoup(vc_web_page, "html.parser")
artitle_list = soup.find_all(name="span", class_="titleline")
title_list = [article.text for article in artitle_list]

upvote_list = soup.find_all(name="span", class_="score")
score_list = [int(score.text.split(" ")[0]) for score in upvote_list]

highest_score = 0
highest_index = 0

for i in range(len(score_list)):
    if score_list[i] > highest_score:
        highest_score = score_list[i]
        highest_index = i

print(highest_score, title_list[highest_index])