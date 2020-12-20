from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/health')
def health():
    return 'pong'

@app.route('/hello')
def hello():
    return 'This is an app served with gunicorn.'
