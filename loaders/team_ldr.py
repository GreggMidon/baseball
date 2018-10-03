'''
Name.......: team_ldr.py
Descr......: loads Team records into database
Author.....: Gregg Midon
Date.......: 8/26/2018
'''
from db.sqlrepo import *
from db.db_funcs import getconnection
import datetime


def load(file, season):

    # open file for source data
    tfil = open(file, 'r')

    # connect to database
    conn = getconnection()
    cur = conn.cursor()

    # iterate through the file
    for line in tfil:
        line = line[:-1]
        fields = line.split(',')

        team_id = fields[0]
        al_nl = fields[1]
        tm_city = fields[2]
        tm_name = fields[3]

        cur.execute(team_ins_sql,(team_id,al_nl,tm_city,tm_name,season,datetime.datetime.now()))

    conn.commit()

    tfil.close()
    cur.close()
    conn.close()
