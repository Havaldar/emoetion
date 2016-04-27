import praw

file = open('evaluation.txt', 'r')
animes = [w.split('\t')[0] for w in file.read().split('\n') if w != '']

reddit = praw.Reddit("OtakuNLP")
reddit.login("OtakuNLP", "adam_meyers")

for anime in animes:
    name = anime.replace('/', '')
    output = open('data/'+ name, 'w+')
    for submission in reddit.search(anime,limit=50, subreddit='anime'):
        submission.replace_more_comments(limit=16, threshold=10)
        for comment in praw.helpers.flatten_tree(submission.comments):
            output.write(">> ARTICLE\n" + comment.body.encode('ascii', 'ignore') + "\n")
    output.close()