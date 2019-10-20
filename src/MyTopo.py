#!/usr/bin/python                                                                            
                                                                                             
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.log import setLogLevel
#[TODO] Import the required module 'dumpNodeConnections' and 'CLI' here



'''
Build switchs and hosts with links
'''
class MyTopo(Topo):
    def build(self):
        print("[INFO] Building Topology")
        #[TODO] Define your topology here




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


    print("[INFO] Start CLI")
    #[TODO] Start CLI mode



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