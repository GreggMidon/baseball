from db.sqlrepo import *


def parse(game_id, conn):

    # database cursor
    cur = conn.cursor()

    # retrieve event records for given game_id
    cur.execute(events_sel, (game_id,))

    for record in cur:
        evnt_str = record[3]
        tokens = []

        if '.' in evnt_str:
            segments = evnt_str.split('.')

            left_seg = segments[0]
            right_seg = segments[1]

            if '/' in left_seg:
                left_tokens = left_seg.split('/')

                for token in left_tokens:
                    tokens.append(token)

            else:
                tokens.append(left_seg)

            if ';' in right_seg:
                right_tokens = right_seg.split(';')

                for token in right_tokens:
                    tokens.append(token)

            else:
                tokens.append(right_seg)

        elif '/' in evnt_str:
            segments = evnt_str.split('/')

            for token in segments:
                tokens.append(token)

        else:
            tokens.append(evnt_str)

        return tokens


    # close communication with the database
    cur.close()
    conn.close()
