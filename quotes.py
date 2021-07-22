from flask import Flask, render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:Maha1996@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://ynilcbqdavpmnq:c35cd563f1720776508bfd0b842110a0e4805cfd94057dc4313788e6d937722f@ec2-54-195-76-73.eu-west-1.compute.amazonaws.com:5432/d7i3f66mhuiaj4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))




@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
	return render_template('quotes.html')


@app.route('/process',methods =['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata =Favquotes(author=author,quote=quote)
	db.session.add(quotedata)
	db.session.commit()

	return redirect(url_for('index'))

