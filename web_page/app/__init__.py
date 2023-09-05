from flask import Flask, render_template,redirect, url_for,session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import RadioField
from wtforms.validators import InputRequired
from fuzzy_system.main_system import system
import secrets

app = Flask(__name__)
bootstrap = Bootstrap(app)

key = secrets.token_bytes(32)
key_hex = key.hex()
app.config['SECRET_KEY'] = key_hex

class ExpertSystemForm(FlaskForm):
    choices = ["1","2","3","4","5","6","7"]
    validators=[InputRequired("debes elegir una opción.")]
    
    # Economic field
    material_cost = RadioField("Material Cost:",choices = choices,
                               validators=validators)           
    labour_cost = RadioField("Labour Cost:",choices = choices,
                             validators=validators)
    lead_time = RadioField("Lead Time:",choices = choices,
                             validators=validators)
    on_time_delivery = RadioField("On-time Delivery:",choices = choices,
                             validators=validators)
    product_quality = RadioField("Product Quality:",choices = choices,
                             validators=validators)
    # Environmental field
    material_usage = RadioField("Material Usage:",choices = choices,
                             validators=validators)
    recicled_used = RadioField("Recycled Material Used:",choices = choices,
                             validators=validators)
    water_usage = RadioField("Water Usage:",choices = choices,
                             validators=validators)
    energy_usage = RadioField("Energy Usage:",choices = choices,
                             validators=validators)
    emissions = RadioField("Emissions:",choices = choices,
                             validators=validators)
    waste = RadioField("Waste:",choices = choices,
                             validators=validators)
    # Social field
    employee_satisfaction = RadioField("Employee Satisfaction:",choices = choices,
                            validators=validators)
    customer_satisfaction = RadioField("Customer Satisfaction:",choices = choices,
                            validators=validators)
    community_satisfaction = RadioField("Community Satisfaction:",choices = choices,
                            validators=validators)
    submit = SubmitField('Enviar')


@app.route("/", methods = ['GET'])
def index_get():
    form  = ExpertSystemForm()
    return render_template("index.html", form = form)

@app.route("/score", methods = ['POST'])
def score_post():
    result={}
    form  = ExpertSystemForm()
    if form.validate_on_submit():
        material_cost_answer = int(form.material_cost.data)
        labour_cost = int(form.labour_cost.data)
        lead_time = int(form.lead_time.data)
        on_time_delivery = int(form.on_time_delivery.data)
        product_quality = int(form.product_quality.data)
        material_usage = int(form.material_usage.data)
        recicled_used = int(form.recicled_used.data)
        water_usage = int(form.water_usage.data)
        energy_usage = int(form.energy_usage.data)
        emissions = int(form.emissions.data)
        waste = int(form.waste.data)
        employee_satisfaction = int(form.employee_satisfaction.data)
        customer_satisfaction = int(form.customer_satisfaction.data)
        community_satisfaction = int(form.community_satisfaction.data)

        result = system(material_cost_answer,labour_cost,lead_time,on_time_delivery,product_quality,material_usage
                        ,recicled_used,water_usage,energy_usage,emissions,waste,employee_satisfaction,customer_satisfaction,community_satisfaction)
        session['result']=result
        return render_template("sustainability_score.html", results=result)

    return render_template("index.html")
@app.route("/score", methods = ['GET'])
def score_get():
    result = session.get('result')
    if result:
        return render_template("sustainability_score.html",  results=result)
    else:
        return redirect(url_for('index_get'))

if __name__ =="__main__":
    #app.jinja_env.auto_reload = True
    #app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
    
