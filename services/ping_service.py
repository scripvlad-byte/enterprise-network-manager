from ping3 import ping

def check_host(ip):
    response = ping(ip, timeout=1)
    return "Online" if response else "Offline"
