# Especificación · Asistente IA para Negocios Locales

## 1. Problema y usuario

- **Quién tiene el problema:** Propietarios y encargados de pequeños comercios, restaurantes y cafeterías.
- **Cómo lo resuelve hoy:** Organizan sus tareas manualmente, redactan mensajes desde cero y anotan citas y recordatorios en agendas, notas u otras herramientas.
- **Qué le molesta de cómo lo hace hoy:** Dedican tiempo a actividades administrativas repetitivas, pueden perder de vista sus prioridades y necesitan cambiar entre distintas herramientas para organizar su trabajo.
- **Qué parte resuelve la IA:** Ayuda a estructurar tareas, establecer prioridades sugeridas y generar mensajes y recordatorios a partir de instrucciones en lenguaje natural. La organización y las decisiones finales siguen siendo responsabilidad del usuario.

## 2. Qué hace el producto

La aplicación tendrá una interfaz sencilla en español, organizada en cinco pestañas principales:

1. **Panel principal:** presenta la aplicación y facilita la navegación entre sus funcionalidades.
2. **Tareas y prioridades:** recibe una descripción de las actividades pendientes y genera una lista organizada con prioridades sugeridas y próximos pasos.
3. **Mensajes para clientes y proveedores:** genera borradores personalizados a partir del destinatario, el objetivo del mensaje, el contexto y el tono deseado.
4. **Citas y recordatorios:** permite introducir los datos de una cita o actividad, genera un resumen estructurado y utiliza las APIs de Google Calendar y Gmail para registrar el evento y enviar un correo electrónico de recordatorio.
5. **Usuarios y accesos:** presenta una demostración visual de diferentes perfiles de usuario y sus respectivos niveles de acceso. Utiliza información


## 3. Entradas y salidas

| El usuario da… | La app devuelve… | Ejemplo |
|---|---|---|
| Una descripción de tareas pendientes y, opcionalmente, tiempo disponible | Una lista organizada por prioridad y próximos pasos | “Recibir mercancía, revisar inventario y preparar el pedido de mañana” |
| Destinatario, objetivo, contexto y tono | Un borrador de mensaje personalizado | Solicitar a un proveedor el precio y la disponibilidad de café en grano |
| Fecha, hora, motivo y detalles de una actividad | Un resumen estructurado, registro del evento en Google Calendar y envío de un correo de recordatorio mediante Gmail | “Revisar el pedido con el proveedor el jueves a las 10:00” |

## 4. La pieza de IA

- **Opción elegida:** API de Gemini mediante el SDK oficial `google-genai`.
- **Por qué:** permite interpretar instrucciones en lenguaje natural y generar resultados diferentes según el contexto de cada tarea.
- **Instrucciones para el modelo (system prompt):**

  Eres un asistente práctico para propietarios y encargados de comercios locales, restaurantes y cafeterías. Responde siempre en español, con lenguaje claro, profesional y sencillo. Ayuda a organizar tareas, sugerir prioridades, redactar mensajes y estructurar citas y recordatorios. Adapta las respuestas al contexto proporcionado por el usuario. No inventes fechas, precios, cantidades, acuerdos ni datos que no se hayan proporcionado. Si falta información importante, pregunta o señala qué dato falta. Presenta los resultados de forma ordenada y fácil de utilizar. En las solicitudes de citas, conserva exactamente las fechas, horas y detalles proporcionados para que la aplicación pueda utilizarlos en las integraciones con Google Calendar y Gmail. No afirmes que has enviado correos, creado eventos o guardado información si la aplicación no ha confirmado que esas acciones se realizaron correctamente.
  
- **Si falla:** muestra un mensaje comprensible, conserva los datos introducidos cuando sea posible y permite volver a intentarlo. No debe mostrar claves ni detalles técnicos sensibles.

## 5. Flujo del usuario

