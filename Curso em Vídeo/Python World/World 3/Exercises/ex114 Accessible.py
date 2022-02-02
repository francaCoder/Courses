"""
Verify if the website 'pudim.com.br' is accessible
"""

import urllib
import urllib.request

try:
    website = urllib.request.urlopen("http://pudim.com.br/")
except:
    print("[ERROR] I couldn't access the site.")
else:
    print("OK")
    print(website.read()) #HTML
