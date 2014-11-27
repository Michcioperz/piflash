#!/usr/bin/env python3
from argparse import ArgumentParser
import subprocess, os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

if not os.path.exists(os.path.join('static','out.log')):
	with open(os.path.join('static', 'out.log'), 'w') as f:
		f.write("")
if not os.path.exists(os.path.join('static','err.log')):
	with open(os.path.join('static', 'err.log'), 'w') as f:
		f.write("")

@app.route('/make', methods=['POST','GET'])
def make():
	if request.method == 'POST':
		with open('static/main.cpp', 'w') as file:
			file.write(request.form['code'])
		subprocess.call(['bash', 'doit.sh'])
		return redirect(url_for('index'))
	return render_template('form.html')

@app.route("/")
def index():
    return render_template('index.html', cout=stdout(), cerr=stderr())

@app.route("/stdout")
def stdout():
	with open('static/out.log') as outlog:
		return outlog.read()

@app.route("/stderr")
def stderr():
	with open('/static/err.log') as errlog:
		return errlog.read()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-h', '--host', type=str, default='0.0.0.0')
    parser.add_argument('-p', '--port', type=int, default=8123)
    args = parser.parse_args()
    app.run(debug=True, host=args.host, port=args.port)
