# File:             wikpediawordcounter.py
# Author:           Michael Cassio
# Date:             11/14/17
# E-mail:           catastrio@gmail.com
# Description:      A program that will grab the contents of a Wikipedia page
#                   then count the number of times a specific word appears.

from bs4 import BeautifulSoup
import requests

def main():

    import requests
    from bs4 import BeautifulSoup

    number = 0

    userInput = input('Please input a Wikipedia article URL. Try "http://en.wikipedia.org/wiki/Special:Random" to get a random article!: ')
    req = requests.get(userInput)
    soup = BeautifulSoup(req.text, "lxml")

    length = len(soup.find_all('p'))

    while(number < length):
        print(soup.find_all('p')[number].get_text())
        number += 1

main()
