#Email_Extractor.py
#Name:dohyun kim
#Date:2020/02/19
#Assignment:email exracting

import urllib.request
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from re import *

def main():

    #prompt the user for a webpage url
    #url = 'https://www.unomaha.edu/college-of-information-science-and-technology/about/faculty-staff/index.php'
    print("if it does not pass to input URL and pop-up in chrome browser, add white-space in the end of the input URL")
    try:
        url = str(input("input URL : "))
        url+=" "
        url_html = urllib.request.urlopen(url)
    except HTTPError:
        print(HTTPError)
        print("unusable URL : maybe because of blocking function in target wesite....")
        print("it might be blocked with 404 error when you access web need log-in")
        return
    soup = BeautifulSoup(url_html, "html.parser")

    #Convert the soup to a string version
    soup = str(soup)

    reg1 = r"\w+@\w+\.\w+\b"
    reg2 = r"\w+@\w+\.\w+\.\w+\b"

    emails = findall(reg1, soup)
    emails2 = findall(reg2,soup)

    # delete redundancy , there's too many same email in test site.
    emails += emails2


    emails = list(set(emails))

    if emails:
        print("Found Emails below.. ")
        for elem in emails:
            print(elem)
    else:
        print("NO email strings. in this web...")

main()