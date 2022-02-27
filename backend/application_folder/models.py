from click import password_option
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class UserInfoModel(db.Model):
    __tablename__ = 'User_table'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    password = db.Column(db.Integer())
 
    def __init__(self, name,password):
        self.name = name
        self.password = password
 
    def __repr__(self):
        return f"{self.name}:{self.password}"