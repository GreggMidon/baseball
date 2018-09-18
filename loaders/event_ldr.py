'''
Name.......: event_ldr.py
Descr......: loads Event records into database
Author.....: Gregg Midon
Date.......: 8/26/2018
'''
from db.db_funcs import getconnection, gameindex, insertinfo, insertstart, insertplay, insertsub, insertdata


def load(file, season):

    # connect to database
    conn = getconnection()

    # open file for source data
    tfil = open(file, 'r')

    # iterate through the file
    lnum = 0
    firsttime = True

    for line in tfil:
        line = line[:-1]
        recordList = line.split(',')
        rectyp = recordList[0]
        lnum += 1

        if rectyp == 'id':
            id = recordList[1]
            lnum = 0
            index = gameindex(conn)

            if firsttime:
                firsttime = False
            else:
                insertinfo(conn, index, season, info)

            # setup for next game
            info = dict()
            info['id'] = id

        elif rectyp == 'info':
            rkey = recordList[1]
            rval = recordList[2]
            info[rkey] = rval

        elif rectyp == 'start':
            # insert start record
            insertstart(conn, index, lnum, recordList)

        elif rectyp == 'play':
            # insert play record
            insertplay(conn, index, lnum, recordList)

        elif rectyp == 'sub':
            # insert sub record
            insertsub(conn, index, lnum, recordList)

        elif rectyp == 'data':
            # insert data record
            insertdata(conn, index, lnum, recordList)

    conn.commit()

    # close communication with the database
    conn.close()
    tfil.close()
