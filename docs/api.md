# API Documentation

## Base URL
http://localhost:5000/

## GET /devices

Returns list of all devices.

### Response
```json id="d5"
[
  {
    "id": 1,
    "hostname": "Router-01",
    "ip_address": "8.8.8.8",
    "status": "Online"
  }
]
Future Endpoints (planned)
POST /devices

Add new device

DELETE /devices/{id}

Remove device

PUT /devices/{id}

Update device information

Status Update Logic

Device status is updated automatically using ICMP ping:

Online → device responds
Offline → no response
