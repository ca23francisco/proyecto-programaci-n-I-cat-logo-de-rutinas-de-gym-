# MANUEL DE JESÚS VIGIL CHICA VC23019
# Emerson Alexander Alfaro Hidalgo AH23012
# Francisco Adonay Cabrera Álvarez CA23055

import sqlite3

class BaseDeDatos:
    def __init__(self, db_name='gym.db'):
        self.db_name = db_name
        self.create_database()

    def create_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rutinas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                grupo_muscular TEXT NOT NULL,
                rutina TEXT NOT NULL,
                gif TEXT  -- Nueva columna para almacenar la ruta del GIF
            )
        ''')
        conn.commit()
        conn.close()

    def insertar_rutina(self, grupo_muscular, rutina, gif=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO rutinas (grupo_muscular, rutina, gif)
            VALUES (?, ?, ?)
        ''', (grupo_muscular, rutina, gif))
        conn.commit()
        conn.close()

    def obtener_rutinas(self, grupo_muscular):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT rutina, gif FROM rutinas WHERE grupo_muscular = ?
        ''', (grupo_muscular,))
        rutinas = cursor.fetchall()
        conn.close()
        return rutinas
