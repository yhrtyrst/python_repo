import requests 
from bs4 import BeautifulSoup


def main():
	url = 'https://www.imdb.com/chart/top'
	response = requests.get(url)
	# print(response)  # html 代號
	html = response.text  # 所有網頁原始碼
	soup = BeautifulSoup(html)
	items = soup.find_all('span', {'class': 'secondaryInfo'})
	d = {}
	for item in items:
		target = item.text
		if target in d:
			d[target] += 1
		else:
			d[target] = 1
	for key, value in sorted(d.items(), key=lambda t: t[1]):
		print(f'{key}->{value}')


if __name__ == '__main__':
	main()
