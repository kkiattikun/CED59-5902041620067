from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/', methods=["post"])
def register():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template(form=form)


if __name__ == '__main__':
    app.run()

