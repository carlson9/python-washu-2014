import time
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
#Stratos Safioleas 49058




