import sender as sender
#ip = "192.168.6.106"  					#Specify sender's ip here
ip = "127.0.0.1"
instance_name="firstpy"						#Specify name for instance here
image_id="44bc1de0-b04c-4d8d-bca6-645465980ac0"			#specify remote image id here
flavor_id="2"							#Specify flavor number/id here
ssh_key="anoop_key2"						#Specify key name here
print "Pick an option"
print "1. Create remote vm"
print "2. Delete remote vm"
choice = input()
ch = int(choice)
if ch==1:
	sender.createvm(ip,instance_name,image_id,flavor_id,ssh_key)
elif ch==2:
	sender.deletevm(ip,instance_name)
else:
	print "Invalid choice." 
