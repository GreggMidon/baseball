from pathlib import Path
from util.common import *


def get_roster_files(season):
    return get_files(season, rosterfiles)


def get_event_files(season):
    return get_files(season, all_events)


def get_team_file(season):
    return rootdir + str(season) + '/TEAM' + str(season)


def get_al_events(season) :
    return get_files(season, al_events)


def get_nl_events(season):
    return get_files(season, nl_events)


def get_all_season_files(season):
    return get_files(season, all_files)


def get_event_files_staged():
    workingdir = stagedir
    p = Path(workingdir)
    return list(p.glob(all_files))


def get_files(season, fglob):
    workingdir = rootdir + str(season) + '/'
    p = Path(workingdir)
    return list(p.glob(fglob))