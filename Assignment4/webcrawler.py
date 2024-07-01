"""
File: webcrawler.py
Name: Blair
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    d = {}
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        items = soup.find_all('table', {'class': 't-stripe'})
        male = 0
        female = 0
        lst = []
        for item in items:
            lst = item.tbody.text.split()[:1000]  # 200個排名 * 5個item
        for i in range(2, len(lst), 5):  # 每五個為一個排名的循環
            num = lst[i].replace(',', '')
            male += int(num)
        print('Male Number: ', male)
        for j in range(4, len(lst), 5):
            num = lst[j].replace(',', '')
            female += int(num)
        print('Female Number: ', female)




if __name__ == '__main__':
    main()
