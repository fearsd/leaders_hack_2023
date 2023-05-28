from typing import Optional, List
from datetime import datetime
from sqlalchemy import func
from sqlalchemy import Column, DateTime

from sqlmodel import SQLModel, Field, Enum, Relationship


class QuestionType(str, Enum):
    Multi = 'Multi'
    Check = 'Check'


class PollBase(SQLModel):
    datetime_created: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    

class Poll(PollBase, table=True):
    id: int = Field(default=None, primary_key=True)
    questions: List["Question"] = Relationship(back_populates="poll")
    results: List["Result"] = Relationship(back_populates="poll")
        
    
class QuestionBase(SQLModel):
    question_type: QuestionType
    text: str = Field(default='')
    slug: str
    num: int


class Question(QuestionBase, table=True):
    id: int = Field(default=None, primary_key=True)
    poll_id: Optional[int] = Field(default=None, foreign_key="poll.id")
    poll: Optional[Poll] = Relationship(back_populates="questions")
    options: List["Option"] = Relationship(back_populates="question")
        
    
class OptionBase(SQLModel):
    slug: str
    text: str

class OptionResultLink(SQLModel, table=True):
    option_id: Optional[int] = Field(
        default=None, foreign_key="option.id", primary_key=True
    )
    answer_id: Optional[int] = Field(
        default=None, foreign_key="answer.id", primary_key=True
    )


class Option(OptionBase, table=True):
    id: int = Field(default=None, primary_key=True)
    question_id: Optional[int] = Field(default=None, foreign_key="question.id")
    question: Optional[Question] = Relationship(back_populates="options")
    answers: List["Answer"] = Relationship(back_populates="options", link_model=OptionResultLink)
        

class Result(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    poll_id: Optional[int] = Field(default=None, foreign_key="poll.id")
    poll: Optional[Poll] = Relationship(back_populates="results")
    answers: List["Answer"] = Relationship(back_populates="result")
        
    
class Answer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    options: List["Option"] = Relationship(back_populates="answers", link_model=OptionResultLink)
    result_id: Optional[int] = Field(default=None, foreign_key="result.id")
    result: Optional[Result] = Relationship(back_populates="answers")
    
    