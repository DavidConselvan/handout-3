import sqlite3
from dataclasses import dataclass


def create_database(conn):
        conn.execute(f"CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL);")
@dataclass
class Note:
    id:int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self,db_name):
        self.conn= sqlite3.connect(db_name+ '.db')
        create_database(self.conn)
    
    def add(self, note):
         self.conn.execute(f"INSERT INTO note (title, content) VALUES ('{note.title}', '{note.content}');")
         self.conn.commit()

   


    