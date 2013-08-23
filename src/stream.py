#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aditya
#
# Created:     21/08/2013
# Copyright:   (c) aditya 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##def main():
##    pass
##
##if __name__ == '__main__':
##    main()

from twython import Twython
from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    def on_success(self,status):
       with open('workfiles.txt', 'a') as f:
        f.write(status['user']['name']+ ' ' +( status['created_at']+ ' '+ status['text'] ))
        f.write('\n')
       print (status)

    def on_error(self, status_code,resp):
        print resp

APP_KEY = 'gRFoHczqjlVC352V9EIg'
APP_SECRET = '0CvD65ylEIk24smjUXurSMkbBLXOJ1k6A4av3PSXJr4'
TOK = '1688617718-mDy72hDhln7K88mGBJs2nDHO5lYmVXOIM7Sirx2'
TOK_SEC = 'gMMktKJHz1q9miKmuWQKDIYfMJVQahUR0Xd40wGtw'

stream = MyStreamer(APP_KEY,APP_SECRET,TOK,TOK_SEC)
stream.statuses.filter(track='modi , raga', language='en')

