from sqlalchemy.orm import Session
from db.db import get_db
from db.poll_models import Question, Answer, Option

ML_PARSER_CONFIG = {
    'first_question_id': 1
}

def filter_groups_by_poll(result):
    # first question
    first_question_id = 1
    db: Session = next(get_db())
    answers = {}
    for i in result.answers: 
        if(i.question_id == ML_PARSER_CONFIG['first_question_id']):
            print('@ii', i.options)
    print(result)
