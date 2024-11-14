
# Knock_Knock Lab
This project is about capturing the flag in the VM Knock_Knock. In order to do that, we will have to use some techniques including "port knocking, an easy image cryptography and Buffer Overflow".

# Attacker & Target
Attacker: Kali Linux (192.168.190.132)

Target: Knock_Knock: Linux (192.168.190.134)

# Method
+ Scanned the network to discover the target server [Net Discover]
+ Port scanned the target to discover the running services and open ports [nmap]
+ Analysis and write script to brute force port knocking [port knockin]
+ Port scanned again to dicover the real open ports [nmap]
+ Web application vulnerability scanned to discover any web vulnerability [nikto]
+ Web information gathering and interacting with the web server [firefox]
+ Download picture and reveal the hidden information
+ Crack the cipher text to get login creditional in plain text [Caesar shift with ROT 13]
+ Login SSH with cracked login creditional
+ Look around and found suspicious program with SUID bit set
+ Analysis and work out PoC to exploit BoF vulnerability in the target program to get ROOT

# Walkthrough
See the docx 


