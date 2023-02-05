import sys
from scapy.all import *

def sniffBeacons(p):
    if p.haslayer(Dot11Beacon):
        if p.addr2 == ap_mac.lower():
            print("\r{0}      {1}".format(ap_mac,-(256 - ord(p.notdecoded[:1]))), end="")


if __name__=='__main__':
    if(len(sys.argv) != 3):
        print("[*] How to use?\n# python3 {} [interface_name] [ap_mac]".format(sys.argv[0]))
        print("ex) python3 {} wlan0 11:22:33:44:55:66".format(sys.argv[0]))
        sys.exit(0)

    global ap_mac
    ap_mac = sys.argv[2]

    print("      AP_MAC           SIG")
    sniff(iface=sys.argv[1], prn=sniffBeacons)
