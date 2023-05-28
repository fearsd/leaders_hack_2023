from sqlalchemy.orm import Session
from db.poll_models import QuestionType, Question, Option
from db.db import get_db
questions = [
    {
        'text': 'Пол',
        'slug': '#1',
        'num': 1,
        'question_type': QuestionType.Check,
        'poll_id': 1
    },
    {
        'text': 'Ваш возраст',
        'slug': '#2',
        'num': 2,
        'question_type': QuestionType.Check,
        'poll_id': 1
        
    },{
        'text': 'Какие занятия Вам нравятся сейчас больше всего?',
        'slug': '#3',
        'num': 3,
        'question_type': QuestionType.Multi,
        'poll_id': 1
        
    },{
        'text': 'В каком формате Вы предпочитаете заниматься?',
        'slug': '#4',
        'num': 4,
        'question_type': QuestionType.Check,
        'poll_id': 1
        
    },{
        'text': 'Какие навыки или интересы Вы бы хотели развивать или изучать?',
        'slug': '#5',
        'num': 5,
        'question_type': QuestionType.Multi,
        'poll_id': 1
        
    },{
        'text': 'Занимаетесь ли Вы физическими упражнениями?',
        'slug': '#6',
        'num': 6,
        'question_type': QuestionType.Check,
        'poll_id': 1
        
    },{
        'text': 'Какую категорию интеллектуальных игр Вы считаете наиболее привлекательной и интересной для себя?',
        'slug': '#7',
        'num': 7,
        'question_type': QuestionType.Check,
        'poll_id': 1
        
    },{
        'text': 'Какую категорию занятий Вы считаете наиболее привлекательной и интересной для себя в области образования и саморазвития?',
        'slug': '#8',
        'num': 8,
        'question_type': QuestionType.Check,
        'poll_id': 1
        
    },{
        'text': ' Какую категорию занятий Вы считаете наиболее привлекательной и интересной для себя в области творчества и активного образа жизни?',
        'slug': '#9',
        'num': 9,
        'question_type': QuestionType.Check,
        'poll_id': 1
        
    },
]

options = [
    {
        'text': 'Мужской',
        'question_id': 1,
        'slug': 'male',
    },
    {
        'text': 'Женский',
        'question_id': 1,
        'slug': 'female',
    },

    {
        'text': 'Младше 60 лет',
        'question_id': 2,
        'slug': '<60',
    },
    {
        'text': '60-70 лет',
        'question_id': 2,
        'slug': '>=60,<=70',
    },
    {
        'text': '71-80 лет',
        'question_id': 2,
        'slug': '>=71,<=80',
    },
    {
        'text': 'Старше 80 лет',
        'question_id': 2,
        'slug': '>80',
    },

    {
        'text': 'Соревнования',
        'question_id': 3,
        'slug': 'competition'
    },
    {
        'text': 'Лекции и обучение',
        'question_id': 3,
        'slug': 'lectures'
    },
    {
        'text': 'Путешествия',
        'question_id': 3,
        'slug': 'travel'
    },
    {
        'text': 'Активные прогулки',
        'question_id': 3,
        'slug': 'walking'
    },
    {
        'text': 'Садоводство и огородничество',
        'question_id': 3,
        'slug': 'gardening'
    },


    {
        'text': 'Онлайн (через интернет)',
        'question_id': 4,
        'slug': 'online'
    },
    {
        'text': 'Вживую (в группе или индивидуально)',
        'question_id': 4,
        'slug': 'offline'
    },


    {
        'text': 'Изучение новых языков',
        'question_id': 5,
        'slug': 'languages'
    },
    {
        'text': 'Рисование или живопись',
        'question_id': 5,
        'slug': 'drawing'
    },{
        'text': 'Музыка (игра на инструменте, пение)',
        'question_id': 5,
        'slug': 'music'
    },{
        'text': 'Кулинария',
        'question_id': 5,
        'slug': 'cooking'
    },{
        'text': 'Рукоделие (вязание, шитье и т.д.)',
        'question_id': 5,
        'slug': 'needlework'
    },

    {
        'text': 'Да',
        'question_id': 6,
        'slug': 'yes',
    },
    {
        'text': 'Нет',
        'question_id': 6,
        'slug': 'no',
    },


    {
        'text': 'Интеллектуальные игры (включая настольные игры и шахматы/шашки)',
        'question_id': 7,
        'slug': 'offline_games',
    },
    {
        'text': 'Онлайн интеллектуальные игры',
        'question_id': 7,
        'slug': 'online_games',
    },



    {
        'text': 'Здорово жить (включая образовательный практикум, пеший лекторий, психологию и коммуникации, финансовую и правовую грамотность, личную безопасность, экологию жизни)',
        'question_id': 8,
        'slug': 'healthy',
    },
    {
        'text': 'История, искусство, краеведение',
        'question_id': 8,
        'slug': 'history',
    },
    {
        'text': 'Иностранные языки',
        'question_id': 8,
        'slug': 'languages',
    },
    {
        'text': 'Информационные технологии',
        'question_id': 8,
        'slug': 'it',
    },



    {
        'text': 'Рисование',
        'question_id': 9,
        'slug': 'drawing',
    },
    {
        'text': 'Пение',
        'question_id': 9,
        'slug': 'vocal',
    },
    {
        'text': 'Танцы',
        'question_id': 9,
        'slug': 'dancing',
    },
    {
        'text': 'Спорт и фитнес (включая борьбу, велоспорт, ГТО, гимнастику, коньки, лыжи, скандинавскую ходьбу, спортивные игры, фитнес и тренажеры)',
        'question_id': 9,
        'slug': 'sport',
    },
]

def _run_saving(list, model):
    db: Session = next(get_db())
    db.bulk_insert_mappings(model, list)
    db.commit()

def run_saving_questions():
    _run_saving(questions, Question)

def run_saving_options():
    _run_saving(options, Option)