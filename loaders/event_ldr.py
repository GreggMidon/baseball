'''
Name.......: event_ldr.py
Descr......: loads Event records into database
Author.....: Gregg Midon
Date.......: 8/26/2018
'''
import datetime
from db.db_funcs import get_connection, retr_game_index, insert_info_rec, insert_start_rec, insert_play_rec, insert_sub_rec, insert_data_rec


def load(file, season):

    # connect to database
    conn = get_connection()

    # source file
    tfil = open(file, 'r')

    # iterate through the file
    firsttime = True
    lnum = 0;

    for line in tfil:
        line = line[:-1]
        recordList = line.split(',')
        rectyp = recordList[0]

        if rectyp == 'id':
            id = recordList[1]
            #print(' -> ' + id)
            index = retr_game_index(conn)

            if firsttime:
                firsttime = False
            else:
                insert_info_rec(conn, _info)
                insert_start_rec(conn, _start)
                insert_sub_rec(conn, _sub)
                insert_data_rec(conn, _data)
                insert_play_rec(conn, _play)

            # setup for next game
            _info = dict()
            _info['id'] = id
            _info['index'] = index
            _info['season'] = season
            _start = []
            _play = []
            _sub = []
            _data = []
            lnum = 0

        elif rectyp == 'info':
            rkey = recordList[1]
            rval = recordList[2]
            _info[rkey] = rval

        elif rectyp == 'start':
            d = dict()
            d['game_ndx'] = index
            d['player_id'] = recordList[1]
            d['player_nm'] = recordList[2]
            d['visit_home'] = recordList[3]
            d['order'] = recordList[4]
            d['position'] = recordList[5]
            d['entry_dt'] = datetime.datetime.now()
            _start.append(d)

        elif rectyp == 'play':
            lnum += 1
            d = dict()
            d['game_ndx'] = index
            d['seq_num'] = lnum
            d['inning'] = recordList[1]
            d['visit_home'] = recordList[2]
            d['player_id'] = recordList[3]
            d['pitch_cnt'] = recordList[4]
            d['pitches'] = recordList[5]
            d['event_str'] = recordList[6]
            d['entry_dt'] = datetime.datetime.now()
            _play.append(d)


        elif rectyp == 'sub':
            lnum += 1
            d = dict()
            d['game_ndx'] = index
            d['seq_num'] = lnum
            d['player_id'] = recordList[1]
            d['player_nm'] = recordList[2]
            d['visit_home'] = recordList[3]
            d['order'] = recordList[4]
            d['position'] = recordList[5]
            d['entry_dt'] = datetime.datetime.now()
            _sub.append(d)

        elif rectyp == 'data':
            d = dict()
            d['game_ndx'] = index
            d['data_typ'] = recordList[1]
            d['player_id'] = recordList[2]
            d['smint_val'] = recordList[3]
            d['entry_dt'] = datetime.datetime.now()
            _data.append(d)

    insert_info_rec(conn, _info)
    insert_start_rec(conn, _start)
    insert_sub_rec(conn, _sub)
    insert_data_rec(conn, _data)
    insert_play_rec(conn, _play)

    # close communication with the database
    conn.close()
    tfil.close()
