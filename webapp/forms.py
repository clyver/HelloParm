from flask.ext.wtf import Form
from wtforms import IntegerField
from wtforms.validators import InputRequired

class ChickenParmForm(Form):
  num_parms = IntegerField(validators=[InputRequired()])
