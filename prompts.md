# Prompts utilizados durante el desarrollo de ImpulsaIA

## 1. El plan, antes de escribir código

**Prompt**

> Antes de comenzar el desarrollo, lee `AGENTS.md` y
> `especificacion.md`. Resume las reglas principales, el problema que
> resolverá la aplicación, el usuario objetivo, las funcionalidades, las
> restricciones técnicas y las pruebas necesarias. Identifica los
> archivos que debemos crear y propón un plan de desarrollo por etapas.
> No escribas código todavía y señala cualquier duda que encuentres en
> la documentación.

**Objetivo**

Asegurar que la IA comprendiera el alcance del proyecto antes de generar
código. Esta etapa permitió establecer una base de trabajo y evitar
agregar funcionalidades que no estuvieran contempladas.

**Decisión y revisión**

Se utilizaron los documentos de contexto como referencia para definir
qué debía incluir la primera versión y qué elementos quedaban fuera de
su alcance.

------------------------------------------------------------------------

## 2. La corrección del plan y la arquitectura

**Prompt**

> Con base en la especificación, quiero desarrollar ImpulsaIA con Python
> y Streamlit. Antes de modificar `app.py`, define la arquitectura y
> revisa la configuración necesaria. Considera dos ambientes,
> Development y Production, la integración de Gemini en las
> funcionalidades principales y el manejo seguro de las claves mediante
> secretos. Mantén separadas la configuración y la lógica de la
> aplicación. Presenta los archivos que necesitamos actualizar y explica
> cómo se relacionan.

**Objetivo**

Ajustar la propuesta inicial y establecer una estructura que permitiera
ampliar la aplicación sin concentrar toda la configuración y lógica en
un solo archivo.

**Decisión y revisión**

Se revisó la organización de los archivos y se mantuvo la separación
entre configuración y aplicación. También se definió el uso de secretos
para proteger las credenciales y distinguir los ambientes de desarrollo
y producción.

------------------------------------------------------------------------

## 3. La construcción de la aplicación

**Prompt**

> Desarrolla la aplicación ImpulsaIA utilizando Python y Streamlit,
> respetando `AGENTS.md` y `especificacion.md`. Implementa las
> funcionalidades de tareas y prioridades, generación de mensajes y
> citas y recordatorios. Integra Gemini mediante `google-genai` y
> utiliza los archivos de configuración para seleccionar el ambiente y
> recuperar las credenciales desde los secretos. Mantén la interfaz en
> español, valida los campos obligatorios y muestra mensajes claros
> cuando ocurra un error. No incluyas claves API directamente en el
> código.

**Objetivo**

Pasar a una interfaz inicial de una aplicación y una estructura preparada para su despliegue.

**Decisión y revisión**

Se revisó que las funcionalidades correspondieran con las necesidades
definidas en la especificación.

------------------------------------------------------------------------

## 4. La integración de Google y la mejora de la interfaz

**Prompt**

> Amplía ImpulsaIA para integrar Google Calendar y Gmail mediante OAuth
> 2.0, de modo que el usuario pueda autorizar su cuenta, crear eventos y
> enviar correos electrónicos relacionados con sus citas. Además,
> reorganiza la interfaz con una barra de navegación lateral y cinco
> secciones: Panel principal, Tareas y Prioridades, Mensajes, Citas y
> Recordatorios, y Usuarios y Accesos. La última sección debe ser una
> demostración visual de roles y permisos, no un sistema de
> autenticación real. Mantén la experiencia sencilla y consistente.

**Objetivo**

Incorporar servicios externos y ampliar la interfaz para que la
aplicación ofreciera una experiencia más completa.

**Decisión y revisión**

Se buscó que Calendar y Gmail debían operar con autorización del
usuario mediante OAuth 2.0. También se delimitó que la sección de
Usuarios y Accesos sería únicamente demostrativa, sin implementar
autenticación ni administración real de usuarios.

------------------------------------------------------------------------

## 5. Las correcciones y la revisión antes de publicar

**Prompt**

> Revisa la aplicación y prueba sus funcionalidades. Corrige los
> problemas de visualización para que los textos de los botones y campos
> sean legibles, incluso cuando el usuario interactúe con ellos. Revisa
> también el flujo de autorización de Google Calendar y Gmail, los
> mensajes que aparecen cuando no hay una cuenta conectada y el manejo
> de errores. Comprueba que las claves y credenciales se recuperen desde
> los secretos y que no se expongan en pantalla, registros o archivos
> del repositorio. No afirmes que una prueba fue superada si no se ha
> ejecutado.

**Objetivo**

Identificar problemas de experiencia de usuario, revisar las
integraciones.

**Decisión y revisión**

Se revisaron los problemas de contraste y legibilidad de los controles,
así como los flujos de autorización y los mensajes relacionados con la
conexión de Google. Las correcciones se incorporaron de acuerdo con los
resultados observados durante las pruebas.

------------------------------------------------------------------------

## Qué delegué y qué revisé manualmente

### Actividades delegadas a la IA

-   Proponer la arquitectura con Chatgpt y la organización de los archivos con Gemini.
-   Generar y modificar código Python.
-   Construir y reorganizar la interfaz de Streamlit.
-   Apoyar en la integración de Gemini y los servicios de Google.

### Actividades revisadas manualmente

-   Comprobar que la aplicación correspondiera con la especificación.
-   Revisar las respuestas generadas por Gemini.
-   Probar la navegación, los formularios y la legibilidad de la
    interfaz.
-   Generar la conexión de las APIs necesarias de Google Calendar y Gmail. Así como verificar el funcionamiento de las integraciones con Google Calendar
    y Gmail.
-   Revisar el manejo de credenciales y secretos.
