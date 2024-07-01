"""
File: web_crawler_directors.py
Name:
--------------------------
This file demonstrates how to get
directors who appear on www.imdb.com/chart/top
most frequently! Do you know who is the top one?
Let's use Python code to dig out the answer
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html)
	#########################
	items = soup.find_all('td', {'class': "titleColumn"})
	d = {}
	for item in items:
		info = item.a['title']
		director = info.split(',')[0]  # return a list
		if director not in d:
			d[director] = 1
		else:
			d[director] += 1

	for key, value in sorted(d.items(), key=lambda t: t[1]):
		print(f'{key} -> {value}')


	#########################


if __name__ == '__main__':
	main()