1. El usuario abre la aplicación y encuentra el panel principal con una descripción de sus funciones.
2. Selecciona la pestaña correspondiente a la actividad que desea realizar.
3. Introduce la información solicitada mediante campos sencillos.
4. Pulsa el botón para procesar la información.
5. La aplicación utiliza Gemini cuando corresponde para interpretar los datos y generar un resultado estructurado.
6. En la funcionalidad de citas y recordatorios, la aplicación utiliza Google Calendar API para registrar el evento y Gmail API para enviar el correo de recordatorio, utilizando la cuenta autorizada.
7. El usuario puede revisar los resultados y comprobar las acciones realizadas.
8. En la pestaña Usuarios y Accesos puede consultar la demostración visual de los perfiles disponibles.


## 6. Restricciones

- El desarrollo se realizará con Python desde Google Colab.
- La interfaz se construirá con Streamlit.
- La aplicación se desplegará gratuitamente en Streamlit Community Cloud.
- Se utilizará la API de Gemini mediante google-genai, respetando las cuotas y condiciones del servicio.
- Se utilizarán Google Calendar API y Gmail API para las funcionalidades de citas, registro de eventos y envío de correos.
- La autorización para acceder a los servicios de Google se realizará mediante OAuth 2.0.
- Las credenciales y secretos se gestionarán se guardará en los secretos de la plataforma, nunca en el código ni en el repositorio.
- No se utilizarán datos personales reales en las pruebas.
- La interfaz estará en español y se diseñará para personas sin conocimientos técnicos.
- La pestaña Usuarios y Accesos es una demostración visual y no representa un sistema real de autenticación, autorización o gestión de usuarios.
- No se afirmará que las tareas, mensajes o citas quedan almacenados permanentemente si no existe un mecanismo de persistencia implementado.

## 7. Criterios de aceptación
## 7. Criterios de aceptación

| Entrada o acción | Resultado esperado |
|---|---|
| Acceder a la aplicación | La app muestra el panel principal y permite navegar por las cinco pestañas. |
| Una lista de tareas con información suficiente | La app devuelve una lista organizada, con prioridades sugeridas y próximos pasos. |
| Una solicitud para escribir a un proveedor | La app genera un mensaje coherente, profesional y basado en los datos proporcionados. |
| Una cita con fecha, hora y motivo | La app presenta un resumen estructurado y utiliza los datos para registrar el evento en Google Calendar y enviar un correo mediante Gmail. |
| Una autorización de Google válida | La aplicación puede utilizar los servicios autorizados de Calendar y Gmail. |
| Falta de autorización o permisos insuficientes | La app informa al usuario que debe autorizar el acceso correspondiente. |
| Un campo obligatorio vacío | La app solicita completar la información necesaria antes de procesarla. |
| Una instrucción ambigua | La app solicita aclaraciones o indica la información que falta. |
| Una petición fuera del propósito de la herramienta | La app explica amablemente sus funciones y orienta al usuario. |
| La API de Gemini o alguno de los servicios de Google no responde | La app muestra un mensaje claro y no confirma acciones que no se hayan completado. |
| Consulta de Usuarios y Accesos | La app muestra los perfiles y niveles de acceso de ejemplo. |


## 8. Fuera de alcance (por ahora)

- Integración con WhatsApp para enviar mensajes.
- Gestión de inventarios, ventas, facturación y pagos.
- Almacenamiento permanente de tareas, clientes, mensajes y citas.
- Autenticación real de usuarios, gestión de permisos y administración de múltiples negocios.
- Automatizaciones que se ejecuten en segundo plano.
- Paneles de indicadores y análisis de ventas.
- Integración con otros calendarios o servicios de correo diferentes de Google Calendar y Gmail.
Estas funcionalidades podrán evaluarse como mejoras futuras después de validar el prototipo.

## 9. Despliegue

- **Ruta:** A — Streamlit Community Cloud.
- **Entorno de desarrollo:** Google Colab con Python y asistencia de Gemini.
- **Modelo de IA:** Gemini.
- **Servicios externos:** Google Calendar API y Gmail API.
- **Autorización:** OAuth 2.0 mediante credenciales configuradas en Google Cloud Platform.
- **Proyecto de GCP:** ImpulsaIA.
- **Archivos principales:** `app.py`, `requirements.txt`, `especificacion.md`, `AGENTS.md` y `README.md`.
- **Repositorio:** GitHub.
- **Gestión de secretos:** configuración de secretos de Streamlit Community Cloud.
- **Ambientes:** Development y Production, con sus respectivas configuraciones.
