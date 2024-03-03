from flask import Blueprint, Flask, render_template

app = Flask(__name__)

bp = Blueprint("driver", __name__, url_prefix="/driver")

data = []

@bp.route("/", methods=("GET","POST"))
def render():
    return render_template("driver.html",
                           ip="wiiid.local",
                           configs=[
                               ["Left ", "CMD+Z"],
                               ["Right", "CMD+SHIFT+Z"],
                               ["DOWN ", "CMD+Z"],
                               ["Left ", "CMD+Z"],
                               ["Left ", "CMD+Z"],
                               ["Left ", "CMD+Z"],
                               ],
                           data=data)

def update_data(new_data):
    global data
    data = new_data

@bp.before_app_request
def load():
    print("load")

if __name__ == '__main__':
    app.run(debug=True, host='wiiid.local', port=80)
