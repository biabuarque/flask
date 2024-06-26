from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', css_template='index.css')

@app.route('/pomodoro')
def blog():
    return render_template('pomodoro.html', css_template='blog.css')

if __name__ == '__main__':
    app.run(debug=True)