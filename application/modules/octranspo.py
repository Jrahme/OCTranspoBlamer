# Oc Transpo getter
import json
import requests

class OcTranspoGetter:
	#import credentials from file, my credentials are not in sample file,
	#they can be gotten from http://www.octranspo1.com/developers/
	def __init__(self):
		credentials = json.loads(open('../config/logins.json').read())[0]
		json.dumps(credentials)

		
		self.apiKey = credentials['apiLogin']['appId']
		self.apiPass = credentials['apiLogin']['apiKey']
		self.payLoad = {'appID':self.apiKey,'apikey':self.apiPass}

#Get live data
	def getLiveData(self,bus,stop):
		soapData = requests.get('https://api.octranspo1.com/v1.2/GetRouteSummaryForStop',params = self.payLoad)
		return soapData
		
		

#Get scheduled arrial time for bus
#	def getScheduledArrival(self,bus,stop):