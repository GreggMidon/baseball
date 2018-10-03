'''
Name.......: season_loader.py
Descr......: Script to manage processing of game files (event, team, roster).
Author.....: Gregg Midon
Date.......: 8/26/2018
'''
import argparse
from filesys import *
from fileproc import readlist


def main(args):

    # get a list of file names to process
    if args.staging:
        readlist(geteventfilesstaged())

    elif args.season > 0:

        if args.fa:
            readlist(getamerleagevents(args.season))

        elif args.fn:
            readlist(getnatlleagevents(args.season))

        elif args.fr:
            readlist(getrosterfiles(args.season))

        elif args.ft:
            readlist(getteamfile(args.season))

        elif args.fall:
            readlist(getallseasonfiles(args.season))

        else:
            readlist(geteventfiles(args.season))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--season', help='The season (year) to process.', type=int, dest='season')
    parser.add_argument('-g', '--staging', help='Process files from staging area.', action='store_true')
    parser.add_argument('-fa', help='Process American League event files (*.EVA).', action='store_true')
    parser.add_argument('-fn', help='Process National League event files (*.EVN).', action='store_true')
    parser.add_argument('-fr', help='Process Roster files (*.ROS).', action='store_true')
    parser.add_argument('-ft', help='Process Team files (TEAMyyyy).', action='store_true')
    parser.add_argument('-fall', help='Process all event files (*.EVA & *.EVN', action='store_true')

    args = parser.parse_args()

    main(args)