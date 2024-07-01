"""
File: web_crawler_avg.py
Name:
--------------------------
This file demonstrates how to get
averages on www.imdb.com/chart/top
Do you know the average score of 250 movies?
Let's use Python code to find out the answer
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html)
	#########################
	items = soup.find_all('td', {'class': 'ratingColumn imdbRating'})
	counter = 0
	total = 0
	for item in items:
		target = item.text  # item.span.text
		total += float(target)
		counter += 1
	print(total/counter)
	#########################


if __name__ == '__main__':
	main()
