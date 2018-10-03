import psycopg2
from psycopg2.extras import execute_values
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


def insertinfo(conn, info):
    cur = conn.cursor()

    # insert into game_hdr
    cur.execute(gm_hdr_ins_sql,(info['index'],info['id'],info['season'],info['visteam'],info['hometeam'],info['date'],info['number'],info['starttime'],datetime.datetime.now()))

    # insert into ev_info
    cur.execute(info_ins_sql,(info['index'],info['umphome'],info['ump1b'],info['ump2b'],info['ump3b'],info['usedh'],info['howscored'],info['pitches'],info['oscorer'],datetime.datetime.now()))

    # insert into game_cond
    cur.execute(gm_cond_ins_sql,(info['index'],info['site'],info['daynight'],info['temp'],info['winddir'],info['windspeed'],info['fieldcond'],info['precip'],info['sky'],info['timeofgame'],info['attendance'],datetime.datetime.now()))

    # insert into game_pitching
    cur.execute(gm_pitch_ins_sql,(info['index'],info['wp'],info['lp'],info['save'],datetime.datetime.now()))

    conn.commit()
    cur.close()


def insertstart(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, start_ins_sql, datalist, template=start_ins_templ, page_size=start_pg_sz)
    conn.commit()
    cur.close()


def insertplay(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, play_ins_sql, datalist, template=play_ins_templ, page_size=play_pg_sz)
    conn.commit()
    cur.close()


def insertsub(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, sub_ins_sql, datalist, template=sub_ins_templ, page_size=sub_pg_sz)
    conn.commit()
    cur.close()


def insertdata(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, data_ins_sql, datalist, template=data_ins_templ, page_size=data_pg_sz)
    conn.commit()
    cur.close()

def insertroster(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, roster_ins_sql, datalist, template=roster_ins_templ, page_size=roster_pg_sz)
    conn.commit()
    cur.close()
