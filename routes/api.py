from flask import Blueprint, jsonify
from services.device_service import get_devices

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/devices", methods=["GET"])
def api_devices():
    devices = get_devices()
    return jsonify(devices)
