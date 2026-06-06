from flask import Blueprint, render_template

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    devices = [
        {"hostname": "Router", "ip_address": "8.8.8.8", "status": "Online"}
    ]

    return render_template("dashboard.html", devices=devices)
