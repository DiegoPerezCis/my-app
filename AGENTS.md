## 1. Qué es este proyecto
Este proyecto consiste en desarrollar una aplicación web con inteligencia artificial generativa para ayudar a propietarios y encargados de comercios locales, restaurantes y cafeterías a organizar tareas, priorizar actividades, redactar mensajes personalizados para clientes y proveedores, y preparar citas y recordatorios.
El objetivo es reducir el tiempo dedicado a tareas administrativas repetitivas mediante una herramienta sencilla, práctica y accesible para personas sin conocimientos técnicos.
La aplicación forma parte de un reto académico de cuatro semanas del máster de Inteligencia Artificial y Machine Learning. Se debe priorizar un prototipo funcional, fácil de probar y desplegar, antes que una solución compleja.

## 2. Objetivos funcionales
La aplicación tendrá tres pestañas principales:
1. **Tareas y prioridades:** transformar las actividades descritas por el usuario en listas organizadas, con prioridades sugeridas y próximos pasos.
2. **Mensajes para clientes y proveedores:** generar borradores de mensajes personalizados según el destinatario, el objetivo, el contexto y el tono deseado.
3. **Citas y recordatorios:** estructurar la información de citas y actividades y generar textos de recordatorio a partir de los datos proporcionados.
Todas las funcionalidades deben estar disponibles desde una misma aplicación Streamlit.
No se deben incorporar funcionalidades adicionales sin valorar primero su utilidad, su viabilidad y su relación con el alcance del reto.

## 3. Cómo está construido
- Lenguaje de programación: Python.
- Entorno de desarrollo: Google Colab.
- Interfaz web: Streamlit.
- Modelo de IA: API de Gemini mediante el SDK oficial `google-genai`.
- Repositorio y control de versiones: GitHub.
- Plataforma de despliegue: Streamlit Community Cloud.
- Archivos principales:
  - `app.py`: interfaz, lógica y funcionalidades de la aplicación.
  - `requirements.txt`: dependencias necesarias.
  - `AGENTS.md`: contexto e instrucciones para el asistente de programación.
  - `especificacion.md`: descripción funcional y criterios de aceptación.
  - `README.md`: documentación, instrucciones de uso y resultados de las pruebas.
La especificación funcional es la referencia principal para decidir qué debe hacer la aplicación.

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
El objetivo es aprender a especificar, dirigir, revisar y validar el trabajo realizado con ayuda de la IA, no aceptar automáticamente todo el código generado.

## 5. Diseño de la interfaz
La aplicación debe cumplir los siguientes requisitos:
- Toda la interfaz estará en español.
- Utilizará un lenguaje claro, natural y profesional.
- Estará diseñada para personas sin conocimientos de programación.
- Tendrá un título, una descripción breve y una navegación sencilla.
- Utilizará pestañas para separar las tres funcionalidades principales.
- Cada pestaña tendrá campos de entrada claramente identificados y un botón para procesar la información.
- Los resultados deben mostrarse de forma ordenada, legible y fácil de reutilizar.
- Se deben mostrar instrucciones cuando el usuario no sepa qué información introducir.
- La interfaz debe funcionar en navegadores de escritorio y móviles.
Prioriza la claridad y la facilidad de uso frente a los elementos visuales innecesarios.

## 6. Integración con Gemini
La API de Gemini se utilizará para interpretar las solicitudes y generar contenido adaptado a cada funcionalidad.
### Comportamiento esperado
- En tareas y prioridades, organizar las actividades y sugerir prioridades razonables a partir de la información proporcionada.
- En mensajes, generar borradores adecuados al destinatario, al objetivo y al tono solicitado.
- En citas y recordatorios, estructurar los datos recibidos y redactar un recordatorio coherente sin alterar fechas u horas proporcionadas.

### Instrucciones para el modelo
El asistente integrado en la aplicación debe:
- Responder en español.
- Utilizar un tono profesional, amable y práctico.
- Adaptar sus respuestas al contexto de comercios locales, restaurantes y cafeterías.
- No inventar precios, fechas, cantidades, acuerdos ni información empresarial.
- Señalar los datos que falten y solicitar aclaraciones cuando sean necesarios.
- Presentar la información en un formato estructurado y fácil de entender.
- Diferenciar las sugerencias de los datos proporcionados por el usuario.
- No afirmar que ha enviado mensajes, realizado pedidos, creado eventos o guardado información si la aplicación no ha ejecutado realmente esas acciones.
Mantén las instrucciones del modelo separadas de la lógica de la interfaz para facilitar su mantenimiento.

