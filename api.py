from flask import *
import os
from database import *
from recognize_faces_image import *
import demjson

api=Blueprint('api',__name__)

@api.route('/imei_check/', methods=['get','post'])
def imei_check():
	data = {}
	imei = request.args['imei']
	q = "SELECT `caretaker`.`phone` FROM `blind` INNER JOIN `caretaker` ON `cartaker_id` = `care_taker_id` WHERE `imei` = '%s'" %(imei)
	res = select(q)
	if (res):
		data['data'] = res[0]['phone']
		data['status'] = 'success'
	else:
		data['status'] = 'failed'
	data['method'] = 'imei_check'
	return demjson.encode(data)

@api.route('/get_emergency_number/', methods=['get','post'])
def get_emergency_number():
	data = {}
	imei = request.args['imei']
	q = "SELECT `phone_number` FROM `emergency_numbers` WHERE `blind_id` = (SELECT `blind_id` FROM `blind` WHERE `imei` = '%s')" %(imei)
	res = select(q)
	if (res):
		data['data'] = res[0][phone_number]
		data['status'] = 'success'
	else:
		data['status'] = 'failed'
	data['method'] = 'get_emergency_number'
	return demjson.encode(data)

@api.route('/face_check/', methods=['get','post'])
def face_check():
	print("hg")
	data = {}
	imei=request.form['imei']
	image=request.files['image']

	path="static/uploads/"+image.filename
	image.save(path)

	id=rec_face_image(path)
	print(id)
	q = "SELECT CONCAT(`person_first_name`, ' ', `person_last_name`) AS face_name FROM `faces` WHERE `blind_id` = (SELECT `blind_id` FROM `blind` WHERE `imei` = '%s')" %(imei)
	res = select(q)
	if (res):
		data['data'] = res[0][face_name]
		data['status'] = "success"
	else:
		data['status'] = "failed"
	data['method'] = "face_check"
	return demjson.encode(data)