# Emoetion

## INTRODUCTION

Anime is a popular form of media in Japan that is gaining popularity in the United States.
Since most of the shows have Japanese audio, most commentary on anime hinges on bilingual
elements from both English and Japanese using the Roman alphabet. This poses several
challenges in analyzing text critiquing anime. We are hoping to build a system that given an
anime can predict the common sentiment and its rating on myanimelist.com by using Twitter
comments mentioning the specified show.


## STRATEGY FOR SOLVING THE PROBLEM

1. **Building the classifier**
We plan on making two classifiers to get a clear comparison of which works better with
our answering scheme. The first will be a Boolean Naive Baye’s Classifier that uses Laplace
Smoothing (Add­One Smoothing) to improve statistical analysis. Including Laplace Smoothing
adds another layer of inclusion for out­of­vocabulary words that appear; normally, the Naive
Bayes calculation for a particular sentence with an out­of­vocabulary word would have a
probability of 0 which contradicts to the very existence of the sentence and its according nonzero
probability.
The other classifier is a Maximum Entropy classifier that has no assumptions and aims
for a uniform distribution despite that; it will handle the out­of­vocabulary supposedly better
than the Boolean Naive Baye’s classifier. For both classifiers, we plan on using the
Sentiment140 corpus of tweets as our training data set to establish our vocabulary..
2. **Scraping and Tokenizing Tweets**
We will leveraging the Reddit API to gather posts. We will search query them by post
and topic. We will query by discussion with topics of anime­related and consider each thread of
the discuss as an opinion that we will analyze. Then we have to normalize them to accommodate
emoticons, emojis, misspellings, abbreviations, usernames, colloquialism (“loooooool” is
essentially “lol”) to name a few.
3. **Evaluation**
We plan on using the rankings and ratings on imdb.com as a comparison to check our
system. We will use Mean Average Precision that represents the average precision up to some
cutoff (in terms of some ranking number, some recall number, etc). With each classifiers results,
we can analyze and infer which system is better and why.