## 7. Seguridad y gestión de secretos
La clave de la API de Gemini nunca debe incluirse directamente en el código fuente.
- En desarrollo local o en Google Colab, utiliza un mecanismo seguro de gestión de secretos o variables de entorno.
- En Streamlit Community Cloud, configura la clave en la sección **Settings → Secrets**.
- No escribas claves reales en `app.py`, `requirements.txt`, `README.md`, `AGENTS.md` ni en las consultas al asistente.
- No publiques archivos que contengan credenciales.
- No muestres claves ni información sensible en mensajes de error.
- Utiliza únicamente datos ficticios durante las pruebas del reto.
Si la clave no está configurada, muestra un mensaje claro que explique que falta la configuración necesaria.

## 8. Gestión de errores
Cada llamada a la API debe estar protegida mediante un manejo de excepciones adecuado.
La aplicación debe contemplar, como mínimo:
- Clave de API ausente o inválida.
- Cuota de uso agotada o límite de solicitudes alcanzado.
- Problemas de conexión.
- Respuesta vacía del modelo.
- Campos obligatorios sin completar.
- Instrucciones ambiguas o insuficientes.
Los mensajes de error deben ser comprensibles para el usuario y no incluir credenciales ni detalles técnicos sensibles.
Cuando sea posible, conserva la información introducida para evitar que el usuario tenga que escribirla de nuevo.
No simules respuestas de Gemini como si fueran resultados reales.

## 9. Restricciones del proyecto
- El desarrollo debe mantenerse dentro de un alcance viable para cuatro semanas.
- Se utilizarán las opciones gratuitas disponibles de las herramientas, respetando sus cuotas y condiciones.
- La aplicación debe poder desplegarse en Streamlit Community Cloud.
- No se utilizarán datos personales reales en las pruebas.
- No se implementarán integraciones externas sin una solicitud explícita.
- La aplicación no enviará automáticamente mensajes, correos ni pedidos.
- La aplicación no creará eventos en calendarios externos en la versión inicial.
- No se afirmará que la información queda almacenada permanentemente si no existe un mecanismo de persistencia implementado.
- Cualquier nueva funcionalidad debe respetar la especificación y los criterios de aceptación.

## 10. Cómo comprobar que funciona
Antes de considerar terminada una funcionalidad, comprueba los siguientes casos:
1. **Tareas:** al introducir varias actividades, la aplicación devuelve una lista organizada con prioridades sugeridas.
2. **Mensajes:** al introducir un destinatario, un objetivo y un contexto, la aplicación genera un borrador apropiado.
3. **Citas:** al introducir una fecha, una hora y un motivo, la aplicación devuelve un resumen y un recordatorio coherentes con los datos originales.
4. **Entrada vacía:** la aplicación solicita la información necesaria sin realizar llamadas innecesarias a la API.
5. **Entrada ambigua:** la aplicación solicita aclaraciones o identifica la información que falta.
6. **Error de API:** la aplicación muestra un mensaje claro sin interrumpirse de forma inesperada ni exponer secretos.
7. **Navegación:** las tres pestañas funcionan y los cambios en una funcionalidad no rompen las demás.
8. **Despliegue:** la aplicación arranca correctamente en Streamlit Community Cloud con las dependencias y los secretos configurados.
Registra los resultados de las pruebas y cualquier mejora realizada para documentarlos en el README y en la entrega final del reto.

## 11. Qué no hacer
- No reescribas toda la aplicación sin necesidad.
- No elimines funcionalidades que ya funcionan sin autorización.
- No cambies de Streamlit a otro framework.
- No cambies el proveedor de IA sin consultarlo.
- No añadas dependencias innecesarias.
- No inventes resultados de pruebas.
- No incorpores credenciales al repositorio.
- No afirmes que se ha enviado o guardado información cuando solo se ha generado un borrador.
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
