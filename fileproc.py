'''
Name.......: fileproc.py
Descr......: Provided with a list of files, delegate processing of file data to the
             appropriate loader.
Author.....: Gregg Midon
Date.......: 8/26/2018
'''
import re
import loaders.roster_ldr as rl
import loaders.team_ldr as tl
import loaders.event_ldr as el
from common import *


def readlist(filelist):

    # prepare the regex's
    roster_pattern = re.compile(regex_roster)
    event_pattern = re.compile(regex_event)
    team_pattern = re.compile(regex_team)
    matched = False

    for file in filelist:
        print('Reading/Processing file = {}'.format(file.name))

        match = roster_pattern.search(file.name)
        if match:
            season = int(match.group(2))
            matched = True
            rl.load(file, season)

        match = event_pattern.search(file.name)
        if match:
            season = int(match.group(1))
            matched = True
            el.load(file, season)

        match = team_pattern.search(file.name)
        if match:
            season = int(match.group(1))
            matched = True
            tl.load(file, season)

        if not matched:
            if file.name != '.DS_Store':
                print('Unknown file type: ', file.name)
