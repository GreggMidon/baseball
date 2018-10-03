'''
Name.......: roster_ldr.py
Descr......: loads Roster records into database
Author.....: Gregg Midon
Date.......: 8/26/2018
'''
from db.sqlrepo import *
from db.db_funcs import getconnection, insertroster
import datetime


def load(file, season):

    # connect to database
    conn = getconnection()

    # open file for source data
    rfil = open(file, 'r')

    # read each line from file
    _ros = []
    for line in rfil:
        line = line[:-1]
        fields = line.split(',')

        d = dict()
        d['player_id'] = fields[0]
        d['last_nm'] = fields[1]
        d['first_nm'] = fields[2]
        d['bat_hnd'] = fields[3]
        d['throw_hnd'] = fields[4]
        d['team_id'] = fields[5]
        d['fld_pos'] = fields[6]
        d['season'] = season
        d['entry_dt'] = datetime.datetime.now()
        _ros.append(d)

    # insert into Roster table
    insertroster(conn, _ros)

    # close communication with the database
    conn.close()
    rfil.close()
