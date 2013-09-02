"""
<PLease enter module docstring here>
Created on 21/08/2013
@author: Aditya Tewari, Abhineshwar Tomar
@version: <version number>
@copyright: Aditya Tewari, Abhineshwar Tomar
@license: <license>
"""

from twython import Twython
from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    """
    <Class docstring>
    """
    def on_success(self,status):
        """
        <Docsting for method>
        """
        with open('workfiles.txt', 'a') as f:
            f.write(status['user']['name']+ ' ' +( status['created_at']+ ' '+ status['text'] ))
            f.write('\n')
            print (status)

    def on_error(self, status_code,resp):
        """
        <Docstring for method>
        """
        print resp

APP_KEY = 'gRFoHczqjlVC352V9EIg'
APP_SECRET = '0CvD65ylEIk24smjUXurSMkbBLXOJ1k6A4av3PSXJr4'
TOK = '1688617718-mDy72hDhln7K88mGBJs2nDHO5lYmVXOIM7Sirx2'
TOK_SEC = 'gMMktKJHz1q9miKmuWQKDIYfMJVQahUR0Xd40wGtw'

stream = MyStreamer(APP_KEY,APP_SECRET,TOK,TOK_SEC)
stream.statuses.filter(track='modi , raga', language='en')
