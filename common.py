'''
Name.......: common.py
Descr......: Application properties.
Author.....: Gregg Midon
Date.......: 8/26/2018
'''

# constants
rosterfiles = '*.ROS'
al_events = '*.EVA'
nl_events = '*.EVN'
all_events = '*.EV?'
all_files = '*'

# parameters
constring = 'host=Black.local user=postgres password=effin*shit dbname=dev'

# paths
rootdir = '/Users/greggmidon/data/bbx/'
stagedir = rootdir + 'staging/'

# regular expression patterns
regex_evt = r'^([0-9A-Z()]*)[/.;]?'
regex_mod = r'/([0-9A-Z+-]*)(?=[/.]?)'
regex_ra = r'[.;]([123H]-[123H])(?=[;]?)'
regex_roster = r'^([A-Z]{3})(\d{4})\.ROS'
regex_event = r'^(\d{4})([A-Z]{3})\.EV[A|N]'
regex_team = r'^TEAM(\d{4})'
