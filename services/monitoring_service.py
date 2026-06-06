from services.ping_service import check_host

def update_device_status(devices):
    for device in devices:
        device["status"] = check_host(device["ip_address"])
    return devices
