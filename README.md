ImpulsaIA

ImpulsaIA es un prototipo desarrollado con Python y Streamlit para ayudar a propietarios y encargados de pequeños comercios, restaurantes y cafeterías a organizar actividades cotidianas, cuenta con un asistente para ayudarlo a redactar mensajes de acuerdo a cierto modo de lenguaje y poder crear recordatorios o citas a través de google calendar y correo electronico.


Problema

Los pequeños negocios suelen gestionar tareas, comunicaciones y citas de manera manual. Esto puede consumir tiempo y dificultar el seguimiento de actividades importantes.


Usuario objetivo

Propietarios y encargados de pequeños comercios, restaurantes y cafeterías que necesitan herramientas sencillas para organizar su operación diaria y no necesariamente tienen conocimientos técnicos.

¿Qué hace la aplicación?

La aplicación contempla tres funcionalidades:

1) Tareas y prioridades: recibe una descripción de actividades pendientes y utiliza Gemini para proponer una lista organizada y priorizada.
   
2) Mensajes para clientes y proveedores: genera borradores a partir del destinatario, objetivo, contexto y tono solicitado.
   
3) Citas y recordatorios: interpreta los detalles proporcionados y devuelve la información estructurada y un texto de recordatorio.

Inteligencia artificial
Se utilizará la API de Gemini mediante el SDK oficial `google-genai`.
Se elige un modelo generativo porque las tres funciones requieren comprender texto en lenguaje natural y producir respuestas adaptadas al contexto: ordenar tareas, redactar mensajes y extraer/organizar datos de citas.
La disponibilidad de modelos, cuotas y modalidad gratuita depende de las condiciones vigentes de Google AI Studio / Gemini API; no se garantiza una cuota gratuita permanente.

Ambientes
ImpulsaIA contempla dos ambientes:
Development: para desarrollar, experimentar con instrucciones (prompts), depurar y probar cambios.
Production: para ejecutar una versión estable con mensajes de error adecuados para usuarios.
Cada ambiente puede tener su propia clave API y configuración. El ambiente se selecciona mediante `APP_ENV`. La clave se obtiene de variables de entorno o de Streamlit Secrets.

Tecnologías
Python
Streamlit
Google Gen AI SDK (`google-genai`)
Gemini API
Google Colab para desarrollo
Streamlit Community Cloud para despliegue

Estructura del proyecto
├── app.py
├── config.py
├── AGENTS.md
├── especificacion.md
├── README.md
├── prompts.md
├── requirements.txt
├── .gitignore
└── .streamlit/
    ├── config.toml
    └── secrets.toml.example

Cómo se construyó
El proyecto se definió a partir de un problema concreto de pequeños negocios. Se especificaron tres casos de uso y se creó un prototipo en Streamlit con tres pestañas y formularios. El desarrollo se realiza en Google Colab, con control de versiones en GitHub y despliegue en Streamlit Community Cloud.
La asistencia de Gemini durante el desarrollo se guía mediante `AGENTS.md` y `especificacion.md`. Los prompts relevantes se registran en `prompts.md`.

Configuración de ambientes
Define `APP_ENV` como `development` o `production`. `config.py` buscará la configuración específica de ese ambiente.
Ejemplo de variables de entorno:
```
APP_ENV=development
GEMINI_API_KEY_DEVELOPMENT=tu_clave_de_desarrollo
GEMINI_MODEL_DEVELOPMENT=gemini-2.5-flash
```

¿Qué sucede si Gemini falla?
La aplicación puede manejar estos casos:
Falta la clave API o no es válida.
Error de conexión o tiempo de espera.
Cuota o límite de solicitudes alcanzado.
Respuesta vacía o que no se puede interpretar.
Error inesperado del servicio.
En esos casos debe mostrarse un mensaje claro, evitar exponer credenciales o trazas técnicas al usuario final y permitir que vuelva a intentarlo. La información introducida debe conservarse cuando sea técnicamente posible. La aplicación no debe inventar una respuesta como si Gemini hubiera funcionado.

Pruebas
ID	Prueba	Resultado esperado
T01	Enviar un conjunto de tareas no vacío	Gemini devuelve tareas organizadas y prioridades comprensibles.
T02	Enviar formulario de tareas vacío	La app solicita completar la descripción y no llama a Gemini.
T03	Generar mensaje con destinatario, objetivo, contexto y tono	Se obtiene un borrador coherente con los datos y el tono.
T04	Omitir objetivo o contexto del mensaje	La app solicita completar los campos requeridos.
T05	Introducir detalles de una cita	Gemini devuelve datos estructurados y un recordatorio claro, sin inventar datos faltantes.
T06	Ejecutar sin clave API	Se muestra un aviso de configuración sin revelar secretos.

Limitaciones de la primera versión
No envía mensajes por WhatsApp, correo ni otros canales.
No sincroniza citas con Google Calendar.
No incluye base de datos persistente ni garantiza que la información sobreviva al reinicio de la sesión.
No incluye cuentas, roles ni gestión multiusuario.

Mejoras futuras
Historial de resultados.
Exportación de recordatorios y listas.
Mejoras de accesibilidad y experiencia de usuario.
Integraciones externas como google calendar, mail, whatsapp, etc.
