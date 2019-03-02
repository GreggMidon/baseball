'''
Name.......: load_season.py
Descr......: Script to manage processing of game files (event, team, roster).
Author.....: Gregg Midon
Date.......: 8/26/2018
'''
import argparse
from fileio.filesys import *
from fileio.fileproc import read_list


def main(args):

    # get a list of file names to process
    if args.staging:
        read_list(get_event_files_staged())

    elif args.season > 0:

        if args.fa:
            read_list(get_al_events(args.season))

        elif args.fn:
            read_list(get_nl_events(args.season))

        elif args.fr:
            read_list(get_roster_files(args.season))

        elif args.ft:
            read_list(get_team_file(args.season))

        elif args.fall:
            read_list(get_all_season_files(args.season))

        else:
            read_list(get_event_files(args.season))


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