from db.sqlrepo import *
from db.db_funcs import get_connection

def main():
    print('Begin...')
    fname = '/Users/greggmidon/data/bbx/parks.csv'
    print('Reading file: ' + fname)

    # open file for source data
    src = open(fname, 'r')

    # connect to database
    conn = get_connection()
    cur = conn.cursor()

    # iterate through the file
    for line in src:
        line = line[:-1]
        fields = line.split(',')

        park_id = fields[0]
        park_name = fields[1]
        alt_names = fields[2]
        city = fields[3]
        state = fields[4]
        open_date = fields[5]
        close_date = fields[6]
        if close_date == '':
            close_date = None

        league = fields[7]

        cur.execute(park_ins,(park_id,park_name,alt_names,city,state,open_date,close_date,league))

    conn.commit()

    src.close()
    cur.close()
    conn.close()


if __name__ == '__main__':

    main()
