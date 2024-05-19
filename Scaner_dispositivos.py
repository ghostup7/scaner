from scapy.all import ARP, Ether, srp
from scapy.all import ARP, Ether, srp

def escanear_red(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    paquete = ether/arp

    result = srp(paquete, timeout=3, verbose=0)[0]

    dispositivos = []

    for sent, received in result:
        dispositivos.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Dispositivos conectados a la red:")
    print("IP" + " "*18+"MAC")
    for dispositivo in dispositivos:
        print("{:16}    {}".format(dispositivo['ip'], dispositivo['mac']))

escanear_red("192.168.0.0/24")
