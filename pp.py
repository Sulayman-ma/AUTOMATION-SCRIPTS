#! python3


"""
PLUS PREMIERES

Find the latest releases on PlusPremieres.
Usage:
A batch file is already available. Add the path of the batch folder to the PATH
    pp <number of songs>
    default will return the 25 most recent uploads.
"""



# Python Imports
import re
import bs4
import requests
import sys


if len(sys.argv) == 2:
    maxResult = int(sys.argv[1])
else:
    maxResult = 25

nameFilter = re.compile(r'<script>document.write\(getAlbum\("(.*) - Single",.*')
removeAmp = re.compile(r'amp;')

# Link to new songs page
newSongs = requests.get(
'https://www.pluspremieres.to/search/label/New%20Music+Single?max-results={}'.format
(maxResult))

soap = bs4.BeautifulSoup(newSongs.text, features = 'lxml')

# Selector with raw song name
songLink = soap.select('#Blog1 > div > div.new-songs-wrapper > a > .song > '
                       '.song-title-wrap > .song-title > script')

for song in songLink:
    # Removing excess info and 'amp;' to get pure file name
    filteredName = nameFilter.sub(r'\1', str(song))
    filteredName = removeAmp.sub('', filteredName)

    print(filteredName)