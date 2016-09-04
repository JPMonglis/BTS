#!/usr/bin/python
# coding: utf-8
import sys
import os
import re
import base64
import binascii
import urllib

# \
# Author: Paul Laîné
# Data: Sat Sep, 2016
# Version: 1.0
# /


def file_base64_to_text():
    try:
        path = raw_input("\nPlease enter the path of your file: ")
        try:
            data = open(path, 'r')
            content = data.read()
            print "[+] Start decoding the base 64 content ..."
            try:
                plain = base64.b64decode(content)
            except TypeError:
                return "Your bases 64 content don't work..."
            print "[+] Start decoding the base 64 content ... OK"
            data.close()
        except IOError:
            return "File not found ..."
        save = raw_input("Do you want to save the plain text (Y/N): ")
        if save == "y" or save == "Y":
            path_save = raw_input("Where you want to save the plain text: ")
            try:
                print "[+] Trying to generate the file ..."
                data = open(path_save, 'a')
                print "[+] Trying to generate the file ... OK"
                print "[+] Start writing the plain text on the file ..."
                data.write(plain)
                print "[+] Start writing the plain text on the file ... OK"
                data.close()
            except IOError:
                return "Ooops something goes wrong with your file, retry ..."
        raw_input("\nHit any key to continue ...")
        return plain
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def base64_to_text():
    try:
        while True:
            print "\nInput in base 64:"
            cypher = raw_input("Cypher> ")
            if re.match('^[a-zA-z0-9]+(=)?(==)?$', cypher):
                try:
                    print "Plain> "+base64.b64decode(cypher)+"\n"
                except TypeError:
                    print "Your base 64 input don't work"
            else:
                print "Input in base 64 please, bjAwYg== "
            if raw_input("\nAnother time (Y/N): ") in ("N", 'n'):
                break
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def file_binary_to_text():
    try:
        path = raw_input("\nPlease enter the path of you file: ")
        try:
            data = open(path, 'r')
            content = data.read()
            content = int(content, 2)
            print "[+] Start decoding the binary content ..."
            try:
                plain = binascii.unhexlify('%x' % content)
            except TypeError:
                return "Your binary content don't work"
            print "[+] Start decoding the binary content ... OK"
            data.close()
        except IOError:
            return "File not found ..."
        save = raw_input("Do you want to save the plain text (Y/N): ")
        if save == "y" or save == "Y":
            path_save = raw_input("Where you want to save the plain text: ")
            try:
                print "[+] Trying to generate the file ..."
                data = open(path_save, 'a')
                print "[+] Trying to generate the file ... OK"
                print "[+] Start writing the plain text on the file ..."
                data.write(plain)
                print "[+] Start writing the plain text on the file ... OK"
                data.close()
            except IOError:
                return "Ooops something goes wrong with your file, retry ..."
        raw_input("\nHit any key to continue ...")
        return plain
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def binary_to_text():
    try:
        while True:
            print "\nInput binary: "
            cypher = raw_input("Cypher> ")
            if re.match('^[0-1]+$', cypher):
                cypher = int(cypher, 2)
                try:
                    print "Plain> "+(binascii.unhexlify('%x' % int(cypher)))
                except TypeError:
                    print "Your binary input don't work..."
            else:
                print "Input a binary please, only 1 and 0"
            if raw_input("\nAnother time (Y/N): ") in ('N', 'n'):
                break
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def file_hexadecimal_to_text():
    try:
        path = raw_input("\nPlease enter the path of you file: ")
        try:
            data = open(path, 'r')
            content = data.read()
            print "[+] Start decoding the hexadecimal content ..."
            try:
                plain = base64.b16decode(content)
            except TypeError:
                return "Your hexadecimal content don't work..."
            print "[+] Start decoding the hexadecimal content ... OK"
            data.close()
        except IOError:
            return "File not found ... "
        save = raw_input("Do you want to save the plain text (Y/N): ")
        if save == "y" or save == "Y":
            path_save = raw_input("Where you want to save the plain text: ")
            try:
                print "[+] Trying to generate the file ..."
                data = open(path_save, 'a')
                print "[+] Trying to generate the file ... OK"
                print "[+] Start writing the plain text on the file ..."
                data.write(plain)
                print "[+] Start writing the plain text on the file ... OK"
                data.close()
            except IOError:
                return "Ooops something goes wrong with your file, retry ..."
        raw_input("\nHit any key to continue ...")
        return plain
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def hexadecimal_to_text():
    try:
        while True:
            print "\nInput hexadecimal: "
            cypher = raw_input("Cypher> ")
            if re.match('^[0-9a-fA-F]+', cypher):
                try:
                    print "Plain> "+(base64.b16decode(cypher))
                except TypeError:
                    print "Your hexadecimal input don't work..."
            else:
                print "Input a hexadecimal please"
            if raw_input("\nAnother time (Y/N): ") in ('N', 'n'):
                break
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def file_url_to_text():
    try:
        path = raw_input("\nPlease enter the path of you file: ")
        try:
            data = open(path, 'r')
            content = data.read()
            print "[+] Start encoding the URL..."
            try:
                plain = urllib.unquote(content)
            except TypeError:
                return "Your URL content don't work..."
            print "[+] Start encoding the URL ... OK"
            data.close()
        except IOError:
            return "File not found ... "
        save = raw_input("Do you want to save the plain text (Y/N): ")
        if save == "y" or save == "Y":
            path_save = raw_input("Where you want to save the cypher text: ")
            try:
                print "[+] Trying to generate the file ..."
                data = open(path_save, 'a')
                print "[+] Trying to generate the file ... OK"
                print "[+] Start writing the cypher text on the file ..."
                data.write(plain)
                print "[+] Start writing the cypher text on the file ... OK"
                data.close()
            except IOError:
                return "Ooops something goes wrong with your file, retry ..."
        raw_input("\nHit any key to continue ...")
        return plain
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def url_to_text():
    try:
        while True:
            print "\nInput URL: "
            cypher = raw_input("Cypher> ")
            try:
                print "Plain> " + urllib.unquote(cypher)
            except TypeError:
                print "Your URL don't work..."
            if raw_input("\nAnother time (Y/N): ") in ('N', 'n'):
                break
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def file_text_to_base64():
    try:
        path = raw_input("\nPlease enter the path of you file: ")
        try:
            data = open(path, 'r')
            content = data.read()
            print "[+] Start encode in base 64 the content ..."
            try:
                cypher = base64.b64encode(content)
            except TypeError:
                return "Your text input don't work..."
            print "[+] Start encode in base 64 the content ... OK"
            data.close()
        except IOError:
            return "File not found ..."
        save = raw_input("Do you want to save the cypher (Y/N): ")
        if save == "y" or save == "Y":
            path_save = raw_input("Where you want to save the cypher: ")
            try:
                print "[+] Trying to generate the file ..."
                data = open(path_save, 'a')
                print "[+] Trying to generate the file ... OK"
                print "[+] Start writing the cypher on the file ..."
                data.write(cypher)
                print "[+] Start writing the cypher on the file ... OK"
                data.close()
            except IOError:
                return "Ooops something goes wrong with your file, retry ..."
        raw_input("\nHit any key to continue ...")
        return cypher
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def text_to_base64():
    try:
        while True:
            print "\nInput some text: "
            plain = raw_input("Plain> ")
            if re.match('^(.)+$', plain):
                try:
                    print "Cypher> "+(base64.b64encode(plain))
                except TypeError:
                    print "Your text don't work 0_0"
            else:
                print "You don't input text!"
            if raw_input("\nAnother time (Y/N): ") in ('N', 'n'):
                break
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def file_text_to_binary():
    try:
        path = raw_input("\nPlease enter the path of you file: ")
        try:
            data = open(path, 'r')
            content = data.read()
            print "[+] Start encode in binary the content ..."
            try:
                cypher = bin(int(binascii.hexlify(content), 16)).split('b')
                cypher = cypher[0] + cypher[1]
            except TypeError:
                return "Your text input don't work retry ..."
            print "[+] Start encode in binary the content ... OK"
            data.close()
        except IOError:
            return "File not found ..."
        save = raw_input("Do you want to save the cypher (Y/N): ")
        if save == "y" or save == "Y":
            path_save = raw_input("Where you want to save you cypher: ")
            try:
                print "[+] Trying to generate the file ..."
                data = open(path_save, 'a')
                print "[+] Trying to generate the file ... OK"
                print "[+] Start writing the cypher on the file ..."
                data.write(cypher)
                print "[+] Start writing the cypher on the file ... OK"
                data.close()
            except IOError:
                return "Ooops something goes wrong with your file, retry ..."
        raw_input("\nHit any key to continue ...")
        return cypher
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def text_to_binary():
    try:
        while True:
            print "\nInput some binary: "
            plain = raw_input("Plain> ")
            if re.match('^(.)+$', plain):
                try:
                    cypher = bin(int(binascii.hexlify(plain), 16)).split('b')
                    print "Cypher> "+(cypher[0] + cypher[1])
                except TypeError:
                    print "Your text don't work 0_0"
            else:
                print "You don't input text!"
            if raw_input("\nAnother time (Y/N): ") in ('N', 'n'):
                break
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def file_text_to_hexadecimal():
    try:
        path = raw_input("\nPlease enter the path of you file: ")
        try:
            data = open(path, 'r')
            content = data.read()
            print "[+] Start encode in hexadecimal the content ..."
            try:
                cypher = base64.b16encode(content)
            except TypeError:
                return "Your text input don't work ..."
            print "[+] Start encode in hexadecimal the content ... OK"
            data.close()
        except IOError:
            return "File not found ..."
        save = raw_input("Do you want to save the cypher (Y/N): ")
        if save == "y" or save == "Y":
            path_save = raw_input("Where you want to save the cypher: ")
            try:
                print "[+] Trying to generate the file ..."
                data = open(path_save, 'a')
                print "[+] Trying to generate the file ... OK"
                print "[+] Start writing the cypher on the file ..."
                data.write(cypher)
                print "[+] Start writing the cypher on the file ... OK"
                data.close()
            except IOError:
                return "Ooops something goes wrong with your file, retry ..."
        raw_input("\nHit any key to continue ...")
        return cypher
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def text_to_hexadecimal():
    try:
        while True:
            print "\nInput some hexadecimal: "
            plain = raw_input("Plain> ")
            if re.match('^(.)+$', plain):
                try:
                    print "Cypher> "+(base64.b16encode(plain))
                except TypeError:
                    print "Your text don't work 0_0"
            else:
                print "You don't input text!"
            if raw_input("\nAnother time (Y/N): ") in ('N', 'n'):
                break
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def file_text_to_url():
    try:
        path = raw_input("\nPlease enter the path of you file: ")
        try:
            data = open(path, 'r')
            content = data.read()
            print "[+] Start decoding the URL..."
            try:
                plain = urllib.quote_plus(content)
            except TypeError:
                return "Your URL content don't work..."
            print "[+] Start decoding the URL ... OK"
            data.close()
        except IOError:
            return "File not found ... "
        save = raw_input("Do you want to save the plain text (Y/N): ")
        if save == "y" or save == "Y":
            path_save = raw_input("Where you want to save the plain text: ")
            try:
                print "[+] Trying to generate the file ..."
                data = open(path_save, 'a')
                print "[+] Trying to generate the file ... OK"
                print "[+] Start writing the plain text on the file ..."
                data.write(plain)
                print "[+] Start writing the plain text on the file ... OK"
                data.close()
            except IOError:
                return "Ooops something goes wrong with your file, retry ..."
        raw_input("\nHit any key to continue ...")
        return plain
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def text_to_url():
    try:
        while True:
            print "\nInput URL: "
            cypher = raw_input("Cypher> ")
            if re.match("^(https?://|www\.)[a-z-]+\.[a-z0-9-]+[a-z.]{0,4}/?[a-z0-9A-Z*_\-'();:@&=+$,/?#.]+$", cypher):
                try:
                    print "Plain> "+urllib.quote_plus(cypher)
                except TypeError:
                    print "Your URL don't work..."
            else:
                print "Input a good URL please"
            if raw_input("\nAnother time (Y/N): ") in ('N', 'n'):
                break
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def report(info):
    return "+" + "-" * 20 + "   REPORT   " + "-" * 20+"\n"+info+"\n+" + "-" * 52 + "\n"


