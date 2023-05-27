from mimesis import Generic
from mimesis import Locale
from mimesis import Gender
from mimesis.builtins import RussiaSpecProvider

from db.models import UserAccount, Gender as G
from db.db import get_db

generic = Generic(locale=Locale.RU)
generic.add_provider(RussiaSpecProvider)


def generate_name(gender):
    return [
            generic.person.full_name(gender, reverse=True),
            generic.russia_provider.patronymic(gender=gender)
            ]


def _get_fake_names(count: int):
    for i in range(count):
        name = ' '.join(generate_name(Gender.FEMALE))
        yield name


def save_fake_names_to_db():
    db = next(get_db())
    count = db.query(UserAccount).count()
    for i, name in enumerate(_get_fake_names(count)):
        print(i, name)
        user = db.query(UserAccount).filter_by(id=i+1).first()
        if user.gender == G.male:
            user.fullname = ' '.join(generate_name(Gender.MALE))
        else:
            user.fullname = name
        db.commit()
