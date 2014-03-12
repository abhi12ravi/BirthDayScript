# Thanking everyone who wish you on your birthday
import requests
import json
import random
# Abhi's post time
AFTER = 1353233754
TOKEN = '<Your_Access_Token>'


thank_you_notes = [
    "A friend like you is the best gift from life. Thank you ",
    "Your birthday greeting was cool. Thank you ",
    "Messages such as yours make me feel happy about my birthday. Thank you ",
    "Your wish made my day special. Thank you ",
    "Means a lot to me. Thank you ",
    "I greatly appreciate your birthday wishes. Your friendship has always meant so much to me. Thank you "
]
def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall
    between start and end time"""
    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
            "filter_key = 'others' AND source_id = me() AND "
            "created_time > 1353233754 LIMIT 200")

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def commentall(wallposts):
    """Comments thank you on all posts"""
    #TODO convert to batch request later
    for wallpost in wallposts:

        r = requests.get('https://graph.facebook.com/%s' %
                wallpost['actor_id'])
        url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
        user = json.loads(r.text)
	thank_note  = thank_you_notes[random.randint(0, len(thank_you_notes) -1) ] + user['first_name'] + "! :) "
        #message = ' Thanks %s! You made my day. :) ' % user['first_name']
        payload = {'access_token': TOKEN, 'message': thank_note}
        s = requests.post(url, data=payload)

        #The bellow messages get printed at the back-end. Just a confirmation!
        print "Wall post %s done" % wallpost['post_id']
	      print "Wished %s .." % (user['first_name'])

if __name__ == '__main__':
    commentall(get_posts())
