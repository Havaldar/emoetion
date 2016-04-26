import praw

##List contains all the tuples of anime
##Only need to glean Name and date
animes = ['fullmetal alchemist'] 

reddit = praw.Reddit("OtakuNLP")
reddit.login("OtakuNLP", "adam_meyers")

for anime in animes:
    output = open(anime, 'w+')
    for submission in reddit.search(anime,limit=100):
        print str(submission)
        for comment in submission.comments:
            print str(comment)
    output.close()