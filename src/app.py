from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    current_env = os.getenv("FLASK_ENV")
    return f"Hello there, {current_env}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)

