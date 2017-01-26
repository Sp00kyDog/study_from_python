#! /usr/bin/python3
# -*- coding: utf-8 -*-
# PyQt5でtweepy_tkinterを実装します
# Forkしないてすと

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QLabel,
                             QLineEdit)
from PyQt5.QtCore import Qt
from tweet_api import*

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()

    tw_api = get_twitter_api()

    def getTweet():
        label = QLabel(tw_api.get_tl(), window)
        label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        Ylayout.addWidget(label)

    def post_tweet():
        get_value = twinput.text()
        tw_api.post(get_value)

    # ボタンを作成
    hi_there = QPushButton('Get Tweet', window)
    end      = QPushButton('QUIT', window)
    send     = QPushButton('Post Tweet', window)

    # 入力フォームの作成
    twinput  = QLineEdit(window)

    # ボタンのスタイルシートを設定
    end.setStyleSheet('color:red')

    # スロットを設定
    hi_there.clicked.connect(getTweet)
    end.clicked.connect(app.quit)
    send.clicked.connect(post_tweet)

    # レイアウト作成
    Xlayout1 = QHBoxLayout()
    Xlayout2 = QHBoxLayout()
    Ylayout  = QVBoxLayout()

    # レイアウトにボタンを追加
    Xlayout1.addWidget(twinput)
    Xlayout1.addWidget(send)
    Xlayout2.addWidget(hi_there)
    Xlayout2.addWidget(end)

    # 縦レイアウトに横レイアウト*2を追加
    Ylayout.addLayout(Xlayout1)
    Ylayout.addLayout(Xlayout2)

    # レイアウトをセット
    window.setLayout(Ylayout)

    window.show()
    sys.exit(app.exec_())
