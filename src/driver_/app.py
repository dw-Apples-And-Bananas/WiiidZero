from flask import Blueprint, Flask, render_template
from turbo_flask import Turbo
import threading
import time

app = Flask(__name__)
turbo = Turbo(app)

data = 0

@app.route("/")
def index():
    return render_template("base.html")

@app.context_processor
def inject_data():
    global data
    data += 1
    return {"data":data}


def update_data():
    with app.app_context():
        while True:
            time.sleep(1)
            turbo.push(turbo.replace(render_template("driver.html"), "data"))


first = 0
@app.before_request
def before_request():
    global first
    if first == 0:
        first = 1
        threading.Thread(target=update_data).start()



# if __name__ == '__main__':
# # app.run(debug=True, host='wiiid.local', port=80)
#     app.run(debug=True, host='0.0.0.0', port=80)
