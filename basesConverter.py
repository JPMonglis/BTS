#!/usr/bin/python
#coding: utf-8

#\
# Author: Paul Laîné
# Date: Thu Sep 1, 2016
# Version: 1.0
#/
def base10():
	print "b4se/menu/base10>"

def base8():
	print "b4s3/menu/base8>"

def base2():
	print "b4s3/menu/base2>"

def menu():
	styleOn= '\x1b[7m'
	styleOff= '\x1b[27m'
 
	while True:
		print "\t\t  "+styleOn+" M A I N - M E N U "+styleOff
		print "\n\t01. Insert base 10 number"
		print "\t02. Insert base 8 number"
		print "\t03. Insert base 2 number"
		print "\t66. EXIT\n"

		rep= raw_input('b4s3/menu> ')
		if rep== 1 or rep== '1':
			base10()
		elif rep== 2 or rep== '2':
			base8()
		elif rep== 3 or rep== '3':
			base2()
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
	print '                   Version: '+r+'1.0'+b
	print '                   Codename: '+y+'\'b4s3\' '+b
	print ' [---]     On Github: '+y+'https://www.github.com/palaine'+b+'     [---]'+d+'\n'
	 
if __name__ == "__main__" :
	banner()
	menu()
