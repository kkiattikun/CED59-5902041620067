from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/', methods=["post"])
def register():
    fname = request.form['txt_fname']
    lname = request.form['txt_lname']
    email = request.form['txt_email']
    username = request.form['txt_user']
    password = request.form['txt_pwd']
    return (fname+' : '+lname+' : '+email+' : '+username+' : '+password)

if __name__ == '__main__':
    app.run()

