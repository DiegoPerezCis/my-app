
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import re
import secrets
import time
from datetime import datetime, date, time as dt_time, timedelta
from email.mime.text import MIMEText
from urllib.parse import urlencode
from zoneinfo import ZoneInfo

import requests
import streamlit as st

from config import get_settings, create_gemini_client


# ============================================================
# 1. CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="ImpulsaIA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

APP_NAME = "ImpulsaIA"
TIMEZONE = ZoneInfo("America/Mexico_City")

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_CALENDAR_URL = (
    "https://www.googleapis.com/calendar/v3/calendars/primary/events"
)
GOOGLE_GMAIL_URL = (
    "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"
)

GOOGLE_SCOPES = [
    "https://www.googleapis.com/auth/calendar.events.owned",
    "https://www.googleapis.com/auth/gmail.send",
]


# ============================================================
# 2. ESTILOS
# ============================================================

st.markdown("""
<style>

/* =========================================
   FONDO Y TEXTO GENERAL
========================================= */

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #F5F7FB !important;
    color: #172554 !important;
}

/* Textos del panel principal */
[data-testid="stMain"] h1,
[data-testid="stMain"] h2,
[data-testid="stMain"] h3,
[data-testid="stMain"] h4,
[data-testid="stMain"] p,
[data-testid="stMain"] label,
[data-testid="stMain"] li,
[data-testid="stMain"] strong {
    color: #172554 !important;
}

/* =========================================
   BARRA LATERAL
========================================= */

[data-testid="stSidebar"] {
    background-color: #172554 !important;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* =========================================
   BOTONES
========================================= */

[data-testid="stMain"] .stButton > button,
[data-testid="stMain"] .stLinkButton > a,
[data-testid="stMain"] .stDownloadButton > button {
    background-color: #1D4ED8 !important;
    color: #FFFFFF !important;
    border: 1px solid #1D4ED8 !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
}

/* Asegurar que el texto interno también sea blanco */
[data-testid="stMain"] .stButton > button *,
[data-testid="stMain"] .stLinkButton > a *,
[data-testid="stMain"] .stDownloadButton > button * {
    color: #FFFFFF !important;
}

/* Estado al pasar el cursor */
[data-testid="stMain"] .stButton > button:hover,
[data-testid="stMain"] .stLinkButton > a:hover,
[data-testid="stMain"] .stDownloadButton > button:hover {
    background-color: #1E40AF !important;
    color: #FFFFFF !important;
    border-color: #1E40AF !important;
}

/* =========================================
   CAJAS DE TEXTO
========================================= */

[data-testid="stMain"] input,
[data-testid="stMain"] textarea,
[data-testid="stMain"] [data-baseweb="input"],
[data-testid="stMain"] [data-baseweb="textarea"] {
    background-color: #FFFFFF !important;
    color: #172554 !important;
    -webkit-text-fill-color: #172554 !important;
    border-color: #CBD5E1 !important;
}

/* Elementos internos de los campos */
[data-testid="stMain"] [data-baseweb="input"] input,
[data-testid="stMain"] [data-baseweb="textarea"] textarea {
    background-color: #FFFFFF !important;
    color: #172554 !important;
    -webkit-text-fill-color: #172554 !important;
    caret-color: #172554 !important;
}

/* Texto de ejemplo o placeholder */
[data-testid="stMain"] input::placeholder,
[data-testid="stMain"] textarea::placeholder {
    color: #94A3B8 !important;
    -webkit-text-fill-color: #94A3B8 !important;
    opacity: 1 !important;
}

/* =========================================
   LISTAS DESPLEGABLES Y SELECTORES
========================================= */

[data-testid="stMain"] [data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #172554 !important;
    border-color: #CBD5E1 !important;
}

[data-testid="stMain"] [data-baseweb="select"] * {
    color: #172554 !important;
}

/* Opciones de los desplegables */
[data-baseweb="popover"],
[data-baseweb="menu"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="menu"] *,
[data-baseweb="popover"] * {
    color: #172554 !important;
}

/* =========================================
   TARJETAS Y CONTENEDORES
========================================= */

.info-card {
    background-color: #FFFFFF !important;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #E2E8F0;
    min-height: 120px;
}

.info-card h3 {
    color: #64748B !important;
    font-size: 0.9rem;
    margin-bottom: 8px;
}

.info-card p {
    color: #172554 !important;
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0;
}

[data-testid="stMain"] [data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF !important;
    border-color: #E2E8F0 !important;
    border-radius: 14px !important;
}

/* =========================================
   TEXTOS SECUNDARIOS
========================================= */

[data-testid="stMain"] small,
[data-testid="stMain"] .stCaption {
    color: #64748B !important;
}

/* =========================================
   CASILLAS Y CONTROLES
========================================= */

[data-testid="stMain"] input[type="checkbox"] {
    accent-color: #1D4ED8;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 3. ESTADO DE LA APLICACIÓN
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Panel principal"

if "google_tokens" not in st.session_state:
    st.session_state.google_tokens = None

if "tasks_result" not in st.session_state:
    st.session_state.tasks_result = None

if "message_result" not in st.session_state:
    st.session_state.message_result = None

if "appointment_result" not in st.session_state:
    st.session_state.appointment_result = None


# ============================================================
# 4. CONFIGURACIÓN Y CONEXIÓN CON GEMINI
# ============================================================
def generate_gemini_response(prompt: str) -> str:
    """Envía una solicitud a Gemini con reintentos ante errores temporales."""

    import time

    client = create_gemini_client()
    settings = get_settings()

    primary_model = settings["gemini_model"]
    fallback_model = settings.get("gemini_fallback_model")

    def generate_with_retry(model: str) -> str:
        last_error = None

        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if not response.text:
                    raise RuntimeError(
                        "Gemini no devolvió una respuesta."
                    )

                return response.text.strip()

            except Exception as exc:
                last_error = exc

                error_code = getattr(exc, "code", None)
                error_message = str(exc).lower()

                temporary_error = (
                    error_code in (429, 500, 502, 503, 504)
                    or any(code in error_message for code in (
                        "429", "500", "502", "503", "504",
                        "unavailable", "resource_exhausted",
                        "high demand", "deadline exceeded"
                    ))
                )

                if not temporary_error:
                    raise

                if attempt < 2:
                    time.sleep(2 ** (attempt + 1))

        raise last_error

    try:
        return generate_with_retry(primary_model)

    except Exception as primary_error:

        if fallback_model and fallback_model != primary_model:
            try:
                return generate_with_retry(fallback_model)
            except Exception as fallback_error:
                raise RuntimeError(
                    "Gemini no está disponible temporalmente. "
                    "Intenta nuevamente más tarde."
                ) from fallback_error

        raise RuntimeError(
            "Gemini no está disponible temporalmente. "
            "Intenta nuevamente más tarde."
        ) from primary_error



def extract_json(text: str):
    """Intenta extraer JSON de una respuesta de Gemini."""

    cleaned = re.sub(r"```(?:json)?", "", text).replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}|\[.*\]", cleaned, re.DOTALL)

        if match:
            return json.loads(match.group())

        raise ValueError("No se pudo interpretar la respuesta de Gemini.")


# ============================================================
# 5. CONFIGURACIÓN OAUTH DE GOOGLE
# ============================================================

def get_google_oauth_settings():
    """Lee las credenciales OAuth desde Streamlit Secrets."""

    try:
        oauth = st.secrets["google_oauth"]

        return {
            "client_id": oauth["client_id"],
            "client_secret": oauth["client_secret"],
            "redirect_uri": oauth["redirect_uri"],
        }

    except Exception:
        raise RuntimeError(
            "No se encontró la configuración google_oauth "
            "en Streamlit Secrets."
        )


def create_signed_state():
    """Genera un estado OAuth firmado para validar el retorno de Google."""

    oauth = get_google_oauth_settings()

    payload = {
        "created": int(time.time()),
        "nonce": secrets.token_urlsafe(24)
    }

    encoded = base64.urlsafe_b64encode(
        json.dumps(payload).encode()
    ).decode().rstrip("=")

    signature = hmac.new(
        oauth["client_secret"].encode(),
        encoded.encode(),
        hashlib.sha256
    ).hexdigest()

    return f"{encoded}.{signature}"


def validate_oauth_state(state: str) -> bool:
    """Comprueba firma y antigüedad del estado OAuth."""

    try:
        oauth = get_google_oauth_settings()
        encoded, received_signature = state.split(".", 1)

        expected_signature = hmac.new(
            oauth["client_secret"].encode(),
            encoded.encode(),
            hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(
            received_signature,
            expected_signature
        ):
            return False

        padding = "=" * (-len(encoded) % 4)

        payload = json.loads(
            base64.urlsafe_b64decode(encoded + padding)
        )

        age = int(time.time()) - payload["created"]

        return 0 <= age <= 600

    except Exception:
        return False


def build_google_authorization_url():
    """Construye la URL para solicitar autorización a Google."""

    oauth = get_google_oauth_settings()
    state = create_signed_state()

    params = {
        "client_id": oauth["client_id"],
        "redirect_uri": oauth["redirect_uri"],
        "response_type": "code",
        "scope": " ".join(GOOGLE_SCOPES),
        "access_type": "offline",
        "prompt": "consent",
        "include_granted_scopes": "true",
        "state": state,
    }

    return f"{GOOGLE_AUTH_URL}?{urlencode(params)}"


def exchange_google_code(code: str):
    """Intercambia el código de autorización por tokens."""

    oauth = get_google_oauth_settings()

    response = requests.post(
        GOOGLE_TOKEN_URL,
        data={
            "code": code,
            "client_id": oauth["client_id"],
            "client_secret": oauth["client_secret"],
            "redirect_uri": oauth["redirect_uri"],
            "grant_type": "authorization_code",
        },
        timeout=30
    )

    response.raise_for_status()
    token_data = response.json()

    token_data["expires_at"] = (
        time.time() + token_data.get("expires_in", 3600)
    )

    st.session_state.google_tokens = token_data


def process_google_callback():
    """Procesa el retorno OAuth de Google."""

    params = st.query_params

    if "error" in params:
        error = params.get("error")
        st.query_params.clear()
        st.error(f"Google no autorizó la conexión: {error}")
        return

    code = params.get("code")
    state = params.get("state")

    if not code:
        return

    if not state or not validate_oauth_state(state):
        st.query_params.clear()
        st.error(
            "No se pudo validar la autorización de Google. "
            "Intenta conectar nuevamente."
        )
        return

    try:
        exchange_google_code(code)
        st.query_params.clear()
        st.success("¡Tu cuenta de Google está conectada!")
        st.rerun()

    except Exception as error:
        st.query_params.clear()
        st.error(f"No fue posible completar la conexión: {error}")


def get_google_access_token():
    """Obtiene o renueva el token de acceso."""

    tokens = st.session_state.google_tokens

    if not tokens:
        raise RuntimeError("Primero debes conectar tu cuenta de Google.")

    if time.time() < tokens.get("expires_at", 0) - 60:
        return tokens["access_token"]

    refresh_token = tokens.get("refresh_token")

    if not refresh_token:
        raise RuntimeError(
            "La sesión de Google expiró. Vuelve a conectar tu cuenta."
        )

    oauth = get_google_oauth_settings()

    response = requests.post(
        GOOGLE_TOKEN_URL,
        data={
            "client_id": oauth["client_id"],
            "client_secret": oauth["client_secret"],
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        },
        timeout=30
    )

    response.raise_for_status()
    new_tokens = response.json()

    tokens.update(new_tokens)
    tokens["expires_at"] = (
        time.time() + new_tokens.get("expires_in", 3600)
    )

    st.session_state.google_tokens = tokens

    return tokens["access_token"]


# Procesar retorno de Google antes de dibujar la interfaz.
process_google_callback()


# ============================================================
# 6. GOOGLE CALENDAR
# ============================================================

def create_calendar_event(
    title: str,
    description: str,
    email: str,
    start_datetime: datetime,
    duration_minutes: int
):
    """Crea un evento en Google Calendar e invita al destinatario."""

    access_token = get_google_access_token()

    end_datetime = start_datetime + timedelta(
        minutes=duration_minutes
    )

    event = {
        "summary": title,
        "description": description,
        "start": {
            "dateTime": start_datetime.isoformat(),
            "timeZone": "America/Mexico_City",
        },
        "end": {
            "dateTime": end_datetime.isoformat(),
            "timeZone": "America/Mexico_City",
        },
        "attendees": [
            {"email": email}
        ],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {
                    "method": "email",
                    "minutes": 30
                }
            ]
        }
    }

    response = requests.post(
        GOOGLE_CALENDAR_URL,
        params={"sendUpdates": "all"},
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        json=event,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


# ============================================================
# 7. GMAIL
# ============================================================

def send_gmail_message(
    recipient: str,
    subject: str,
    body: str
):
    """Envía un correo desde la cuenta Google autorizada."""

    access_token = get_google_access_token()

    message = MIMEText(body, "plain", "utf-8")
    message["to"] = recipient
    message["subject"] = subject

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    response = requests.post(
        GOOGLE_GMAIL_URL,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        json={"raw": encoded_message},
        timeout=30
    )

    response.raise_for_status()

    return response.json()


# ============================================================
# 8. BARRA LATERAL Y ROLES DEMOSTRATIVOS
# ============================================================

with st.sidebar:

    st.markdown("# 🚀 ImpulsaIA")
    st.caption("Tu negocio, mejor organizado.")

    st.divider()

    st.markdown("### Navegación")

    pages = [
        "Panel principal",
        "Tareas y prioridades",
        "Mensajes",
        "Citas y recordatorios",
        "Usuarios y accesos",
    ]

    selected_page = st.radio(
        "Menú",
        pages,
        index=pages.index(st.session_state.page),
        label_visibility="collapsed"
    )

    st.session_state.page = selected_page

    st.divider()

    st.markdown("### Perfil de demostración")

    selected_role = st.selectbox(
        "Seleccionar rol",
        [
            "Administrador",
            "Encargado",
            "Colaborador"
        ]
    )

    st.caption(
        "Los roles son demostrativos. "
        "No representan autenticación ni restricciones de seguridad."
    )

    st.divider()

    if st.session_state.google_tokens:
        st.success("Google conectado")

        if st.button("Desconectar Google", use_container_width=True):
            st.session_state.google_tokens = None
            st.rerun()

    else:
        st.warning("Google no conectado")

    st.caption("ImpulsaIA · Versión inicial")


# ============================================================
# 9. ENCABEZADO GENERAL
# ============================================================

def page_header(title: str, description: str):
    st.markdown(
        f'<div class="main-title">{title}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="subtitle">{description}</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 10. PANEL PRINCIPAL
# ============================================================

if st.session_state.page == "Panel principal":

    page_header(
        "Panel principal",
        "Bienvenido a ImpulsaIA. Organiza y administra tu negocio."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🤖 Inteligencia artificial</h3>
            <p>Gemini</p>
            <small>Asistencia para tu negocio</small>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>📅 Gestión de citas</h3>
            <p>Calendar</p>
            <small>Organización de eventos</small>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        status = (
            "Conectado"
            if st.session_state.google_tokens
            else "Pendiente"
        )

        st.markdown(f"""
        <div class="info-card">
            <h3>✉️ Correo electrónico</h3>
            <p>{status}</p>
            <small>Integración con Gmail</small>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Herramientas de tu negocio")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("📋 Tareas y prioridades")
            st.write(
                "Organiza tus actividades y descubre "
                "qué debes atender primero."
            )

            if st.button(
                "Ir a tareas",
                key="go_tasks",
                use_container_width=True
            ):
                st.session_state.page = "Tareas y prioridades"
                st.rerun()

        with st.container(border=True):
            st.subheader("📅 Citas y recordatorios")
            st.write(
                "Registra citas, crea eventos en Calendar "
                "y envía invitaciones."
            )

            if st.button(
                "Ir a citas",
                key="go_calendar",
                use_container_width=True
            ):
                st.session_state.page = "Citas y recordatorios"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.subheader("💬 Mensajes")
            st.write(
                "Genera mensajes profesionales y personalizados "
                "para clientes y proveedores."
            )

            if st.button(
                "Ir a mensajes",
                key="go_messages",
                use_container_width=True
            ):
                st.session_state.page = "Mensajes"
                st.rerun()

        with st.container(border=True):
            st.subheader("👥 Usuarios y accesos")
            st.write(
                "Consulta los roles disponibles "
                "en la demostración de ImpulsaIA."
            )

            if st.button(
                "Ver roles",
                key="go_roles",
                use_container_width=True
            ):
                st.session_state.page = "Usuarios y accesos"
                st.rerun()

    st.info(
        "Consejo: utiliza datos ficticios durante las pruebas "
        "y evita introducir información confidencial."
    )


# ============================================================
# 11. TAREAS Y PRIORIDADES
# ============================================================

elif st.session_state.page == "Tareas y prioridades":

    page_header(
        "Tareas y prioridades",
        "Gemini te ayuda a organizar el trabajo de tu negocio."
    )

    with st.form("tasks_form"):

        tasks_input = st.text_area(
            "Describe tus tareas pendientes:",
            height=180,
            placeholder=(
                "Ejemplo:\n"
                "- Recibir el pedido de frutas.\n"
                "- Revisar la nevera.\n"
                "- Limpiar el mostrador.\n"
                "- Llamar al proveedor."
            )
        )

        submit_tasks = st.form_submit_button(
            "✨ Organizar tareas con Gemini",
            use_container_width=True
        )

    if submit_tasks:

        if not tasks_input.strip():
            st.warning("Escribe al menos una tarea.")

        else:
            prompt = f"""
Eres un asistente especializado en organización de pequeños negocios.

Analiza la siguiente lista de tareas:

{tasks_input}

Clasifica cada tarea según su urgencia:
- Alta
- Media
- Baja

Estima el tiempo en minutos para completar cada tarea.
Ordena las tareas desde la más urgente hasta la menos urgente.

No inventes tareas que el usuario no haya mencionado.
Si falta información, realiza una estimación razonable.

Devuelve exclusivamente un JSON con esta estructura:

{{
  "resumen": "Resumen breve de la organización",
  "tareas": [
    {{
      "tarea": "Nombre de la tarea",
      "prioridad": "Alta",
      "tiempo_minutos": 30,
      "justificacion": "Motivo de la prioridad"
    }}
  ]
}}
"""

            try:
                with st.spinner("Gemini está organizando tus tareas..."):
                    result = generate_gemini_response(prompt)
                    st.session_state.tasks_result = extract_json(result)

            except Exception as error:
                st.error(f"No fue posible organizar las tareas: {error}")

    if st.session_state.tasks_result:

        result = st.session_state.tasks_result

        st.divider()
        st.subheader("Resultado de la organización")

        st.write(result.get("resumen", ""))

        tasks = result.get("tareas", [])

        if tasks:

            for task in tasks:

                priority = task.get("prioridad", "Media")

                if priority.lower() == "alta":
                    color = "🔴"
                elif priority.lower() == "media":
                    color = "🟡"
                else:
                    color = "🟢"

                with st.container(border=True):

                    st.markdown(
                        f"**{color} {task.get('tarea', 'Tarea')}**"
                    )

                    col1, col2 = st.columns(2)

                    col1.write(
                        f"Prioridad: **{priority}**"
                    )

                    col2.write(
                        f"Tiempo estimado: **{task.get('tiempo_minutos', 'N/D')} minutos**"
                    )

                    st.caption(
                        task.get("justificacion", "")
                    )

        else:
            st.warning("Gemini no devolvió tareas estructuradas.")


# ============================================================
# 12. MENSAJES PARA CLIENTES Y PROVEEDORES
# ============================================================

elif st.session_state.page == "Mensajes":

    page_header(
        "Mensajes para clientes y proveedores",
        "Genera borradores personalizados con inteligencia artificial."
    )

    with st.form("messages_form"):

        recipient_type = st.selectbox(
            "¿A quién va dirigido?",
            ["Cliente", "Proveedor"]
        )

        objective = st.text_input(
            "Objetivo del mensaje:",
            placeholder="Ej. Confirmar un pedido o responder una queja."
        )

        context = st.text_area(
            "Contexto e información relevante:",
            height=150,
            placeholder=(
                "Ej. El pedido de harina llegará mañana "
                "debido a un retraso en el transporte."
            )
        )

        tone = st.selectbox(
            "Tono del mensaje:",
            [
                "Formal y profesional",
                "Cercano y amable",
                "Urgente"
            ]
        )

        submit_message = st.form_submit_button(
            "✨ Generar borrador con Gemini",
            use_container_width=True
        )

    if submit_message:

        if not objective.strip() or not context.strip():
            st.warning("Completa el objetivo y el contexto.")

        else:

            prompt = f"""
Eres un asistente de comunicación para pequeños negocios.

Redacta un mensaje dirigido a un {recipient_type.lower()}.

Objetivo:
{objective}

Contexto:
{context}

Tono solicitado:
{tone}

Instrucciones:
- Redacta en español.
- Mantén un lenguaje natural y profesional.
- No inventes fechas, precios ni compromisos.
- No agregues información que no esté en el contexto.
- Devuelve únicamente el borrador del mensaje.
"""

            try:
                with st.spinner("Gemini está redactando tu mensaje..."):
                    st.session_state.message_result = (
                        generate_gemini_response(prompt)
                    )

            except Exception as error:
                st.error(f"No fue posible generar el mensaje: {error}")

    if st.session_state.message_result:

        st.divider()
        st.subheader("Borrador generado")

        st.text_area(
            "Puedes revisar y editar el texto:",
            value=st.session_state.message_result,
            height=220,
            key="editable_message"
        )

        st.caption(
            "El borrador no se envía automáticamente."
        )

        st.download_button(
            "Descargar borrador",
            data=st.session_state.editable_message,
            file_name="borrador_impulsaia.txt",
            mime="text/plain",
            use_container_width=True
        )


# ============================================================
# 13. CITAS Y RECORDATORIOS
# ============================================================

elif st.session_state.page == "Citas y recordatorios":

    page_header(
        "Citas y recordatorios",
        "Organiza tus citas y crea eventos en Google Calendar."
    )

    if not st.session_state.google_tokens:

        st.warning(
            "Primero debes conectar tu cuenta personal de Google "
            "para utilizar Gmail y Google Calendar."
        )

        try:
            auth_url = build_google_authorization_url()

            st.link_button(
                "🔗 Conectar mi cuenta de Google",
                auth_url,
                use_container_width=True
            )

        except Exception as error:
            st.error(f"No se pudo iniciar la conexión: {error}")

    else:

        st.success("Tu cuenta de Google está conectada.")

        with st.form("appointment_form"):

            client_name = st.text_input(
                "Nombre del cliente o contacto:",
                placeholder="Ej. Juan Gómez"
            )

            recipient_email = st.text_input(
                "Correo electrónico del destinatario:",
                placeholder="cliente@ejemplo.com"
            )

            appointment_details = st.text_area(
                "Descripción de la cita o recordatorio:",
                height=120,
                placeholder=(
                    "Ej. Reunión para confirmar el pedido "
                    "de la próxima semana."
                )
            )

            col1, col2 = st.columns(2)

            with col1:
                appointment_date = st.date_input(
                    "Fecha de la cita:",
                    value=date.today() + timedelta(days=1),
                    min_value=date.today()
                )

            with col2:
                appointment_time = st.time_input(
                    "Hora de la cita:",
                    value=dt_time(10, 0)
                )

            duration = st.selectbox(
                "Duración estimada:",
                [30, 45, 60, 90, 120],
                format_func=lambda x: f"{x} minutos",
                index=2
            )

            submit_appointment = st.form_submit_button(
                "📅 Estructurar y registrar cita",
                use_container_width=True
            )

        if submit_appointment:

            if not recipient_email.strip() or not appointment_details.strip():
                st.warning(
                    "Completa el correo electrónico y la descripción."
                )

            elif not re.fullmatch(
                r"[^@\s]+@[^@\s]+\.[^@\s]+",
                recipient_email.strip()
            ):
                st.warning("Introduce un correo electrónico válido.")

            else:

                start_datetime = datetime.combine(
                    appointment_date,
                    appointment_time,
                    tzinfo=TIMEZONE
                )

                if start_datetime <= datetime.now(TIMEZONE):
                    st.warning(
                        "Selecciona una fecha y hora futuras."
                    )

                else:

                    prompt = f"""
Eres un asistente de gestión de citas para pequeños negocios.

Organiza la siguiente cita:

Contacto: {client_name or "No especificado"}
Descripción: {appointment_details}
Fecha: {appointment_date.isoformat()}
Hora: {appointment_time.strftime("%H:%M")}

Devuelve exclusivamente un JSON con esta estructura:

{{
  "titulo": "Título breve y claro del evento",
  "descripcion": "Descripción organizada de la cita"
}}

No inventes datos que no se hayan proporcionado.
"""

                    try:

                        with st.spinner(
                            "Gemini está estructurando la cita..."
                        ):

                            ai_result = extract_json(
                                generate_gemini_response(prompt)
                            )

                        event_title = ai_result.get(
                            "titulo",
                            "Cita de negocio"
                        )

                        event_description = ai_result.get(
                            "descripcion",
                            appointment_details
                        )

                        with st.spinner(
                            "Registrando el evento en Google Calendar..."
                        ):

                            calendar_event = create_calendar_event(
                                title=event_title,
                                description=event_description,
                                email=recipient_email.strip(),
                                start_datetime=start_datetime,
                                duration_minutes=duration
                            )

                        st.session_state.appointment_result = {
                            "title": event_title,
                            "description": event_description,
                            "email": recipient_email.strip(),
                            "event_link": calendar_event.get("htmlLink", "")
                        }

                        st.success(
                            "La cita se creó correctamente en Google Calendar."
                        )

                        # Correo de confirmación inmediato.
                        email_body = f"""
Hola {client_name or ""},

Te compartimos la información de la cita:

{event_title}

Fecha: {appointment_date.strftime("%d/%m/%Y")}
Hora: {appointment_time.strftime("%H:%M")}
Duración: {duration} minutos

Detalles:
{event_description}

Se ha generado una invitación de Google Calendar.
Puedes consultar los detalles desde la invitación recibida.

Saludos,
ImpulsaIA
"""

                        try:
                            send_gmail_message(
                                recipient=recipient_email.strip(),
                                subject=f"Confirmación de cita: {event_title}",
                                body=email_body
                            )

                            st.success(
                                "También se envió un correo de confirmación."
                            )

                        except Exception as email_error:
                            st.warning(
                                "El evento fue creado, pero no se pudo "
                                f"enviar el correo de confirmación: {email_error}"
                            )

                    except Exception as error:
                        st.error(
                            f"No fue posible completar la cita: {error}"
                        )

        if st.session_state.appointment_result:

            result = st.session_state.appointment_result

            st.divider()
            st.subheader("Última cita registrada")

            st.write(f"**Evento:** {result['title']}")
            st.write(f"**Destinatario:** {result['email']}")
            st.write(f"**Descripción:** {result['description']}")

            if result.get("event_link"):
                st.link_button(
                    "Abrir evento en Google Calendar",
                    result["event_link"]
                )

            st.info(
                "El correo de confirmación se envía inmediatamente al "
                "registrar la cita. Calendar también envía una invitación "
                "al destinatario. El aviso de 30 minutos configurado en "
                "el evento corresponde al calendario del organizador; "
                "no garantiza un correo personalizado al invitado."
            )


# ============================================================
# 14. USUARIOS Y ACCESOS — DEMOSTRACIÓN VISUAL
# ============================================================

elif st.session_state.page == "Usuarios y accesos":

    page_header(
        "Usuarios y accesos",
        "Demostración de los perfiles que podría utilizar un negocio."
    )

    st.info(
        "Esta sección es una demostración visual. "
        "No existe todavía autenticación, registro de usuarios "
        "ni control real de permisos."
    )

    roles = [
        {
            "name": "Administrador",
            "icon": "👑",
            "description": (
                "Visualiza y administra todas las herramientas "
                "y configuraciones del negocio."
            ),
            "permissions": [
                "Panel principal",
                "Tareas y prioridades",
                "Mensajes",
                "Citas y recordatorios",
                "Usuarios y accesos",
                "Configuración"
            ]
        },
        {
            "name": "Encargado",
            "icon": "🧑‍💼",
            "description": (
                "Coordina las actividades diarias y la atención "
                "a clientes y proveedores."
            ),
            "permissions": [
                "Panel principal",
                "Tareas y prioridades",
                "Mensajes",
                "Citas y recordatorios"
            ]
        },
        {
            "name": "Colaborador",
            "icon": "👤",
            "description": (
                "Consulta y organiza las actividades operativas "
                "del negocio."
            ),
            "permissions": [
                "Panel principal",
                "Tareas y prioridades"
            ]
        }
    ]

    for role in roles:

        with st.container(border=True):

            st.subheader(f"{role['icon']} {role['name']}")
            st.write(role["description"])

            st.markdown("**Accesos propuestos:**")

            for permission in role["permissions"]:
                st.write(f"✓ {permission}")


# ============================================================
# 15. PIE DE PÁGINA
# ============================================================

st.divider()

st.caption(
    "ImpulsaIA · Asistente inteligente para pequeños negocios. "
    "Las estimaciones generadas por IA deben revisarse antes de utilizarlas."
)
