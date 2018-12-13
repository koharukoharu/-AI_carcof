# -*- coding: utf-8 -*-
import os

path = "./study/new_tweet.txt"
tuika = ""

#追加textをtwitterから取得し、書き込み用データにする。

if os.path.isfile(path):
    contents = open(path, "a+", encoding="utf8", errors="ignore")
    contents.write(tuika + "\n")

contents.close()
