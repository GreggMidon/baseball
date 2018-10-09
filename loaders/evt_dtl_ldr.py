"""
Name.......: evt_dtl_ldr.py
Descr......: Parse and persist play events.
Author.....: Gregg Midon
Date.......: 10/03/2018
"""
import re
import datetime
from db.db_funcs import gameevents, inserteventdtl
from util.common import *


def parse_event(conn, index):

    # prepare the regex's
    evt_pattern = re.compile(regex_evt)
    mod_pattern = re.compile(regex_mod)
    ra_pattern = re.compile(regex_ra)

    # write event strings that pass thru regex's w/o match
    f_err = open(stagedir + "err.txt", "a")

    # retrieve events for specified game
    rows = gameevents(conn, index)

    # loop thru events
    _dtls = []

    for row in rows:
        seq_num = row[1]
        event_str = row[2]

        # event segment
        match = evt_pattern.search(event_str)
        if match:
            event = match.group(1)

            # modifier seqment
            modifiers = re.findall(mod_pattern, event_str)

            # runner advancement segment
            runner_adv = re.findall(ra_pattern, event_str)

            # create db record
            d = dict()
            d['game_ndx'] = index
            d['seq_num'] = seq_num
            d['event_str'] = event_str
            d['event_cd'] = event

            mod_len = len(modifiers)
            if mod_len == 0:
                d['mod_cd1'] = None
                d['mod_cd2'] = None
                d['mod_cd3'] = None

            elif mod_len == 1:
                d['mod_cd1'] = modifiers[0]
                d['mod_cd2'] = None
                d['mod_cd3'] = None

            elif mod_len == 2:
                d['mod_cd1'] = modifiers[0]
                d['mod_cd2'] = modifiers[1]
                d['mod_cd3'] = None

            elif mod_len == 3:
                d['mod_cd1'] = modifiers[0]
                d['mod_cd2'] = modifiers[1]
                d['mod_cd3'] = modifiers[2]

            elif mod_len > 3:
                d['mod_cd1'] = modifiers[0]
                d['mod_cd2'] = modifiers[1]
                d['mod_cd3'] = modifiers[2]
                f_err.write('{},{},{}'.format(index, seq_num, event_str))

            ra_len = len(runner_adv)
            if ra_len == 0:
                d['ra_1'] = None
                d['ra_2'] = None
                d['ra_3'] = None

            elif ra_len == 1:
                d['ra_1'] = runner_adv[0]
                d['ra_2'] = None
                d['ra_3'] = None

            elif ra_len == 2:
                d['ra_1'] = runner_adv[0]
                d['ra_2'] = runner_adv[1]
                d['ra_3'] = None

            elif ra_len == 3:
                d['ra_1'] = runner_adv[0]
                d['ra_2'] = runner_adv[1]
                d['ra_3'] = runner_adv[2]

            d['entry_dt'] = datetime.datetime.now()
            _dtls.append(d)
            #print(d)

        else:
            out = '{},{},{}'.format(index, seq_num, event_str)
            f_err.write(out)

    # insert into db
    inserteventdtl(conn, _dtls)

    # close the db connection
    f_err.close()
