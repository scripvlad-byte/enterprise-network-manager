CREATE DATABASE IF NOT EXISTS enterprise_network;

USE enterprise_network;

CREATE TABLE devices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    ip_address VARCHAR(45) NOT NULL UNIQUE,
    status VARCHAR(20) DEFAULT 'Unknown',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
