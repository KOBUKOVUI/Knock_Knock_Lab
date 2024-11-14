#!/usr/bin/env python3

from socket import *
from itertools import permutations
import time

ip = "10.10.10.140"  # target IP

def Knockports(ports):
    for port in ports:
        try:
            print("[*] Knocking on port:", port)
            s2 = socket(AF_INET, SOCK_STREAM)
            s2.settimeout(0.1)  # set timeout to 0.1s
            s2.connect_ex((ip, port))
            s2.close()
        except Exception as e:
            print("[-] %s" % e)

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((ip, 1337))  # connect to port 1337 to grab three random ports
    r = eval(s.recv(1024))
    s.close()

    print("received:", r)

    for comb in permutations(r):  # try all the possibilities of 3-port orders
        print("\n[*] Trying sequence %s" % str(comb))
        Knockports(comb)

    print("[*] Done")

main()


#decrypted Ceaser 

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  
    return decrypted_text

def brute_force_caesar(ciphertext, reverse=False):
    for shift in range(1, 26):
        result = caesar_decrypt(ciphertext, shift)
        if reverse:
            result = result[::-1]  # Đảo ngược kết quả
        print(f"Shift {shift}: {result}")


ciphertext = "Khoor Zruog"  
brute_force_caesar(ciphertext, reverse=True)
