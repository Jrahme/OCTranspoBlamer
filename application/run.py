import sys
sys.path.insert(0, 'modules')

from octranspo import OcTranspoGetter
import utilities

octranspo = OcTranspoGetter();

soapData = octranspo.getLiveData('3017','94')

print soapToJson(soapData)