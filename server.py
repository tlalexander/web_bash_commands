
import time
from flask import Flask, render_template, request, send_from_directory, jsonify

import re
import pickle
import datetime
import subprocess

app = Flask(__name__, template_folder="templates")

# If you wanted to use redis, you would configure it this way.
# app.config['REDIS_URL'] = "redis://:@localhost:6379/0"
# redis_client = FlaskRedis(app)

@app.route('/')
def main_route():
    return "Hello World"

@app.route('/bluetooth/on')
def bluetooth_on():
    subprocess.run(["sudo", "rfkill", "unblock", "bluetooth"])
    return "Bluetooth On"

@app.route('/bluetooth/off')
def bluetooth_off():
    subprocess.run(["sudo", "rfkill", "block", "bluetooth"])
    return "Bluetooth Off"


if __name__ == "__main__":
    while True:
        try:
            app.run(debug=True,
                    use_reloader=True,
                    host="0.0.0.0",
                    port=int("80"))
        except BaseException as e:
            print(e)
            print("Server had some error. Restarting...")
            time.sleep(5)
