from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String


Model = declarative_base()


class User(UserMixin, Model):
     __tablename__ = "users"

     username = Column(String, primary_key=True)
     password = Column(String, nullable=False)

     def get_id(self):
          return self.username

