from flask import Flask,request
import requests,json
app=Flask(__name__)
@app.route('/')
def ahmed():
	return '<center><h3><a href="https://t.me/Z_2_W">MY</center></h3>'
@app.route('/CheckVisa/',methods=['GET'])
def Check():
	visa=request.args.get('Visa')
	url='https://www.visatk.com/checker/api.php'
	head={
'Host':'www.visatk.com',
'Connection':'keep-alive',
'Content-Length':'39',
'Accept':'*/*',
'X-Requested-With':'XMLHttpRequest',
'User-Agent':'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A025F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Origin':'https://www.visatk.com',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Referer':'https://www.visatk.com/checker/',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'ar-EG,ar-AE;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
'Cookie':'__gads=ID=85acc2e4ed870ea2-22365cbda9d10068:T=1649520506:RT=1649520506:S=ALNI_MYRCbX-o2gAiVR1oHahSjOlTySfPw; __gpi=UID=0000086efcc654df:T=1654670511:RT=1655027513:S=ALNI_Mb7MwBQpDN33zxwwfJKsv3ZlkFEQg'
}
	data={
'data':visa
}

	p=(requests.post(url,headers=head,data=data).text)
	if 'Live' in p:
		return {'data':{'Live ':visa},'Dev':'Azef','TG':'https://t.me/Z_2_W'}
	elif 'Unknown' in p:
		return {'data':{'Unknown ':visa},'Dev':'Azef','TG':'https://t.me/Z_2_W'}
	else:
		return {'data':{'Die ':visa},'Dev':'azef','TG':'https://t.me/Z_2_W'}
app.run(host='0.0.0.0', port=81)