#!/usr/bin/python
#coding: utf-8

#\
# Author: Paul Laîné
# Date: Sat Sep 3, 2016
# Version: 1.1
#/
import os
import re 
import sys

def report(base16, base10, base8, base2):
	os.system('clear')
	print "+"+"-"*20+"   REPORT   "+"-"*20
	print "|  Hexadecimal: \t"+base16
	print "|  Decimal:\t\t"+base10
	print "|  Octal:\t\t"+base8
	print "|  Binary:\t\t"+base2
	print "+"+"-"*52+"\n"

def menu():
	styleOn= '\x1b[7m'
	styleOff= '\x1b[27m'
 
	while True:
		print "\t\t  "+styleOn+" M A I N - M E N U "+styleOff
		print "\n\t01. Hexadecimal to other"
		print "\t02. Decimal     to other"
		print "\t03. Octal       to other"
		print "\t04. Binary      to other"
		print "\n\t66. EXIT\n"

		rep= raw_input('b4s3/menu> ')

		if rep== 1 or rep== '1':
			print '\nInput a base 16 number ...'
			hexa= raw_input('b4s3/menu/hexa> ')
			if re.match( '^[0-9a-fA-F]+$', hexa):
				decimal= str(int(hexa, 16))
				octal=   oct(int(hexa, 16))[1:]
				binary=  bin(int(hexa, 16)).split('0b')[1]
				report(hexa, decimal, octal, binary)

		elif rep== 2 or rep== '2':
			print '\nInput a base 10 number ...'
			decimal= raw_input('b4s3/menu/decimal> ')
			if re.match('^[0-9]+$', decimal):
				hexa=   hex(int(decimal)).split('0x')[1]
				octal=  oct(int(decimal))[1:]
				binary= bin(int(decimal)).split('0b')[1]
				report(hexa, decimal, octal, binary)
		
		elif rep== 3 or rep== '3':
			print '\nInput a base 8 number ...'
			octal= raw_input('b4s3/menu/octal> ')
			if re.match('^[0-9]+$', octal):
				hexa=    hex(int(octal, 8)).split('0x')[1]
				decimal= str(int(octal, 8))
				binary=  bin(int(octal, 8)).split('0b')[1]
				report(hexa, decimal, octal, binary)

		elif rep== 4 or rep== '4':
			print '\nInput a base 2 number ...'
			binary= raw_input('b4s3/menu/binary> ')
			if re.match( '^[0-1]+$', binary):
				hexa=    hex(int(binary, 2)).split('0x')[1]
				decimal= str(int(binary, 2))
				octal=   oct(int(binary, 2))[1:]
				report(hexa, decimal, octal, binary)

		elif rep== 66 or rep== '66':
			print "Have a nice day 1337\n"
			exit()
		else:
			print "Input a good value ...\n"
			pass

def banner():
	r= '\x1b[31m'
	b= '\x1b[34m'
	y= '\x1b[33m'
	d= '\x1b[97m'

	print '\n'+b+' [---]     The base (10/2/8) Converter                   [---]'
	print ' [---]     Created by: '+r+'Paul Laîné'+b+' ('+y+'palaine'+b+')              [---]'
	print '                   Version: '+r+'1.1'+b
	print '                   Codename: '+y+'\'b4s3\' '+b
	print ' [---]     On Github: '+y+'https://www.github.com/palaine'+b+'     [---]'+d+'\n'
	 
if __name__ == "__main__" :
	banner()
	sys.exit(menu())
