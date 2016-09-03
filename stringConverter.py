#!/usr/bin/python
#coding: utf-8 
import sys
import os
import re
import base64
import binascii

#\
# Author: Paul Laîné
# Data: Sat Sep, 2016
# Version: 1.0
#/

def base64ToText():
	try:
		path= raw_input("\nPlease enter the path of you file: ")
		try:
			data= open(path, 'r')
			content= data.read()
			print "[+] Start decoding the base 64 content ..."
			try:
				plain= base64.b64decode(content)
			except TypeError:
				return "Ooops something goes wrong, retry ..."
			print "[+] Start decoding the base 64 content ... OK"
			data.close()
		except IOError:
			return "Ooops something goes wrong, retry ..."
		save= raw_input("Do you want to save the plain text (Y/N): ")
		if save== "y" or save== "Y":
			path_save= raw_input("Where you want to save the plain text: ")
			try:
				print "[+] Trying to generat the file ..."
				data= open(path_save, 'a')
				print "[+] Trying to generat the file ... OK"
				print "[+] Start writing the plain text on the file ..."
				data.write(plain)
				print "[+] Start writing the palin text on the file ... OK"
				data.close() 
			except IOError:
				return "Ooops something goes wrong, retry ..."
		raw_input("\nHit any key to continue ...")
		return plain
	except KeyboardInterrupt, EOFError:
		print "\nHave a nive day 1337."

def binaryToText():
	try:
		path= raw_input("\nPlease enter the path of you file: ")
		try:
			data= open(path, 'r')
			content= data.read()
			content= int(content, 2)
			print "[+] Start decoding the binary content ..."
			try: 
				plain= binascii.unhexlify('%x' % content)
			except TypeError:
				return "Ooops something goes wrong, retry ..."
			print "[+] Start decoding the binary content ... OK"
			data.close()
		except IOError:
			return "Ooops something goes wrong, retry ..."
		save= raw_input("Do you want to save the plain text (Y/N): ")
		if save== "y" or save== "Y":
			path_save= raw_input("Where you want to save the plain text: ")
			try:
				print "[+] Trying to generat the file ..."
				data= open(path_save, 'a')
				print "[+] Trying to generat the file ... OK"
				print "[+] Start writing the plain text on the file ..."
				data.write(plain)
				print "[+] Start writing the palin text on the file ... OK"
				data.close() 
			except IOError:
				return "Ooops something goes wrong, retry ..."
		raw_input("\nHit any key to continue ...")
		return plain
	except KeyboardInterrupt, EOFError:
		print "\nHave a nive day 1337."
	
def hexaToText():
	try:
		path= raw_input("\nPlease enter the path of you file: ")
		try:
			data= open(path, 'r')
			content= data.read()
			print "[+] Start decoding the hexadecimal content ..."
			try: 
				plain= base64.b16decode(content)
			except TypeError:
				return "Ooops something goes wrong, retry ..."
			print "[+] Start decoding the hexadecimal content ... OK"
			data.close()
		except IOError:
			return "Ooops something goes wrong, retry ... 64165341"
		save= raw_input("Do you want to save the plain text (Y/N): ")
		if save== "y" or save== "Y":
			path_save= raw_input("Where you want to save the plain text: ")
			try:
				print "[+] Trying to generat the file ..."
				data= open(path_save, 'a')
				print "[+] Trying to generat the file ... OK"
				print "[+] Start writing the plain text on the file ..."
				data.write(plain)
				print "[+] Start writing the palin text on the file ... OK"
				data.close() 
			except IOError:
				return "Ooops something goes wrong, retry ... 777777777 "
		raw_input("\nHit any key to continue ...")
		return plain
	except KeyboardInterrupt, EOFError:
		print "\nHave a nive day 1337."

def textToBase64():
	try:
		path= raw_input("\nPlease enter the path of you file: ")
		try:
			data= open(path, 'r')
			content= data.read()
			print "[+] Start encode in base 64 the content ..."
			try:
				cypher= base64.b64encode(content)
			except TypeError:
				return "Ooops something goes wrong, retry ..."
			print "[+] Start encode in base 64 the content ... OK"
			data.close()
		except IOError:
			return "Ooops something goes wrong, retry ..."
		save= raw_input("Do you want to save the cypher (Y/N): ")
		if save== "y" or save== "Y":
			path_save= raw_input("Where you want to save the cypher: ")
			try:
				print "[+] Trying to generat the file ..."
				data= open(path_save, 'a')
				print "[+] Trying to generat the file ... OK"
				print "[+] Start writing the cypher on the file ..."
				data.write(cypher)
				print "[+] Start writing the cypher on the file ... OK"
				data.close() 
			except IOError:
				return "Ooops something goes wrong, retry ..."
		raw_input("\nHit any key to continue ...")
		return cypher
	except KeyboardInterrupt, EOFError:
		print "\nHave a nive day 1337."
	
