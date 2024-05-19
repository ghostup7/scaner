import socket
from tqdm import tqdm
import nmap

class Scaner_ip:

    def __init__(self, host):
        self.host = host
        self.inicio = 1
        self.fin =  65500
        self.puertos_abiertos = [] 

    def Escaneo_ip_locales():
        None

    def Escaneo_socket(self):

        try:
            for puerto in tqdm(range(self.inicio, self.fin+1),desc="Escaneo de puertos"):
                
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                
                resultado_sock = sock.connect_ex((self.host, puerto))
                
                if resultado_sock == 0:
                    self.puertos_abiertos.append(puerto)
                sock.close()

            print(f'\n[$] Puertos abiertos en {self.host} entre {self.inicio} y {self.fin}: {self.puertos_abiertos}')

        except:
            print(f'\n[!]No se pudo ejecutarel escaeo a la ip {self.host}')

# Crear una instancia de la clase y llamar al método
#ip_scaner = Scaner_ip('192.168.0.27')

#ip_scaner.Escaneo_socket()