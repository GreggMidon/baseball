'''
Name.......: ev_brkout_test.py
Descr......:
Author.....: Gregg Midon
Date.......:
'''
from db.db_funcs import get_connection, retr_game_event_errs
import difflib


def main():
    conn = get_connection()
    ev_recs = retr_game_event_errs(conn)

    diff = difflib.Differ()

    for r in ev_recs:
        game_ndx = r[0]
        seq_num = r[1]
        evt_str = r[2]
        evt_bld = r[3]

        prfx = '{},{},{},{},'.format(game_ndx, seq_num, evt_str, evt_bld)
        combo = ''


        chars = list(diff.compare(evt_str, evt_bld))
        for char in chars:
            combo += char + ','

        print(prfx + combo)

    conn.close()

if __name__ == '__main__':

    main()