def menu(info_version):
    style_on = '\x1b[7m'
    style_off = '\x1b[27m'
    notifications = ''
    if info_version == "active_version":
        set_version = 1
    elif info_version == "file_version":
        set_version = 2
    try:
        while True:
            os.system('clear')
            print notifications
            print "\t\t  " + style_on + " M A I N - M E N U " + style_off
            print "\n    01. Base 64 to text\t\t 05. Text to base 64"
            print "    02. Binary  to text\t\t 06. Text to binary"
            print "    03. Hexa    to text\t\t 07. Text to hexadecimal"
            print "    04. URL     to text\t\t 08. Text to URL"
            print "\n\t\t\t66. EXIT\n"
            rep = raw_input('strC0nv3rt/menu> ')
            if rep == 1 or rep == "1" and set_version == 2:
                plain = file_base64_to_text()
                notifications = report(plain)
            elif rep == 1 or rep == "1" and set_version == 1:
                base64_to_text()

            elif rep == 2 or rep == "2" and set_version == 2:
                plain = file_binary_to_text()
                notifications = report(plain)
            elif rep == 2 or rep == "2" and set_version == 1:
                binary_to_text()

            elif rep == 3 or rep == "3" and set_version == 2:
                plain = file_hexadecimal_to_text()
                notifications = report(plain)
            elif rep == 3 or rep == "3" and set_version == 1:
                hexadecimal_to_text()

            elif rep == 4 or rep == "4" and set_version == 2:
                plain = file_url_to_text()
                notifications = report(plain)
            elif rep == 4 or rep == "4" and set_version == 1:
                url_to_text()

            elif rep == 5 or rep == "5" and set_version == 2:
                cypher = file_text_to_base64()
                notifications = report(cypher)
            elif rep == 5 or rep == "5" and set_version == 1:
                text_to_base64()

            elif rep == 6 or rep == "6" and set_version == 2:
                cypher = file_text_to_binary()
                notifications = report(cypher)
            elif rep == 6 or rep == "6" and set_version == 1:
                text_to_binary()

            elif rep == 7 or rep == "7" and set_version == 2:
                cypher = file_text_to_hexadecimal()
                notifications = report(cypher)
            elif rep == 7 or rep == "7" and set_version == 1:
                text_to_hexadecimal()

            elif rep == 8 or rep == "8" and set_version == 2:
                cypher = file_text_to_url()
                notifications = report(cypher)
            elif rep == 8 or rep == "8" and set_version == 1:
                text_to_url()

            elif rep == 66 or rep == "66":
                os.system('clear')
                break

            else:
                os.system('clear')
                print "Input a good value ...\n"
    except KeyboardInterrupt:
        print "\nHave a nice day 1337."
        sys.exit()


