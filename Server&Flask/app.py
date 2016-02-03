from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello World!'

FILE_PATH = '/home/honeycomb/SparkTeam/part-00000'

@app.route('/path')
def path():
    return FILE_PATH

@app.route('/result')
def result():
    return 'Result'

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username


if __name__ == '__main__':
	app.run()

