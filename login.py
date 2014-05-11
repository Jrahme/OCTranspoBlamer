import json

class login(object):
	
	def __init__():
		logins = open('config/logins.json')
		formattedLogins = json.dumps(logins)
		self.loginSet = [formattedLogins]
		
	def ocTranspo():
		return self.loginSet['apiLogin']
		
	def databaseLogin():
		return self.loginSet['database']
		
