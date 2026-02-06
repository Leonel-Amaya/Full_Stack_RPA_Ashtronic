import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def init_database():
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    conn.close()

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()

    cursor.execute("""
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
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        job_id INT NOT NULL,
        order_number VARCHAR(100), -- De columna "No. Orden"
        patient_name VARCHAR(255), -- De columna "Nombres"
        patient_document VARCHAR(50), -- De columna "Documento"
        date_service DATETIME, -- De columna "Fecha cita"
        sede VARCHAR(100), -- Del detalle (+)
        contrato VARCHAR(50), -- Del columna cups
        raw_row_json JSON, -- REQUERIDO por el criterio de "Trazabilidad" del documento
        captured_ad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT fk_job FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE
    )
    """)

    cursor.close()
    conn.close()

    print("DB creada")

if __name__ == "__main__":
    init_database()
