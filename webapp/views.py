from flask import flash
from flask import render_template
from webapp import app
from webapp import parm_pics
from webapp.forms import ChickenParmForm
from parm.fetch_food import parm_perfection

@app.route('/', methods=['GET'])
def index():
    form = ChickenParmForm()
    return render_template('index.html', title='An Ode to Parmesan', form=form)

@app.route('/parm', methods=['POST'])
def parm_me_bro():
    form = ChickenParmForm()
    if form.validate_on_submit():
        parm_urls = parm_pics.get_recent_parms(form.num_parms.data)
        flash('You can eat %d parms?! Sick dude!"', form.num_parms.data)
        return render_template('parm.html',
                               title='An Ode to Parmesan',
                               num_parms=form.num_parms.data,
                               parm_urls=parm_urls,
                               ingredients=parm_perfection)
    return render_template('index.html', title='An Ode to Parmesan', form=form)


