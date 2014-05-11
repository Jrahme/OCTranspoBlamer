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
		#self.apiKey = credentials['apiLogin']['apiKey']
		#self.apiKey = '79e65ca434f89797b63aa0bb4c9ae528'
		self.payLoad = {'apiID':self.apiID,'apiKey':self.apiKey}

		print self.payLoad

#Get live data
	def getLiveData(self,bus,stop):
		self.payLoad['stopNum'] = stop
		soapData = requests.post('https://api.octranspo1.com/v1.2/GetRouteSummaryForStop',data = self.payLoad)
		return soapData
		
		

#Get scheduled arrial time for bus
#	def getScheduledArrival(self,bus,stop):