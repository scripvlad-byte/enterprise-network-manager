from flask import Blueprint, request, jsonify
from services.device_service import get_devices

devices_bp = Blueprint("devices", __name__)

@devices_bp.route("/devices", methods=["GET"])
def devices_list():
    devices = get_devices()
    return jsonify(devices)
