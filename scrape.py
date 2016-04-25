from bs4 import BeautifulSoup
import requests

output = open('evaluation.txt','w+')
url = "http://myanimelist.net/topanime.php?limit="
pages = [0, 50, 100, 150, 200, 250]

for page in pages:
	page_url = url + str(page)
	r = requests.get(page_url)
	markup = BeautifulSoup(r.text,'html.parser')
	rows = markup.find_all('tr', 'ranking-list')
	for row in rows:
		name = row.find_all('div', 'detail')[0].find_all('a')[0].text
		rating = row.find_all('span', 'text on')[0].text
		type_show = row.find_all('div', 'information di-ib mt4')[0].text.strip()
		if 'TV' == type_show[:2]:
			output.write(name.encode('ascii','ignore') + '\t' + rating.encode('ascii','ignore') + '\n')
output.close()