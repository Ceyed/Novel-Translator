import sqlite3

DB_NAME = 'story_translation_record.sqlite3'
TABLE_NAME = 'chapters'

CREATE_TABLE_COMMAND = f'''CREATE TABLE IF NOT EXISTS '{TABLE_NAME}' (
    'id'	            INTEGER,
    'chapter_name'	    TEXT,
    'chapter_link'	    TEXT,
    'done_translation'	INTEGER DEFAULT 0 COLLATE BINARY,
    PRIMARY KEY('id' AUTOINCREMENT)
);'''


def get_conn_cur():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(CREATE_TABLE_COMMAND)
    conn.commit()

    return conn, cur


def create_chapter_names_in_db(chapter_names):
    conn, cur = get_conn_cur()
  
    cur.executemany(f'INSERT INTO {TABLE_NAME} (chapter_name) VALUES (?)', chapter_names)

    conn.commit()
    conn.close()


def set_translation(chapter_name):
    conn, cur = get_conn_cur()
  
    cur.execute(f'UPDATE chapters SET done_translation=1 WHERE chapter_name="{chapter_name}"')

    conn.commit()
    conn.close()


