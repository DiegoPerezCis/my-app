## 1. Qué es este proyecto
Este proyecto consiste en desarrollar una aplicación web con inteligencia artificial generativa para ayudar a propietarios y encargados de comercios locales, restaurantes y cafeterías a organizar tareas, priorizar actividades, redactar mensajes personalizados para clientes y proveedores, y preparar citas y recordatorios.
El objetivo es reducir el tiempo dedicado a tareas administrativas repetitivas mediante una herramienta sencilla, práctica y accesible para personas sin conocimientos técnicos.

## 2. Objetivos funcionales
La aplicación cuenta con cinco pestañas principales:
1. **Panel principal:** página de inicio que presenta la aplicación y facilita la navegación entre sus funcionalidades.
2. **Tareas y prioridades:** transformar las actividades descritas por el usuario en listas organizadas, con prioridades sugeridas y próximos pasos.
3. **Mensajes:** generar borradores de mensajes personalizados según el destinatario, el objetivo, el contexto y el tono deseado.
4. **Citas y recordatorios:** interpretar los datos de una cita o actividad futura, estructurar la información y utilizar las APIs de Google Calendar y Gmail para registrar eventos y enviar correos de recordatorio.
5. **Usuarios y accesos:** mostrar una demostración visual de perfiles de usuario y sus respectivos niveles de acceso. Esta sección utiliza información dummy.

Gemini debe utilizarse para las tareas de interpretación y generación de contenido. Las acciones sobre Google Calendar y Gmail deben ejecutarse mediante sus respectivas APIs y después de contar con la autorización correspondiente.

No se deben incorporar funcionalidades adicionales sin valorar primero su utilidad, su viabilidad.

## 3. Cómo está construido
- Lenguaje de programación: Python.
- Entorno de desarrollo: Google Colab.
- Interfaz web: Streamlit.
- Modelo de IA: API de Gemini `google-genai`.
- Servicios de Google: Google Calendar API y Gmail API.
- Autorización de servicios de Google: OAuth 2.0.
- Plataforma de servicios en la nube: Google Cloud Platform (GCP).
- Repositorio y control de versiones: GitHub.
- Plataforma de despliegue: Streamlit Community Cloud.
- Archivos principales:
  - `app.py`: interfaz, lógica y funcionalidades de la aplicación.
  - `config.py`: configuración de los ambientes y parámetros de ejecución.
  - `requirements.txt`: dependencias necesarias.
  - `AGENTS.md`: contexto e instrucciones para el asistente de programación.
  - `especificacion.md`: descripción funcional y criterios de aceptación.
  - `README.md`: documentación, instrucciones de uso y resultados de las pruebas.

## 4. Cómo trabajar conmigo
El desarrollo se realizará de forma progresiva mediante consultas al asistente de Gemini integrado en Google Colab.
Sigue estas reglas:
- Trabaja una funcionalidad o un cambio cada vez.
- Lee y respeta la especificación antes de proponer modificaciones.
- Explica brevemente qué vas a cambiar y por qué.
- Cuando generes código, entrega el contenido completo de los archivos que deban crearse o modificarse, salvo que se solicite expresamente un fragmento.
- Indica en qué archivo debe colocarse cada cambio.
- No introduzcas funcionalidades que no se hayan solicitado.
- No reconstruyas toda la aplicación cuando un cambio pequeño sea suficiente.
- Mantén las funcionalidades que ya funcionan al incorporar nuevas.
- Si una instrucción es ambigua o una decisión afecta al alcance, pregunta antes de asumir.
- Si encuentras un error, identifica su causa probable y propón una corrección concreta.
- Después de cada cambio, indica cómo comprobar manualmente que funciona.
- Si añades una dependencia, actualiza `requirements.txt` y explica para qué sirve.
- No afirmes que una funcionalidad ha sido probada si no se ha ejecutado o comprobado.

