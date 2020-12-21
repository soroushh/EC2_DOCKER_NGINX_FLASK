from flask import Flask, render_template, url_for, redirect, jsonify, make_response

app = Flask(__name__)

@app.route('/health')
def health():
    return 'pong'

@app.route('/hello')
def hello():
    return 'This is an app served with gunicorn.'

@app.route('/real')
def real_endpoint():
    response = jsonify({'message': 'This is the real endpoint.'})
    corrected_response = make_response(response)
    corrected_response.set_cookie('name', 'Soroush')
    return corrected_response

@app.route('/hoy')
def hey():
    return jsonify({'message': 'hey man.'})


@app.route('/test')
def test():
    return jsonify({'MESSAGE': 'THIS IS A FINAL TEST VIEW.'})
