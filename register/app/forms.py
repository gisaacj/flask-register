# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField,SelectField,RadioField,TextAreaField,BooleanField
from wtforms.validators import DataRequired,Required,Length

class RegisterForm(Form):
    name = StringField(u'姓名',validators=[DataRequired()])
    class_=StringField(u'专业班级',validators=[DataRequired()])
    sex=RadioField(u'性别',choices=[(u'男',u'男'),(u'女',u'女')],validators=[DataRequired()])
    qq=StringField('QQ',validators=[DataRequired()])
    phone=StringField(u'手机',validators=[DataRequired()])
    room=StringField(u'宿舍',validators=[DataRequired()])
    hobby=StringField(u'兴趣爱好',validators=[DataRequired()])
    expen=TextAreaField(u'个人经历',validators=[DataRequired()])
    wish=SelectField(u'部门意愿',choices=[(u'技术部',u'技术部'),(u'综管部',u'综管部'),(u'公关部',u'公关部'),(u'策划部',u'策划部')],validators=[DataRequired()])
