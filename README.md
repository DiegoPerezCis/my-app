ImpulsaIA
Asistente de inteligencia artificial para negocios locales.
ImpulsaIA es un prototipo desarrollado con Python y Streamlit para ayudar a propietarios y encargados de pequeños comercios, restaurantes y cafeterías a organizar actividades cotidianas y preparar comunicaciones.
> **Estado del proyecto:** prototipo de interfaz existente. La integración de Gemini en las tres funcionalidades está planificada para la siguiente etapa y debe validarse mediante pruebas antes de considerarse terminada.
Problema
Los pequeños negocios suelen gestionar tareas, comunicaciones y citas de manera manual y dispersa. Esto puede consumir tiempo y dificultar el seguimiento de actividades importantes.
Usuario objetivo
Propietarios y encargados de pequeños comercios, restaurantes y cafeterías que necesitan herramientas sencillas para organizar su operación diaria y no necesariamente tienen conocimientos técnicos.
¿Qué hace la aplicación?
La primera versión contempla tres funcionalidades:
Tareas y prioridades: recibe una descripción de actividades pendientes y utiliza Gemini para proponer una lista organizada y priorizada.
Mensajes para clientes y proveedores: genera borradores a partir del destinatario, objetivo, contexto y tono solicitado.
Citas y recordatorios: interpreta los detalles proporcionados y devuelve la información estructurada y un texto de recordatorio.
La aplicación genera sugerencias y borradores. No realiza envíos ni sincronizaciones externas.
Inteligencia artificial
Se utilizará la API de Gemini mediante el SDK oficial `google-genai`.
Se elige un modelo generativo porque las tres funciones requieren comprender texto en lenguaje natural y producir respuestas adaptadas al contexto: ordenar tareas, redactar mensajes y extraer/organizar datos de citas.
El modelo se configura mediante `GEMINI_MODEL`, de modo que pueda cambiarse sin modificar la lógica de la interfaz. La disponibilidad de modelos, cuotas y modalidad gratuita depende de las condiciones vigentes de Google AI Studio / Gemini API; no se garantiza una cuota gratuita permanente.
Ambientes
ImpulsaIA contempla dos ambientes:
Development: para desarrollar, experimentar con instrucciones (prompts), depurar y probar cambios.
Production: para ejecutar una versión estable con mensajes de error adecuados para usuarios.
Cada ambiente puede tener su propia clave API y configuración. El ambiente se selecciona mediante `APP_ENV`. La clave se obtiene de variables de entorno o de Streamlit Secrets; nunca debe escribirse en el código ni publicarse en GitHub.
Tecnologías
Python
Streamlit
Google Gen AI SDK (`google-genai`)
Gemini API
GitHub
Google Colab para desarrollo
Streamlit Community Cloud para despliegue
Estructura del proyecto
```text
.
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
```
`app.py` es la interfaz Streamlit existente. En esta etapa no se modifica; la integración se realizará después de revisar y aprobar la documentación y `config.py`.
Cómo se construyó
El proyecto se definió a partir de un problema concreto de pequeños negocios. Se especificaron tres casos de uso y se creó un prototipo en Streamlit con tres pestañas y formularios. El desarrollo se realiza en Google Colab, con control de versiones en GitHub y despliegue en Streamlit Community Cloud.
La asistencia de Gemini durante el desarrollo se guía mediante `AGENTS.md` y `especificacion.md`. Los prompts relevantes se registran en `prompts.md`.
Instalación local
Clona o descarga el repositorio.
Crea un entorno virtual e instala dependencias:
```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
Configura `APP_ENV` y la clave correspondiente. Puedes utilizar variables de entorno o copiar `.streamlit/secrets.toml.example` a `.streamlit/secrets.toml` y completar los valores localmente.
Ejecuta:
```bash
   streamlit run app.py
   ```
No subas `.streamlit/secrets.toml` al repositorio.
Configuración de ambientes
Define `APP_ENV` como `development` o `production`. `config.py` buscará la configuración específica de ese ambiente.
Ejemplo de variables de entorno:
```text
APP_ENV=development
GEMINI_API_KEY_DEVELOPMENT=tu_clave_de_desarrollo
GEMINI_MODEL_DEVELOPMENT=gemini-2.5-flash
```
Para producción utiliza `GEMINI_API_KEY_PRODUCTION` y, si se requiere, `GEMINI_MODEL_PRODUCTION`. Los nombres de modelo son configurables y deben verificarse en la documentación vigente de Gemini antes del despliegue.
En Streamlit Community Cloud, configura los secretos desde la sección Settings → Secrets de la aplicación. No incluyas claves reales en archivos de ejemplo.
¿Qué sucede si Gemini falla?
La aplicación debe manejar, como mínimo, estos casos:
Falta la clave API o no es válida.
Error de conexión o tiempo de espera.
Cuota o límite de solicitudes alcanzado.
Respuesta vacía o que no se puede interpretar.
Error inesperado del servicio.
En esos casos debe mostrarse un mensaje claro, evitar exponer credenciales o trazas técnicas al usuario final y permitir que vuelva a intentarlo. La información introducida debe conservarse cuando sea técnicamente posible. La aplicación no debe inventar una respuesta como si Gemini hubiera funcionado.
Pruebas
Estado inicial: las pruebas de integración de Gemini están pendientes. No se deben presentar como realizadas hasta ejecutarlas y registrar sus resultados.
Plan mínimo de pruebas:
ID	Prueba	Resultado esperado
T01	Enviar un conjunto de tareas no vacío	Gemini devuelve tareas organizadas y prioridades comprensibles.
T02	Enviar formulario de tareas vacío	La app solicita completar la descripción y no llama a Gemini.
T03	Generar mensaje con destinatario, objetivo, contexto y tono	Se obtiene un borrador coherente con los datos y el tono.
T04	Omitir objetivo o contexto del mensaje	La app solicita completar los campos requeridos.
T05	Introducir detalles de una cita	Gemini devuelve datos estructurados y un recordatorio claro, sin inventar datos faltantes.
T06	Ejecutar sin clave API	Se muestra un aviso de configuración sin revelar secretos.
T07	Simular error o límite de Gemini	Se muestra un mensaje controlado y la app sigue disponible.
T08	Cambiar `APP_ENV`	Se selecciona la configuración correspondiente al ambiente.
Los resultados, fecha, ambiente y observaciones deben añadirse a esta sección después de ejecutar las pruebas.
Limitaciones de la primera versión
No envía mensajes por WhatsApp, correo ni otros canales.
No sincroniza citas con Google Calendar.
No incluye base de datos persistente ni garantiza que la información sobreviva al reinicio de la sesión.
No gestiona inventario, ventas, pagos ni facturación.
No incluye cuentas, roles ni gestión multiusuario.
Las respuestas de IA pueden contener errores; el usuario debe revisarlas antes de utilizarlas.
Mejoras futuras
Persistencia segura de tareas y citas.
Historial de resultados.
Exportación de recordatorios y listas.
Pruebas automatizadas y evaluación sistemática de prompts.
Mejoras de accesibilidad y experiencia de usuario.
Integraciones externas, únicamente si se incorporan como alcance aprobado.
Seguridad y privacidad
Utiliza datos ficticios durante las pruebas. No introduzcas información personal, financiera o confidencial de clientes o proveedores. Protege las claves API mediante secretos y limita los datos enviados al modelo a lo estrictamente necesario.
