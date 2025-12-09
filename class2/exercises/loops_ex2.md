
Use cp_mgmt_simple_gateway_facts to retrieve facts about the firewall.

From this output, extract the '.ansible_facts.simple_gateway.interfaces' 
which will be a list of interfaces.

Loop over this list of interfaces and for only 'eth0' print out the
name, ipv4-address and ipv4-network-mask. In this task you should combine a
loop and a conditional ("when" statement).

