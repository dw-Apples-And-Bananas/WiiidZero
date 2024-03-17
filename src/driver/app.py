import time
import random
from flask import Flask, render_template
from turbo_flask import Turbo
import threading

app = Flask(__name__)
turbo = Turbo(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.context_processor
def inject_data():
    with open("data.txt", "r") as f:
        line = f.readlines()
        return {"data": line[0], "data2": line[1]}

def update_data():
    with app.app_context():
        while True:
            time.sleep(.5)
            turbo.push(turbo.replace(render_template("driver.html"), "data"))

first = 0
@app.before_request
def before_request():
    global first
    if first == 0:
        first = 1
        threading.Thread(target=update_data).start()

if __name__ == '__main__':
    app.run(debug=True, host='wiiid.local', port=80)
    # app.run(debug=True, host='0.0.0.0', port=80)
