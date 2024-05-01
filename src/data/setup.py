import sqlite3

DATABASE = 'service.db'

def create_table():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS page (
                page_id INTEGER PRIMARY KEY,
                token TEXT,
                sender_id TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_table()
