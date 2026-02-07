CREATE DATABASE IF NOT EXISTS rpa_ashtronic;
USE rpa_ashtronic;

CREATE TABLE IF NOT EXISTS jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(20) NOT NULL,
    fecha_inicial DATE NOT NULL,
    fecha_final DATE NOT NULL,
    limit_rows INT NOT NULL,
    started_at DATETIME NULL,
    finished_at DATETIME NULL,
    error_message TEXT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_id INT NOT NULL,
    order_number VARCHAR(100),
    patient_name VARCHAR(255),
    patient_document VARCHAR(50),
    date_service DATETIME,
    sede VARCHAR(100),
    contrato VARCHAR(50),
    raw_row_json JSON,
    captured_ad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_job FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE
)