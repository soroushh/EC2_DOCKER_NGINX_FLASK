from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/health')
def health():
    return 'pong'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
