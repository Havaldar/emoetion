from nltk.tokenize import RegexpTokenizer

articles_total = 5006
class_freqs = [615, 1553, 1998, 840]
priors = [w / float(5006) for w in class_freqs]
file = open('word_count.txt','r')
word_counts = {w.split('\t')[0] : [int(a) for a in w.split('\t')[1:]] for w in file.read().split('\n')}
file.close()

def NBC_phrase(article):
    result = [class_freqs[w] / float(5006) for w in xrange(4)]
    for token in article: 
        for i in xrange(4):
            try:
                result[i] *= (word_counts[token][i] / float(class_freqs[i])) / (sum(word_counts[token]) / float(5006))
            except KeyError:
                continue
    return result

print NBC_phrase()

