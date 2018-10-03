from pathlib import Path
from util.common import *


def getrosterfiles(season):
    return getfiles(season, rosterfiles)


def geteventfiles(season):
    return getfiles(season, all_events)


def getteamfile(season):
    return rootdir + str(season) + '/TEAM' + str(season)


def getamerleagevents(season) :
    return getfiles(season, al_events)


def getnatlleagevents(season):
    return getfiles(season, nl_events)


def getallseasonfiles(season):
    return getfiles(season, all_files)


def geteventfilesstaged():
    workingdir = stagedir
    p = Path(workingdir)
    return list(p.glob(all_files))


def getfiles(season, fglob):
    workingdir = rootdir + str(season) + '/'
    p = Path(workingdir)
    return list(p.glob(fglob))