import psycopg2
from common import *
from db.sqlrepo import *
import datetime

def getconnection():
    return psycopg2.connect(constring)


def gameevents(game_id, conn):
    cur = conn.cursor()
    cur.execute(events_select,(game_id,))
    return cur.fetchall()


def gameindex(conn):
    cur = conn.cursor()
    cur.execute("select nextval('prod.mstr_gm_seq')")
    return cur.fetchone()


def insertinfo(conn, index, season, info):
    cur = conn.cursor()

    # insert into game_hdr
    cur.execute(gm_hdr_ins,(index,info['id'],season,info['visteam'],info['hometeam'],info['date'],info['number'],info['starttime'],datetime.datetime.now()))

    # insert into ev_info
    cur.execute(info_ins,(index,info['umphome'],info['ump1b'],info['ump2b'],info['ump3b'],info['usedh'],info['howscored'],info['pitches'],info['oscorer'],datetime.datetime.now()))

    # insert into game_cond
    cur.execute(gm_cond_ins,(index,info['site'],info['daynight'],info['temp'],info['winddir'],info['windspeed'],info['fieldcond'],info['precip'],info['sky'],info['timeofgame'],info['attendance'],datetime.datetime.now()))

    cur.close()


def insertstart(conn, index, lnum, rec):
    cur = conn.cursor()
    cur.execute(start_ins,(index,lnum,rec[1],rec[2],rec[3],rec[4],rec[5],datetime.datetime.now()))
    cur.close()


def insertplay(conn, index, lnum, rec):
    cur = conn.cursor()
    cur.execute(play_ins,(index,lnum,rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],datetime.datetime.now()))
    cur.close()


def insertsub(conn, index, lnum, rec):
    cur = conn.cursor()
    cur.execute(sub_ins,(index,lnum,rec[1],rec[2],rec[3],rec[4],rec[5],datetime.datetime.now()))
    cur.close()


def insertdata(conn, index, lnum, rec):
    cur = conn.cursor()
    cur.execute(data_ins,(index,lnum,rec[1],rec[2],rec[3],datetime.datetime.now()))
    cur.close()