def textToBinary():
	try:
		path= raw_input("\nPlease enter the path of you file: ")
		try:
			data= open(path, 'r')
			content= data.read()
			print "[+] Start encode in binary the content ..."
			try:
				cypher= bin(int(binascii.hexlify(content), 16)).split('b')
				cypher= cypher[0]+cypher[1]
			except TypeError:
				return "Ooops something goes wrong, retry ..."
			print "[+] Start encode in binary the content ... OK"
			data.close()
		except IOError:
			return "Ooops something goes wrong, retry ..."
		save= raw_input("Do you want to save the cypher (Y/N): ")
		if save== "y" or save== "Y":
			path_save= raw_input("Where you want to save you cypher: ")
			try:
				print "[+] Trying to generat the file ..."
				data= open(path_save, 'a')
				print "[+] Trying to generat the file ... OK"
				print "[+] Start writing the cypher on the file ..."
				data.write(cypher)
				print "[+] Start writing the cypher on the file ... OK"
				data.close() 
			except IOError:
				return "Ooops something goes wrong, retry ..."
		raw_input("\nHit any key to continue ...")
		return cypher
	except KeyboardInterrupt, EOFError:
		print "\nHave a nive day 1337."
	
def textToHexa():
	try:
		path= raw_input("\nPlease enter the path of you file: ")
		try:
			data= open(path, 'r')
			content= data.read()
			print "[+] Start encode in hexadecimal the content ..."
			try:
				cypher= base64.b16encode(content)
			except TypeError:
				return "Ooops something goes wrong, retry ..."
			print "[+] Start encode in hexadecimal the content ... OK"
			data.close()
		except IOError:
			return "Ooops something goes wrong, retry ..."
		save= raw_input("Do you want to save the cypher (Y/N): ")
		if save== "y" or save== "Y":
			path_save= raw_input("Where you want to save the cypher: ")
			try:
				print "[+] Trying to generat the file ..."
				data= open(path_save, 'a')
				print "[+] Trying to generat the file ... OK"
				print "[+] Start writing the cypher on the file ..."
				data.write(cypher)
				print "[+] Start writing the cypher on the file ... OK"
				data.close() 
			except IOError:
				return "Ooops something goes wrong, retry ..."
		raw_input("\nHit any key to continue ...")
		return cypher
	except KeyboardInterrupt, EOFError:
		print "\nHave a nive day 1337."
	
def report(info):
	os.system('clear')
	print "+"+"-"*20+"   REPORT   "+"-"*20
	print "\n"
	print info
	print "+"+"-"*52+"\n"
	

def menu():
	styleOn= '\x1b[7m'
	styleOff= '\x1b[27m'
	try:
		while True:
			print "\t\t  "+styleOn+" M A I N - M E N U "+styleOff
			print "\n    01. Base 64 to text\t\t 04. Text to base 64"
			print "    02. Binary  to text\t\t 05. Text to binary"
			print "    03. Hexa    to text\t\t 06. Text to hexadecimal"
			print "\n\t\t\t66. EXIT"
			print "\t\t\t77. BANNER\n"
			rep= raw_input('strC0nv3rt/menu> ')
			if rep== 1 or rep== "1":
				plain= base64ToText()
				report(plain)
			
			elif rep== 2 or rep== "2":
				plain= binaryToText()
				report(plain)
				
			elif rep== 3 or rep== "3":
				plain= hexaToText()
				report(plain)
				
			elif rep== 4 or rep== "4":
				cypher= textToBase64()
				report(cypher)
			
			elif rep== 5 or rep== "5":
				cypher= textToBinary()
				report(cypher)
			
			elif rep== 6 or rep== "6":
				cypher= textToHexa()
				report(cypher)
			
			elif rep== 66 or rep== "66":
				print "Have a nive day 1337."
				break
			
			elif rep== 77 or rep== "77":
				os.system('clear')
				banner()
			else:
				os.system('clear')
				print "Input a good value ...\n"
	except KeyboardInterrupt, EOFError:
		print "\nHave a nive day 1337."
		
def banner():
	r= '\x1b[31m'
	b= '\x1b[34m'
	y= '\x1b[33m'
	d= '\x1b[97m'

	print '\n'+b+' [---]     The String Converter                          [---]'
	print ' [---]     Created by: '+r+'Paul Laîné'+b+' ('+y+'palaine'+b+')              [---]'
	print '                   Version: '+r+'1.1'+b
	print '                   Codename: '+y+'\'strC0nv3rt\' '+b
	print ' [---]     On Github: '+y+'https://www.github.com/palaine'+b+'     [---]'+d+'\n'
	
if __name__ == '__main__':
    banner()
    sys.exit(menu())
