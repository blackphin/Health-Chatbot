from typing import List
from fastapi import Depends, status, APIRouter
from pydantic import UUID4
from utils import summarize

from sqlalchemy.orm import Session

from database import get_db

import models
import schemas
import oauth2

router = APIRouter(
    tags=['GPT'], prefix="/api/gpt_logs"
)


@router.get("/get/{chat_session_id}")
def get_gptlogs(
    chat_session_id: UUID4,
    db: Session = Depends(get_db),
    user_id: UUID4 = Depends(oauth2.get_current_user)
):
    logs = db.query(models.GPTLogs).filter(
        models.GPTLogs.chat_session_id == chat_session_id,
        models.GPTLogs.user_id == user_id
    ).order_by(
        models.GPTLogs.asked_at.asc()
    ).all()
    chat = ""
    for log in logs:
        chat+= f"User: {log.query}\nChat Bot: {log.response}\n"
    logs.append({"summary": summarize(chat)})
    return logs


@router.get("/get", response_model=List[schemas.UserGPTLogs])
def get_gptlog_id(db: Session = Depends(get_db), user_id: UUID4 = Depends(oauth2.get_current_user)):
    chat_session_ids = db.query(models.GPTLogs.chat_session_id).distinct().filter(
        models.GPTLogs.user_id == user_id).all()
    response = []
    for chat_session_id in chat_session_ids:
        asked_at = db.query(models.GPTLogs.asked_at).filter(
            models.GPTLogs.chat_session_id == chat_session_id[0]).first()
        response.append(
            {"asked_at": asked_at[0], "chat_session_id": chat_session_id[0]})
    return response


@router.delete("/delete/{chat_session_id}", status_code=status.HTTP_404_NOT_FOUND)
def delete_gptlogs(
    chat_session_id: UUID4,
    db: Session = Depends(get_db),
    user_id: UUID4 = Depends(oauth2.get_current_user)
):
    delete_logs = db.query(models.GPTLogs).filter(
        models.GPTLogs.chat_session_id == chat_session_id,
        models.GPTLogs.user_id == user_id
    )
    delete_logs.delete(synchronize_session=False)
    db.commit()

    return {"chat_session_id": chat_session_id}
