import sys
import tweepy
import mongodb
from mongodb import *
import csv

consumer_key="mMIHCZwY3aulqkgTAx1PnCVLD"
consumer_secret="gDfYtuumjAzIySIKfl0R2AbIGuxn6iD3u1LGDDPAJpZw6Tog1u"
access_key="261144009-stGBGbRD5YvDQg213OdpaTzMbvIPw0ipNEP7E3j1"
access_secret="SqSE4JEavFaKGt82Mck4kowdYxox7zbONwgoebdY6lRkU"
alchemy_key = 'a42e52676e99bc7b0fdcb1fd7e19988bfa6f22ae'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
        
    def on_status(self, status):
            with open('file.txt', 'w') as f: 
        		f.write(status.text.encode('utf8'))
                        print status.text.encode('utf8')
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=[-117.162348, 32.73954803,-117.1545436, 32.74849182])

'''
 [-117.162348, 32.73954803,-117.1545436, 32.74849182] : 0.0143884892086
 [-117.162348, 32.74506392,-117.1545436, 32.74215273]  : 0.409302325581
 [-117.162348, 32.74227153,-117.1545436, 32.74506392] : -0.0310344827586

'''
