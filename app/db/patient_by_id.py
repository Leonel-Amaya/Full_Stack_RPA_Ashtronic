from app.db.connection import get_connection
import logging
import json

logger = logging.getLogger(__name__)

def get_patient_by_id(patient_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM patients WHERE id = %s"
        cursor.execute(query, (patient_id,))

        patient = cursor.fetchone()

        cursor.close()
        conn.close()

        if patient and isinstance(patient.get('raw_row_json'), str):
            try:
                patient['raw_row_json'] = json.loads(patient['raw_row_json'])
            except:
                patient['raw_row_json'] = {}
        return patient
    except Exception as e:
        logger.error(f"Error al hacer la query: {e}")
        return None
    
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close