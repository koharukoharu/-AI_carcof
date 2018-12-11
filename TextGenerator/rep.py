import re

replypattern = '@[\w]+'
urlpattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'

contents = open("momobako.txt", "r", encoding="utf8", errors='ignore')

for text in contents:
    i = re.sub(replypattern, '', text)
    i = re.sub(urlpattern, '', i)
    writefile = open("new_tweet.txt", "a", encoding="utf8", errors='ignore')
    writefile.write(i)
writefile.close()
contents.close()


