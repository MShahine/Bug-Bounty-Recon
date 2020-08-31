#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  getthem.py
#  


from os import system
lista = ['tomnomnom/gf', 'tomnomnom/meg', 'tomnomnom/assetfinder', 'tomnomnom/httprobe', 'tomnomnom/unfurl', 'tomnomnom/fff', 'tomnomnom/waybackurls', 'ffuf/ffuf' ,'OJ/gobuster', 'lc/gau', 'hakluke/hakrawler', 'hakluke/hakrevdns', 'hakluke/hakcheckurl', 'hakluke/haksecuritytxt', 'hakluke/haktldextract']


for i in lista:
	cmd = 'go get github.com/'+i
	system(cmd)
print("*"*90)
print("done!")
