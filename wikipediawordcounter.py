# File:             wikpediawordcounter.py
# Author:           Michael Cassio
# Date:             11/14/17
# E-mail:           catastrio@gmail.com
# Description:      A program that will grab the contents of a Wikipedia page
#                   then count the number of times a specific word appears.

from bs4 import BeautifulSoup
import requests

def main():
    
    userURL = input("Please enter a Wikipedia URL to download: ")

    page = requests.get(userURL)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.find_all('p')[0].get_text())

main()
