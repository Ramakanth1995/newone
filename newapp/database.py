from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin

db = SQLAlchemy()

class Products(db.Model):

    __tablename__ = "Productslist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    paid_amount = db.Column(db.Integer,  nullable=False)
    remaning_amount =  db.Column(db.Integer,  nullable=False)
    total_amount = db.Column(db.Integer,  nullable=False)

    def __init__(self,name,category, paid_amount, remaning_amount,total_amount):

        self.name = name
        self.category = category
        self.paid_amount = paid_amount
        self.remaning_amount = remaning_amount
        self.total_amount = total_amount

    def __repr__(self):
        return f"{self.id}:{self.name}:{self.paid_amount}::{self.remaning_amount}:{self.total_amount}"

    #total_amount = db.relationship('Todo_List_Model', backref='todolist')


# class Users(UserMixin, db.Model):
#     __tablename__ = "newusertable"
#
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(200), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     is_active =  db.Column(db.String(200))
#     posts = db.relationship('Todo_List_Model', backref='todolist')
#
#     # def __repr__(self):
#     #     return f"{self.id},{self.username},{self.password},{self.is_active}{self.posts}"
#
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return str(self.id)
#
#
# class Todo_List_Model(db.Model):
#     __tablename__ = "newtodolisttss"
#     id = db.Column(db.Integer, primary_key=True)
#     Task_name = db.Column(db.String())
#     Description = db.Column(db.String())
#     us_id = db.Column(db.Integer, db.ForeignKey('newusertable.id'))
#
#     def __init__(self, Task_name, Description,us_id):
#         self.Task_name = Task_name
#         self.Description = Description
#         self.us_id = us_id
#
#     def __repr__(self):
#         return f"{self.id}:{self.Task_name}:{self.Description}:{self.us_id}"
#
# class Register_Model(db.Model):
#     __tablename__ = "regis"
#     r_id = db.Column(db.Integer, primary_key=True)
#     Email  = db.Column(db.String())
#     Password = db.Column(db.String())
#     Repeat_Password= db.Column(db.String())
#
#     def __init__(self, Email, Password,Repeat_Password):
#         self.Email = Email
#         self.Password = Password
#         self.Repeat_Password = Repeat_Password
#
#     def __repr__(self):
#         return f"{self.r_id},{self.Email},{self.Password},{self.Repeat_Password}"
#
#
