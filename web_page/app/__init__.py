from flask import Flask, render_template,redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import RadioField
from wtforms.validators import InputRequired
import secrets

app = Flask(__name__)
bootstrap = Bootstrap(app)

key = secrets.token_bytes(32)
key_hex = key.hex()
app.config['SECRET_KEY'] = key_hex

class ExpertSystemForm(FlaskForm):
    choices = ["Poor","Average","Good"]
    validators=[InputRequired("You must choose one option.")]
    
    # Economic field
    material_cost = RadioField("Material cost:",choices = choices,
                               validators=validators)           
    labour_cost = RadioField("Labour cost:",choices = choices,
                             validators=validators)
    lead_time = RadioField("Lead time:",choices = choices,
                             validators=validators)
    on_time_delivery = RadioField("On-time-delivery:",choices = choices,
                             validators=validators)
    product_quality = RadioField("Product quality:",choices = choices,
                             validators=validators)
    # Environmental field
    material_usage = RadioField("Material usage:",choices = choices,
                             validators=validators)
    recicled_used = RadioField("Recicled used:",choices = choices,
                             validators=validators)
    water_usage = RadioField("Water usage:",choices = choices,
                             validators=validators)
    energy_usage = RadioField("Energy usage:",choices = choices,
                             validators=validators)
    emissions = RadioField("Emissions:",choices = choices,
                             validators=validators)
    waste = RadioField("Waste:",choices = choices,
                             validators=validators)
    # Social field
    employee_satisfaction = RadioField("Employee satisfaction:",choices = choices,
                            validators=validators)
    customer_satisfaction = RadioField("Customer satisfaction:",choices = choices,
                            validators=validators)
    community_satisfaction = RadioField("Community satisfaction:",choices = choices,
                            validators=validators)
    submit = SubmitField('Submit')


@app.route("/", methods = ['GET', 'POST'])
def index():
    form  = ExpertSystemForm()
    if form.validate_on_submit():
        material_cost_answer = form.material_cost.data
        labour_cost = form.labour_cost.data
        lead_time = form.lead_time.data
        on_time_delivery = form.on_time_delivery.data
        product_quality = form.product_quality.data
        material_usage = form.material_usage.data
        recicled_used = form.recicled_used.data
        water_usage = form.water_usage.data
        energy_usage = form.energy_usage.data
        emissions = form.emissions.data
        waste = form.waste.data
        employee_satisfaction = form.employee_satisfaction.data
        customer_satisfaction = form.customer_satisfaction.data
        community_satisfaction = form.community_satisfaction.data
        return redirect(url_for('index'))

    return render_template("index.html", form = form)



if __name__ =="__main__":
    #app.jinja_env.auto_reload = True
    #app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
    