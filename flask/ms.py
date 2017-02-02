import os,pymongo,gridfs
from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename
from bson.objectid import ObjectId
import json

global input_handle	

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	#shouts = collection.find()
	return render_template('index.html')

@app.route("/chart", methods=['GET'])
def maps():
	return render_template('ch.html', input_handle)

@app.route("/fup", methods=['GET'])
def fup():
	return render_template('upld.html')

@app.route("/down", methods=['GET'])
def down():
	return render_template('dnld.html')


@app.route('/downloader', methods = ['GET', 'POST'])
def download_file():
    if request.method == 'POST':
		f = request.form['filename']
		MONGO_URL=os.environ.get('MONGODB_URI')
		client =pymongo.MongoClient(MONGO_URL)
		db=client.Flask
		q=db['FilesUp']
		cursor=q.find({})
		#f='tamil.txt'
		for doc in cursor:
			if doc['file_name'] == f:
				ids=doc['ref']
		print ids
		fs = gridfs.GridFS(db)
		q1=db['fs.files']
		cursor1=q1.find({})
		for doc in cursor1:
			if(doc['_id']==ObjectId(ids)):
				print('found')
				n=f.split('.')
				n[0]=n[0]+'(copy)'
				f='./copyfolders/'+n[0]+'.'+n[1]
				t=open(f,'w')
				print('opened')
				t.write(fs.get(doc['_id']).read())
				print('written')
		return 'downloaded successfully'

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():  
	if request.method == 'POST':
		f = request.files['file']
		raw=f.read()
		#f.save(secure_filename(f.filename))
		MONGO_URL=os.environ.get('MONGODB_URI')
		client=pymongo.MongoClient(MONGO_URL)
		db=client.Flask
		fs=gridfs.GridFS(db)
		newfile_id=fs.put(raw,file_name=f.filename)
		print type(newfile_id)
		db.FilesUp.insert({"id":1,"file_name":f.filename,"ref":newfile_id})
		return 'file uploaded successfully'


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.debug==True
	with open('input.json', 'r') as fp:
		input_handle = json.loads(fp.read())
	app.run(host='0.0.0.0', port=port)
	

