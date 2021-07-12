from flask import *

from database import *
import uuid
from encode_faces import *
caretaker=Blueprint('caretaker',__name__)

@caretaker.route('/caretakerhome',methods=['get','post'])
def caretakerhome():
	return render_template('caretakerhome.html')

@caretaker.route('/care_manage_blind_account',methods=['get','post'])
def care_manage_blind_account():
	ids=session['log_id']

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		photo=request.files['photo']
		path='static/blind_images/'+str(uuid.uuid4())+photo.filename
		photo.save(path)
		phnno=request.form['phn']
		Gender=request.form['gender']
		DOB=request.form['Dob']
		imei = request.form['imei']
		Latitude=request.form['lat']
		Longitude=request.form['lon']

		q="insert into blind values(null,(SELECT `care_taker_id` FROM `caretaker` WHERE `log_id` = '%s'),'%s','%s','%s','%s','%s','%s','%s','%s', '%s')" %(ids,fname,lname,path,phnno,Gender,DOB, imei,Latitude,Longitude)
		# print(q)
		insert(q)
	return render_template('care_manage_blind_account.html')

@caretaker.route('/care_view_help_request',methods=['get','post'])
def care_view_help_request():
	data={}
	q="SELECT *,CONCAT(first_name,' ',last_name)AS Name,help.`Latitude`,help.`Longitude` FROM HELP INNER JOIN blind USING(blind_id)"
	res=select(q)
	data['viewhelp']=res
	return render_template('care_view_help_request.html',data=data)

@caretaker.route('/add_emergency_num',methods=['get','post'])
def add_emergency_num():
	data = {}
	ids = session['log_id']
	q = "SELECT blind_id, CONCAT(first_name,' ',last_name) AS `name` FROM blind WHERE `cartaker_id` = (SELECT `care_taker_id` FROM `caretaker` WHERE `log_id` = '%s')" %(ids)
	res = select(q)
	# print(res)
	data['blind'] = res
	if 'submit' in request.form:
		blind_id=request.form['blind_id']
		phnno=request.form['phn']
		Relation=request.form['relation']
		Latitude=request.form['lat']
		Longitude=request.form['lon']

		q="insert into emergency_numbers values(null, '%s','%s','%s','%s','%s')" %(blind_id, phnno,Relation,Latitude,Longitude)
		insert(q)
	return render_template('add_emergency_num.html', data=data)

@caretaker.route('/care_train_faces',methods=['get','post'])
def care_train_faces():
	data = {}
	ids = session['log_id']
	q = "SELECT blind_id, CONCAT(first_name,' ',last_name) AS `name` FROM blind WHERE `cartaker_id` = (SELECT `care_taker_id` FROM `caretaker` WHERE `log_id` = '%s')" %(ids)
	res = select(q)
	# print(res)
	data['blind'] = res
	if 'submit' in request.form:
		blind_id=request.form['id']
		image=request.files['image']

		first_Name=request.form['fname']
		Last_name=request.form['lname']
		Relation=request.form['relation']
		
		ins_qry="insert into faces values(null,'%s','%s','%s',CURDATE(),'%s')"%(blind_id, first_Name,Last_name,Relation)
		face_id = insert(ins_qry)

		# path = 'static/uploads/'
		path=""
		# Check whether the   
		# specified path is   
		# an existing file 
		isFile = os.path.isdir("static/uploads/"+face_id)  
		print(isFile)
		if(isFile==False):
			os.mkdir('static\\uploads\\'+face_id)
		path="static/uploads/"+face_id+"/"+image.filename
		image.save(path)

	if 'train' in request.form:
		print("started")
		enf("static/uploads/")
		print("complete")
		
	return render_template('care_train_faces.html',data=data)