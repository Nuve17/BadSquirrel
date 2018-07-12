from flask import Flask,render_template
from flask import request, Response
from flask_restful import Resource, Api
import json
import glob
import os.path


app = Flask(__name__)

@app.route('/client.min.js')
def hello():
	path = "./templates/client.min.js"
	return open(path, 'rb').read()



@app.route('/receive', methods=['POST'])
#@app.route('/receive')
def receive():
	dico={}
	data1=request.form['name']
	print(data1)
	newtab=data1.split(",")
	print(len(newtab))
	for el in newtab:
		print(el)
	#renewdata=data1.replace("u\'","\'")
	#f = open('history.json','a')
	#f.write(json.dumps(renewdata, indent=4))
	#json.dump(renewdata,f)
	dico['id']=newtab[0]
	dico['ip']=newtab[1]
	dico['timezone']=newtab[2]
	dico['processeur']=newtab[3]
	dico['useragent']=newtab[4]+newtab[5]
	dico['os']=newtab[6]
	dico['website']=newtab[7]
	f = open('./static/json_data/'+newtab[0]+'.json','w')
	f.write(json.dumps(dico, indent=4))
	#with open('history.json', mode='a') as file:
		#json.dump('{"id" : "'+newtab[0]+'"}',file)
	return ('fin')




@app.route('/dashboard')
def dashboard():
	path = "static/json_data/"
	fichier = []
	#l = glob.glob(path+'\\*.json')
	#for i in l:
	#	print ("noooooooooooowaaaaaay"+str(i))
	#	if os.path.isdir(i):
	#		fichier.extend(listdirectory(i))
	#	else:
	#		fichier.append(i)
	for root, dirs, files in os.walk(path):
		for i in files:
			print("fichhhhhhhhiiiiers : "+i)
			print("https://127.0.0.1:5000/"+root+i)
			fichier.append(os.path.join(root, i))
			#fichier.append("https://127.0.0.1:5000/"+root+i)
	return render_template('index.html',fichier=fichier, simple='simple')





if __name__ == '__main__':
	#app.run(debug=True, host='0.0.0.0', ssl_context=('../certs/web.squirrel.bad.crt','../cert.key'))
	app.run(debug=True, host='0.0.0.0', ssl_context=('adhoc')) # Debug mode with self signed certificate
