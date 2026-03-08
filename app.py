import streamlit as st

# Lista de preguntas
preguntas = [
    {
        "texto": "¿Cuál es el río más largo del mundo?",
        "opciones": ["🌊 Amazonas", "🏞 Nilo", "🏞 Misisipi", "🌊 Ebro"],
        "correcta": "🌊 Amazonas"
    },
    {
        "texto": "¿En qué año llegó el ser humano a la Luna por primera vez?",
        "opciones": ["1965", "1967", "1969", "1971"],
        "correcta": "1969"
    },
    {
        "texto": "¿Quién escribió Don Quijote de la Mancha?",
        "opciones": ["Garcilso de la vega", "Miguel de Cervantes", "Federico García Lorca", "Lope de Vega"],
        "correcta": "Miguel de Cervantes"
    },
    {
        "texto": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "opciones": ["1935", "1938", "1943", "1939"],
        "correcta": "1939"
    },
    {
        "texto": "¿Cuál es el elemento químico con símbolo ·Au·?",
        "opciones": ["Plata", "Argón", "Aluminio", "Oro"],
        "correcta": "Oro"
    },    
    {
        "texto": "¿Quién formuló la teoría de la relatividad?",
        "opciones": ["Albert Einstein", "Nikola Tesla", "Isaac Newton", "Galileo Galilei"],
        "correcta": "Albert Einstein"
    },
    {
        "texto": "¿Qué país tiene la mayor cantidad de islas en el mundo?",
        "opciones": ["Indonesia", "Suecia", "Noruega", "Filipinas"],
        "correcta": "Suecia"
    },    
    {
        "texto": "¿Cuál es la montaña más alta del mundo sobre el nivel del mar?",
        "opciones": ["Kangchenjunga", "K2", "Everest", "Teide"],
        "correcta": "Everest"
    },
    {
        "texto": "¿Qué científico propuso las tres leyes del movimiento en el siglo XVII?",
        "opciones": ["Isaac Newton", "Johannes Kepler", "Albert Einstein", "Nicolás Copérnico"],
        "correcta": "Isaac Newton"
    },    
    
    
]

# Configuración visual de la página
st.title("🎯🧠 ¡Trivia Test! ❓💡")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")
st.markdown("🍀✨ ¡Mucha suerte! 🎯🧠💡 Que tus respuestas sean perfectas 🏆🎉😃")

# FORMULARIO
with st.form("quiz_form"):
    respuestas_usuario = []

    for pregunta in preguntas:
        st.subheader(pregunta["texto"])
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")

# CORRECCIÓN
if boton_enviar:
    aciertos = 0
    total = len(preguntas)

    st.divider()
    st.header("📋 aqui estan tus resultados a tus preguntas:")

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1
            st.success(f"Pregunta {i+1}: ¡Correcta! ✅")
        else:
            st.error(f"Pregunta {i+1}: Incorrecta ❌. La respuesta correcta era {preguntas[i]['correcta']}")

    nota = (aciertos / total) * 10
    st.divider()
    st.header(f"Resultado final: {nota:.2f} / 10")

    # Mensajes según aciertos
    if aciertos > 5:
        st.success(f"🎉 ¡Felicidades! Has acertado {aciertos} preguntas. 🎈🎈🎈")
        st.balloons()
    elif aciertos == 5:
        st.warning(f"🌟 Has sacado 5 aciertos, ¡casi perfecto! 🌟")
    else:
        st.error(f"Has sacado {aciertos} aciertos. 📚 ¡Toca estudiar un poco más!")

