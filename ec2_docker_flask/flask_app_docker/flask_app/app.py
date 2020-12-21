from flask import Flask, render_template, url_for, redirect, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return 'pong'

@app.route('/hello')
def hello():
    return 'This is an app served with gunicorn.'

@app.route('/real')
def real_endpoint():
    return jsonify({'message': 'This is the real endpoint.'})
