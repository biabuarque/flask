from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', css_template='index.css')

@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html', css_template='blog.css')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/forgotmypassword')
def forgotmypassword():
    return render_template('forgotmypassword.html')

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')

if __name__ == '__main__':
    app.run(debug=True)