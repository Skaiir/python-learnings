from logging import log
from math import log10
import os, sys, praw, json, io
from re import sub
from praw.reddit import Subreddit
from prawcore.exceptions import NotFound
import snob_constants as constants
from datetime import datetime

def was_updated_within_hours(latest_update: str, hours: int) -> bool:
    return (datetime.utcnow() - datetime.fromisoformat(latest_update)).total_seconds() // 3600 < hours

def obscurity_score(uc: int) -> float:
    lower_bound = 10**4
    upper_bound = 10**7
    log_range = log10(upper_bound / lower_bound)
    uc_clamped = min(upper_bound, max(lower_bound, uc))
    log_uc = log10(uc_clamped / lower_bound)
    return (log_range - log_uc) / log_range
    
def total_obscurity_score(user_datum: dict, sr_data: dict) -> float:
    total_count = user_datum["total_count"]
    if total_count == 0:
        return 0
    return sum(obscurity_score(sr_data[sr_name]["user_count"]) * count for sr_name, count in user_datum["sr_activity"].items()) / user_datum["total_count"]

def build_subreddit_datum(sr: Subreddit) -> dict:
    return {"user_count": sr.subscribers, "latest_update": datetime.utcnow().isoformat()}

def get_user_obscurity_score(reddit, user_data, subreddit_data, username):   
    # Fetch outdated DATA
    if username in user_data and was_updated_within_hours(user_data[username]["latest_update"], 24):
        user_datum = user_data[username]
    else:
        print(f"New or outdated user: {username} detected, querying...")
        user_datum = {"sr_activity": {}, "latest_update": datetime.utcnow().isoformat()}
        user = reddit.redditor(username)
        comment_count = 0
        for comment in user.comments.new(limit = 1000):
            # Ditto but with the subreddit data, we just update subreddit data less frequently
            comment_count += 1
            sr_name = comment.subreddit.display_name
            if sr_name in subreddit_data and was_updated_within_hours(subreddit_data[sr_name]["latest_update"], 96):
                sr_datum = subreddit_data[sr_name]
            else:
                print(f"New or outdated subreddit: {sr_name} detected, querying...")
                sr = comment.subreddit
                sr_datum = build_subreddit_datum(sr)
                subreddit_data[sr_name] = sr_datum
            if sr_name in user_datum["sr_activity"]:
                user_datum["sr_activity"][sr_name] += 1
            else:
                user_datum["sr_activity"][sr_name] = 1
        user_datum["total_count"] = comment_count
        user_data[username] = user_datum
    return total_obscurity_score(user_datum, subreddit_data)

def user_exists(reddit, name):
    try:
        reddit.redditor(name).id
    except NotFound:
        return False
    return True

def main():
    os.chdir(sys.path[0])
    reddit = praw.Reddit(constants.bot_config_name)
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

    while True:
        user_input = input("Enter username to analyze or 'x' to save data and exit: ")
        if (user_input == 'x'):
            break
        if not user_exists(reddit, user_input):
            print("User does not exist")
            continue
        obscurity = get_user_obscurity_score(reddit, user_data, subreddit_data, user_input)
        print(f"User {user_input} is {obscurity:.0%} obscure")


    with open(constants.user_datafile, "w") as user_data_file:
        user_data_file.write(json.dumps(user_data))

    with open(constants.sr_datafile, "w") as subreddit_data_file:
        subreddit_data_file.write(json.dumps(subreddit_data))

main()