from pathlib import Path
import os
import shutil
from random import choice
import argparse



"""
usage: music.py [-h] [-n N]

A command line tool used to easily copy a number of random songs from your music library into a folder on the desktop.

optional arguments:
  -h, --help  show this help message and exit
  -n N        number of songs to copy, 30 by default
"""


parser = argparse.ArgumentParser(description="A command line tool used to easily copy a number of random songs from your music library into a folder on the desktop.")
parser.add_argument('-n', type=int, help='number of songs to copy, 30 by default', default=30)
args = vars(parser.parse_args())


library = []
selection = []

# music library path
music = Path.home() / 'Music'

for root, folders, songs in os.walk(music):
    for song in songs:
        if song.endswith('mkv') or song.endswith('mp3'):
            library.append(Path(os.path.join(root, song)))

# create destination folder
try:
    Path.mkdir(Path.home() / 'Desktop\\Random Selection')
except FileExistsError:
    pass

total = 0
for i in range(args['n']):
    song = Path(choice(library))
    shutil.copy(song, str(Path.home() / 'Desktop\\Random Selection'))
    total += song.stat().st_size / 1048576
    library.remove(song)

print('Files copied successfully ✔\nTotal size = {:.2f}MB'.format(total))
