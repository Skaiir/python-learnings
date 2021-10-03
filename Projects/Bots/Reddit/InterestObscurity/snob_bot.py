from datetime import datetime
import os, sys, snob_constants as constants, praw, json
from snob_calculator import get_user_obscurity_score

SRS_TO_PROCESS = ['pythonforengineers']
SRD_SAVE_S_FREQ = 60

def crawl():
    return

def load_data():
    with open(constants.user_datafile, "r") as user_data_file:
        try:
            user_data = json.loads(user_data_file.read())
        except ValueError:
            user_data = {}
            print("User data was invalid, loading blank...")
    with open(constants.sr_datafile, "r") as subreddit_data_file:
        try:
            subreddit_data = json.loads(subreddit_data_file.read())
        except ValueError:
            subreddit_data = {}
            print("Subreddit data was invalid, loading blank")
    return user_data, subreddit_data

def main():
    os.chdir(sys.path[0])
    reddit = praw.Reddit(constants.bot_config_name)
    user_data, subreddit_data = load_data()    
    last_save: datetime = datetime.now()

    for found_request_comment in crawl():
        process(found_request_comment)
        if (datetime.now - last_save).total_seconds() > SRD_SAVE_S_FREQ:
            save_data(user_data, subreddit_data)

def process(reddit, user_data, subreddit_data, comment):
    # Do something with the comment
    username = comment.author.name
    obscurity = get_user_obscurity_score(reddit, user_data, subreddit_data, user_input)
    return

def save_data(user_data, subreddit_data):
    with open(constants.user_datafile, "w") as user_data_file:
        user_data_file.write(json.dumps(user_data))
    with open(constants.sr_datafile, "w") as subreddit_data_file:
        subreddit_data_file.write(json.dumps(subreddit_data))

main()