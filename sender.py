"""IMAGE_ID=""  #Paste image ID here
FLAVOR_ID=""	#Paste Flavor_ID here
SSH_KEY=""	#Paste key name here - Assuming key already exists"""
from wsgiref.simple_server import make_server
import json

def createvm(ip,instance_name,image_id,flavor_id,ssh_key=None):
	"""Creates an instance remotely"""
	if ssh_key==None:
		print "SSH key not found"
		print "Create a new key and try again"
		
	else:
		global cmd 
		cmd= "nova boot "+instance_name+" --image \""+image_id+"\" --flavor "+flavor_id+" --key-name "+ssh_key
		send(ip)
		""" Now, send cmd to the ip specified in the parameters through a server.
		    Receive at the other end and execute as a command"""  

def deletevm(ip,instance_name):
	global cmd
	cmd = "nova delete "+instance_name
	send(ip)
	

def application(environ, start_response):
	global cmd
	#result = get_data 
	response_body = json.dumps(cmd)
	status = '200 OK'
	response_headers = [('Content-Type', 'application/json'),
               	  ('Content-Length', str(len(response_body)))]
        start_response(status, response_headers)
	print response_body
       	return [response_body]


def send(ip_addr):
	httpd = make_server(ip_addr,8051,application)
	httpd.handle_request()	
