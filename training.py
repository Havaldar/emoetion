import nltk
import re
import os

ratings_probability = {x / float(10) : 0 for x in xrange(1,10)}
all_words = set([])


texts = {}
ratings = {}

authors = ['Dennis+Schwartz', 'James+Berardinelli', 'Scott+Renshaw', 'Steve+Rhodes']
for author in authors:
	# getting texts
	addr = 'scale_whole_review/scale_whole_review/'+author+'/txt.parag'
	file_names = [f for f in os.listdir(addr)]
	for file_name in file_names:
		file = open(addr + '/' + file_name, 'r')
		key = file_name[:-4]
		texts[int(key)] = file.read()
		file.close()

	# getting ratings 
	rating_file = open('scale_data/scaledata/' + author + '/rating.'+ author,'r')
	id_file = open('scale_data/scaledata/' + author + '/id.' + author, 'r')
	tokenized_ratings = rating_file.read().split('\n')
	rating_file.close()
	tokenized_ids = id_file.read().split('\n')
	id_file.close()
	for i in xrange(1,len(tokenized_ids)):
		ratings[(tokenized_ids[i])] = (tokenized_ratings[i])
