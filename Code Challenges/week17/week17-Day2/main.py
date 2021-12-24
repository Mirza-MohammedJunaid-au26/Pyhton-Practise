"""

describe CAP Theorem ?

                                            ____________________
                                           |                    |
                                           |                    |
                                           |     CONSISTENCY    |
                               ____________|____         _______|________
                               \           |    \       /       |       /
                                \          | CA  \     /    CP  |      /                                     
                                 \         |_____ \___/_________|     /
                                  \                \ /               /
                                   \  AVAILABILITY /\   PARTITION   /
                                    \             /AP\  TOLERANCE  /
                                     \___________/____\ __________/


Consistency
Consistency means that all clients see the same data at the same time, no matter which node they connect to. For this to happen, whenever data is written to one node, it must be instantly forwarded or replicated to all the other nodes in the system before the write is deemed successful.

Availability
Availability means that that any client making a request for data gets a response, even if one or more nodes are down. Another way to state this—all working nodes in the distributed system return a valid response for any request, without exception.

Partition tolerance
A partition is a communications break within a distributed system—a lost or temporarily delayed connection between two nodes. Partition tolerance means that the cluster must continue to work despite any number of communication breakdowns between nodes in the system.


"""

"""

Explain DHCP, ARP and NAT ?

---> DHCP :

Dynamic Host Configuration Protocol (DHCP) is a network management protocol used to dynamically assign an IP address to nay device, or node, on a network so they can communicate using IP (Internet Protocol).

DHCP does the following:
-> DHCP manages the provision of all the nodes or devices added or dropped from the network.
-> DHCP maintains the unique IP address of the host using a DHCP server.
-> It sends a request to the DHCP server whenever a client/node/device, which is configured to work with DHCP, connects to a network. The server acknowledges by providing an IP address to the client/node/device.

---> ARP :

ARP: ARP stands for (Address Resolution Protocol) it is responsible to find the hardware address of a host from a know IP address there are three basic ARP terms.

The important terms associated with ARP are: 

1) ARP Cache: After resolving the MAC address, the ARP sends it to the source where it is stored in a table for future reference. The subsequent             
   communications can use the MAC address from the table
2) ARP Cache Timeout: It indicates the time for which the MAC address in the ARP cache can reside
3) ARP request: This is nothing but broadcasting a packet over the network to validate whether we came across the destination MAC address or not. 
    -> The physical address of the sender.
    -> The IP address of the sender.
    -> The physical address of the receiver is FF:FF:FF:FF:FF:FF or 1’s.
    -> The IP address of the receiver
4) ARP response/reply: It is the MAC address response that the source receives from the destination which aids in further communication of the data. 
   
---> NAT :

Network Address Translation (NAT) conserves IP addresses by enabling private IP networks using unregistered IP addresses to go online. Before NAT forwards packets between the networks it connects, it translates the private internal network addresses into legal, globally unique addresses.

NAT configurations can reveal just one IP address for an entire network to the outside world as part of this capability, effectively hiding the entire internal network and providing additional security. Network address translation is typically implemented in remote-access environments, as it offers the dual functions of address conservation and enhanced security.

"""

# lONGEST PALINDROME

def palindrome(s):
    pairs = 0
    unpaired_chars = set()
        
    for char in s:
        if char in unpaired_chars:
            pairs += 1
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)
        
    return pairs * 2 + 1 if unpaired_chars else pairs * 2

str = "abccccdd"
print(palindrome(str))
