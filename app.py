from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'expo_tecnica_2025_secret'
DATABASE = os.path.join(os.path.dirname(__file__), 'database', 'questions.db')

# Helper to get DB connection
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/reset_results', methods=['POST'])
def reset_results():
    conn = get_db()
    conn.execute('DELETE FROM results')
    conn.commit()
    return redirect(url_for('results'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exam', methods=['GET', 'POST'])
def exam():
    conn = get_db()
    feedback = None
    preguntas = []
    materia = request.form.get('materia') if request.method == 'POST' else None
    dificultad = request.form.get('dificultad') if request.method == 'POST' else None
    num_preguntas_raw = request.form.get('num_preguntas', '5') if request.method == 'POST' else '5'
    num_preguntas = int(num_preguntas_raw) if num_preguntas_raw.isdigit() else 5
    # Si se presiona el botón 'Iniciar simulacro' (POST pero sin respuestas)
    if request.method == 'POST' and not any(k.startswith('resp_') for k in request.form.keys()):
        query = "SELECT * FROM questions WHERE 1=1"
        params = []
        if materia:
            query += " AND materia=?"
            params.append(materia)
        if dificultad:
            query += " AND dificultad=?"
            params.append(dificultad)
        query += " ORDER BY RANDOM() LIMIT ?"
        params.append(num_preguntas)
        preguntas = conn.execute(query, params).fetchall()
        # Guardar preguntas en sesión para usarlas al calificar
        session['preguntas_simulacro'] = [dict(p) for p in preguntas]
        return render_template('exam.html', preguntas=preguntas, materia=materia, dificultad=dificultad)
    # Si se envían respuestas
    elif request.method == 'POST':
        preguntas = session.get('preguntas_simulacro', [])
        respuestas = {}
        correctas = 0
        incorrectas = 0
        explicaciones = []
        for p in preguntas:
            user_answer = request.form.get(f'resp_{p["id"]}')
            respuestas[p["id"]] = user_answer
            if user_answer:
                # Normalizar ambas respuestas para comparar
                import re
                def normalize(text):
                    return re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ]', '', str(text)).lower()
                if normalize(user_answer) == normalize(p["respuesta_correcta"]):
                    correctas += 1
                    explicaciones.append(f'✓ {p["pregunta"]}: Correcto. {p["explicacion"]}')
                else:
                    incorrectas += 1
                    explicaciones.append(f'✗ {p["pregunta"]}: Incorrecto. {p["explicacion"]}')
            else:
                incorrectas += 1
                explicaciones.append(f'✗ {p["pregunta"]}: Sin respuesta. {p["explicacion"]}')
        usuario = session.get('usuario', 'Invitado')
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M')
        puntaje = correctas * 1
        conn.execute("INSERT INTO results (fecha, usuario, puntaje, respuestas_correctas, respuestas_incorrectas) VALUES (?, ?, ?, ?, ?)",
                    (fecha, usuario, puntaje, correctas, incorrectas))
        conn.commit()
        session['feedback'] = explicaciones
        session.pop('preguntas_simulacro', None)
        return redirect(url_for('results'))
    # GET: solo muestra el formulario de personalización
    else:
        preguntas = []
        return render_template('exam.html', preguntas=preguntas)

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    conn = get_db()
    mensaje = None
    if request.method == 'POST':
        materia = request.form.get('materia')
        dificultad = request.form.get('dificultad')
        pregunta = request.form.get('pregunta')
        opciones = request.form.get('opciones')
        respuesta_correcta = request.form.get('respuesta_correcta')
        explicacion = request.form.get('explicacion')
        if materia and dificultad and pregunta and opciones and respuesta_correcta:
            conn.execute('''INSERT INTO questions (materia, dificultad, pregunta, opciones, respuesta_correcta, explicacion) VALUES (?, ?, ?, ?, ?, ?)''',
                (materia, dificultad, pregunta, opciones, respuesta_correcta, explicacion))
            conn.commit()
            mensaje = "Pregunta agregada exitosamente."
    preguntas = conn.execute("SELECT * FROM questions ORDER BY materia, dificultad").fetchall()
    return render_template('questions.html', preguntas=preguntas, mensaje=mensaje)

@app.route('/delete_question/<int:question_id>', methods=['POST'])
def delete_question(question_id):
    conn = get_db()
    conn.execute('DELETE FROM questions WHERE id=?', (question_id,))
    conn.commit()
    return redirect(url_for('questions'))

@app.route('/results')
def results():
    conn = get_db()
    usuario = session.get('usuario', 'Invitado')
    # Obtener últimos resultados del usuario
    res = conn.execute("SELECT * FROM results WHERE usuario=? ORDER BY fecha DESC LIMIT 1", (usuario,)).fetchone()
    puntaje = res['puntaje'] if res else 0
    correctas = res['respuestas_correctas'] if res else 0
    incorrectas = res['respuestas_incorrectas'] if res else 0
    # Obtener todos los resultados
    todos = conn.execute("SELECT * FROM results ORDER BY fecha DESC").fetchall()
    feedback = session.pop('feedback', None)
    return render_template('results.html', puntaje=puntaje, correctas=correctas, incorrectas=incorrectas, todos=todos, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
