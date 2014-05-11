import sys
import pickle
sys.path.insert(0, 'modules')
from octranspo import OcTranspoGetter
import utilities

octranspo = OcTranspoGetter();
soapData = octranspo.getLiveData('3017','94')

print soapData.text

'''
credentials = {'database': {'username': 'null', 'host': 'null', 'password': 'null', 'port': 'null'}, 'apiLogin': {'apiID': 'apiID', 'apiKey': 'apikey'}}
file = open('../config/logins.ser','w');
pickle.dump(credentials,file)
file.close()
'''