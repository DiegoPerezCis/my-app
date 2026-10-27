import streamlit as st

st.title("Convertidor de Texto a Mayúsculas")

# Caja de texto para la entrada del usuario
texto_entrada = st.text_input("Escribe tu texto aquí:", "")

# Procesar el texto si no está vacío
texto_procesado = texto_entrada.upper()

# Caja de texto (deshabilitada para simular salida) para mostrar el resultado
st.text_input("Texto en mayúsculas (Resultado):", value=texto_procesado, disabled=True)
