import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'questions.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()

for row in c.execute('SELECT id, materia, pregunta, opciones FROM questions LIMIT 10'):
    print(row)

conn.close()
print('Consulta finalizada.')
