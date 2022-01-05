#!/bin/bash
IP_ADDRESS=$(curl ifconfig.me/ip)
printf "[*] Your IP Address Is: $IP_ADDRESS"