def version():
    style_on = '\x1b[7m'
    style_off = '\x1b[27m'
    try:
        while True:
            os.system('clear')
            banner()
            print "\t\t  " + style_on + " M A I N - M E N U " + style_off + "\n"
            print "      01. Active version\t  02.File version"
            print "\n\t\t       66. EXIT"
            print "\n The active version is a instant conversion mode."
            print "\n In the file version you input a file and output\n a converted file"
            rep = raw_input("\nstrC0v3rt> ")
            if rep == 1 or rep == "1":
                menu('active_version')
            elif rep == 2 or rep == "2":
                menu('file_version')
            elif rep == 66 or rep == "66":
                print "\nHave a nice day 1337.\n"
                sys.exit()
    except KeyboardInterrupt:
        print "n\nHave a nice day 1337.\n"
        sys.exit()


def banner():
    r = '\x1b[31m'
    b = '\x1b[34m'
    y = '\x1b[33m'
    d = '\x1b[97m'

    print '\n' + b + ' [---]     The String Converter                          [---]'
    print ' [---]     Created by: ' + r + 'Paul Laîné' + b + ' (' + y + 'palaine' + b + ')              [---]'
    print '                   Version: ' + r + '1.2' + b
    print '                   Codename: ' + y + '\'strC0nv3rt\' ' + b
    print ' [---]     On GitHub: ' + y + 'https://www.github.com/palaine' + b + '     [---]' + d + '\n'


if __name__ == '__main__':
    sys.exit(version())
