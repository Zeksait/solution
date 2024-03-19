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

    achievement_1 = Achievement(name='Соня', points=5, description='Уснул во время разговора')
    achievement_2 = Achievement(name='Обжора', points=10, description='Сьел весь торт')
    achievement_3 = Achievement(name='Кодер', points=10, description='Сделал тестовое задание')
    achievement_4 = Achievement(name='Волшебник', points=15, description='Починил очки')
    achievement_5 = Achievement(name='Храбрец', points=20, description='Усыпил младенца')


    user_achievement_1 = UserAchievement(user=user_1, achievement=achievement_1)
    user_achievement_2 = UserAchievement(user=user_2, achievement=achievement_2)
    user_achievement_3 = UserAchievement(user=user_3, achievement=achievement_3)


    # post1.tags.append(tag1)  # Tag the first post with 'animals'
    # post1.tags.append(tag4)  # Tag the first post with 'writing'
    # post3.tags.append(tag3)  # Tag the third post with 'cooking'
    # post3.tags.append(tag2)  # Tag the third post with 'tech'
    # post3.tags.append(tag4)  # Tag the third post with 'writing'


    db.session.add_all([user_1, user_2, user_3])
    db.session.add_all([achievement_1, achievement_2, achievement_3, achievement_4, achievement_5])
    db.session.add_all([user_achievement_1, user_achievement_2, user_achievement_3])

    db.session.commit()

if __name__ == "__main__":
    cli()
