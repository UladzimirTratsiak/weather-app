import os

from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField

from weather import get_weather

app = Flask(__name__, template_folder="templates")
csrf = CSRFProtect(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


class CityForm(FlaskForm):
    city = StringField("Город")
    submit = SubmitField("Получить погоду")


@app.route("/", methods=["GET", "POST"])
def index():
    form = CityForm()

    if form.validate_on_submit():
        city = form.city.data
        weather_data = get_weather(city)

        return render_template("index.html", data=weather_data, form=form)
    # Temporary plug
    data = get_weather("Wroclaw")
    return render_template("index.html", data=data, form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
