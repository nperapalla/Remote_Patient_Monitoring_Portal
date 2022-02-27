from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, UserInfoModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Nihari123@localhost:5432/telehealth"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        new_user = UserInfoModel(name=name, password=password)
        db.session.add(new_user)
        db.session.commit()
        return f"Done!!"
 
if __name__ == '__main__':
    app.run(debug=True)
