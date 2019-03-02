import psycopg2
from psycopg2.extras import execute_values
from util.common import *
from db.sqlrepo import *
import datetime

def get_connection():
    return psycopg2.connect(constring)


def retr_game_events(conn, game_ndx):
    cur = conn.cursor()
    cur.execute(evt_sel_sql,(game_ndx,))
    return cur.fetchall()


def retr_game_index(conn):
    cur = conn.cursor()
    cur.execute("select nextval('prod.mstr_gm_seq')")
    return cur.fetchone()

def retr_game_index_list(conn):
    cur = conn.cursor()
    cur.execute(evt_nsel_sql)
    return cur.fetchall()

def retr_game_event_errs(conn):
    cur = conn.cursor()
    cur.execute(evt_err_sql)
    return cur.fetchall()

def insert_info_rec(conn, info):
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


def insert_start_rec(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, start_ins_sql, datalist, template=start_ins_templ, page_size=start_pg_sz)
    conn.commit()
    cur.close()


def insert_play_rec(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, play_ins_sql, datalist, template=play_ins_templ, page_size=play_pg_sz)
    conn.commit()
    cur.close()


def insert_sub_rec(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, sub_ins_sql, datalist, template=sub_ins_templ, page_size=sub_pg_sz)
    conn.commit()
    cur.close()


def insert_data_rec(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, data_ins_sql, datalist, template=data_ins_templ, page_size=data_pg_sz)
    conn.commit()
    cur.close()


def insert_roster_rec(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, roster_ins_sql, datalist, template=roster_ins_templ, page_size=roster_pg_sz)
    conn.commit()
    cur.close()


def  insert_event_dtl_rec(conn, datalist):
    cur = conn.cursor()
    execute_values(cur, dtl_ins_sql, datalist, template=dtl_ins_templ, page_size=dtl_pg_sz)
    conn.commit()
    cur.close()
