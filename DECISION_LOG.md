# Registro de Decisiones Técnicas (Decision Log)

## 1. Arquitectura y Estructura
Se optó por una estructura de carpetas basada en Clean Architecture (`domain`, `application`, `infrastructure`). Esto permite separar las responsabilidades, aislando la lógica de negocio de los detalles del framework (FastAPI) y facilitando la escalabilidad futura.

## 2. Base de Datos
Se eligió **SQLite** por sobre motores más pesados como PostgreSQL o MySQL. 
* **Justificación:** Dado el límite de 12 horas de trabajo efectivo para la resolución del desafío y el enfoque en entregar un MVP funcional, SQLite proporciona almacenamiento persistente en disco sin requerir configuraciones adicionales ni levantar servicios extra en contenedores, agilizando el desarrollo y la evaluación.

## 3. Integración de la IA
* **Atajo tomado:** Por cuestiones de tiempo y para priorizar la estructura base y los endpoints, se implementó un "mock" (simulación) de la respuesta del asistente. La arquitectura permite que, en el futuro, solo se modifique la capa de infraestructura/aplicación para conectar un LLM real (ej. OpenAI o LangChain) sin romper los contratos del dominio.

## 4. Frontend Integrado
Se decidió servir los archivos estáticos (HTML/JS/CSS) directamente desde FastAPI. Esto elimina los problemas de CORS durante la fase de desarrollo y permite tener una solución Fullstack contenida en un solo servicio fácilmente desplegable.