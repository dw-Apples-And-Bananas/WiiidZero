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

bp = Blueprint("driver", __name__, url_prefix="/driver")

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
                               ])

@bp.before_app_request
def load():
    print("load")
