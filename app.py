# Flask Application
from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f"Hai Salam Kenal, {name}!"

if __name__== '_main_':
    app.run(debug=True)