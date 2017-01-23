import tkinter as tk
import tweepy

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
#        self.hi_there = tk.Button(self)
#        self.hi_there["text"] = "Get Tweet!"
#        self.hi_there["command"] = self.test
#        self.hi_there.pack(side="top")
        self.hi_there = tk.Button(self, text="Get Tweet",command=self.test)
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        TL = twitter()
        print(TL.get_tl())

    def test(self):
        TL = twitter()
        buff = tk.StringVar()
        buff.set(TL.get_tl())
        label = tk.Label(root, textvariable = buff)
        label.pack()
        


class twitter:

    _CONSUMER_KEY = 'xxxxx'
    _CONSUMER_SECRET = 'xxxxx'
    _auth = tweepy.OAuthHandler(_CONSUMER_KEY, _CONSUMER_SECRET)
    _ACCESS_TOKEN = 'xxxxx'
    _ACCESS_SECRET = 'xxxxx'
    _auth.set_access_token(_ACCESS_TOKEN, _ACCESS_SECRET)
    _api = tweepy.API(_auth)

    if(_CONSUMER_KEY    == 'xxxxx' or
       _CONSUMER_SECRET == 'xxxxx' or
       _ACCESS_TOKEN    == 'xxxxx' or
       _ACCESS_SECRET   == 'xxxxx'):

        print('Consumer Key等が設定されていないようです')
        print('詳細はこちら -> '
              'http://statsbeginner.hatenablog.com/'
              'entry/2015/10/21/131717')

        _CONSUMER_KEY = input('Consumer Keyを入力してください :')
        _CONSUMER_SECRET = input('Consumer Secretを入力してださい :')
        _ACCESS_TOKEN = input('Access Tokenを入力してください :')
        _ACCESS_SECRET = input('Access Token Secretを入力してください :')

    def get_tl(self):
        try:
            return self._api.home_timeline()[0].text

        except Exception as err:
            #return ('Error:Something happened(なにかがおきました)')
            return ('エラー:', err.args)

root = tk.Tk()
app = Application(master=root)
app.mainloop()