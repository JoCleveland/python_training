from math import e


import tweepy


import logging


import os


logger = logging.getLogger()


def create_api():
    # consumer_key = "mGqJ1Lk7LkjbHQrCCKeBXl88B"
    # consumer_secret = "BgtpP2By8hv9wL7KjbIv1yzanqgIa8yZyoJfUI3hQpaqvnlmcM"
    # access_token = "1541539358393524225-Ood1f19uND9KztDCzuQNbVXisaNSW5"
    # access_token_secret = "j7tHggJbep4m7G8xjGKgJGgXdUOSRC79Gbrx300VUoY7O"


    auth = tweepy.OAuthHandler("mGqJ1Lk7LkjbHQrCCKeBXl88B", "BgtpP2By8hv9wL7KjbIv1yzanqgIa8yZyoJfUI3hQpaqvnlmcM")
    auth.set_access_token("1541539358393524225-Ood1f19uND9KztDCzuQNbVXisaNSW5", "j7tHggJbep4m7G8xjGKgJGgXdUOSRC79Gbrx300VUoY7O")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


    try:
        api.verify_credentials()


    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    
    
    return api


if __name__ == "__main__":
    create_api()
