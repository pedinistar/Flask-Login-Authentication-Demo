from flask import Flask, request, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import bcrypt


app = Flask(__name__)
db_url = 'sqlite:///database.db'
Base = declarative_base()
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True)
  password = Column(String)

password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.getsalt()).decode('utf-8')

@app.route('/')
def index():
  return 'hi'

@app.route('/register', methods=['GET','POST'])
def register():
  if request.method == 'POST':
    pass

  return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    pass

  return render_template('login.html')


if __name__=='__main__':
  app.run(debug=True)
