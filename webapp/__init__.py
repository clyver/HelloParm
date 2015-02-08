from flask import Flask
from parm.parm_pics import ParmPics

app = Flask(__name__)

app.config.from_object('config')

# load parm pics insta api once
parm_pics = ParmPics()

# import statement at the end to avoid circular refs
from webapp import views