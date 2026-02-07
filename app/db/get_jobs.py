from app.db.connection import get_connection
import logging

logger = logging.getLogger(__name__)

def get_jobs():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT status, error_message, created_at FROM jobs ORDER BY created_at DESC"
        cursor.execute(query)

        jobs = cursor.fetchall()

        cursor.close()
        conn.close()

        return jobs
    except Exception as e:
        logger.error(f"Error al hacer la query: {e}")
        return []
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close