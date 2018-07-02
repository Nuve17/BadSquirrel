#! /usr/bin/python
# coding: utf-8

import os, sys, argparse
import threading
from time import sleep
import signal
# Mylib
from http_server import web_server
from http_transparent import interception_http
from https_transparent import interception_https
from graphismes import banniere

def main():

	parser = argparse.ArgumentParser(description='ESGI final projet')
	parser.add_argument('-i', '--interface',help='Interface used for MITM ')
	args = parser.parse_args()

	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	os.system("iptables -t nat -A POSTROUTING -o"+args.interface+" -j MASQUERADE")

	os.system("service dnsmasq start") # Start du serveur DHCP

	"""	# configure routing (IPTABLES)
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 9090")
	os.system("ip6tables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
	os.system("ip6tables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 9090")"""
	#Action a effectuer

	try:
		http_server_thread = threading.Thread(target=web_server)
		print("[+]Lancement du thread http_server")
		http_server_thread.start()
		interception_http_thread = threading.Thread(target=interception_http)
		print("[+]Lancement du thread interception_http")
		interception_http_thread.start()
		sleep(1)
		interception_https_thread = threading.Thread(target=interception_https)
		print("[+]Lancement du thread interception_https")
		interception_https_thread.start()
		print "[+] Ready for interception !! "
		#Force a rester dans le try:
		while True:
			pass
	#Action a effectuer avant la fermeture de script
	except KeyboardInterrupt as e:
		print "[+]InteruptionOK clavier"
		print "[+]Fermeture du serveur web"
		#http_server_thread.join()
		print "[+]Fermeture des proxys"
		#interception_http_thread.join()
		#interception_https_thread.join()
		os.system("service dnsmasq stop") # Start du serveur DHCP
		print "[+]Suppréssion des regles iptables"
		os.system("bash ./ShellScript/CleanIpTables.sh")
		print "Bye"
		os.kill( os.getpid(), signal.SIGKILL)


banniere()
main()
