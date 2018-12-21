# -*- coding: utf-8 -*-
import os
from requests_oauthlib import OAuth1Session
import config, json

path = "./study/new_tweet.txt"
tuika = ""

def create_addtext():
    #RTやURLの削除リプレース処理が必要

    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_seacret = config.access_token_seacret
    
    oath = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_seacret)

    #twitterAPIからリストのTLを日付フィルタして取得する
    url = "https://api.twitter.com/1.1/lists/statuses.json" #リストのエンドポイント
    


    jointext(tuika)
    

def jointext(tuika):
    #追加textをtwitterから取得し、書き込み用データにする。


    if os.path.isfile(path):
        contents = open(path, "a+", encoding="utf8", errors="ignore")
        contents.write(tuika + "\n")
    contents.close()


if __name__ == '__main__':
    create_addtext()
