from datetime import datetime

from flask.cli import FlaskGroup
from app import app
from models import *

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("create_data")
def create_data():

    user_1 = User(username='Андрей', lang='ru')
    user_2 = User(username='Donald', lang='en')
    user_3 = User(username='Анастасия', lang='ru')

    achievement_1 = Achievement(name='Соня', points=5, description='Уснул пока усыплял ребенка')
    achievement_2 = Achievement(name='Обжора', points=10, description='Сьел весь торт')
    achievement_3 = Achievement(name='Волшебник', points=15, description='Починил очки')
    achievement_4 = Achievement(name='Безумец', points=20, description='Усыпил младенца')
    achievement_5 = Achievement(name='СуперКодер', points=50, description='Сделал тестовое задание между тостами на дне рождения тещи')

    db.session.add_all([user_1, user_2, user_3])
    db.session.add_all([achievement_1, achievement_2, achievement_3, achievement_4, achievement_5])
    db.session.flush()

    user_achievement_1 = UserAchievement(user_id=user_1.id, achievement_id=achievement_1.id, d_create=datetime.now())
    user_achievement_2 = UserAchievement(user_id=user_2.id, achievement_id=achievement_2.id, d_create=datetime.now())
    user_achievement_3 = UserAchievement(user_id=user_3.id, achievement_id=achievement_3.id, d_create=datetime.now())

    db.session.add_all([user_1, user_2, user_3])
    db.session.add_all([achievement_1, achievement_2, achievement_3, achievement_4, achievement_5])
    db.session.add_all([user_achievement_1, user_achievement_2, user_achievement_3])

    db.session.commit()

if __name__ == "__main__":
    cli()
