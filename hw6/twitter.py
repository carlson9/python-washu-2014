import time
from datetime import timedelta
followers = api.followers_ids('mcdickenson')
followers_count = 0
i=0
while i<len(followers):
    try:
        user = api.get_user(followers[i])
        if user.followers_count > followers_count:
            followers_count = user.followers_count
            most_followed = str(user.name)
        i+=1
    except: time.sleep(.25)
#Virgin America 554395
followed = api.friends_ids('mcdickenson')
i = 0
time_between = timedelta(100)
while i<len(followed):
    try:
        user = api.get_user(followed[i])
        tweets = user.timeline()
        if len(tweets) == 20:
            time_delta = tweets[0].created_at - tweets[19].created_at
            if time_delta < time_between:
                time_between = time_delta
                most_active = str(user.name)
        i+=1
    except: time.sleep(.25)





