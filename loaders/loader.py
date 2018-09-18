'''
name......: season_ldr.py
desc......: script to populate database tables with event file records, for an entire season.
author....: Gregg Midon

version history:

'''
from loaders.ldr_funcs import inforec
from filesys import geteventfiles
from common import *

def load(file, season):
    lnum = 0
    firsttime = True

    # open files
    fil_info = open(stagedir + 'info.txt', 'a')
    fil_start = open(stagedir + 'start.txt', 'a')
    fil_play = open(stagedir + 'play.txt', 'a')
    fil_sub = open(stagedir + 'sub.txt', 'a')
    fil_data = open(stagedir + 'data.txt', 'a')
    fil_unk = open(stagedir + 'unknown.txt', 'a')

    filelist = geteventfiles(year)

    for f in filelist:
        fname = f.name
        print('Scanning file: ' + fname)

        # open file for source data
        source = open(f.as_posix(), 'r')

        # iterate through the file
        for line in source:
            line = line[:-1]
            recordList = line.split(',')
            rectyp = recordList[0]
            lnum += 1

            if rectyp == 'id':
                id = recordList[1]
                lnum = 0

                if firsttime:
                    firsttime = False
                else:
                    fil_info.write(inforec(info) + '\n')

                # setup for next game
                info = dict()
                info['id'] = id

            elif rectyp == 'info':
                rkey = recordList[1]
                rval = recordList[2]
                info[rkey] = rval

            elif rectyp == 'start':
                outrec = '{},{},{},{},{},{},{}'.format(id, lnum, recordList[1], recordList[2], recordList[3], recordList[4], recordList[5])
                fil_start.write(outrec + '\n')

            elif rectyp == 'play':
                outrec = '{},{},{},{},{},{},{},{}'.format(id, lnum, recordList[1], recordList[2], recordList[3], recordList[4], recordList[5], recordList[6])
                fil_play.write(outrec + '\n')

            elif rectyp == 'sub':
                outrec = '{},{},{},{},{},{},{}'.format(id, lnum, recordList[1], recordList[2], recordList[3], recordList[4], recordList[5])
                fil_sub.write(outrec + '\n')

            elif rectyp == 'data':
                outrec = '{},{},{},{},{}'.format(id, lnum, recordList[1], recordList[2], recordList[3])
                fil_data.write(outrec + '\n')

            else:
                outrec = id + ',' + str(lnum) + ',' + line
                fil_unk.write(outrec + '\n')

        # last info record needs written
        fil_info.write(inforec(info) + '\n')


    fil_info.close()
    fil_start.close()
    fil_play.close()
    fil_sub.close()
    fil_data.close()


if __name__ == '__main__':

    year = 2015
    main(year)