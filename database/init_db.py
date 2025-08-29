preguntas = [
    # Español
    ("Español", "Media", "Identifique la figura literaria presente en la frase: 'El silencio gritaba en la habitación vacía'.", "Personificación|Metáfora|Hipérbole|Antítesis", "Personificación.", "Se atribuye al silencio una acción humana (gritar)."),
    ("Español", "Media", "¿Cuál es la diferencia entre el hipérbaton y la anáfora en la construcción poética?", "El hipérbaton altera el orden|La anáfora repite palabras|Ambos son metáforas|No tienen diferencia", "El hipérbaton altera el orden normal de las palabras; la anáfora repite una palabra o frase al inicio de varios versos u oraciones.", ""),
    ("Español", "Media", "Señale el error de concordancia en la oración: 'La mayoría de los estudiantes aprobaron el examen con sobresaliente'.", "No hay error|Error de concordancia|Error de puntuación|Error de tiempo verbal", "Error de concordancia. Debe ser: 'La mayoría de los estudiantes aprobó…'.", ""),
    ("Español", "Media", "¿Qué recurso narrativo utiliza un autor al alterar la cronología de los hechos en un cuento?", "Anacronía|Metáfora|Narrador omnisciente|Ironía", "Anacronía (analepsis o prolepsis).", ""),
    ("Español", "Media", "Analice el valor semántico de la conjunción en: 'Estudió mucho, pero no logró aprobar'.", "Copulativa|Adversativa|Disyuntiva|Causal", "Conjunción adversativa, expresa contraste.", ""),
    ("Español", "Media", "Identifique la oración subordinada en: 'El profesor explicó que el examen sería el próximo lunes'.", "El profesor explicó|que el examen sería el próximo lunes|El examen sería el próximo lunes|El profesor explicó el examen", "que el examen sería el lunes.", ""),
    ("Español", "Media", "¿Qué tipo de texto corresponde a un editorial de periódico y por qué?", "Narrativo|Descriptivo|Argumentativo|Expositivo", "Argumentativo, porque defiende una postura.", ""),
    ("Español", "Media", "Determine el tipo de narrador en la frase: 'Entré en la casa y vi todo destruido'.", "Primera persona|Tercera persona|Narrador omnisciente|Narrador testigo", "Narrador en primera persona (protagonista/testigo).", ""),
    ("Español", "Media", "En un ensayo argumentativo, ¿cuál es la función de la tesis?", "Presentar datos|Exponer la idea central|Describir personajes|Narrar hechos", "Exponer la idea central que se va a defender.", ""),
    ("Español", "Media", "¿Qué efecto produce la ironía en un texto literario?", "Genera humor|Crea contraste|No produce efecto|Aumenta la tensión", "Crear contraste entre lo que se dice y lo que se quiere significar; genera crítica o humor.", ""),
    # Estudios Sociales
    ("Estudios Sociales", "Media", "¿Cuál fue el impacto económico y social de la Revolución Industrial en América Latina?", "Industrialización|Dependencia económica|Aislamiento|Desarrollo tecnológico", "Dependencia económica de Europa/EE.UU. y aumento de exportaciones de materias primas.", ""),
    ("Estudios Sociales", "Media", "Explique el papel de Costa Rica en la Campaña Nacional de 1856 contra los filibusteros.", "Defender soberanía|Aliarse con Walker|Neutralidad|No participó", "Derrotar a William Walker y defender la soberanía regional.", ""),
    ("Estudios Sociales", "Media", "¿Cómo influyó la Guerra Fría en los procesos políticos de Centroamérica?", "Unión regional|Guerras civiles|Desarrollo económico|Desmilitarización", "Guerras civiles, intervención de EE.UU. y la URSS, polarización política.", ""),
    ("Estudios Sociales", "Media", "Analice las causas y consecuencias de la crisis del petróleo de 1973.", "Aumento de precios|Reducción de exportaciones|Inflación|Crecimiento económico", "Aumento del precio del petróleo → inflación, crisis económica mundial.", ""),
    ("Estudios Sociales", "Media", "Explique el concepto de Estado benefactor y cómo se aplicó en Costa Rica durante el siglo XX.", "Privatización|Estado benefactor|Descentralización|Liberalismo", "Modelo donde el Estado invierte en salud, educación y bienestar social.", ""),
    ("Estudios Sociales", "Media", "¿Qué papel jugó la independencia de Centroamérica (1821) en el desarrollo político de la región?", "Estabilidad|Inestabilidad|Inicio de vida política autónoma|Colonización", "Inicio de la vida política autónoma, aunque con inestabilidad inicial.", ""),
    ("Estudios Sociales", "Media", "Relacione la globalización con las transformaciones económicas en Costa Rica.", "Apertura comercial|Aislamiento|Desindustrialización|Proteccionismo", "Apertura comercial, inversión extranjera, exportación de alta tecnología.", ""),
    ("Estudios Sociales", "Media", "Explique cómo la Revolución Francesa influyó en los movimientos independentistas en América.", "Inspiró ideales|No influyó|Aumentó la represión|Fomentó el comercio", "Inspiró ideales de libertad e igualdad en los movimientos independentistas.", ""),
    ("Estudios Sociales", "Media", "¿Qué importancia tuvo la abolición del ejército en 1948 para la política costarricense?", "Fortalecimiento democrático|Debilitamiento|Aumento de conflictos|Reducción de educación", "Fortalecimiento democrático, inversión en educación y salud.", ""),
    ("Estudios Sociales", "Media", "Analice los efectos del cambio climático en la economía y sociedad costarricense actual.", "Aumento de sequías|Reducción de biodiversidad|Crecimiento económico|Estabilidad política", "Aumento de sequías, inundaciones y pérdida de biodiversidad.", ""),
    # Matemáticas
    ("Matemáticas", "Media", "Resuelva para x: 2x+1=64.", "x=5|x=6|x=7|x=8", "x=5.", "2^6=64."),
    ("Matemáticas", "Media", "Si una función es f(x)=x^2−6x+8, encuentre sus raíces.", "x=2 y x=4|x=1 y x=8|x=0 y x=8|x=3 y x=5", "x=2 y x=4.", ""),
    ("Matemáticas", "Media", "Calcule el valor de lim x→∞ (3x^2+5)/(2x^2+1).", "3/2|2/3|1|0", "3/2.", ""),
    ("Matemáticas", "Media", "Una urna contiene 5 bolas rojas y 7 negras. ¿Cuál es la probabilidad de sacar 2 bolas rojas sin reemplazo?", "5/33|5/12|1/7|2/11", "5/33.", ""),
    ("Matemáticas", "Media", "Encuentre la derivada de f(x)=ln(3x^2).", "2/x|1/x|x|3x", "2/x.", ""),
    ("Matemáticas", "Media", "Resuelva el sistema: 2x+y=5, 3x−y=4.", "x=3, y=−1|x=2, y=4|x=1, y=5|x=0, y=0", "x=3, y=−1.", ""),
    ("Matemáticas", "Media", "Determine el área bajo la curva f(x)=x^2 entre x=0 y x=3.", "9|6|3|12", "9.", "∫0^3 x^2 dx=9."),
    ("Matemáticas", "Media", "Si el 40% de un grupo son mujeres y el grupo tiene 250 personas, ¿cuántas son hombres?", "150|100|200|50", "150 hombres.", ""),
    ("Matemáticas", "Media", "Resuelva la inecuación: 3x−7>2x+5.", "x>12|x>7|x>5|x>2", "x>12.", ""),
    ("Matemáticas", "Media", "Un dado se lanza dos veces. ¿Cuál es la probabilidad de obtener suma 7?", "1/6|1/12|1/36|1/3", "1/6.", ""),
    # Biología
    ("Biología", "Media", "Explique la diferencia entre respiración aerobia y respiración anaerobia.", "Aerobia usa oxígeno|Anaerobia usa oxígeno|Ambas producen igual ATP|No hay diferencia", "Aerobia usa oxígeno y produce más ATP; anaerobia no usa oxígeno y produce menos energía.", ""),
    ("Biología", "Media", "¿Cuál es la función de los ribosomas en la célula?", "Síntesis de proteínas|Producción de energía|Transporte celular|Digestión", "Síntesis de proteínas.", ""),
    ("Biología", "Media", "Describa el proceso de la meiosis y su importancia biológica.", "Produce 4 gametos|Produce 2 células|No hay división|Produce células idénticas", "Dos divisiones celulares que producen 4 gametos haploides genéticamente diferentes.", ""),
    ("Biología", "Media", "¿Cómo se relaciona la fotosíntesis con la respiración celular?", "Fotosíntesis produce glucosa|Respiración produce glucosa|No hay relación|Ambas producen energía", "La fotosíntesis produce glucosa y oxígeno; la respiración los utiliza para producir energía (ATP).", ""),
    ("Biología", "Media", "¿Qué consecuencias tiene una mutación puntual en el ADN?", "Puede alterar proteínas|No tiene efecto|Siempre es letal|Produce energía", "Puede alterar una proteína, generar enfermedades o ser neutra.", ""),
    ("Biología", "Media", "Explique la función de las enzimas en el metabolismo.", "Catalizan reacciones|Inhiben reacciones|No tienen función|Producen energía", "Catalizan reacciones químicas, disminuyendo la energía de activación.", ""),
    ("Biología", "Media", "¿Cuál es la diferencia entre dominancia incompleta y codominancia en genética?", "Fenotipo intermedio|Ambos alelos se expresan|No hay diferencia|Solo un alelo se expresa", "En la incompleta aparece un fenotipo intermedio; en la codominancia se expresan ambos alelos a la vez.", ""),
    ("Biología", "Media", "Describa el papel de los neurotransmisores en la sinapsis.", "Transmiten impulso|Inhiben impulso|No participan|Producen energía", "Transmiten el impulso nervioso entre neuronas.", ""),
    ("Biología", "Media", "¿Qué es la homeostasis y cómo la regula el sistema nervioso?", "Equilibrio interno|Producción de energía|Digestión|No regula nada", "Mantenimiento del equilibrio interno del organismo.", ""),
    ("Biología", "Media", "Analice la importancia de la biodiversidad en el equilibrio de los ecosistemas.", "Estabilidad|No es importante|Reduce resiliencia|Produce energía", "Garantiza estabilidad de ecosistemas y resiliencia frente a cambios ambientales.", ""),
]
preguntas = [
    # Español
    ("Español", "Media", "Identifique la figura literaria presente en la frase: 'El silencio gritaba en la habitación vacía'.", "", "Personificación.", "Se atribuye al silencio una acción humana (gritar)."),
    ("Español", "Media", "¿Cuál es la diferencia entre el hipérbaton y la anáfora en la construcción poética?", "", "El hipérbaton altera el orden normal de las palabras; la anáfora repite una palabra o frase al inicio de varios versos u oraciones.", ""),
    ("Español", "Media", "Señale el error de concordancia en la oración: 'La mayoría de los estudiantes aprobaron el examen con sobresaliente'.", "", "Error de concordancia. Debe ser: 'La mayoría de los estudiantes aprobó…'.", ""),
    ("Español", "Media", "¿Qué recurso narrativo utiliza un autor al alterar la cronología de los hechos en un cuento?", "", "Anacronía (analepsis o prolepsis).", ""),
    ("Español", "Media", "Analice el valor semántico de la conjunción en: 'Estudió mucho, pero no logró aprobar'.", "", "Conjunción adversativa, expresa contraste.", ""),
    ("Español", "Media", "Identifique la oración subordinada en: 'El profesor explicó que el examen sería el próximo lunes'.", "", "que el examen sería el lunes.", ""),
    ("Español", "Media", "¿Qué tipo de texto corresponde a un editorial de periódico y por qué?", "", "Argumentativo, porque defiende una postura.", ""),
    ("Español", "Media", "Determine el tipo de narrador en la frase: 'Entré en la casa y vi todo destruido'.", "", "Narrador en primera persona (protagonista/testigo).", ""),
    ("Español", "Media", "En un ensayo argumentativo, ¿cuál es la función de la tesis?", "", "Exponer la idea central que se va a defender.", ""),
    ("Español", "Media", "¿Qué efecto produce la ironía en un texto literario?", "", "Crear contraste entre lo que se dice y lo que se quiere significar; genera crítica o humor.", ""),
    # Estudios Sociales
    ("Estudios Sociales", "Media", "¿Cuál fue el impacto económico y social de la Revolución Industrial en América Latina?", "", "Dependencia económica de Europa/EE.UU. y aumento de exportaciones de materias primas.", ""),
    ("Estudios Sociales", "Media", "Explique el papel de Costa Rica en la Campaña Nacional de 1856 contra los filibusteros.", "", "Derrotar a William Walker y defender la soberanía regional.", ""),
    ("Estudios Sociales", "Media", "¿Cómo influyó la Guerra Fría en los procesos políticos de Centroamérica?", "", "Guerras civiles, intervención de EE.UU. y la URSS, polarización política.", ""),
    ("Estudios Sociales", "Media", "Analice las causas y consecuencias de la crisis del petróleo de 1973.", "", "Aumento del precio del petróleo → inflación, crisis económica mundial.", ""),
    ("Estudios Sociales", "Media", "Explique el concepto de Estado benefactor y cómo se aplicó en Costa Rica durante el siglo XX.", "", "Modelo donde el Estado invierte en salud, educación y bienestar social.", ""),
    ("Estudios Sociales", "Media", "¿Qué papel jugó la independencia de Centroamérica (1821) en el desarrollo político de la región?", "", "Inicio de la vida política autónoma, aunque con inestabilidad inicial.", ""),
    ("Estudios Sociales", "Media", "Relacione la globalización con las transformaciones económicas en Costa Rica.", "", "Apertura comercial, inversión extranjera, exportación de alta tecnología.", ""),
    ("Estudios Sociales", "Media", "Explique cómo la Revolución Francesa influyó en los movimientos independentistas en América.", "", "Inspiró ideales de libertad e igualdad en los movimientos independentistas.", ""),
    ("Estudios Sociales", "Media", "¿Qué importancia tuvo la abolición del ejército en 1948 para la política costarricense?", "", "Fortalecimiento democrático, inversión en educación y salud.", ""),
    ("Estudios Sociales", "Media", "Analice los efectos del cambio climático en la economía y sociedad costarricense actual.", "", "Aumento de sequías, inundaciones y pérdida de biodiversidad.", ""),
    # Matemáticas
    ("Matemáticas", "Media", "Resuelva para x: 2x+1=64.", "", "x=5.", "2^6=64."),
    ("Matemáticas", "Media", "Si una función es f(x)=x^2−6x+8, encuentre sus raíces.", "", "x=2 y x=4.", ""),
    ("Matemáticas", "Media", "Calcule el valor de lim x→∞ (3x^2+5)/(2x^2+1).", "", "3/2.", ""),
    ("Matemáticas", "Media", "Una urna contiene 5 bolas rojas y 7 negras. ¿Cuál es la probabilidad de sacar 2 bolas rojas sin reemplazo?", "", "5/33.", ""),
    ("Matemáticas", "Media", "Encuentre la derivada de f(x)=ln(3x^2).", "", "2/x.", ""),
    ("Matemáticas", "Media", "Resuelva el sistema: 2x+y=5, 3x−y=4.", "", "x=3, y=−1.", ""),
    ("Matemáticas", "Media", "Determine el área bajo la curva f(x)=x^2 entre x=0 y x=3.", "", "9.", "∫0^3 x^2 dx=9."),
    ("Matemáticas", "Media", "Si el 40% de un grupo son mujeres y el grupo tiene 250 personas, ¿cuántas son hombres?", "", "150 hombres.", ""),
    ("Matemáticas", "Media", "Resuelva la inecuación: 3x−7>2x+5.", "", "x>12.", ""),
    ("Matemáticas", "Media", "Un dado se lanza dos veces. ¿Cuál es la probabilidad de obtener suma 7?", "", "1/6.", ""),
    # Biología
    ("Biología", "Media", "Explique la diferencia entre respiración aerobia y respiración anaerobia.", "", "Aerobia usa oxígeno y produce más ATP; anaerobia no usa oxígeno y produce menos energía.", ""),
    ("Biología", "Media", "¿Cuál es la función de los ribosomas en la célula?", "", "Síntesis de proteínas.", ""),
    ("Biología", "Media", "Describa el proceso de la meiosis y su importancia biológica.", "", "Dos divisiones celulares que producen 4 gametos haploides genéticamente diferentes.", ""),
    ("Biología", "Media", "¿Cómo se relaciona la fotosíntesis con la respiración celular?", "", "La fotosíntesis produce glucosa y oxígeno; la respiración los utiliza para producir energía (ATP).", ""),
    ("Biología", "Media", "¿Qué consecuencias tiene una mutación puntual en el ADN?", "", "Puede alterar una proteína, generar enfermedades o ser neutra.", ""),
    ("Biología", "Media", "Explique la función de las enzimas en el metabolismo.", "", "Catalizan reacciones químicas, disminuyendo la energía de activación.", ""),
    ("Biología", "Media", "¿Cuál es la diferencia entre dominancia incompleta y codominancia en genética?", "", "En la incompleta aparece un fenotipo intermedio; en la codominancia se expresan ambos alelos a la vez.", ""),
    ("Biología", "Media", "Describa el papel de los neurotransmisores en la sinapsis.", "", "Transmiten el impulso nervioso entre neuronas.", ""),
    ("Biología", "Media", "¿Qué es la homeostasis y cómo la regula el sistema nervioso?", "", "Mantenimiento del equilibrio interno del organismo.", ""),
    ("Biología", "Media", "Analice la importancia de la biodiversidad en el equilibrio de los ecosistemas.", "", "Garantiza estabilidad de ecosistemas y resiliencia frente a cambios ambientales.", ""),
]
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'questions.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Tabla de preguntas
c.execute('''CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    materia TEXT NOT NULL,
    dificultad TEXT NOT NULL,
    pregunta TEXT NOT NULL,
    opciones TEXT NOT NULL,
    respuesta_correcta TEXT NOT NULL,
    explicacion TEXT NOT NULL
)''')

