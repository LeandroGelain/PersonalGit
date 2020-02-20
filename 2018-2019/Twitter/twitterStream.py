from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

ACCESS_TOKEN = "3394891725-e7I9TOUGPCYWxhhUhETDdCMvIaGuswiSylg4kke"
ACCESS_TOKEN_SECRET = "Bab6fwyyPOUuKRY3sKoNpNJDNpBom3iFvsZ3Ko58v15vY"
CONSUMER_KEY = "IqTDckfkpCG78dpVLVgSw6Hlk"
CONSUMER_SECRET = "LwTkNiYO7C2qEtLBmYIMXRgWEp76aAcRHXekKC3iwoHkAG5dFy"

class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list)



class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            data = json.loads(data)
            print(data["text"])

            with open(self.fetched_tweets_filename, 'a') as tf:
                textJson = '{"Twittes:" "%s"}' %data["text"] 
                tf.write(data["text"]+";\n")
            return True

        except BaseException as e:
            print("Error on_data %s" % str(e))

        return True
          
    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    hash_tag_list = [""]
    fetched_tweets_filename = "allCommits.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)