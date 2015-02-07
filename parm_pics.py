from instagram.client import InstagramAPI
import urllib
from keys import Keys

# Call our secrets
keys = Keys()

# Instantiate the Api
api = InstagramAPI(client_id=keys.get_instagram_client_id(), client_secret=keys.get_instagram_client_secret())

# Ask for the raw data about the most recent '#chickenparm' post
media = api.tag_recent_media(1,1,"chickenparm")[0]

# Pull out the url the parm
most_recent_chickenparm_pic = media[0].images['standard_resolution'].url 

print most_recent_chickenparm_pic

