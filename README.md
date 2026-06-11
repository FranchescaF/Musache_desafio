# Musache AI Assistant - Desafío Técnico

## Descripción
Este proyecto es una Single Page Application (SPA) que integra un asistente de IA básico. El sistema expone una API REST construida con FastAPI (Backend) y una interfaz web sencilla utilizando HTML, CSS y Vanilla JS (Frontend). El objetivo principal es permitir la simulación de preguntas sobre un documento y mantener el historial de la conversación.

## Estructura del Proyecto
El proyecto sigue los principios de Clean Architecture, dividido en:
* `domain/`: Modelos de datos y tipado fuerte (Pydantic).
* `application/`: Lógica de negocio.
* `infrastructure/`: Configuración de FastAPI, endpoints y base de datos (SQLite).

## Instrucciones para configurar el entorno local
1. Clona este repositorio.
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # En Windows
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
4. Ejecuta el servidor de desarrollo:
    ```bash
    uvicorn app.main:app --reload
5. Accede a la web en: `http://127.0.0.1:8000/web` y a la documentación de la API en `http://127.0.0.1:8000/docs`.

## Instrucciones para ejecutar en Docker
Para levantar la aplicación empaquetada con su entorno completo, asegúrate de tener Docker y Docker Compose instalados y ejecuta:
    ```bash
    docker-compose up --build
La aplicación estará disponible en el puerto 8000.

## Instrucciones para correr las pruebas
Para ejecutar los tests unitarios e integrados, así como validar la calidad del código, corre los siguientes comandos:
    
    pytest
    black app/
    isort app/
    ruff check app/

