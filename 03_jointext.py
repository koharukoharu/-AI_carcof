# -*- coding: utf-8 -*-
import os
from requests_oauthlib import OAuth1Session
import config
import json

path = "./study/new_tweet.txt"
tuika = ""

def create_addtext():
    #RTやURLの削除リプレース処理が必要

    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_seacret = config.access_token_seacret

    twitter = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_seacret)

    #twitterAPIからリストのTLを日付フィルタして取得する
    url = "https://api.twitter.com/1.1/lists/statuses.json" #リストのエンドポイント

    #since_IDをファイルで保持させて読み込むと前回取得ツイートの続きから取得できそう

    since_id_read = open("since.txt", "r", encoding="utf8", errors="ignore")
    since_id_load = since_id_read.read()
    since_id_read.close()

    list_id = "?list_id=xxx"
    count = "&count=" + "200"
    since_id = "&since_id=" + since_id_load
    url_list = url  + list_id + count + since_id

    req = twitter.get(url_list)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            tuika = tuika + tweet['text']
    else:
        print("no connection" + url_list)

    jointext(tuika)
    

def jointext(tuika):
    #追加textをtwitterから取得し、書き込み用データにする。


    if os.path.isfile(path):
        contents = open(path, "a+", encoding="utf8", errors="ignore")
        contents.write(tuika + "\n")
        contents.close()

if __name__ == '__main__':
    create_addtext()
