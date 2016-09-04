#!/usr/bin/python
#coding: utf-8
import os

def main():
	r= '\x1b[31m'
	d= '\x1b[97m'
	
	print '['+r+'!'+d+'] Changing identity ...'
	print '[-] Start purging the config file ...'
	print '[-] echo "" > ~/.gitconfig'
	os.system('echo "" > ~/.gitconfig')
	print '[+] Purging the config file ... OK\n'
	
	print '[-] Start changing username ...'
	print '[-] git config --global user.name palaine'
	os.system('git config --global user.name palaine')
	print '[+] Username ... OK\n'
	
	print '[-] Start changing email ...'
	print '[-] git config --global user.email paullaine@protonmail.com'
	os.system('git config --global user.email paullaine@protonmail.com')
	print '[+] Email ... OK\n'
	
	print '['+r+'!'+d+'] Changing Git identity ... OK'
	print '['+r+'!'+d+'] Have nice commit'
	print '['+r+'!'+d+'] And see you later 1337.'
	print '['+r+'!'+d+'] Exiting from the program ...'

if __name__ == '__main__':
	main()
