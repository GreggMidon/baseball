'''
Name.......: load_season.py
Descr......: Script to manage processing of event files (event, team, roster).
Author.....: Gregg Midon
Date.......: 8/26/2018
'''
#import argparse
from loaders.evt_dtl_ldr import parse_event
from db.db_funcs import getconnection, gameindexlist

def main():

    print('Event Parser: begin.')

    # by game index
    #parse_event(getconnection(), 20180)

    # by home team
    #parse_event(getconnection(), 'ANA')

    # by number range
    conn = getconnection()
    games = gameindexlist(conn)

    for game in games:
        game_ndx = game[0]
        print('parsing game index -> {}'.format(game_ndx))
        parse_event(conn, game_ndx)


    print('Event Parser: end.')

    conn.close()

if __name__ == '__main__':

    main()