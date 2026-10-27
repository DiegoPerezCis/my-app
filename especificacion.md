# Especificación · Asistente IA para Negocios Locales

## 1. Problema y usuario

- **Quién tiene el problema:** Propietarios y encargados de pequeños comercios, restaurantes y cafeterías.
- **Cómo lo resuelve hoy:** Organizan sus tareas manualmente, redactan mensajes desde cero y anotan citas y recordatorios en agendas, notas u otras herramientas.
- **Qué le molesta de cómo lo hace hoy:** Dedican tiempo a actividades administrativas repetitivas, pueden perder de vista sus prioridades y necesitan cambiar entre distintas herramientas para organizar su trabajo.
- **Qué parte resuelve la IA:** Ayuda a estructurar tareas, establecer prioridades sugeridas y generar mensajes y recordatorios a partir de instrucciones en lenguaje natural. La organización y las decisiones finales siguen siendo responsabilidad del usuario.

## 2. Qué hace el producto

La aplicación tendrá una interfaz sencilla en español, organizada en tres pestañas principales:

1. **Tareas y prioridades:** recibe una descripción de las actividades pendientes y genera una lista organizada con prioridades sugeridas y próximos pasos.
2. **Mensajes para clientes y proveedores:** genera borradores personalizados a partir del destinatario, el objetivo del mensaje, el contexto y el tono deseado.
3. **Citas y recordatorios:** permite introducir los datos de una cita o actividad y genera un resumen estructurado con fecha, hora, motivo y texto sugerido para el recordatorio.

Las tres funcionalidades deben estar accesibles desde una misma aplicación Streamlit.

## 3. Entradas y salidas

| El usuario da… | La app devuelve… | Ejemplo |
|---|---|---|
| Una descripción de tareas pendientes | Una lista organizada por prioridad y próximos pasos | “Recibir mercancía, revisar inventario y preparar el pedido de mañana” |
| Destinatario, objetivo, contexto y tono | Un borrador de mensaje personalizado | Solicitar a un proveedor el precio y la disponibilidad de café en grano |
| Fecha, hora, motivo y detalles de una actividad | Un resumen de la cita y un recordatorio redactado | “Revisar el pedido con el proveedor el jueves a las 10:00” |

## 4. La pieza de IA

- **Opción elegida:** API de Gemini mediante el SDK oficial `google-genai`.
- **Por qué:** permite interpretar instrucciones en lenguaje natural y generar resultados diferentes según el contexto de cada tarea.
- **Instrucciones para el modelo (system prompt):**

  Eres un asistente práctico para propietarios y encargados de comercios locales, restaurantes y cafeterías. Responde siempre en español, con lenguaje claro, profesional y sencillo. Ayuda a organizar tareas, sugerir prioridades, redactar mensajes y estructurar citas y recordatorios. Adapta las respuestas al contexto proporcionado por el usuario. No inventes fechas, precios, cantidades, acuerdos ni datos que no se hayan proporcionado. Si falta información importante, pregunta o señala qué dato falta. Presenta los resultados de forma ordenada y fácil de utilizar. No afirmes que has enviado mensajes, creado eventos o guardado información si la aplicación no ha realizado realmente esas acciones.

- **Si falla:** muestra un mensaje comprensible, conserva los datos introducidos cuando sea posible y permite volver a intentarlo. No debe mostrar claves ni detalles técnicos sensibles.

## 5. Flujo del usuario

1. El usuario abre la aplicación y encuentra una descripción breve de sus funciones.
2. Selecciona la pestaña de tareas, mensajes o citas y recordatorios.
3. Introduce la información solicitada mediante campos sencillos.
4. Pulsa el botón para procesar la información.
5. La aplicación utiliza Gemini cuando corresponde y presenta un resultado estructurado.
6. El usuario revisa el resultado y puede copiarlo o modificar su solicitud.

## 6. Restricciones

- El desarrollo se realizará con Python desde Google Colab.
- La interfaz se construirá con Streamlit.
- La aplicación se desplegará gratuitamente en Streamlit Community Cloud.
- Se utilizará la capa gratuita disponible de Gemini, respetando sus límites.
- La clave de la API se guardará en los secretos de la plataforma, nunca en el código ni en el repositorio.
- No se utilizarán datos personales reales en las pruebas.
- La interfaz estará en español y se diseñará para personas sin conocimientos técnicos.
- La primera versión no enviará mensajes, no realizará compras ni creará eventos en calendarios externos.
- No se afirmará que las tareas o citas quedan guardadas permanentemente si esa funcionalidad no se ha implementado.
- Se evitarán funcionalidades innecesarias para mantener el proyecto viable en cuatro semanas.

## 7. Criterios de aceptación

| Entrada | Resultado esperado |
|---|---|
| Una lista de tareas con información suficiente | La app devuelve una lista organizada, con prioridades sugeridas y próximos pasos. |
| Una solicitud para escribir a un proveedor | La app genera un mensaje coherente, profesional y basado en los datos proporcionados. |
| Una cita con fecha, hora y motivo | La app presenta un resumen estructurado y un recordatorio redactado sin modificar los datos introducidos. |
| Un campo obligatorio vacío | La app solicita completar la información necesaria antes de procesarla. |
| Una instrucción ambigua | La app solicita aclaraciones o indica los supuestos que necesita confirmar. |
| Una petición fuera del propósito de la herramienta | La app explica amablemente sus funciones y orienta al usuario. |
| La API no responde o se agota la cuota | La app muestra un mensaje claro y permite reintentar sin exponer información sensible. |

## 8. Fuera de alcance (por ahora)

- Integración real con Google Calendar u otros calendarios.
- Envío automático de correos, mensajes de WhatsApp o pedidos a proveedores.
- Gestión de inventarios, ventas, facturación y pagos.
- Almacenamiento permanente de tareas, clientes y citas.
- Gestión de usuarios, permisos y múltiples negocios.
- Automatizaciones que se ejecuten en segundo plano.
- Paneles de indicadores y análisis de ventas.

Estas funcionalidades podrán evaluarse como mejoras futuras después de validar el prototipo.

## 9. Despliegue

- **Ruta:** A — Streamlit Community Cloud.
- **Entorno de desarrollo:** Google Colab con Python y asistencia de Gemini.
- **Archivos principales:** `app.py`, `requirements.txt`, `especificacion.md`, `AGENTS.md` y `README.md`.
- **Repositorio:** GitHub.
- **Gestión de secretos:** configuración de secretos de Streamlit Community Cloud.
- **Pruebas:** ejemplos ficticios de comercios, restaurantes y cafeterías.

## Plan de desarrollo

1. Crear la interfaz inicial con las tres pestañas y campos de entrada.
2. Implementar y probar el procesamiento de tareas y prioridades.
3. Implementar la generación de mensajes personalizados.
4. Implementar la preparación de citas y recordatorios.
5. Integrar la API de Gemini, gestionar errores y probar casos límite.
6. Desplegar, recopilar feedback y realizar al menos una mejora documentada.