## 5. Diseño de la interfaz
La aplicación debe cumplir los siguientes requisitos:
- Toda la interfaz estará en español.
- Utilizará un lenguaje claro, natural y profesional.
- Estará diseñada para personas sin conocimientos de programación.
- Tendrá un título, una descripción breve y una navegación sencilla.
- Utilizará pestañas para separar las tres funcionalidades principales.
- Contará con cinco pestañas: Panel principal, Tareas y Prioridades, Mensajes, Citas y Recordatorios, y Usuarios y Accesos.
- Cada funcionalidad tendrá campos de entrada claramente identificados y botones para ejecutar las acciones correspondientes.
- Los resultados deben mostrarse de forma ordenada, legible y fácil de reutilizar.
- Se deben mostrar instrucciones cuando el usuario no sepa qué información introducir.
- La pestaña de Citas y Recordatorios debe permitir utilizar las integraciones autorizadas de Google Calendar y Gmail.
- La pestaña Usuarios y Accesos es únicamente una demostración visual; no debe presentarse como un sistema de seguridad real.
- La interfaz debe funcionar en navegadores de escritorio y móviles.

## 6. Integración con Gemini
La API de Gemini se utilizará para interpretar las solicitudes y generar contenido adaptado a cada funcionalidad.
### Comportamiento esperado
- En tareas y prioridades, organizar las actividades y sugerir prioridades razonables a partir de la información proporcionada, considerando el tiempo disponible cuando se indique.
- En mensajes, generar borradores adecuados al destinatario, al objetivo, al contexto y al tono solicitado.
- En citas y recordatorios, interpretar y estructurar los datos recibidos, respetando las fechas y horas proporcionadas.
- La información estructurada por Gemini debe utilizarse para preparar las acciones correspondientes en Google Calendar y Gmail.
- Gemini no debe afirmar que una cita fue registrada o que un correo fue enviado. Estas acciones solo deben confirmarse cuando las APIs correspondientes hayan respondido satisfactoriamente.

### Instrucciones para el modelo
El asistente integrado en la aplicación debe:
- Responder en español.
- Utilizar un tono profesional, amable y práctico.
- Adaptar sus respuestas al contexto de comercios locales, restaurantes y cafeterías.
- Señalar los datos que falten y solicitar aclaraciones cuando sean necesarios.
- Presentar la información en un formato estructurado y fácil de entender.
- Diferenciar las sugerencias de los datos proporcionados por el usuario.
- No afirmar que ha enviado mensajes, realizado pedidos, creado eventos o guardado información si la aplicación no ha ejecutado realmente esas acciones.
Mantén las instrucciones del modelo separadas de la lógica de la interfaz para facilitar su mantenimiento.

## 7. Seguridad y gestión de secretos
Las credenciales de los servicios externos nunca deben incluirse directamente en el código fuente ni publicarse en GitHub.

1) Gemini API
La clave de Gemini debe obtenerse mediante variables de entorno o Streamlit Secrets.

No incluir claves reales en app.py, config.py, requirements.txt, README.md, AGENTS.md ni en las consultas al asistente.

2) Google Calendar y Gmail

Utilizar OAuth 2.0 para autorizar el acceso a la cuenta de Google.Gestionar de forma segura el Client ID y Client Secret de OAuth.

No solicitar ni almacenar directamente la contraseña de Google del usuario.

Solicitar únicamente los permisos necesarios para las operaciones de Calendar y Gmail.

No mostrar credenciales, tokens ni información sensible en pantalla o mensajes de error.

Gestión de ambientes

En desarrollo, utilizar las variables de entorno o mecanismos seguros de Google Colab.

En producción, configurar las credenciales y secretos correspondientes en Streamlit Community Cloud.

Si falta una credencial o autorización, mostrar un mensaje claro que indique qué configuración o permiso es necesario, sin exponer información sensible.

