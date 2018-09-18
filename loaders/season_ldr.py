'''
Name......: season_ldr.py
Desc......: script to populate database tables with event file records, for an entire season.
Author....: Gregg Midon
Date.......: 8/26/2018
'''
from loaders.ldr_funcs import inforec
from filesys import geteventfilesstaged
from common import *

def main():
    lnum = 0
    firsttime = True

    # get all files in the staging directory
    filelist = geteventfilesstaged()

    for f in filelist:
        fname = f.name

        # open event file
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


if __name__ == '__main__':

    year = 2015
    main(year)