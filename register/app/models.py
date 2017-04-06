from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.String(45),primary_key=True)
    user_name=db.Column(db.String(255))
    user_class=db.Column(db.String(255))
    user_sex=db.Column(db.String(255))
    user_qq=db.Column(db.String(255))
    user_phone=db.Column(db.String(255))
    user_room=db.Column(db.String(255))
    user_hobby=db.Column(db.String(255))
    user_expen=db.Column(db.String(512))
    user_wish=db.Column(db.String(255))
    
    def __init__(self,user_name):
        self.user_name=user_name

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.user_name)
