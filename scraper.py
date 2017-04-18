'''
[v] receive a list of companies
[v] go to ft.com (or any other page) and get all links to articles that their headline includes at least one of the company names
[ ] create a spreadsheet with the list of the relevant articles
[ ] bonus: print nicely on terminal

empji <title + colored company name>
<url>
<source>

'''

import requests
from lxml import html
from bs4 import BeautifulSoup
import csv


'''---------------
getting the companies from the 'companies.txt' file, and adding them to an array/list [companies]
---------------'''
companies = tuple(open("companies.txt", 'r'))
companies_file = open("companies.txt", 'r')
companies = []
for line in companies_file.readlines():
    companies.append(line.rstrip('\n'))


'''---------------
getting the website URLs from the 'websites.txt' file, and adding them to an array/list [urls]
---------------'''
websites_file = tuple(open("websites.txt", 'r'))
websites_file = open("websites.txt", 'r')
urls = []
for line in websites_file.readlines():
    urls.append(line.rstrip('\n'))


'''---------------
getting homepage content for [urls], and storing relvant articles by [companies] on {articles}
---------------'''
problematic_urls = []
articles = []

for website in urls:
    web_content = requests.get(website)

    if (web_content.status_code == 403):
        problematic_urls.append(website)
        continue

    html = BeautifulSoup(web_content.text, "lxml")

    for link in html.find_all('a'):
        title = link.get_text().strip()
        for c in companies:
            if (c.lower() in title.lower()) and (c.lower() != title.lower()) and ('google+'.lower() != title.lower()):
                obj = {
                'title': link.get_text().strip().split('\t')[0].split('\n')[0],
                'url': link.get('href').split('?')[0],
                'source': website,
                }
                articles.append(obj)


'''---------------
saving articles from {articles} to csv file
---------------'''
with open('articles.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for item in articles:
        row = []
        row.append(item['title'])
        row.append(item['url'])
        row.append(item['source'])
        writer.writerow(row)


'''---------------
presenting {articles} on the terminal
---------------'''
