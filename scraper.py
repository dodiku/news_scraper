'''
[1] receive a list of companies
[2] go to ft.com (or any other page) and get all links to articles that their headline includes at least one of the company names
[3] create a spreadsheet with the list of the relevant articles
'''


'''---------------
getting the companies from the 'companies.txt' file, and adding them to an array/list (companies)
---------------'''
companies = tuple(open("companies.txt", 'r'))
companies_file = open("companies.txt", 'r')
companies = []
for line in companies_file.readlines():
    companies.append(line.rstrip('\n'))


'''---------------
getting the website URLs from the 'websites.txt' file, and adding them to an array/list (urls)
---------------'''
websites_file = tuple(open("websites.txt", 'r'))
websites_file = open("websites.txt", 'r')
urls = []
for line in websites_file.readlines():
    print (line.rstrip('\n'))
    urls.append(line.rstrip('\n'))
print (urls)
