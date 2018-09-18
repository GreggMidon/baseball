'''
Name.......: roster_ldr.py
Descr......: loads Roster records into database
Author.....: Gregg Midon
Date.......: 8/26/2018
'''
from db.sqlrepo import *
from db.db_funcs import getconnection
import datetime


def load(file, season):

    # connect to database
    conn = getconnection()
    cur = conn.cursor()

    # open file for source data
    rfil = open(file, 'r')

    # read each line from file
    for line in rfil:
        line = line[:-1]
        fields = line.split(',')

        playid = fields[0]
        lname = fields[1]
        fname = fields[2]
        bat_hnd = fields[3]
        thr_hnd = fields[4]
        teamid = fields[5]
        position = fields[6]

        # insert into Roster table
        cur.execute(roster_ins,(playid,lname,fname,bat_hnd,thr_hnd,teamid,position,season,datetime.datetime.now()))

    conn.commit()

    # close communication with the database
    cur.close()
    conn.close()
    rfil.close()
