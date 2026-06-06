from flask import Blueprint, render_template
from services.device_service import get_devices
from services.monitoring_service import update_statuses

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    update_statuses()
    devices = get_devices()

    return render_template("dashboard.html", devices=devices)
