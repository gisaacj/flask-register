from uuid import uuid4
from app import app
from flask import render_template,redirect,url_for,request
from sqlalchemy import func
from app.models import db,User
from forms import RegisterForm

@app.route('/')
def index():
    return '<h1>,,,</h1>'
@app.route('/register',methods=['GET','POST'])
def registerForm():
    form = RegisterForm(request.form)
#    if request.method == 'POST'and form.validate():
    if form.validate_on_submit():
        new_user=User(user_name=form.name.data)
        new_user.id=str(uuid4())
        new_user.user_class=form.class_.data
        new_user.user_sex=form.sex.data
        new_user.user_qq=form.qq.data
        new_user.user_phone=form.phone.data
        new_user.user_room=form.room.data
        new_user.user_hobby=form.hobby.data
        new_user.user_expen=form.expen.data
        new_user.user_wish=form.wish.data
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('index'))
    return render_template('register.html',
                           form=form)
