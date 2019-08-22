from flask import Flask, render_template, request
<<<<<<< HEAD
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
=======
from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email
>>>>>>> 9ac7f1f1c4f8cd5fc175d3b1128940d82655dd5c

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'

class Form(FlaskForm):
    fname = StringField("fname", validators=[InputRequired()])
    lname = StringField("lanme", validators=[InputRequired()])
    email = StringField("email",  [InputRequired(""), Email("Please enter email is ______@gmail.com")])
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8, message="Please enter password as size")])

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route('/')
def SingUp():
    form = Form()
    return render_template('form.html', form=form)

@app.route('/register', methods=["post"])
def register():
<<<<<<< HEAD
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template(form=form)

=======
    username = request.form['username']
    form = Form()
    if form.validate_on_submit():
        return "Index Page!! Welcome your are " + username
    return render_template('form.html', form=form)
>>>>>>> 9ac7f1f1c4f8cd5fc175d3b1128940d82655dd5c

if __name__ == '__main__':
    app.run(debug=True)