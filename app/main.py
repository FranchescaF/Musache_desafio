# app/main.py
import uuid

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.domain.models import (AssistantResponse, HistoryResponse, Message,
                               QuestionRequest)
from app.infrastructure.database import get_db_connection, init_db

app = FastAPI(title="Musache AI Assistant API")

# Inicializar la base de datos al arrancar
init_db()


@app.post("/ask", response_model=AssistantResponse)
def ask_question(request: QuestionRequest, session_id: str = None):
    # Si el frontend no envía un session_id, creamos uno nuevo
    if not session_id:
        session_id = str(uuid.uuid4())

    # 1. Simular la respuesta de la IA (Mock)
    respuesta_ia = (
        f"Esta es una respuesta simulada para tu pregunta: '{request.question}'"
    )

    # 2. Guardar en base de datos
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Guardar pregunta del usuario
        cursor.execute(
            "INSERT INTO history (session_id, role, content) VALUES (?, ?, ?)",
            (session_id, "user", request.question),
        )
        # Guardar respuesta de la IA
        cursor.execute(
            "INSERT INTO history (session_id, role, content) VALUES (?, ?, ?)",
            (session_id, "assistant", respuesta_ia),
        )
        conn.commit()
    except Exception:
        raise HTTPException(
            status_code=500, detail="Error guardando en la base de datos"
        )
    finally:
        conn.close()

    # Devolvemos también el session_id en la respuesta
    return {"answer": respuesta_ia, "session_id": session_id}


@app.get("/history/{session_id}", response_model=HistoryResponse)
def get_history(session_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT role, content FROM history WHERE session_id = ? ORDER BY id ASC",
        (session_id,),
    )
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(
            status_code=404, detail="Historial no encontrado para esta sesión"
        )

    messages = [Message(role=row["role"], content=row["content"]) for row in rows]
    return HistoryResponse(session_id=session_id, history=messages)


# Montar la carpeta estática
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Ruta principal para cargar el frontend
@app.get("/web")
def serve_frontend():
    return FileResponse("app/static/index.html")
