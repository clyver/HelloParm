from flask.ext.wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired

class ChickenParmForm(Form):
  num_parms = IntegerField(validators=[DataRequired()])
