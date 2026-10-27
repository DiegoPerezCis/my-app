app_code = """import streamlit as st

# 1. Configurar la página de Streamlit
st.set_page_config(
    page_title="Asistente de Inteligencia Artificial para Negocios Locales",
    layout="centered"
)

# 2. Título principal y descripción
st.title("Asistente IA para Negocios Locales")
st.write(
    "Bienvenido al asistente inteligente diseñado para ayudar a propietarios y encargados "
    "de pequeños comercios, restaurantes y cafeterías a organizar sus tareas diarias, "
    "redactar mensajes personalizados y gestionar de forma eficiente sus citas y recordatorios."
)

# 3. Definición de pestañas
tab1, tab2, tab3 = st.tabs([
    "Tareas y prioridades", 
    "Mensajes para clientes y proveedores", 
    "Citas y recordatorios"
])

# --- PESTAÑA 1: Tareas y prioridades ---
with tab1:
    st.header("Organización de Tareas y Prioridades")
    st.write("Describe las actividades pendientes y la IA te ayudará a organizarlas y priorizarlas.")
    
    with st.form("tareas_form"):
        descripcion_tareas = st.text_area(
            "Describe tus tareas del día o de la semana:", 
            placeholder="Ej: Tengo que recibir el pedido de frutas, llamar al electricista para revisar la nevera y limpiar el mostrador antes de abrir."
        )
        submit_tareas = st.form_submit_button("Organizar Tareas")
        
        if submit_tareas:
            if not descripcion_tareas.strip():
                st.warning("Por favor, introduce una descripción de tus tareas antes de enviar.")
            else:
                st.info("Integración con Gemini pendiente. Aquí se mostrará tu lista organizada y priorizada.")

# --- PESTAÑA 2: Mensajes para clientes y proveedores ---
with tab2:
    st.header("Generador de Mensajes Personalizados")
    st.write("Redacta borradores profesionales de forma rápida para tus proveedores o clientes.")
    
    with st.form("mensajes_form"):
        destinatario = st.selectbox("Destinatario:", ["Cliente", "Proveedor"])
        objetivo = st.text_input("Objetivo del mensaje:", placeholder="Ej: Retraso en entrega, confirmar un pedido, responder una queja...")
        contexto = st.text_area("Información relevante y contexto:", placeholder="Ej: El pedido de harina no llegará hoy porque el camión se averió.")
        tono = st.selectbox("Tono del mensaje:", ["Formal y profesional", "Cercano y amable", "Urgente"])
        
        submit_mensajes = st.form_submit_button("Generar Borrador")
        
        if submit_mensajes:
            if not objetivo.strip() or not contexto.strip():
                st.warning("Por favor, completa el objetivo y el contexto del mensaje.")
            else:
                st.info("Integración con Gemini pendiente. Aquí se mostrará tu borrador sugerido.")

# --- PESTAÑA 3: Citas y recordatorios ---
with tab3:
    st.header("Preparación de Citas y Recordatorios")
    st.write("Estructura la información de tus citas y obtén textos claros para enviar como recordatorio.")
    
    with st.form("citas_form"):
        detalles_cita = st.text_area(
            "Detalles de la cita o actividad:",
            placeholder="Ej: El señor Gómez tiene una reserva para cenar el viernes a las 9 PM para 4 personas y quiere una mesa cerca de la ventana."
        )
        submit_citas = st.form_submit_button("Estructurar Cita")
        
        if submit_citas:
            if not detalles_cita.strip():
                st.warning("Por favor, introduce los detalles de la cita para poder procesarla.")
            else:
                st.info("Integración con Gemini pendiente. Aquí se mostrará el recordatorio estructurado.")
"""

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("Archivo app.py creado exitosamente con la interfaz estructurada.")
