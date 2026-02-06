from app.db.connection import get_connection

def insert_job(fecha_inicial, fecha_final, limit_rows):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO jobs (status, fecha_inicial, fecha_final, limit_rows)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (
        "queued",
        fecha_inicial,
        fecha_final,
        limit_rows
    ))

    conn.commit()
    job_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return job_id
