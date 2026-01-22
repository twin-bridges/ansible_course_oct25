### Main Project Exercise

You should use roles for this exercise.
* You should have a separate role for Gaia.
* You should have separate roles for the Mgmt Objects and for the FW Policy.
* You should use a shared role for handlers (which would be a required dependency for your other roles in meta/main.yml).

### Gaia Configuration
* Configure a static route for 172.31.128.0/21, interface "eth1", next hop 172.31.128.1
* Configure the following DNS Settings:
  * DNS1: "172.31.0.2"
  * DNS2: "8.8.8.8"
  * DNS3: "8.8.4.4"
  * DNS Domain: lasthop.io

Notes: try to ensure you decouple your tasks from your data. In other words, the specifics of the static route and of the DNS settings should be stored as role variables (and not directly hard-coded in the tasks).

### Mgmt Object Configuration
Host Objects
* Ansible Server, 3.125.34.232
* Windows SmartConsole, 172.31.12.101
* Windows SmartConsole Public, 3.71.9.240

Network Objects (with NAT auto hide behind the gateway)
* hq_net_128, 172.31.128.0/24
* hq_net_129, 172.31.129.0/24
* hq_net_130, 172.31.130.0/24
* hq_net_131, 172.31.131.0/24
* hq_net_132, 172.31.132.0/24
* hq_net_133, 172.31.133.0/24
* hq_net_134, 172.31.134.0/24
* hq_net_135, 172.31.135.0/24

DMZ Object (additional Host Object)
* Corp Web Server, 172.31.144.220

### FW Policy Configuration

First configure management access from the Ansible Server and SmartConsole to not lock us out (from the Ansible Server).

Allow "Any" access from the following to the firewall/mgmt server itself:
* Ansible Server
* Windows SmartConsole
* Windows SmartConsole Public

Also allow "Any", SSH access to the firewall itself (so we can SSH directly into clish/expert mode). AWS firewall has separate access restrictions.

Publish and Install your changes.

Configure HTTP/HTTPS access from Any source to "Corp Web Server" on the DMZ. Publish and Install your changes.

### Try to make all of the above Idempotent (ensure that you did this).

