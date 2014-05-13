# Oc Transpo getter
import json
import requests
import pickle

class OcTranspoGetter:
	#import credentials from file, my credentials are not in sample file,
	#they can be gotten from http://www.octranspo1.com/developers/
	def __init__(self):
		credFile = open('../config/logins.ser')
		credentials = pickle.load(credFile)
		
		self.apiID = credentials['apiLogin']['apiID']
		self.apiKey = credentials['apiLogin']['apiKey']
		self.payLoad = {'appID':self.apiID,'apiKey':self.apiKey}

		print self.payLoad

#Get live data
	def getLiveData(self,bus,stop,route):
		self.payLoad['routeNo'] = route
		self.payLoad['stopNo'] = stop
		soapData = requests.post('https://api.octranspo1.com/v1.2/GetNextTripsForStop',data = self.payLoad)
		return soapData

	def getStopInfo(self,bus,stop):
		self.payLoad['stopNo'] = stop
		soapData = requests.post('https://api.octranspo1.com/v1.2/GetRouteSummaryForStop', data = self.payLoad)
		return soapData

#Get scheduled arrial time for bus
#	def getScheduledArrival(self,bus,stop):