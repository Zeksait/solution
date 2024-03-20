from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import func

from models import *

app_route = Blueprint('route', __name__, template_folder='templates')


@app_route.route('/')
def index():
   """Статистические данные системы"""
   users_count = User.query.count()
   achievements_count = Achievement.query.count()
   return render_template(
      'index.html',
      users_count = users_count,
      achievements_count=achievements_count,
      user_achievements_count = User.query.with_entities(
         UserAchievement.achievement_id,
         func.count(UserAchievement.achievement_id)
         )
         .group_by(UserAchievement.achievement_id)
         .all(),
      )


@app_route.route('/users')
def get_users():
   """предоставляет информацию о всех доступных пользователях"""
   return render_template('users.html', users=User.query.all())


@app_route.route('/users/<user_id>')
def get_user(user_id):
   """ предоставляет информацию о пользователе"""
   user = User.query.filter_by(id=user_id).first()
   achievements = UserAchievement.query.filter(UserAchievement.user_id==user_id).all()
   if user:
      return render_template('user.html', user=user, achievements=achievements)
   else:
      return render_template('404.html')


@app_route.route('/achievements')
def get_achievements():
   """предоставляет информацию о всех доступных достижениях"""
   return render_template('achievements.html', achievements=Achievement.query.all())


@app_route.route('/achievements/add', methods=['GET', 'POST'])
def add_achievement():
   """Добавить достижение"""
   if request.method == 'POST':
      name = request.form.get('name')
      points = request.form.get('points')
      description = request.form.get('description')

      achievement = Achievement(name=name, points=int(points), description=description)
      db.session.add(achievement)
      db.session.commit()

      return redirect(url_for('route.get_achievements'))
   else:
      return render_template('add_achievement.html')


@app_route.route('/achievements/<achievement_id>')
def get_achievement(achievement_id):
   """ предоставляет информацию о достижении"""
   achievement = Achievement.query.filter_by(id=achievement_id).first()
   if achievement:
      return render_template('achievement.html', achievement=achievement)
   else:
      return render_template('404.html')


@app_route.route('/achievements/award', methods=['POST'])
def award_user():
   """Наградить пользователя"""
   try:
      user_id = int(request.form.get('user_id'))
      achievement_id = int(request.form.get('achievement_id'))
      db.session.add(UserAchievement(user_id=user_id, achievement_id=int(achievement_id), d_create=datetime.now()))
      db.session.commit()
      return redirect(url_for('route.get_user', user_id=user_id))
   except:
      return "Error"
