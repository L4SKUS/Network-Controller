from mininet.topo import Topo

class topology(Topo):
    
    def __init__(self):
        Topo.__init__(self)
        
        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")
        s4 = self.addSwitch("s4")
        s5 = self.addSwitch("s5")
        s6 = self.addSwitch("s6")
        s7 = self.addSwitch("s7")
        s8 = self.addSwitch("s8")
        s9 = self.addSwitch("s9")
        s10 = self.addSwitch("s10")
        
        h1 = self.addHost("Warszawa", ip='10.0.0.1')
        h2 = self.addHost("Krakow", ip='10.0.0.2')
        h3 = self.addHost("Lodz", ip='10.0.0.3')
        h4 = self.addHost("Bydgoszcz", ip='10.0.0.4')
        h5 = self.addHost("Lublin", ip='10.0.0.5')
        h6 = self.addHost("Katowice", ip='10.0.0.6')
        h7 = self.addHost("Wroclaw", ip='10.0.0.7')
        h8 = self.addHost("Szczecin", ip='10.0.0.8')
        h9 = self.addHost("Gdansk", ip='10.0.0.9')
        h10 = self.addHost("Poznan", ip='10.0.0.10')
        
        
        # Delay = odległość w linii prostej * sqrt(2) / szybkość propagacji sygnału optycznego w światłowodzie 
        # Szybkość propagacji sygnału optycznego w światłowodzie = 200 000 km/s
        
        link_s1s2 = self.addLink(s1, s2, bw = 20, delay='1.78ms', loss=1, max_queue_size = 1000)
        link_s1s3 = self.addLink(s1, s3, bw = 20, delay='0.84ms', loss=1, max_queue_size = 1000)
        link_s1s4 = self.addLink(s1, s4, bw = 20, delay='1.60ms', loss=1, max_queue_size = 1000)
        link_s1s5 = self.addLink(s1, s5, bw = 20, delay='1.08ms', loss=1, max_queue_size = 1000)
        link_s2s6 = self.addLink(s2, s6, bw = 20, delay='0.49ms', loss=1, max_queue_size = 1000)
        link_s3s7 = self.addLink(s3, s7, bw = 20, delay='1.29ms', loss=1, max_queue_size = 1000)
        link_s4s8 = self.addLink(s4, s8, bw = 20, delay='1.64ms', loss=1, max_queue_size = 1000)
        link_s4s9 = self.addLink(s4, s9, bw = 20, delay='1.01ms', loss=1, max_queue_size = 1000)
        link_s7s10 = self.addLink(s7, s10, bw = 20, delay='1.02ms', loss=1, max_queue_size = 1000)

        link_s1s9 = self.addLink(s1, s9, bw = 20, delay='2.00ms', loss=1, max_queue_size = 1000)
        link_s2s3 = self.addLink(s2, s3, bw = 20, delay='1.36ms', loss=1, max_queue_size = 1000)
        link_s2s5 = self.addLink(s2, s5, bw = 20, delay='1.60ms', loss=1, max_queue_size = 1000)
        link_s3s4 = self.addLink(s3, s4, bw = 20, delay='1.27ms', loss=1, max_queue_size = 1000)
        link_s4s10 = self.addLink(s4, s10, bw = 20, delay='0.75ms', loss=1, max_queue_size = 1000)
        link_s6s7 = self.addLink(s6, s7, bw = 20, delay='1.19ms', loss=1, max_queue_size = 1000)
        link_s8s9 = self.addLink(s8, s9, bw = 20, delay='2.02ms', loss=1, max_queue_size = 1000)
        link_s8s10 = self.addLink(s8, s10, bw = 20, delay='1.38ms', loss=1, max_queue_size = 1000)

        
        
        link_s1h1 = self.addLink(s1, h1)
        link_s2h2 = self.addLink(s2, h2)
        link_s3h3 = self.addLink(s3, h3)
        link_s4h4 = self.addLink(s4, h4)
        link_s5h5 = self.addLink(s5, h5)
        link_s6h6 = self.addLink(s6, h6)
        link_s7h7 = self.addLink(s7, h7)
        link_s8h8 = self.addLink(s8, h8)
        link_s9h9 = self.addLink(s9, h9)
        link_s10h10 = self.addLink(s10, h10)
        
        
        
topos = { 'topology': ( lambda: topology( ) ) }