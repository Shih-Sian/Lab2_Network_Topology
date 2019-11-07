#!/usr/bin/python                                                                            
                                                                                             
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
#[TODO] Import the required module 'dumpNodeConnections' and 'CLI' here



'''
Build switchs and hosts with links
'''
class MyTopo(Topo):
    def build(self):
        print("[INFO] Building Topology")
        #[TODO] Define your topology here
        switch_s1 = self.addSwitch('s1')
        switch_s2 = self.addSwitch('s2')
        switch_s3 = self.addSwitch('s3')
        switch_s4 = self.addSwitch('s4')
        switch_s5 = self.addSwitch('s5')
        switch_s6 = self.addSwitch('s6') 
        host_h1 = self.addHost('h1')
        host_h2 = self.addHost('h2')
        host_h3 = self.addHost('h3')
        host_h4 = self.addHost('h4')
        host_h5 = self.addHost('h5')
        host_h6 = self.addHost('h6')
        host_h7 = self.addHost('h7')
        host_h8 = self.addHost('h8')
        self.addLink(h1, s1, bw = 20, delay = '4ms')
        self.addLink(s1, s3, bw = 40, delay = '3ms')
        self.addLink(h3, s3, bw = 25, delay = '2ms')     
        self.addLink(s3, s4, bw = 50, delay = '1ms')
        self.addLink(h5, s4, bw = 23, delay = '4ms')
        self.addLink(s4, s5, bw = 40, delay = '3ms')
        self.addLink(h7, s5, bw = 18, delay = '5ms')
        self.addLink(h8, s6, bw = 25, delay = '3ms')
        self.addLink(s4, s6, bw = 30, delay = '3ms')
        self.addLink(h6, s4, bw = 28, delay = '2ms')
        self.addLink(h4, s3, bw = 16, delay = '6ms')
        self.addLink(s2, s3, bw = 30, delay = '3ms')
        self.addLink(h2, s2, bw = 25, delay = '2ms')
    
        



'''
Create and test a simple network
'''
def simpleTest():
    # Create topology
    # Hint: You can add function arguments here if necessary
    topo = MyTopo()  

    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)

    # Start a network
    net.start()

    print("[INFO] Dumping connections information")
    #[TODO] Dump every host and switch connections
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)

    print("[INFO] Start CLI")
    CLI(net)



    # Stop a network
    net.stop()

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()
