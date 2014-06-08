import sys
import pickle
import xml.etree.ElementTree as eTree
sys.path.insert(0, 'modules')
from octranspo import OcTranspoGetter
import utilities

octranspo = OcTranspoGetter()
soapData = octranspo.getStopInfo('118','2954')

root =  eTree.fromstring(soapData.text)

for child in root:
	for grandchild in child:
		for greatgrandchild in grandchild:
			print greatgrandchild.tag

for details in root.iter('Routes'):
	print details.attrib
	print details.tag



'''
credentit = 'database': {'username': 'null', 'host': 'null', 'password': 'null', 'port': 'null'}, 'apiLogin': {'apiID': 'apiID', 'apiKey': 'apikey'}}
file = open('../config/logins.ser','w');
pickle.dump(credentials,file)
file.close()
'''