# Tabla de resultados
c.execute('''CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    usuario TEXT NOT NULL,
    puntaje INTEGER NOT NULL,
    respuestas_correctas INTEGER NOT NULL,
    respuestas_incorrectas INTEGER NOT NULL
)''')

conn.commit()
conn.close()
print('Base de datos inicializada.')

# Script para insertar preguntas iniciales
preguntas = [
    # Español
    ("Español", "Media", "Identifique la figura literaria presente en la frase: 'El silencio gritaba en la habitación vacía'.", "", "", ""),
    ("Español", "Media", "¿Cuál es la diferencia entre el hipérbaton y la anáfora en la construcción poética?", "", "", ""),
    ("Español", "Media", "Señale el error de concordancia en la oración: 'La mayoría de los estudiantes aprobaron el examen con sobresaliente'.", "", "", ""),
    ("Español", "Media", "¿Qué recurso narrativo utiliza un autor al alterar la cronología de los hechos en un cuento?", "", "", ""),
    ("Español", "Media", "Analice el valor semántico de la conjunción en: 'Estudió mucho, pero no logró aprobar'.", "", "", ""),
    ("Español", "Media", "Identifique la oración subordinada en: 'El profesor explicó que el examen sería el próximo lunes'.", "", "", ""),
    ("Español", "Media", "¿Qué tipo de texto corresponde a un editorial de periódico y por qué?", "", "", ""),
    ("Español", "Media", "Determine el tipo de narrador en la frase: 'Entré en la casa y vi todo destruido'.", "", "", ""),
    ("Español", "Media", "En un ensayo argumentativo, ¿cuál es la función de la tesis?", "", "", ""),
    ("Español", "Media", "¿Qué efecto produce la ironía en un texto literario?", "", "", ""),
    # Estudios Sociales
    ("Estudios Sociales", "Media", "¿Cuál fue el impacto económico y social de la Revolución Industrial en América Latina?", "", "", ""),
    ("Estudios Sociales", "Media", "Explique el papel de Costa Rica en la Campaña Nacional de 1856 contra los filibusteros.", "", "", ""),
    ("Estudios Sociales", "Media", "¿Cómo influyó la Guerra Fría en los procesos políticos de Centroamérica?", "", "", ""),
    ("Estudios Sociales", "Media", "Analice las causas y consecuencias de la crisis del petróleo de 1973.", "", "", ""),
    ("Estudios Sociales", "Media", "Explique el concepto de Estado benefactor y cómo se aplicó en Costa Rica durante el siglo XX.", "", "", ""),
    ("Estudios Sociales", "Media", "¿Qué papel jugó la independencia de Centroamérica (1821) en el desarrollo político de la región?", "", "", ""),
    ("Estudios Sociales", "Media", "Relacione la globalización con las transformaciones económicas en Costa Rica.", "", "", ""),
    ("Estudios Sociales", "Media", "Explique cómo la Revolución Francesa influyó en los movimientos independentistas en América.", "", "", ""),
    ("Estudios Sociales", "Media", "¿Qué importancia tuvo la abolición del ejército en 1948 para la política costarricense?", "", "", ""),
    ("Estudios Sociales", "Media", "Analice los efectos del cambio climático en la economía y sociedad costarricense actual.", "", "", ""),
    # Matemáticas
    ("Matemáticas", "Media", "Resuelva para x: 2x+1=64.", "", "", ""),
    ("Matemáticas", "Media", "Si una función es f(x)=x^2−6x+8, encuentre sus raíces.", "", "", ""),
    ("Matemáticas", "Media", "Calcule el valor de lim x→∞ (3x^2+5)/(2x^2+1).", "", "", ""),
    ("Matemáticas", "Media", "Una urna contiene 5 bolas rojas y 7 negras. ¿Cuál es la probabilidad de sacar 2 bolas rojas sin reemplazo?", "", "", ""),
    ("Matemáticas", "Media", "Encuentre la derivada de f(x)=ln(3x^2).", "", "", ""),
    ("Matemáticas", "Media", "Resuelva el sistema: 2x+y=5, 3x−y=4.", "", "", ""),
    ("Matemáticas", "Media", "Determine el área bajo la curva f(x)=x^2 entre x=0 y x=3.", "", "", ""),
    ("Matemáticas", "Media", "Si el 40% de un grupo son mujeres y el grupo tiene 250 personas, ¿cuántas son hombres?", "", "", ""),
    ("Matemáticas", "Media", "Resuelva la inecuación: 3x−7>2x+5.", "", "", ""),
    ("Matemáticas", "Media", "Un dado se lanza dos veces. ¿Cuál es la probabilidad de obtener suma 7?", "", "", ""),
    # Biología
    ("Biología", "Media", "Explique la diferencia entre respiración aerobia y respiración anaerobia.", "", "", ""),
    ("Biología", "Media", "¿Cuál es la función de los ribosomas en la célula?", "", "", ""),
    ("Biología", "Media", "Describa el proceso de la meiosis y su importancia biológica.", "", "", ""),
    ("Biología", "Media", "¿Cómo se relaciona la fotosíntesis con la respiración celular?", "", "", ""),
    ("Biología", "Media", "¿Qué consecuencias tiene una mutación puntual en el ADN?", "", "", ""),
    ("Biología", "Media", "Explique la función de las enzimas en el metabolismo.", "", "", ""),
    ("Biología", "Media", "¿Cuál es la diferencia entre dominancia incompleta y codominancia en genética?", "", "", ""),
    ("Biología", "Media", "Describa el papel de los neurotransmisores en la sinapsis.", "", "", ""),
    ("Biología", "Media", "¿Qué es la homeostasis y cómo la regula el sistema nervioso?", "", "", ""),
    ("Biología", "Media", "Analice la importancia de la biodiversidad en el equilibrio de los ecosistemas.", "", "", ""),
]

conn = sqlite3.connect(db_path)
c = conn.cursor()
for p in preguntas:
    c.execute('''INSERT INTO questions (materia, dificultad, pregunta, opciones, respuesta_correcta, explicacion) VALUES (?, ?, ?, ?, ?, ?)''', p)
conn.commit()
conn.close()
print('Preguntas iniciales agregadas.')
