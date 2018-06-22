from django.shortcuts import render
from django.urls import reverse
import requests

# api addresses
nodeAddress = "http://localhost"
port = ":" + "10009" + "/" #handles user specifying invalid local host port
apiVault = "api/example/ious"
apiCreateIOU = "api/example/create-iou?iouValue="

#helper functions
def peerParse(astr):
	party1 = astr[2:astr.find(",")]
	location1 = astr[astr.find(",") + 4 : astr.find(",", astr.find(",") + 1)]
	country1 = astr[astr.find("C=") + 2:]
	peer = party1 + ", " + location1 + ", " + country1
	return(peer)

def listLogs(alist, ajson):  #parses ajson into alist of formatted strings
	for i in ajson:
		value = i['state']['data']['value']
		borrower = str(peerParse(i['state']['data']['borrower']))
		alist.append(borrower + " owing SGD" + str(value))

# views
def index(request):
	return(render(request, 'trade/index.html'))

def detail(request, hostport):
	port = ":" + hostport + "/"
	r = requests.get(nodeAddress + port + apiVault).json()
	x = []
	listLogs(x, r)
	return render(request, 'trade/detail.html', {'rends':x})

