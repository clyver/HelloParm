from flask import render_template
from webapp import app
from webapp.forms import ChickenParmForm

@app.route('/')
def parm_me_bro():
  form = ChickenParmForm()
  return render_template('index.html', title='An Ode to Parmesan', form=form)
