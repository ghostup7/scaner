import nmap

class reconosimiento:
    
    def __init__(self, rango):
        self.rango = rango
    
    def rec_red(self):
        nm = nmap.PortScanner()
        nm.scan(hosts=self.rango, arguments='-sT')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print('{0}:{1}'.host)

ran = reconosimiento("192.168.0.0/24")
ran.rec_red()