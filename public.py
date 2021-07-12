from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			session['log_id']=res[0]['log_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))
			if res[0]['usertype']=="caretaker":
				return redirect(url_for('caretaker.caretakerhome'))	
	return render_template('login.html')


@public.route('/register',methods=['get','post'])
def register():
	if 'reg' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		phnno=request.form['phn']
		mail=request.form['mail']
		username=request.form['User name']
		password=request.form['password']
		q="insert into login values(null,'%s','%s','caretaker')"%(username,password)
		id=insert(q)
		q="insert into caretaker values(null,'%s','%s','%s','%s','%s')"%(fname,lname,phnno,mail,id)
		insert(q)
		return redirect(url_for('public.login'))
	return render_template('caretakerreg.html')

@public.route('/',methods=['get','post'])
def home():
	return render_template('index.html')
