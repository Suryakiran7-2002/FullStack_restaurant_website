
from re import DEBUG
from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy


from datetime import datetime

from werkzeug.utils import HTMLBuilder


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class admin_details(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))


class booking(db.Model):
    _id = db.Column('id',db.Integer, primary_key = True)
    f_name = db.Column('f_name',db.String(20))
    phno = db.Column('phno',db.String(10))
    date = db.Column('date',db.Date)
    time = db.Column('time',db.Time)
    email = db.Column('email',db.String(20))
    nppl = db.Column('no. of people',db.Integer)
    bk = db.Column('booking Date',db.DateTime,default = datetime.now)


    def __init__(self,f_name,phno,date,time,email,nppl):
        self.f_name = f_name
        self.phno = phno
        self.date = date
        self.time = time
        self.email = email
        self.nppl = nppl
        
@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    if request.method == 'GET':
        return render_template('login.html',error = 0)
    
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        vals = admin_details.query.get(1)
        
        if not email or not password:
            return render_template('login.html',error = 1)
        
        elif email != vals.email or password != vals.password:
            return render_template('login.html',error = 2)

        else:
            
            return render_template('/bookings.html',type = 0)


@app.route('/bookings',methods = ['POST'])
def show_bookings():

    
  
        
    date = datetime.strptime(request.form.get('date'),'%Y-%m-%d').date()
    data_from_database = booking.query.filter_by(date=date).all()
    print(data_from_database)
    print(date)
    return render_template('/bookings.html',type = 1, data = data_from_database,date = date,len = len(data_from_database))

        

    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Menu')
def menu():
    return render_template('menu.html')

@app.route('/Menu/starters')
def menu_starters():
    return render_template('starters.html')

@app.route('/Menu/snacks')
def menu_snacks():
    return render_template('snacks.html')

@app.route('/Menu/main_course')
def menu_main_course():
    return render_template('main_course.html')

@app.route('/Menu/biryani')
def menu_biryani():
    return render_template('biryani.html')

@app.route('/Menu/desserts')
def menu_desserts():
    return render_template('desserts.html')

@app.route('/Menu/beverages')
def menu_beverages():
    return render_template('beverages.html')

@app.route('/Menu/fast_food')
def menu_fast_food():
    return render_template('fast_food.html')

@app.route('/Menu/chinese')
def menu_chinese():
    return render_template('chinese.html')

@app.route('/Menu/coffee')
def menu_coffee():
    return render_template('coffee.html')

@app.route('/Book_Table', methods = ['GET','POST'])
def book_table():


    if request.method == "POST":
        f_name = request.form.get('f_name')
        phno = request.form.get('phno')
        date = datetime.strptime(request.form.get('date'),'%Y-%m-%d').date()
        

        time = request.form.get('time') + ':00'
        time = datetime.strptime(time,'%H:%M:%S').time()

        
        


        nppl = request.form.get('nppl')
        email = request.form.get('email')

        print(f_name,phno,date,time,nppl,email)
        if not f_name or not phno or not date or not time or not nppl or not email:
            return render_template('book_table.html',f_name = f_name,phno = phno,email = email,nppl = nppl, date = date, time = time,error = 1)
        else:
            new_data = booking(f_name,phno,date,time,email,nppl)
            db.session.add(new_data)
            db.session.commit()
            return render_template('book_table.html',f_name = f_name,phno = phno,email = email,nppl = nppl, date = date, time = time,error = 0)
    
    else:
        return render_template('book_table.html')
        



if __name__ == '__main__':
    db.create_all()
    app.run(host = '0.0.0.0',debug = False)