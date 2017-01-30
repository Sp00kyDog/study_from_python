#!/usr/bin/python3
# -*- coding: utf-8 -*-
# クラスが増えた

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp,
                             QApplication, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QLabel,
                             QLineEdit)
from PyQt5.QtCore import Qt
from tweet_api import*

class Example(QMainWindow):

    #おまじないみたいなもの
    #呼びだされたらこんなかのものが実行されると考えていい
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # アクションオブジェクト作成
        getAction   = QAction('Get Tweet', self)
        tweetAction = QAction('Post Tweet', self)
        exitAction  = QAction('Exit', self)

        # ショートカットの設定
        getAction.setShortcut('Ctrl+R')
        tweetAction.setShortcut('Ctrl+Return')
        exitAction.setShortcut('Ctrl+Q')

        # カーソルを乗せるとステータスバーへ表示
        getAction.setStatusTip('Tweetを取得')
        tweetAction.setStatusTip('Tweetを送信')
        exitAction.setStatusTip('アプリケーションを終了')

        # スロットの設定
        getAction.triggered.connect(win.getTweet)
        tweetAction.triggered.connect(win.post_tweet)
        exitAction.triggered.connect(app.quit)

        # ステータスバーの設定
        self.statusBar()

        # メニューバー作成
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('ファイル')

        # Actionを紐づける
        fileMenu.addAction(getAction)
        fileMenu.addAction(tweetAction)
        fileMenu.addAction(exitAction)

        # Windowクラスを中央に設置
        self.setCentralWidget(win)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('下半身がグッドゲーム')
        self.show()

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.parts()

    def getTweet(self):
        label = QLabel(tw_api.get_tl(), self)
        label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.Ylayout.addWidget(label)

    def post_tweet(self):
        try:
            get_value = self.twinput.text()

            if(len(get_value) > 140):
                strCnt = '文字数が140を超えているのでTweetできません'
                label = QLabel(strCnt, self)
                label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
                self.Ylayout.addWidget(label)

            else:
                tw_api.post(get_value)
                self.twinput.clear()

        except Exception as err:
            errMess = 'Tweetエラー:{0}'.format(err.args[0][0]['message'])
            label = QLabel(errMess, self)
            label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
            self.Ylayout.addWidget(label)

    def parts(self):
        # ボタンを作成
        hi_there = QPushButton('Get Tweet', self)
        end      = QPushButton('QUIT', self)
        send     = QPushButton('Post Tweet', self)

        # 入力フォームの作成
        self.twinput  = QLineEdit(self)

        # ボタンのスタイルシートを設定
        end.setStyleSheet('color:red')

        # スロットを設定
        hi_there.clicked.connect(self.getTweet)
        end.clicked.connect(app.quit)
        send.clicked.connect(self.post_tweet)

        # レイアウト作成
        Xlayout1 = QHBoxLayout()
        Xlayout2 = QHBoxLayout()
        self.Ylayout  = QVBoxLayout()

        # レイアウトにボタンを追加
        Xlayout1.addWidget(self.twinput)
        Xlayout1.addWidget(send)
        Xlayout2.addWidget(hi_there)
        Xlayout2.addWidget(end)

        # 縦レイアウトに横レイアウト*2を追加
        self.Ylayout.addLayout(Xlayout1)
        self.Ylayout.addLayout(Xlayout2)

        # レイアウトをセット
        self.setLayout(self.Ylayout)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    tw_api = get_twitter_api()
    win = Window()
    ex = Example()
    sys.exit(app.exec_())
