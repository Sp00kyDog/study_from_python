#! /usr/bin/python3
# -*- coding: utf-8 -*-
# PyQt5でtweepy_tkinterを実装します

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QHBoxLayout, QVBoxLayout, QLabel,
                             QLineEdit)
from PyQt5.QtCore import Qt
import tweepy

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()

    try:
        f = open('token.txt')
        token = f.readlines()
        f.close()

        _CONSUMER_KEY    = token[0].rstrip('\r\n')
        _CONSUMER_SECRET = token[1].rstrip('\r\n')
        _ACCESS_TOKEN    = token[2].rstrip('\r\n')
        _ACCESS_SECRET   = token[3].rstrip('\r\n')

    except:
        print('Consumer Key等が設定されていないようです')
        print('詳細はこちら -> '
              'http://statsbeginner.hatenablog.com/'
              'entry/2015/10/21/131717')

        _CONSUMER_KEY    = input('Consumer Keyを入力してください :')
        _CONSUMER_SECRET = input('Consumer Secretを入力してください :')
        _ACCESS_TOKEN    = input('Access Tokenを入力してください :')
        _ACCESS_SECRET   = input('Access Token Secretを入力してください :')

    _auth = tweepy.OAuthHandler(_CONSUMER_KEY, _CONSUMER_SECRET)
    _auth.set_access_token(_ACCESS_TOKEN, _ACCESS_SECRET)

    _api = tweepy.API(_auth)

    def getTweet():
        try:
            TLtweet = _api.home_timeline()[0].text

        except Exception as err:
            TLtweet = 'エラー:{0}'.format(err.args[0][0]['message'])

        label = QLabel(TLtweet, window)
        label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        Ylayout.addWidget(label)

    def post_tweet():
        get_value = twinput.text()
        post(get_value)

    def post(tweet):
        _api.update_status(tweet)

    # ボタンを作成
    hi_there = QPushButton('Get Tweet', window) 
    quit     = QPushButton('QUIT', window)
    tweet     = QPushButton('Post Tweet', window)
    
    # 入力フォームの作成
    twinput  = QLineEdit(window)

    # ボタンのスタイルシートを設定
    quit.setStyleSheet('color:red')

    # スロットを設定
    hi_there.clicked.connect(getTweet)
    quit.clicked.connect(app.quit)
    tweet.clicked.connect(post_tweet)

    # レイアウト作成
    Xlayout1 = QHBoxLayout()
    Xlayout2 = QHBoxLayout()
    Ylayout  = QVBoxLayout()

    # レイアウトにボタンを追加
    Xlayout1.addWidget(twinput)
    Xlayout1.addWidget(tweet)
    Xlayout2.addWidget(hi_there)
    Xlayout2.addWidget(quit)

    # 縦レイアウトに横レイアウト*2を追加
    Ylayout.addLayout(Xlayout1)
    Ylayout.addLayout(Xlayout2)

    # レイアウトをセット
    window.setLayout(Ylayout)


    window.show()
    sys.exit(app.exec_())
