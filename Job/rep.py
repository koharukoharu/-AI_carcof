import re

replypattern = '@[\w]+'
urlpattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
rtpattern = '^RT.*$'
datepattern ='\w+ \w+ \d+ \d+:\d+:\d+ .\d+ \d+$'


contents = open("koko.txt", "r", encoding="utf8", errors='ignore')

for text in contents:
    i = re.sub(replypattern, '', text)

    i = re.sub(urlpattern, '', i)
    i = re.sub(rtpattern, '', i)
    #i = re.sub(datepattern, '', i)

    writefile = open("new_koko.txt", "a", encoding="utf8", errors='ignore')
    writefile.write(i)
writefile.close()
contents.close()


