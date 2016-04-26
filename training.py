import nltk
from nltk.tokenize import RegexpTokenizer
import re
import os

tokenizer = RegexpTokenizer(r'\w+')
ratings_probability = {x : 0 for x in xrange(4)}
ratings_probability['total'] = 0
texts = {}
ratings = {}
uniq_words = set()

authors = ['Dennis+Schwartz', 'James+Berardinelli', 'Scott+Renshaw', 'Steve+Rhodes']
for author in authors:
	addr = 'scale_whole_review/scale_whole_review/'+author+'/txt.parag'
	file_names = [f for f in os.listdir(addr)]
	print len(file_names)
	for file_name in file_names:
		file = open(addr + '/' + file_name, 'r')
		key = file_name[:-4]
		texts[key] = set([w.lower() for w in tokenizer.tokenize(file.read())])
		for word in texts[key]:
			uniq_words.add(word)
		file.close()

	rating_file = open('scale_data/scaledata/' + author + '/label.4class.'+ author,'r')
	tokenized_ratings = rating_file.read().strip().split('\n')
	rating_file.close()
	id_file = open('scale_data/scaledata/' + author + '/id.' + author, 'r')
	tokenized_ids = id_file.read().strip().split('\n')
	id_file.close()
	for i in xrange(len(tokenized_ids)):
		ratings_probability['total'] += 1
		ratings_probability[int(tokenized_ratings[i])] += 1
		ratings[int(tokenized_ids[i])] = int(tokenized_ratings[i])

word_counts = {word : {x : 0 for x in xrange(4)} for word in uniq_words}
for key in texts:
	for word in texts[key]:
		word_counts[word][ratings[int(key)]] += 1

output = open('word_count.txt', 'w+')
for word in word_counts:
	output.write(word + "\t" + str(word_counts[word][0]) + "\t" + str(word_counts[word][1]) + "\t" + str(word_counts[word][2]) + "\t" + str(word_counts[word][3]) + "\n")
