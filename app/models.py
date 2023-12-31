from sqlalchemy import Column, Integer, String, Text, VARCHAR, ARRAY, Uuid
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime

from database import Base
from config import settings
import uuid


class Users(Base):
    __tablename__ = "users"

    id = Column(Uuid(as_uuid=True),
                nullable=False, default=uuid.uuid4)
    status = Column(Text, nullable=False, default="active")
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    email = Column(Text, primary_key=True, nullable=False)
    phone = Column(Text, nullable=False)
    password = Column(Text, nullable=False)


class Questions(Base):
    __tablename__ = "english_questiondataset"

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    id = Column(Uuid(as_uuid=True), primary_key=True,
                nullable=False, default=uuid.uuid4)
    expression = Column(Text, nullable=False)
    keyword_intents = Column(VARCHAR[255], nullable=True)


class HindiQuestions(Base):
    __tablename__ = "hindi_questiondataset"

    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    id = Column(Uuid(as_uuid=True), primary_key=True,
                nullable=False, default=uuid.uuid4)
    expression = Column(Text, nullable=False)
    keyword_intents = Column(VARCHAR[255], nullable=True)


class Answers(Base):
    __tablename__ = "english_answerdataset"

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    id = Column(Uuid(as_uuid=True), primary_key=True,
                nullable=False, default=uuid.uuid4)
    expression = Column(Text, nullable=False)
    score = Column(Integer, nullable=False)
    keyword_intents = Column(ARRAY(String), nullable=True)
    suggested_action = Column(VARCHAR[255], nullable=True)
    elder_question_id = Column(Uuid, nullable=True)
    progeny_question_id = Column(Uuid, nullable=True)
    question_id = Column(Uuid, nullable=False)


class HindiAnswers(Base):
    __tablename__ = "hindi_answerdataset"

    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    id = Column(Uuid(as_uuid=True), primary_key=True,
                nullable=False, default=uuid.uuid4)
    expression = Column(Text, nullable=False)
    score = Column(Integer, nullable=False)
    keyword_intents = Column(ARRAY(String), nullable=True)
    suggested_action = Column(VARCHAR[255], nullable=True)
    elder_question_id = Column(Uuid, nullable=True)
    progeny_question_id = Column(Uuid, nullable=True)
    question_id = Column(Uuid, nullable=False)


class Journal(Base):
    __tablename__ = "journal"
    answered_at = Column(TIMESTAMP(timezone=True),
                         nullable=False, server_default=text('now()'))
    log_id = Column(Uuid(as_uuid=True), primary_key=True, nullable=False)
    journal_id = Column(Uuid(as_uuid=True), nullable=False)
    user_id = Column(Uuid(as_uuid=True), nullable=False)
    score = Column(Integer, nullable=False)
    question_id = Column(Uuid, nullable=False)
    progeny_question_id = Column(Uuid, nullable=True)
    answer_id = Column(Uuid(as_uuid=True), nullable=False)
    question_expression = Column(Text, nullable=False)
    answer_expression = Column(Text, nullable=False)
    suggested_action = Column(VARCHAR(255), nullable=True)


class GPTLogs(Base):
    __tablename__ = "gpt_logs"
    asked_at = Column(TIMESTAMP(timezone=True), primary_key=True,
                      nullable=False, server_default=text('now()'))
    user_id = Column(Uuid(as_uuid=True), nullable=False)
    chat_session_id = Column(Uuid(as_uuid=True), nullable=False)
    message_id = Column(Uuid(as_uuid=True), primary_key=True,
                        nullable=False, default=uuid.uuid4)
    query = Column(Text, nullable=False)
    response = Column(Text, nullable=False)


class PrimaryQuestions(Base):
    __tablename__ = "primary_questions"
    added_at = Column(TIMESTAMP(timezone=True),
                      nullable=False, server_default=text('now()'))
    question_id = Column(Uuid(as_uuid=True), primary_key=True,
                         nullable=False, default=uuid.uuid4)
