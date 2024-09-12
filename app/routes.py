from flask import Flask, render_template, request
import urllib.request, json, os
from dotenv import load_dotenv
from utils import get_movie_url

load_dotenv()
app = Flask(__name__)

app.config['API_KEY'] = os.getenv('API_KEY')
fruits = []
records = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('fruits'):
            fruits.append(request.form.get('fruits'))
    return render_template('index.html', fruits=fruits)

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        if request.form.get('student') and request.form.get('note'):
            records.append({'student': request.form.get('student'), 'note': request.form.get('note')})
    return render_template('about.html', records=records)

@app.route('/movies/<property>')
def movies(property: str):
    url = get_movie_url(property, app.config['API_KEY'])

    response = urllib.request.urlopen(url)
    movies = json.loads(response.read())

    return render_template('movies.html', movies=movies['results'])

app.run(debug=True)