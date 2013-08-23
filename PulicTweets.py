#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aditya
#
# Created:     10/08/2013
# Copyright:   (c) aditya 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tweepy
from tweepy.streaming import StreamListener
#from tweepy import OAuthHandler
#from tweepy import Stream

consumer_key="NgoByN2ByrhkfRxdie65GA"
consumer_secret="I250Jp9LKr9WDeor936RX8g3EvRyjAgpW6sPauUcE"
access_token="18720103-IeDHeMzOzvSlRaGCGXANpJqRLpWU327kSkq8vTBiQ"
access_token_secret="kOXT5hUw53TImGjq6MT27BK5NHxMVNMjHRGXoz1H8E"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self,status):
        print status

#auth = tweepy.auth.BasicAuthHandler(user,passw);
#api = tweepy.API(auth);
#api.update_status("This rarely works");

if __name__ == '__main__':
    l = StdOutListener()
    auth1 = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth1.set_access_token(access_token,access_token_secret)
    try:
        api = tweepy.API(auth1)
        print("this is authaticated")

    except Exception, e:
       print("error complete")
    #api.PostUpdate('Test1')
    #stream = tweepy.Stream(auth1,l);
    #stream.filter(track=['basketball'])
    status = "status=test 1";
    api.public_timeline()