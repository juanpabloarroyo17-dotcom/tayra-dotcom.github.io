
import sqlite3
import os
db_path = os.path.join(os.path.dirname(__file__), 'questions.db')

db_path = os.path.join(os.path.dirname(__file__), 'questions.db')
conn = sqlite3.connect(db_path)
# Borrar todas las preguntas existentes antes de insertar
conn.execute('DELETE FROM questions')
conn.commit()
preguntas = [
    # Español
    ("Español", "Media", "Identifique la figura literaria en “El silencio gritaba en la habitación vacía”.", "Personificación|Metáfora|Hipérbole|Antítesis", "Personificación.", "Se atribuye al silencio una acción humana (gritar)."),
    ("Español", "Media", "Diferencia entre hipérbaton y anáfora.", "El hipérbaton altera el orden|La anáfora repite palabras|Ambos son metáforas|No tienen diferencia", "El hipérbaton altera el orden normal de las palabras; la anáfora repite una palabra o frase al inicio de varios versos u oraciones.", ""),
    ("Español", "Media", "Error en “La mayoría de los estudiantes aprobaron el examen con sobresaliente”.", "No hay error|Error de concordancia|Error de puntuación|Error de tiempo verbal", "Error de concordancia. Debe ser: “La mayoría de los estudiantes aprobó…”.", ""),
    ("Español", "Media", "Recurso narrativo al alterar la cronología de los hechos.", "Anacronía|Metáfora|Narrador omnisciente|Ironía", "Anacronía (analepsis o prolepsis).", ""),
    ("Español", "Media", "Valor semántico de “pero” en: “Estudió mucho, pero no aprobó”.", "Copulativa|Adversativa|Disyuntiva|Causal", "Conjunción adversativa, expresa contraste.", ""),
    ("Español", "Media", "Subordinada en: “El profesor explicó que el examen sería el lunes”.", "El profesor explicó|que el examen sería el lunes|El examen sería el próximo lunes|El profesor explicó el examen", "“que el examen sería el lunes”.", ""),
    ("Español", "Media", "Tipo de texto de un editorial de periódico.", "Narrativo|Descriptivo|Argumentativo|Expositivo", "Argumentativo, porque defiende una postura.", ""),
    ("Español", "Media", "Tipo de narrador en “Entré en la casa y vi todo destruido”.", "Primera persona|Tercera persona|Narrador omnisciente|Narrador testigo", "Narrador en primera persona (protagonista/testigo).", ""),
    ("Español", "Media", "Función de la tesis en un ensayo argumentativo.", "Presentar datos|Exponer la idea central|Describir personajes|Narrar hechos", "Exponer la idea central que se va a defender.", ""),
    ("Español", "Media", "Efecto de la ironía en un texto.", "Genera humor|Crea contraste|No produce efecto|Aumenta la tensión", "Crear contraste entre lo que se dice y lo que se quiere significar; genera crítica o humor.", ""),
    # Estudios Sociales
    ("Estudios Sociales", "Media", "Impacto de la Revolución Industrial en América Latina.", "Industrialización|Dependencia económica|Aislamiento|Desarrollo tecnológico", "Dependencia económica de Europa/EE.UU. y aumento de exportaciones de materias primas.", ""),
    ("Estudios Sociales", "Media", "Papel de Costa Rica en la Campaña Nacional de 1856.", "Defender soberanía|Aliarse con Walker|Neutralidad|No participó", "Derrotar a William Walker y defender la soberanía regional.", ""),
    ("Estudios Sociales", "Media", "Influencia de la Guerra Fría en Centroamérica.", "Unión regional|Guerras civiles|Desarrollo económico|Desmilitarización", "Guerras civiles, intervención de EE.UU. y la URSS, polarización política.", ""),
    ("Estudios Sociales", "Media", "Causas y consecuencias de la crisis del petróleo de 1973.", "Aumento de precios|Reducción de exportaciones|Inflación|Crecimiento económico", "Aumento del precio del petróleo → inflación, crisis económica mundial.", ""),
    ("Estudios Sociales", "Media", "Concepto de Estado benefactor en Costa Rica.", "Privatización|Estado benefactor|Descentralización|Liberalismo", "Modelo donde el Estado invierte en salud, educación y bienestar social.", ""),
    ("Estudios Sociales", "Media", "Importancia de la independencia de 1821.", "Estabilidad|Inestabilidad|Inicio de vida política autónoma|Colonización", "Inicio de la vida política autónoma, aunque con inestabilidad inicial.", ""),
    ("Estudios Sociales", "Media", "Globalización y Costa Rica.", "Apertura comercial|Aislamiento|Desindustrialización|Proteccionismo", "Apertura comercial, inversión extranjera, exportación de alta tecnología.", ""),
    ("Estudios Sociales", "Media", "Influencia de la Revolución Francesa en América.", "Inspiró ideales|No influyó|Aumentó la represión|Fomentó el comercio", "Inspiró ideales de libertad e igualdad en los movimientos independentistas.", ""),
    ("Estudios Sociales", "Media", "Abolición del ejército en 1948 en Costa Rica.", "Fortalecimiento democrático|Debilitamiento|Aumento de conflictos|Reducción de educación", "Fortalecimiento democrático, inversión en educación y salud.", ""),
    ("Estudios Sociales", "Media", "Efectos del cambio climático en Costa Rica.", "Aumento de sequías|Reducción de biodiversidad|Crecimiento económico|Estabilidad política", "Aumento de sequías, inundaciones y pérdida de biodiversidad.", ""),
    # Matemáticas
    ("Matemáticas", "Media", "2x+1=64. Resuelva para x.", "x=5|x=6|x=7|x=8", "x=5.", "2^6=64."),
    ("Matemáticas", "Media", "f(x)=x^2−6x+8. Raíces.", "x=2 y x=4|x=1 y x=8|x=0 y x=8|x=3 y x=5", "x=2 y x=4.", ""),
    ("Matemáticas", "Media", "Calcule el valor de lim x→∞ (3x^2+5)/(2x^2+1).", "3/2|2/3|1|0", "3/2.", ""),
    ("Matemáticas", "Media", "Probabilidad de 2 rojas (5 rojas, 7 negras).", "5/33|5/12|1/7|2/11", "5/33.", ""),
    ("Matemáticas", "Media", "Derivada de f(x)=ln(3x^2).", "2/x|1/x|x|3x", "2/x.", ""),
    ("Matemáticas", "Media", "Sistema: 2x + y = 5, 3x - y = 4.", "x=3, y=−1|x=2, y=4|x=1, y=5|x=0, y=0", "x=3, y=−1.", ""),
    ("Matemáticas", "Media", "Área bajo f(x)=x^2, entre 0 y 3.", "9|6|3|12", "9.", "∫0^3 x^2 dx=9."),
    ("Matemáticas", "Media", "Grupo de 250 personas, 40% mujeres. ¿Cuántos son hombres?", "150|100|200|50", "150 hombres.", ""),
    ("Matemáticas", "Media", "Inecuación: 3x−7>2x+5.", "x>12|x>7|x>5|x>2", "x>12.", ""),
    ("Matemáticas", "Media", "Probabilidad de suma 7 al lanzar dos dados.", "1/6|1/12|1/36|1/3", "1/6.", ""),
    # Biología
    ("Biología", "Media", "Diferencia entre respiración aerobia y anaerobia.", "Aerobia usa oxígeno|Anaerobia usa oxígeno|Ambas producen igual ATP|No hay diferencia", "Aerobia usa oxígeno y produce más ATP; anaerobia no usa oxígeno y produce menos energía.", ""),
    ("Biología", "Media", "Función de los ribosomas.", "Síntesis de proteínas|Producción de energía|Transporte celular|Digestión", "Síntesis de proteínas.", ""),
    ("Biología", "Media", "Proceso de meiosis.", "Produce 4 gametos|Produce 2 células|No hay división|Produce células idénticas", "Dos divisiones celulares que producen 4 gametos haploides genéticamente diferentes.", ""),
    ("Biología", "Media", "Relación fotosíntesis y respiración celular.", "Fotosíntesis produce glucosa|Respiración produce glucosa|No hay relación|Ambas producen energía", "La fotosíntesis produce glucosa y oxígeno; la respiración los utiliza para producir energía (ATP).", ""),
    ("Biología", "Media", "Consecuencias de una mutación puntual en el ADN.", "Puede alterar proteínas|No tiene efecto|Siempre es letal|Produce energía", "Puede alterar una proteína, generar enfermedades o ser neutra.", ""),
    ("Biología", "Media", "Función de las enzimas.", "Catalizan reacciones|Inhiben reacciones|No tienen función|Producen energía", "Catalizan reacciones químicas, disminuyendo la energía de activación.", ""),
    ("Biología", "Media", "Diferencia entre dominancia incompleta y codominancia.", "Fenotipo intermedio|Ambos alelos se expresan|No hay diferencia|Solo un alelo se expresa", "En la incompleta aparece un fenotipo intermedio; en la codominancia se expresan ambos alelos a la vez.", ""),
    ("Biología", "Media", "Papel de los neurotransmisores en la sinapsis.", "Transmiten impulso|Inhiben impulso|No participan|Producen energía", "Transmiten el impulso nervioso entre neuronas.", ""),
    ("Biología", "Media", "Concepto de homeostasis.", "Equilibrio interno|Producción de energía|Digestión|No regula nada", "Mantenimiento del equilibrio interno del organismo.", ""),
    ("Biología", "Media", "Importancia de la biodiversidad.", "Estabilidad|No es importante|Reduce resiliencia|Produce energía", "Garantiza estabilidad de ecosistemas y resiliencia frente a cambios ambientales.", ""),
]

# Insertar preguntas en la base de datos
for p in preguntas:
    conn.execute('''INSERT INTO questions (materia, dificultad, pregunta, opciones, respuesta_correcta, explicacion) VALUES (?, ?, ?, ?, ?, ?)''', p)
conn.commit()
conn.close()
print('Preguntas reseteadas y opciones agregadas.')
