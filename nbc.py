training_set = []
test_set = []

word_counts = {}

for text in training_set:
	uniq_words = set(text.split())
	if text is 'good':

	for word in uniq_words:
		try:
			word_counts[word][token] += 1
		except KeyError:
			word_counts[word][token] = 1





		for token in text:
		if token[1] == 'good':
			good_words.add(token[0])
		else:
			bad.add(token[0])
	for word in good_words:
		try:
			word_counts['good'][word] += 1
		except KeyError:
			word_counts['good'][word] = 1
	for word in bad_words:
		try:
			word_counts['bad'][word] += 1
		except KeyError:
			word_counts['bad'][word] = 1

polarity_probability = {}
num_of_articles = len(training_set)
for word in word_counts['good']:
	polarity_probability[word] = (word_counts['good'][word] / num_of_articles)
for word in word_counts['good']:
	polarity_probability[word] = word_counts['good'][word] / num_of_articles