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
    wordstring = ''

    userArticle = input('Please input a Wikipedia article URL. Try "http://en.wikipedia.org/wiki/Special:Random" to get a random article!: ')
    userWord = input('Please enter a word to get the word count for (THIS IS CASE SENSITIVE): ')
    
    req = requests.get(userArticle)
    soup = BeautifulSoup(req.text, "lxml")

    length = len(soup.find_all('p'))

    while(number < length):
        wordstring  += soup.find_all('p')[number].get_text()
        print(soup.find_all('p')[number].get_text())
        number += 1

    wordlist = wordstring.split()
    wordfreq = [wordlist.count(w) for w in wordlist]
    
    print('\nThe word you entered: "' + userWord + '" appears ' + str(wordlist.count(userWord)) + ' times.')

main()
