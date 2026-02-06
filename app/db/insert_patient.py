from app.db.connection import get_connection

def save_patient(data):
    conn = get_connection()
    cursor = conn.cursor()
    
    raw_date = data["date_service"].strip()
    clean_date = raw_date.split(',')[0] if ',' in raw_date else raw_date

    sql = """
        INSERT INTO patients 
        (job_id, order_number, patient_name, patient_document, date_service, sede, contrato, raw_row_json)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    values = (
        data["job_id"],
        data["order_number"].strip(),
        data["patient_name"].strip(),
        data["patient_document"].strip(),
        clean_date,
        data["sede"].strip(),
        data["contrato"].strip(),
        data["raw_row_json"]
    )

    try:
        cursor.execute(sql, values)
        conn.commit()
    except Exception as e:
        print(f"Error al insertar paciente {data['order_number']}: {e}")
        conn.rollback()
    finally:
        cursor.close()