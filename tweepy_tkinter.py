import sys
import tkinter as tk
import tweepy

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, text="Get Tweet",command=self.get_twitter_tl)
        self.hi_there.grid(column=0,row=1)

        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.quit.grid(column=1,row=1)

        self.tweet_form = tk.Entry(self)
        self.tweet_form.grid(column=0,row=0)

        self.hi_there = tk.Button(self, text="Post Tweet",command=self.post_tweet)
        self.hi_there.grid(column=1,row=0)

    def get_twitter_tl(self):
        TL = get_twitter_api()
        buff = tk.StringVar()
        buff.set(TL.get_tl())
        label = tk.Label(root, textvariable = buff)
        label.pack()

    def post_tweet(self):
        get_value = self.tweet_form.get()
        get_api = get_twitter_api()
        get_api.post(get_value)

class get_twitter_api:

    _CONSUMER_KEY    = 'xxxxx'
    _CONSUMER_SECRET = 'xxxxx'
    _ACCESS_TOKEN    = 'xxxxx'
    _ACCESS_SECRET   = 'xxxxx'

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
        _CONSUMER_SECRET = input('Consumer Secretを入力してださい :')
        _ACCESS_TOKEN    = input('Access Tokenを入力してください :')
        _ACCESS_SECRET   = input('Access Token Secretを入力してください :')

    _auth = tweepy.OAuthHandler(_CONSUMER_KEY, _CONSUMER_SECRET)
    _auth.set_access_token(_ACCESS_TOKEN, _ACCESS_SECRET)

    _api = tweepy.API(_auth)

    def get_tl(self):
        try:
            return self._api.home_timeline()[0].text

        except Exception as err:
            #return ('Error:Something happened(なにかがおきました)')
            return ('エラー:{0}'.format(err.args[0][0]['message']))

    def post(self,tweet):
        self._api.update_status(tweet)

root = tk.Tk()
root.title(sys.argv) #アプリケーションのタイトル
app = Application(master=root)
app.mainloop()
