import xml.etree.ElementTree as ET

def soapToJson(soapData):
	tree = ET.parse(soapData);
	relevantData = tree.find('.//{http://schemas.xmlsoap.org/soap/envelope/}xmlns')
	return relevantData