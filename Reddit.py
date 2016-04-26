import praw

##List contains all the tuples of anime
##Only need to glean Name and date

all_anime = [] 

reddit = praw.Reddit("OtakuNLP")
reddit.login("OtakuNLP", "adam_meyers")

for a in all_anime:
    file1 = open(a,"w+")
##1. General Search
    reddit_appearances = reddit.search(a)
    for b in reddit_appearances:
        file1.write(str(b)+"\n")
        for b1 in b.comments:
            file1.write(str(b1)+"\n")
##2. Subreddit "anime"
   reddit_appearances = reddit.search(a, subreddit="anime")
   for c in reddit_appearances:
        file1.write(str(c)+"\n")
        for c1 in b.comments:
            file1.write(str(c1)+"\n")
##3. Subreddit of anime title
    for d in reddit_appearances = reddit.search(a,subreddit=str(a)):
        file1.write(str(d)+"\n"
        for d1 in d.comments:
            file1.write(str(d1)+"\n"
 
