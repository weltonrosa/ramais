import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS ramais (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    ramal TEXT NOT NULL,
    idsetor INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS setores (
    id INTEGER PRIMARY KEY,
    setor TEXT NOT NULL,
    idsecretaria INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS secretarias (
    id INTEGER PRIMARY KEY,
    secretaria TEXT NOT NULL
);               
''')
conn.commit()
conn.close()
