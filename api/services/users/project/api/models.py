from sqlalchemy.sql import func
from project import db
from sqlalchemy.orm import relationship

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(124))
    tasks = relationship("Tasks")

    def to_json(self):
        return{
            'name': self.name
        }
        
class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(124))
    status = db.Column(db.String(124))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_json(self):
        return{
            'user_id' = self.user_id,
            'description' = self.description,
            'status' = self.status,
            'user_id' = self.user_id
        }
