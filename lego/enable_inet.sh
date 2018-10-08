dudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -F INPUT
sudo iptables -F OUTPUT
sudo iptables -F FORWARD
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -t nat -A POSTROUTING --out-interface wlp2s0 -j MASQUERADE  
sudo iptables -A FORWARD --in-interface enp0s20u2 -j ACCEPT

