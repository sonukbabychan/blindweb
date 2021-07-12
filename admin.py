from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')


@admin.route('/adminviewblinds',methods=['get','post'])
def adminviewblinds():
	data={}
	q="select * from blind"
	res=select(q)
	data['viewblind']=res
	return render_template('adminviewblinds.html',data=data)

@admin.route('/adminviewcaretaker',methods=['get','post'])
def adminviewcaretaker():
	data={}
	q="select * from caretaker"
	res=select(q)
	data['viewcaretaker']=res
	return render_template('adminviewcaretaker.html',data=data)
	
