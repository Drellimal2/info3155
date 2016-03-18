from . import db

class User(db.Model):
    __tablename__ = 'people'
    id=db.Column(db.Integer,primary_key=True,nullable=False,unique=True)
    username=db.Column(db.String(256),unique=True)
    userpassword = db.Column(db.String(256))
    
    def __init__(self,username,userpassword):
        self.username = username
        self.userpassword = userpassword
