from Banner import banner
from Scaner_soccket import Scaner_ip

banner()

ip_scaner = Scaner_ip('192.168.0.27')
ip_scaner.Escaneo_socket()