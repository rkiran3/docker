# let's import the flask
from flask import Flask, render_template
import os
import psycopg2
import logging

# for loading secrets file
from dotenv import load_dotenv

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# read in the secrets file
load_dotenv()

host = os.getenv("HOST")
database = os.getenv("DATABASE")
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")

logging.info(database)

conn = psycopg2.connect(
    host=host,
    database=database,
    user=db_user,
    password=db_password
)


@app.route('/')  # this decorator create the home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = 'Flask Application'
    return render_template('home.html', techs=techs, name=name, title='Home')


@app.route('/about')
def about():
    name = 'Flask Application'
    return render_template('about.html', name=name, title='About Us')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/snippets')
def get_snippets():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM snippet order by lstmoddt desc')
    snippets = cursor.fetchall()
    cursor.close()
    return render_template('snippets.html', snippets=snippets)
    return get_snippet_random(str(2))


@app.route('/snippet')
def get_snippet():
    return get_snippet_random(str(5))


@app.route('/snippet/r/<string:count>')
def get_snippet_random(count):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM snippet order by random() limit ' + count)
    snippets = cursor.fetchall()
    cursor.close()
    return render_template('snippets.html', snippets=snippets, count=count)


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
