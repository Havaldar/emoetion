import nltk
from nltk.tokenize import RegexpTokenizer
import re
import requests
from bs4 import BeautifulSoup
from nltk.stem import SnowballStemmer
from time import sleep


st = SnowballStemmer("english")
tokenizer = RegexpTokenizer(r'\w+')

base_url = "http://myanimelist.net/reviews.php?t=anime&p="
ratings_probability = [0 for x in xrange(11)]
word_counts = {}

for i in xrange(1, 501):
	print i
	url = base_url + str(i)
	r = requests.get(url)
	if r.status_code == 404:
		continue
	soup = BeautifulSoup(r.text, 'html.parser')
	divs = soup.find_all('div', class_='spaceit textReadability word-break')
	for div in divs:
		try:
			rating = int(soup.find_all('td')[-1].text)
		except ValueError:
			continue
		text = [w.lower() for w in tokenizer.tokenize(' '.join(soup.find_all('div',class_='spaceit textReadability word-break')[0].text.split()[15:]))]
		ratings_probability[rating] += 1
		for word in text:
			try:
				word_counts[word][rating] += 1
			except KeyError:
				word_counts[word] = [0 for x in xrange(11)]

output = open('word_count.txt', 'w+')
for word in word_counts:
	s = word + '\t'
	for rate in word_counts[word]:
		s += str(rate) + '\t'
	s = s.strip() + '\n'
	output.write(s.encode('ascii','ignore'))
output.close()
output = open('classes_count.txt', 'w+')
s = ''
for rating in ratings_probability:
	s += str(rating) + '\t'
output.write(s.encode('ascii','ignore'))
output.close()