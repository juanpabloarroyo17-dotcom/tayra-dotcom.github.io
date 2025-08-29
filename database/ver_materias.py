import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'questions.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()

materias = set()
for row in c.execute('SELECT DISTINCT materia FROM questions'):
    print(row)
    materias.add(row[0])

conn.close()
print('Materias encontradas:', materias)