## 8. Gestión de errores
Cada llamada a la API debe estar protegida mediante un manejo de excepciones adecuado.
La aplicación debe contemplar, como mínimo:
- Clave de API ausente o inválida.
- Cuota de uso agotada o límite de solicitudes alcanzado.
- Problemas de conexión.
- Respuesta vacía del modelo.
- Campos obligatorios sin completar.
- Instrucciones ambiguas o insuficientes.
- Error de autorización OAuth 2.0 o permisos insuficientes.
- Token de acceso o actualización inválido, vencido o no disponible.
- Error de conexión con Google Calendar API o Gmail API.
- Cuota o límite de solicitudes alcanzado en los servicios de Google.
- Error al registrar un evento en Google Calendar.
- Error al enviar un correo mediante Gmail.
Los mensajes de error deben ser comprensibles para el usuario y no incluir credenciales ni detalles técnicos sensibles.
Cuando sea posible, conserva la información introducida para evitar que el usuario tenga que escribirla de nuevo.
No simules respuestas de Gemini como si fueran resultados reales.

## 9. Restricciones del proyecto
- Se utilizarán las opciones gratuitas disponibles de las herramientas, respetando sus cuotas y condiciones.
- La aplicación debe poder desplegarse en Streamlit Community Cloud.
- Cualquier nueva funcionalidad debe respetar la especificación y los criterios de aceptación.

## 10. Cómo comprobar que funciona
Antes de considerar terminada una funcionalidad, comprueba los siguientes casos:
1. **Navegación:** las cinco pestañas funcionan correctamente.
2. **Tareas:** al introducir varias actividades, la aplicación devuelve una lista organizada con prioridades sugeridas.
3. **Mensajes:** al introducir un destinatario, objetivo, contexto y tono, la aplicación genera un borrador apropiado.
4. **Entrada vacía:** la aplicación solicita la información necesaria sin realizar llamadas innecesarias a las APIs.
5. **Entrada ambigua:** la aplicación solicita aclaraciones o identifica la información que falta.
6. **Citas:** al introducir los detalles de una cita, Gemini estructura la información y prepara el recordatorio.
7. **Google Calendar:** comprobar que el evento se registra correctamente en el calendario autorizado, con el título, fecha, hora y descripción correspondientes.
8. **Gmail:** comprobar que el correo de recordatorio se envía correctamente desde la cuenta autorizada.
9. **Autorización:** comprobar el comportamiento cuando no se ha concedido autorización o faltan permisos.
10. **Error de API:** comprobar que los errores de Gemini, Google Calendar o Gmail muestran mensajes claros sin exponer secretos.
11. **Usuarios y accesos:** comprobar que se muestran correctamente los perfiles y niveles de acceso de ejemplo.
12. **Despliegue:** la aplicación arranca correctamente en Streamlit Community Cloud con las dependencias y los secretos configurados.
Registra los resultados de las pruebas y cualquier mejora realizada para documentarlos en el README y en la entrega final del reto.

## 11. Qué no hacer
- No reescribas toda la aplicación sin necesidad.
- No elimines funcionalidades que ya funcionan sin autorización.
- No cambies de Streamlit a otro framework.
- No cambies el proveedor de IA sin consultarlo.
- No añadas dependencias innecesarias.
- No inventes resultados de pruebas.
- No incorpores credenciales ni tokens al repositorio.
- No expongas información sensible en pantalla ni en mensajes de error.
- No afirmes que se ha enviado un correo o registrado un evento cuando la API correspondiente no haya confirmado la operación.
- No elimines ni modifiques las integraciones funcionales de Google Calendar y Gmail sin autorización.
- No presentes la demostración de Usuarios y Accesos como un sistema real de autenticación.
- No realices cambios en GitHub ni despliegues versiones nuevas sin que el usuario haya revisado el resultado.

## 12. Prioridad de las decisiones
Cuando existan dudas o conflictos, sigue este orden:
1. Cumplir los requisitos académicos del reto.
2. Respetar `especificacion.md`.
3. Mantener la aplicación funcional y segura.
4. Priorizar una experiencia sencilla para el usuario.
5. Evitar complejidad y funcionalidades innecesarias.
6. Documentar los cambios, las pruebas y las limitaciones.

El resultado esperado es un prototipo funcional, publicado y probado, cuyo proceso de desarrollo pueda explicarse y documentarse de forma transparente.
