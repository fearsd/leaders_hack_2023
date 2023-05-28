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
        if i.question_id == 1:
            answers['gender'] = i.options[0].slug
        elif i.question_id == 2:
            answers['age'] = i.options[0].slug
        elif i.question_id == 3:
            answers['interests'] = [j.slug for j in i.options]
        elif i.question_id == 4:
            answers['is_online'] = True if i.option[0].slug == 'online' else False
        elif i.question_id == 5:
            answers['skills'] = [j.slug for j in i.options]
        elif i.question_id == 6:
            answers['sport'] = True if i.option[0].slug == 'yes' else False
        elif i.question_id == 7:
            answers['is_games_online'] = True if i.option[0].slug == 'online_games' else False
        elif i.question_id == 8:
            answers['edu_skill'] = [j.slug for j in i.options]
        elif i.question_id == 9:
            answers['art_skill'] = [j.slug for j in i.options]

    print(result)
