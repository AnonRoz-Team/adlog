#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Author D4RK5H4D0W5
C0 = '\033[0;36m'
G0 = '\033[0;32m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
Y0 = '\033[0;33m'
import requests,sys,os
from multiprocessing.pool import ThreadPool
def scan(path):
	try:
		cek=requests.get(sys.argv[1]+path)
		if cek.status_code < 200 or cek.status_code <= 201:
			print '%s[ %sFOUND %s] %s'%(W0,G0,W0,sys.argv[1]+path)
			open('results.txt','a+').write(sys.argv[1]+path+'\n')
		else:
			print '%s[ %sNOT FOUND %s] %s'%(W0,R0,W0,sys.argv[1]+path)
	except Exception as r:
		print '%s%s\n'%(R0,r)
		pass

try:
	os.system('clear')
	print '''%s
    ___       ____
   /   | ____/ / /___  ____ _
  / /| |/ __  / / __ \/ __ `/   %sCoded by D4RKSH4D0WS%s
 / ___ / /_/ / / /_/ / /_/ /    %sFB gg.gg/AnonRoz-Team%s
/_/  |_\__,_/_/\____/\__, /     %sIG @anonroz_team%s
                    /____/      Admin Login Finder
	'''%(C0,W0,C0,W0,C0,W0,C0)
	sys.argv[1]
	ThreadPool(30).map(scan,open('adlog').read().splitlines())
	print '\n%s[ %sDONE %s] Saved in results.txt'%(W0,G0,W0)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W0,R0,W0,W0))
except IndexError:
	exit('%s[%s!%s] Use : python2 %s https://domain.com'%(W0,R0,W0,sys.argv[0]))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W0,R0,W0,W0))
