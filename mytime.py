from flask import Flask
from flask import request
import time
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_time():
    return f"{time.time()}"


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0')
    except Exception as exc:
        logging.error(exc)
