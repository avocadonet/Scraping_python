import sqlite3
import json

DB_NAME = 'components.db'
TABLE_NAME = 'search_results'
QUERY_COLUMN = 'query'
SOURCE_COLUMN = 'source'
RESULTS_COLUMN = 'results'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            {QUERY_COLUMN} TEXT,
            {SOURCE_COLUMN} TEXT,
            {RESULTS_COLUMN} TEXT,
            PRIMARY KEY ({QUERY_COLUMN}, {SOURCE_COLUMN})
        )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def save_results_to_db(query, results, source):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    results_json = json.dumps(results, ensure_ascii=False)
    
    insert_query = f'''
        INSERT OR REPLACE INTO {TABLE_NAME} ({QUERY_COLUMN}, {SOURCE_COLUMN}, {RESULTS_COLUMN}) VALUES (?, ?, ?)
    '''
    cursor.execute(insert_query, (query, source, results_json))
    conn.commit()
    conn.close()

def get_results_from_db(query, source):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    select_query = f'SELECT {RESULTS_COLUMN} FROM {TABLE_NAME} WHERE {QUERY_COLUMN} = ? AND {SOURCE_COLUMN} = ?'
    cursor.execute(select_query, (query, source))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return json.loads(row[0])
    else:
        return None

def reset_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    drop_table_query = f'DROP TABLE IF EXISTS {TABLE_NAME}'
    cursor.execute(drop_table_query)
    conn.commit()
    conn.close()
    print("[INFO] База данных сброшена.")
    init_db()
    print("[INFO] База данных инициализирована.")