from app.db.connection import get_connection
from typing import Optional
import logging

logger = logging.getLogger(__name__)

def get_patients(job_id: Optional[int] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM patients WHERE 1=1"
        params = []

        if job_id:
            query += " AND job_id = %s"
            params.append(job_id)
        
        if start_date and end_date:
            query += " AND date_service BETWEEN %s AND %s"
            params.append(start_date)
            params.append(end_date)
        
        cursor.execute(query, tuple(params))
        results = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return results
    
    except Exception as e:
        logger.error(f"Error al hacer la query: {e}")
        return []
    
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close