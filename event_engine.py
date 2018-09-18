from db.db_funcs import getconnection
from db.db_funcs import gameevents
from common import *
import re

def main(game_id):

    # prepare the regex's
    event_pattern = re.compile(regex_evt)
    mod_pattern = re.compile(regex_mod)
    ra_pattern = re.compile(regex_ra)

    # file io
    f_data = open(stagedir + game_id + "_evtdtl.txt", "w")
    f_rej = open(stagedir + game_id + "_reject.txt", "w")

    # connect to database
    conn = getconnection()

    # retrieve events for the game identified by game_id
    rows = gameevents(game_id, conn)

    # loop thru events
    event = ''
    modifiers = []
    runner_adv = []
    row_num = 0

    for row in rows:

        seq_num = row[0]
        event_str = row[4]

        # event/mod1/mod2/.../modn.ra1;ra2;...;ran
        row_num += 1
        print(row_num)

        # event segment
        match = event_pattern.search(event_str)
        if match:
            event = match.group(1)

            # modifier seqment
            modifiers = re.findall(mod_pattern, event_str)

            # runner advancement segment
            runner_adv = re.findall(ra_pattern, event_str)

            # output to file
            out = '{},{},{},{}'.format(game_id, seq_num, event_str, event)
            out += out_string(modifiers, runner_adv)
            to_file(f_data, out)

        else:
            out = '{},{},{}'.format(game_id, seq_num, event_str)
            to_file(f_rej, out)


    # close the db connection
    conn.close()
    f_data.close()
    f_rej.close()


def out_string(modifiers, runner_adv):

    outstr = ','

    mod_len = len(modifiers)
    ra_len = len(runner_adv)
    modstr = ''
    rastr = ''

    if mod_len == 0:
        modstr = ',,'
    elif mod_len == 1:
        modstr = '{},,'.format(modifiers[0])
    elif mod_len == 2:
        modstr = '{},{},'.format(modifiers[0], modifiers[1])
    elif mod_len == 3:
        modstr = '{},{},{}'.format(modifiers[0], modifiers[1], modifiers[2])

    if ra_len == 0:
        rastr = ',,'
    elif ra_len == 1:
        rastr = '{},,'.format(runner_adv[0])
    elif ra_len == 2:
        rastr = '{},{},'.format(runner_adv[0], runner_adv[1])
    elif ra_len == 3:
        rastr = '{},{},{}'.format(runner_adv[0], runner_adv[1], runner_adv[2])

    return ',' + modstr + ',' + rastr



def to_file(f, s):
    f.write(s + '\n')


if __name__ == '__main__':

    game_id = 'MIN201607050'

    main(game_id)