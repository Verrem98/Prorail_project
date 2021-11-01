from flask import Blueprint, render_template, request, json

views = Blueprint('views', __name__)


@views.route('/')
def homepage():
	return render_template('index.html')


@views.route('/', methods=['POST'])
def result():
	test1 = request.form['test1']
	test2 = request.form['test2']
	return json.dumps({'status': 'OK', 'test1': test1, 'test2': test2})
