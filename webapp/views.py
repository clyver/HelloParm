from flask import render_template
from webapp import app
from webapp.forms import ChickenParmForm

@app.route('/', methods=["POST"])
def parm_me_bro():
  form = ChickenParmForm()
  if form.validate_on_submit():
    flash('You can eat %d parms?!"', form.num_parms.data) 
  return render_template('index.html', title='An Ode to Parmesan', form=form)

