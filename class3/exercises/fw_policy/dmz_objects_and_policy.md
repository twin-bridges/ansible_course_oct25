
Use the 'check_point.mgmt.cp_mgmt_host' module to create a host object for 'Corp Web Server' with an IP address
of '172.31.144.220'. Publish this change using a handler.

Use the 'check_point.mgmt.cp_mgmt_access_rule' module to add a firewall rule at position "1" specifying that
"Any" source can reach the DMZ "Corp Web Server" for "http" and "https" services. Use handler to both publish
this change and to install the new firewall policy.

