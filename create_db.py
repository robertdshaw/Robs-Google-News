import sqlite3
import logging

class NewsDatabase:
    def __init__(self, db_name='news.db'):
        """Initialize the NewsDatabase class with the given database name."""
        self.db_name = db_name
    
    def connect(self):
        """Establish a connection to the SQLite database and set it to WAL (Write Ahead Logging) mode."""
        try:
            conn = sqlite3.connect(self.db_name)
            conn.execute('PRAGMA journal_mode = WAL;')   
            return conn
        except sqlite3.Error as e:
            logging.error(f"Error connecting to the database: {e}")
            raise

    def create_table(self):
        """Create the 'news' table if it doesn't already exist."""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, 
                description TEXT, 
                url TEXT, 
                publishedAt TEXT,
                source TEXT
            )
        ''')
        conn.commit()
        conn.close()
