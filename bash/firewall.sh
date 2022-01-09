#!/usr/bin/env bash

# This will configure IPTables with some basic rules.

echo "Configuring Firewall...";
iptables -A INPUT -s 192.168.1.254/24 -j ACCEPT;
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT;
iptables -A INPUT -p tcp --dport 443 -j ACCEPT;
iptables -A INPUT -p tcp --dport 80 -j ACCEPT;
iptables -A INPUT -j DROP;
iptables -A FORWARD -j DROP;
iptables -A OUTPUT -j ACCEPT;
echo "Firewall Setup Successfully!";
iptables -L
exit 0;
