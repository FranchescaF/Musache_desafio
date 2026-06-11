# app/domain/models.py
from typing import List

from pydantic import BaseModel


# Modelo para recibir la pregunta en el endpoint /ask
class QuestionRequest(BaseModel):
    question: str


# Modelo para enviar la respuesta del asistente
class AssistantResponse(BaseModel):
    answer: str
    session_id: str


# Modelos para el historial
class Message(BaseModel):
    role: str
    content: str


class HistoryResponse(BaseModel):
    session_id: str
    history: List[Message]
