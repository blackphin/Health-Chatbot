from pydantic import BaseModel, UUID4, EmailStr
from typing import List, Optional
from datetime import datetime


# REQUEST SCHEMAS

# Request Schema for Creating Account
class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    password: str


# Request Schema for JWT

class TokenData(BaseModel):
    user_id: Optional[UUID4] = None


# Request Schema for Getting Primary Question IDs

class SetPrimaryQuestions(BaseModel):
    question_ids: List[UUID4]


# Request Schema for Getting Answer ID

class GetAnswer(BaseModel):
    answered_at: datetime
    answer_id: UUID4
    journal_id: UUID4
    answered_at: Optional[datetime] = None


# Request Schema for getting Query for generating GPT Response

class GPTQuery(BaseModel):
    chat_session_id: Optional[UUID4] = None
    query: str


# RESPONSE SCHEMAS

class Token(BaseModel):
    access_token: str
    token_type: str


class GetPrimaryQuestions(BaseModel):
    question_ids: List[UUID4]


# Prerequisite Response Schema for Sending Question Expression
class QuestionResponse(BaseModel):
    id: UUID4
    expression: str
    # keyword_intents: list

# Prerequisite Response Schema for Sending Answer Expression


class AnswerOptions(BaseModel):
    id: UUID4
    expression: str
    # score: int
    # keyword_intents: List
    suggested_action: Optional[str] = None
    # elder_question_id: UUID4
    # progeny_question_id: Optional[UUID4] = None
    # question_id: UUID4

# Response Schema for Sending Question and Possible Answers based on Answer IDF


class QuestionAnswers(BaseModel):
    # journal_id: UUID4
    # user_id: UUID4
    question: Optional[QuestionResponse]
    answer_options: Optional[List[AnswerOptions]]

    class Config:
        orm_mode = True

# Prerequisite Response Schema for Sending First Answer Expression (Doesn't have Elder Question ID)


class InitialAnswerOptions(BaseModel):
    id: UUID4
    expression: str
    # score: int
    # keyword_intents: List
    suggested_action: Optional[str] = None
    # progeny_question_id: Optional[UUID4] = None
    # question_id: UUID4

# Response Schema for Journal ID and Initial Question


class InitialQuestion(BaseModel):
    journal_id: UUID4
    question: QuestionResponse
    answer_options: List[InitialAnswerOptions]

    class config:
        orm_mode = True

# Response Schema for GPT Response


class GPTResponse(BaseModel):
    chat_session_id: Optional[UUID4] = None
    response: str

    class config:
        orm_mode = True

# Response Schema for getting Journal IDs


class UserJournals(BaseModel):
    answered_at: datetime
    journal_id: UUID4


# Response Schema for getting Journal Details

class JournalDetails(BaseModel):
    answered_at: datetime
    log_id: UUID4
    # journal_id: UUID4
    # user_id: UUID4
    score: int
    question_id: UUID4
    progeny_question_id: Optional[UUID4] = None
    answer_id: UUID4
    question_expression: str
    answer_expression: str
    suggested_action: Optional[str] = None

    class config:
        orm_mode = True

# Response Schema for getting GPTLog IDs


class UserGPTLogs(BaseModel):
    asked_at: datetime
    chat_session_id: UUID4

    class config:
        orm_model = True

# Response Schema for getting GPTLogs details


class GPTLogsDetails(BaseModel):
    asked_at: datetime
    user_id: UUID4
    chat_session_id: UUID4
    message_id: UUID4
    query: str
    response: str

    class config:
        orm_model = True
