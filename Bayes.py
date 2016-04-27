articles_total = 5006
class_freqs = [615, 1553, 1998, 840]
priors = [w / float(5006) for w in class_freqs]
file = open('word_count.txt','r')
word_counts = {w.split('\t')[0] : [a for a in w.split('\t')[1:]] for w in file.read().split('\n')}
file.close()
print word_counts
file2 = open('___.txt','r')
giant_string = file2.read()
all_words = giant_string.split(' ')

def NBC_phrase(phrase):
    end_class = []
for x in class_freqs:
    current_total = 1; 
    for y in all_words:
        try:
            num = (word_counts[word][x]+1)/float(class_freqs[x])
            for i in word_counts[word]:
                den_num += i
            den_bot = articles_total
            denom  = den_num/float(den_bot)
            this_classifier = num/float(denom)
            current_total *= this_classifier
        except KeyError:
            print("Word doesn't exist in training corpus")
    end_class.append(current_total)
print("Here is the highest sentiment "+max(end_class))
    
        
        
        
