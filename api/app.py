from flask import request, Response
from flask import Flask,render_template
from urllib.parse import urlparse
from flask import request
from flask_restful import Resource, Api
from datetime import datetime
import collections
import json
import glob 
import os
import os.path  


app = Flask(__name__)

@app.route('/client.min.js')
def hello():
	path = "./templates/client.min.js"
	return open(path, 'rb').read()



@app.route('/receive', methods=['POST'])
def receive():
	path = "./static/json_data/"
	dico={}
	dicoOS={}
	isWin = 0
	isLinux = 0
	isOther = 0
	osclient=[]
	formatedata={}
	#datadomains={'y':3,'label':'sitetest'}
	datadomains={}
	data1=request.form['name']
	print(data1)
	newtab=data1.split(",")
	print(len(newtab))
	dico['id']=newtab[0]
	dico['ip']=newtab[1]
	dico['timezone']=newtab[2]
	dico['processeur']=newtab[3]
	dico['useragent']=newtab[4]+newtab[5]
	dico['os']=newtab[6]
	dico['website']=newtab[7]
	f = open('./static/json_data/'+newtab[0]+'.json','w')
	f.write(json.dumps(dico, indent=4))
	maintenant = datetime.now()
	nowdate=str(maintenant.year)+str(maintenant.month)+str(maintenant.day)
	print (nowdate)
	simpletuple=[]
	simpletupledomains=[]
	for root, dirs, files in os.walk(path):  
		for i in files:
			print("fichhhhhhhhiiiiers : "+i)
			if (not os.stat('./static/json_data/'+i).st_size == 0 and '2018' in str(i)):
				with open('./static/json_data/'+i) as f:
					data = json.load(f)
					print(data['os'])
					if ("Windows" in str(data['os'])):
						isWin+=1
						dicoOS['Windows']=isWin
					elif ("Debian" in str(data['os']) or "Ubuntu" in str(data['os'])):
						isLinux+=1
						dicoOS['Linux']=isLinux
					else:
						isOther+=1
						dicoOS['Autres']=isOther
					parsed_uri = urlparse(data['website'])
					domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
					print(domain)
					if(domain in datadomains):
						print('got a label')
						d=int(datadomains[domain])
						d+=1
						datadomains[domain]=d
					else:
						datadomains[domain]=domain
						datadomains[domain]=1

			if(str(nowdate) in str(i)):
				print("Voilà"+i)
				print(i.split('_'))
				res=i.split('_')[1]
				res=res[0:2]
				somekey=res
				if(str(somekey) in formatedata):
					s=int(formatedata[somekey])
					s=s+1
					print("sssssssssss"+str(s))
					formatedata[somekey]=s
				else:
					formatedata[somekey]=1
				print(' formated data :++++++++++++++++++++++++++++++++++++++++>'+str(formatedata))

				print("some_key : "+somekey)
	newformatedata=collections.OrderedDict(sorted(formatedata.items()))
	for item in newformatedata:
		rawdata = {}
		print(' yooooooooooooooooooooooooo'+str(newformatedata))
		print ("check my items : "+str(item))
		rawdata['x']=item
		rawdata['y']=newformatedata[item]
		simpletuple.append(rawdata)


	for item in datadomains:
		rawdatadomains = {}
		print(' D0MMMMMMMMMMMMMMMMMMMMMMMMAAAAAAAAAAAAAAAAAINNNNNNNNNNNNNNS :'+str(datadomains))
		print ("DOMAIN_ITEMS : "+str(item))
		rawdatadomains['label']=item
		rawdatadomains['y']=datadomains[item]
		simpletupledomains.append(rawdatadomains)

	f = open('./static/json_data/os.json','w')
	f.write(json.dumps(dicoOS))	
	print('simple tuple :        '+str(simpletuple))	
	f = open('./static/json_data/datastat.json','w')
	f.write(json.dumps(simpletuple))
	f = open('./static/json_data/domainstat.json','w')
	f.write(json.dumps(simpletupledomains))
	print(dicoOS)
	print(str(simpletupledomains))
	return ('fin')



@app.route('/dashboard')
def dashboard():
	path = "./static/json_data/"
	fichier = []
	for root, dirs, files in os.walk(path):  
		for i in files:
			print("fichhhhhhhhiiiiers : "+i)  
			fichier.append(os.path.join(root, i))
	return render_template('index.html',fichier=fichier, simple='simple')





if __name__ == '__main__':
	#app.run(debug=True, host='0.0.0.0', ssl_context=('../certs/web.squirrel.bad.crt','../cert.key'))
	app.run(debug=True, host='0.0.0.0', ssl_context=('adhoc')) # Debug mode with self signed certificate
