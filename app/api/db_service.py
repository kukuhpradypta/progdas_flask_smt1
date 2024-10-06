import psycopg2
from app.api.db_connection import db1 

def execute_query(query, source):
    connection = None  # Inisialisasi connection di awal
    retry_attempts = 1  # Jumlah percobaan koneksi ulang

    while retry_attempts >= 0:
        try:
            newSource = ''
            if(source == 'db1'):
                newSource = db1
            connection = psycopg2.connect(**newSource)
            cursor = connection.cursor()
            cursor.execute(query)
            
            if query.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
            else:
                connection.commit()
                result = cursor.rowcount

            cursor.close()
            return result
        except psycopg2.Error as e:
            print(f"Error: {e}")
            if retry_attempts > 0:
                print("Retrying connection...")
            retry_attempts -= 1
        finally:
            if connection is not None:
                connection.close()
                connection = None  # Reset connection to None after closing

    return f"Error: Failed to execute query on {source} after multiple attempts"
