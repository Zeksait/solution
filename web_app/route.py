from flask import Blueprint, render_template, request, redirect, url_for
from models import *

app_route = Blueprint('route', __name__, template_folder='templates')

@app_route.route('/')
def index():
   """Статистические данные системы"""
   return render_template('index.html')

@app_route.route('/user/<user_id>')
def get_user(user_id):
   """ предоставляет информацию о пользователе"""
   user = User.query.filter_by(id=user_id).first()
   if user:
      return render_template('user.html', user=user)
   else:
      return render_template('404.html')
   

@app_route.route('/achievements')
def get_all_achievements():
   """предоставляет информацию о всех доступных достижениях"""
   return render_template('achievements.html', achievements=Achievement.query.all())


@app_route.route('/achievements/<achievement_id>')
def get_achievement(achievement_id):
   """ предоставляет информацию о достижении"""
   achievement = Achievement.query.filter_by(id=achievement_id).first()
   if achievement:
      return render_template('achievement.html', achievement=achievement)
   else:
      return render_template('404.html')


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

      return redirect(url_for('route.get_all_achievements'))
   else:
      return render_template('add_achievement.html')
   

@app_route.route('/achievements/<achievement_id>/award', methods=['GET', 'POST'])
def award_user(achievement_id):
   return render_template('award_user.html')


@app_route.route('/')
def set_achievemen_to_user():
   """Выдать достижения пользователю с сохранением времени выдачи 
   (сохранять связь пользователя с достижением и датой выдачи)"""
   return str(User.query.all())
