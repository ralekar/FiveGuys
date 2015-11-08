from twitter import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import unicodedata
import argparse

consumer_key="mMIHCZwY3aulqkgTAx1PnCVLD"
consumer_secret="gDfYtuumjAzIySIKfl0R2AbIGuxn6iD3u1LGDDPAJpZw6Tog1u"
access_token="261144009-stGBGbRD5YvDQg213OdpaTzMbvIPw0ipNEP7E3j1"
access_token_secret="SqSE4JEavFaKGt82Mck4kowdYxox7zbONwgoebdY6lRkU"

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

parser = argparse.ArgumentParser()
parser.add_argument("searchList", nargs='?', default="check_for_empty_string")
args = parser.parse_args()

if args.searchList == 'check_for_empty_string':
 print 'No argument passed. Using Kansas City as Default'
 searchTerms = ['Kansas City']
else: 
 searchTerms = args.searchList.split(",")

for terms in searchTerms:
 q = terms
 
 count = 250
 search_results = t.search.tweets(q=q, count=count)
 statuses = search_results['statuses']
 text = ""

 for status in statuses:
  text = text + status['text']

 text = unicodedata.normalize('NFKD',text).encode('ascii','ignore')
 sent = TextBlob(text)
 polarity = sent.sentiment.polarity
 subjectivity = sent.sentiment.subjectivity
 keyword = q

 sent = TextBlob(text, analyzer=NaiveBayesAnalyzer())
 classification = sent.sentiment.classification
 p_pos = sent.sentiment.p_pos
 p_neg = sent.sentiment.p_neg
 tweetcount = count
 senttype = 'twitter'

