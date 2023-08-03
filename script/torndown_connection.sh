#!/usr/bin/bash

# delete network
nmcli connection down enp0s8_dhcp 2> /dev/null
nmcli connection delete enp0s8_dhcp 2> /dev/null

# delete routing
# change the network destination as needed
# Cisco Devnet APIC route
ip route del 10.10.20.0/24 via 10.0.3.2 dev enp0s8
# Gridtech network
#ip route del 172.20.1.0/24 via 10.0.3.2 dev enp0s8
