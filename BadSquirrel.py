#! /usr/bin/Python
# coding: utf-8

import os, sys, argparse
import threading
# Mylib
import http_server
from http_transparent import interception_http
from https_transparent import interception_https

from graphismes import banniere

def main():

	parser = argparse.ArgumentParser(description='ESGI final projet')
	parser.add_argument('-i', '--interface',help='Interface used for MITM ')
	args = parser.parse_args()
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	os.system("iptables -t nat -A POSTROUTING -o"+args.interface+" -j MASQUERADE")

	"""	# configure routing (IPTABLES)
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 9090")
	os.system("ip6tables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
	os.system("ip6tables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 9090")"""
	#Action a effectuer

	try:
		http_server_thread = threading.Thread(target=http_server.start)
		print("Lancement du thread http_server")
		http_server_thread.start()
		interception_http_thread = threading.Thread(target=interception_http)
		print("Lancement du thread interception")
		interception_http_thread.start()
		#interception_http_thread.join(1)
		interception_https_thread = threading.Thread(target=interception_https)
		print("Lancement du thread interception_https")
		interception_https_thread.start()
		#http_server.main()
	#Action a effectuer avant la fermeture de script

	except KeyboardInterrupt:
		print "fermeture des threds"
		#http_server_thread.join(10)
		print "fermeture des threads"

		interception_https_thread._stop()
		print "Interuption clavier"
		print "suppréssion des regles iptables"
		os.system("bash CleanIpTables.sh")
		sys.exit()

banniere()
main()
