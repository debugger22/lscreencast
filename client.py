import socket,os
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5005))

dst="E:\\Kiosk\\"

while True:
	#folder name
	fln = client_socket.recv(4)
	os.chdir(dst);
	dst = "E:\\Kiosk\\"+fln+"\\"
	if not os.path.exists(dst): os.makedirs(dst)
	fname = client_socket.recv(4)
	os.chdir(dst)
	fname = fname+'.jpg'
	fp = open(fname,'wb')
	# image
	while True:
	    strng = client_socket.recv(1024)
	    if not strng:
	        break
	    fp.write(strng)
	fp.close()
print "Data Received successfully"
exit()
#time.sleep(10)

#data = 'viewnior '+fname
#os.system(data)