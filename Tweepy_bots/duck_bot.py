import tweepy


from math import e


import logging


from configuration import create_api


import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FavRetweetListner(tweepy.Stream):


    def __init__(self, api):
        self.api = api
        self.me = api.me()


    def on_status(self, tweet):
        logger.info(f'Processing tweet with id {tweet.id}.')


        if tweet.in_reply_to_status_id is not None or tweet.user.id \
            == self.me.id:
            return


        if not tweet.favorited:
            try:
                tweet.favorite()


            except Exception as e:
                logger.error("An error occured while favoriting.", exc_info=True)

        
        if not tweet.retweeted:
            try:
                tweet.retweet()


            except Exception as e:
                logger.error("An error occured while retweeting.", exc_info=True)


    def on_error(self, status):
        logger.error(status)


def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id


    for tweet in tweepy.Cursor(api.mentions_timeline,
    since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)


        if tweet.in_reply_to_status_id is not None:
            continue


        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering {tweet.user.name}'s tweet.")

            api.update_status(
                status="Please contact me via DM.",
                in_reply_to_status_id=tweet.id,
            )


    return new_since_id


def main(keywords):
    api = create_api()
    tweets_listner = FavRetweetListner(api)
    stream = tweepy.Stream(api.auth, tweets_listner)
    stream.filter(track=keywords, languages=["en"])

    since_id = 1
    while True:
        since_id = check_mentions(api,["help", "care", "duck"], since_id)
        logger.info("Waiting...")
        time.sleep(300)





if __name__ == "__main__":


    main(["duck", "ducks"])