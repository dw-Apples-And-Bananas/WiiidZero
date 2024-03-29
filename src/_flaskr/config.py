import functools
import json

from flask import (
    Blueprint,
    flash,
    g,
    render_template,
    request,
    session
)

bp = Blueprint("config", __name__, url_prefix="/config")

@bp.route("/", methods=("GET","POST"))
def edit():
    if request.method == "POST":
        config = request.form["config"]
        error = None

        if not config:
            error = "Config should not beauth empty."

        if error is None:
            print("save")
            # with open("/boot/Wiiid/config.json", "w") as f:
            #     f.write(config)
        
        # flash(error)

    load()
    return render_template("config.html")

@bp.before_app_request
def load():
    print("load")
    # with open("/boot/Wiiid/config.json", "r") as f:
    #     g.config = f.read()
