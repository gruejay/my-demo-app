from flask import Flask
import os

app = Flask(__name__)

@app.route('/demo-app')
def hello():
    current_env = os.getenv("FLASK_ENV")
    return f"Hello, {current_env}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)

