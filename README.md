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

Se utiliza la API de Gemini mediante `google-genai`. Esto se debe a que las tres funciones requieren comprender texto en lenguaje natural y producir respuestas adaptadas al contexto: ordenar tareas, redactar mensajes y extraer/organizar datos de citas.
Un punto a considerar es la disponibilidad de modelos, cuotas y modalidad gratuita de la API de Gemini.

Tecnologías

1) Python

2) Streamlit

3) Gemini API

4) Google Colab para desarrollo

5) Streamlit

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
    
    └── config.toml

¿Cómo se construyó?

El proyecto se definió a partir del problema de gestión de actividades cotidianas repetitivas de pequeños negocios. A partir de esta necesidad, se especificaron tres casos de uso con la finalidad de ayudar a los usuarios a reducir sus tiempos de gestión, revisión de pendientes, entre otros. 

Se desarrolló un prototipo utilizando Python y Streamlit, estructurado en cinco pestañas: Panel principal, Tareas y Prioridades, Mensajes, Citas y Recordatorios, y Usuarios y Accesos.

Se utilizaron algunas APIs permitiendo integrar algunos servicios de Google para la pestaña de Citas y Recordatorios. Además se utiliza la autenticación de OAuth 2.0 para poder conceder accesos al gmail.

Para las integraciones se utilizo el ambiente de GCP creando un proyecto independiente con el mismo nombre de la app. Habilitando las APIs desde la biblioteca, se configuro el consentimiento de OAuth (considerando un usuario externo y registrando la cuenta autorizada como usuario de prueba) y creación de las credenciales de OAuth. Se configuro la URL del despliegue de la app junto con la gestión del Client ID y Client Secret también incluidos en los secretos de Streamlit.

El desarrollo se realizó utilizando Google Colab como entorno de programación y experimentación. GitHub para almacenar el código fuente así como las versiones del mismo. Publicando mediante Streamlit Community Cloud. 

Ambientes

La aplicación contempla dos ambientes:

1) Development: para desarrollar, experimentar con instrucciones (prompts), depurar y probar cambios.

2) Production: para ejecutar una versión estable con mensajes de error adecuados para usuarios.

Cada ambiente tiene su propia clave API y configuración. El ambiente se selecciona mediante `APP_ENV`. La clave se obtiene de variables de entorno y de Streamlit Secrets.

Integración de Google Calendar y Gmail

Se contempló la integración con los servicios de Google para ampliar las capacidades de la pestaña de Citas y Recordatorios. Para ello se definió el uso de las siguientes APIs:

1) Google Calendar API: permitiendo crear y gestionar eventos en el calendario, incluyendo información como título, fecha, hora y descripción.

2) Gmail API: permitiendo preparar y enviar correos electrónicos desde una cuenta de Google autorizada.

La integración se planteó mediante OAuth 2.0, un mecanismo de autorización que permite al usuario conceder acceso a los servicios de Google sin compartir directamente su contraseña con la aplicación.

Durante la construcción se utilizó asistente de IA, el proceso se apoyó en tres archivos de referencia "AGENTS.md", "especificacion.md".


¿Qué puedes encontrar en la aplicación?

ImpulsaIA cuenta con cinco pestañas principales, diseñadas para facilitar la organización y gestión de las actividades cotidianas:

1) Panel principal: Página principal con el menú de navegación de las demás pestañas.

2) Tareas y Prioridades: Página que permite escribir una descripción de las actividades pendientes y, cuando se proporciona: información adicional, instrucción de considerar el tiempo disponible para realizarlas. Gemini analiza la información y propone una lista organizada de tareas, clasificadas según su prioridad, para facilitar la planificación del trabajo diario.

3) Mensajes: Página que ofrece un asistente para redactar comunicaciones dirigidas a clientes y proveedores. El usuario llena un formulario con: el destinatario, el objetivo del mensaje, el contexto y el tono deseado. Gemini genera un borrador que puede utilizarse como base para la comunicación.

4) Citas y recordatorios: Página que permite introducir información sobre una cita o actividad futura. Gemini interpreta los detalles y genera junto con la api de google calendar y gmail un correo de recordatorio además de agregar a google calendar el recordatorio o cita en el dia y horario seleccionado.

5) Usuarios y accesos: Página que presenta una demostración visual de los diferentes perfiles de usuario y sus respectivos niveles de acceso. Es una página con información dummy.


Configuración de ambientes

Para la configuración de los dos ambientes mencionados se realizará de la siguiente forma:

Define `APP_ENV` como `development` o `production`. De este modo en el archivo `config.py` buscará la configuración específica de ese ambiente.

Ejemplo de variables de entorno:
```
APP_ENV=development
GEMINI_API_KEY_DEVELOPMENT= clave_de_desarrollo
GEMINI_MODEL_DEVELOPMENT=gemini-3.8-flash
```

¿Qué sucede si Gemini falla?

La aplicación puede manejar estos casos:

1) Falta la clave API o no es válida.

2) Error de conexión o tiempo de espera.

3) Cuota o límite de solicitudes alcanzado.

4) Respuesta vacía o que no se puede interpretar.

5) Error inesperado del servicio.

En esos casos debe mostrarse un mensaje claro, evitar exponer credenciales o mensajes técnicos al usuario y permitir que vuelva a intentarlo. La aplicación no debe inventar una respuesta como si Gemini hubiera funcionado.

Pruebas

ID	Prueba	Resultado 

T01      Envio de un listado de tareas      R:Gemini devolvió tareas organizadas y prioridades comprensibles.

T02      Llenar el formulario de mensaje con destinatario, objetivo, contexto y tono en el formulario de la pestaña de Mensajes       R:Se obtiene un borrador coherente con los datos y el tono.

T03      Omitir objetivo o contexto del mensaje en el formulario de la pestaña de Mensajes      R: La app solicita completar los campos requeridos.

T04      Introducir detalles de una cita      R: Se envía un correo de recordatorio y se agrega al google calendar la cita con los detalles correctos.

Mejoras futuras

1) Historial de resultados.

2) Historial de conversaciones.

3) Integración de whatsapp para la pestaña de Mensajes.
