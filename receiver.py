import urllib2
import urllib
import json  
import os
def rec(ip):
	#req = urllib2.Request("http://10.10.10.208:8051")
	req = urllib2.Request(ip)
	print req
	req.add_header('Content-type', 'application/json')
	try:
		response = urllib2.urlopen(req)
	except  urllib2.HTTPError, e:
    		return None
	except urllib2.URLError, e:
    		return None
	
	res = response.read()
	res2 = json.loads(res)

	#t = eval(res)
	#print t
	return res2
