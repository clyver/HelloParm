from flask import Flask

app = Flask(__name__)

app.config.from_object('config')
# import statement at the end to avoid circular refs
from webapp import views
