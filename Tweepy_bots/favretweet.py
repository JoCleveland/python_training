import tweepy


import logging


from configuration import create_api


import json


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FavRetweetListner(tweepy.StreamListner):
    
    
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    
    def on_status(self, tweet):
        logger.info(f'Processing tweet id {tweet.id}')
        
        
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            return
        
        
        if not tweet.favorited:
            try:
                tweet.favorite()


            except Exception as e:
                logger.error("Error on favorite", exc_info=True)
       
       
        if not tweet.retweeted:
            try:
                tweet.retweet()


            except Exception as e:
                logger.error("Error on retweet", exc_info=True)

        
    def on_error(self, status):
        logger.error(status)

    
def main(keywords):
    api = create_api()
    tweets_listner = FavRetweetListner(api)
    stream = tweepy.Stream(api.auth, tweets_listner)
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    
    
    main(["cactus","succulent"])