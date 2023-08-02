#!/usr/bin/bash

# configure network
nmcli connection down enp0s8_dhcp 2> /dev/null
nmcli connection delete enp0s8_dhcp 2> /dev/null
nmcli connection add con-name enp0s8_dhcp connection.interface-name enp0s8 type ethernet connection.autoconnect no ipv4.method auto
nmcli connection up enp0s8_dhcp 2> /dev/null

# configure routing
ip route del default
ip route add default via 192.168.1.1 dev enp0s3
# change the network destination as needed
ip route add 10.10.20.0/24 via 10.0.3.2 dev enp0s8
