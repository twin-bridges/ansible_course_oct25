
Use the 'cp_gaia_static_route' module to configure a new static route of 172.31.128.0/21
with a next_hop of 172.31.128.1 using interface eth1.

Use 'cp_gaia_routes_facts' to verify the routing table after configuration.

Extract the new route and use assert/that conditions to verify the route is correct. This
verification should ensure that 172.31.128.0/21 is in the routing table, has a next_hop
of '172.31.128.1' and uses interface 'eth1'.

Note: you will probably need to loop over the entire routing table and find the correct route
using a conditional.

