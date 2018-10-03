
# park insert parameters
park_ins_sql = '''
insert into prod.parks (park_id,park_nm,alt_nm,city,state,open_dt,close_dt,league,entry_dt)
values (%s, %s, %s, %s, %s, %s, %s, %s);
'''

# roster insert parameters
roster_ins_sql = '''
insert into prod.roster (player_id,last_nm,first_nm,bat_hnd,throw_hnd,team_id,fld_pos,season,entry_dt) values %s
'''
roster_ins_templ = "(%(player_id)s,%(last_nm)s,%(first_nm)s,%(bat_hnd)s,%(throw_hnd)s,%(team_id)s,%(fld_pos)s,%(season)s,%(entry_dt)s)"
roster_pg_sz = 10

# data event insert parameters
data_ins_sql = '''
insert into prod.ev_data (game_ndx,data_typ,player_id,smint_val,entry_dt) values %s
'''
data_ins_templ = "(%(game_ndx)s,%(data_typ)s,%(player_id)s,%(smint_val)s,%(entry_dt)s)"
data_pg_sz = 100

# team insert parameters (not loaded in bulk)
team_ins_sql = '''
insert into prod.team (team_id,al_nl,team_cty,team_nm,season,entry_dt)
values (%s, %s, %s, %s, %s, %s)
'''

# parsed game play event records (not loaded in bulk)
dtl_ins_sql = '''
insert into prod.evt_dtl (game_id,seq_num,event_str,event_cd,mod_cd1,mod_cd2,mod_cd3,ra_1,ra_2,ra_3,entry_dt)
values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

# game header insert (not loaded in bulk)
gm_hdr_ins_sql = '''
insert into prod.game_hdr(game_ndx,game_id,season,vis_tm,home_tm,game_dt,game_num,start_tm,entry_dt)
values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

# game condition insert (not loaded in bulk)
gm_cond_ins_sql = '''
insert into prod.game_cond(game_ndx,site,day_nite,temperature,wind_dir,wind_spd,fld_cond,precip,sky,time_of_gm,attend,entry_dt)
values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

# game information records (not loaded in bulk)
info_ins_sql = '''
insert into prod.ev_info(game_ndx,ump_hm,ump_1st,ump_2nd,ump_3rd,use_dh,howscored,pitches,oscorer,entry_dt)
values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

# game pitching outcome insert (not loaded in bulk)
gm_pitch_ins_sql = '''
insert into prod.game_pitching(game_ndx,win_pitcher,lose_pitcher,save,entry_dt) 
values(%s, %s, %s, %s, %s)
'''

# play event insert parameters
play_ins_sql = '''
insert into prod.ev_play(game_ndx,seq_num,inning,visit_home,player_id,pitch_cnt,pitches,event_str,entry_dt) values %s
'''
play_ins_templ = "(%(game_ndx)s,%(seq_num)s,%(inning)s,%(visit_home)s,%(player_id)s,%(pitch_cnt)s,%(pitches)s,%(event_str)s,%(entry_dt)s)"
play_pg_sz = 100

# start event insert parameters
start_ins_sql = '''
insert into prod.ev_start(game_ndx,player_id,player_nm,visit_home,"order","position",entry_dt) values %s
'''
start_ins_templ = "(%(game_ndx)s,%(player_id)s,%(player_nm)s,%(visit_home)s,%(order)s,%(position)s,%(entry_dt)s)"
start_pg_sz = 100

# substitute event insert parameters
sub_ins_sql = '''
insert into prod.ev_sub(game_ndx,seq_num,player_id,player_nm,visit_home,"order","position",entry_dt) values %s
'''
sub_ins_templ = "(%(game_ndx)s,%(seq_num)s,%(player_id)s,%(player_nm)s,%(visit_home)s,%(order)s,%(position)s,%(entry_dt)s)"
sub_pg_sz = 100

events_select = '''
select  seq_num,inning,visitinghome,player_id,event_string 
from    prod.ev_play 
where   game_id = %s
order by seq_num
'''
