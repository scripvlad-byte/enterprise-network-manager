# System Architecture

## Overview

Enterprise Network Manager is a web-based system for monitoring network devices and managing IT assets.

## Architecture Layers

### 1. Presentation Layer
- HTML (Bootstrap dashboard)
- JavaScript (future updates)

### 2. Backend Layer
- Python Flask application
- Routes (Blueprints)
- Services (business logic)

### 3. Service Layer
- ping_service → checks device availability
- monitoring_service → updates device status

### 4. Data Layer
- MySQL database
- devices table stores network assets

## Data Flow

User → Flask Route → Service Layer → MySQL → Response → Dashboard

## Key Features

- Network monitoring via ICMP ping
- Device status tracking
- REST-ready architecture
- Modular design (scalable)
