
park_ins = '''
insert into prod.parks (park_id,park_name,alt_names,city,state,open_date,close_date,league,entry_date)
values (%s, %s, %s, %s, %s, %s, %s, %s);
'''

roster_ins = '''
insert into prod.roster (player_id,last_name,first_name,batting_hand,throwing_hand,team_id,position,season,entry_date) 
values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

data_ins = '''
insert into prod.ev_data (game_ndx,seq_num,data_typ,player_id,smint_val,entry_date)
values (%s, %s, %s, %s, %s)
'''

team_ins = '''
insert into prod.team (team_id,al_nl,tm_city,tm_name,season,entry_date)
values (%s, %s, %s, %s, %s, %s)
'''

dtl_ins = '''
insert into prod.evt_dtl(game_id,seq_num,event_str,event_cd,mod_cd1,mod_cd2,mod_cd3,ra_1,ra_2,ra_3,entry_date)
values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

gm_hdr_ins = '''
insert into prod.game_hdr(game_ndx,game_id,season,visteam,hometeam,gm_date,gm_number,starttime,entry_date)
values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

gm_cond_ins = '''
insert into prod.game_cond(game_ndx,site,daynight,temp,winddir,windspeed,fieldcond,precip,sky,timeofgame,attendance,entry_date)
values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

info_ins = '''
insert into prod.ev_info(game_ndx,umphome,ump1b,ump2b,ump3b,usedh,howscored,pitches,oscorer,entry_date)
values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

play_ins = '''
insert into prod.ev_play(game_ndx,seq_num,inning,visitinghome,player_id,pitch_count,pitches,event_string,entry_date)
values(%s, %s, %s, %s, %s, %s, %s, %s)
'''

start_ins = '''
insert into prod.ev_start(game_ndx,seq_num,player_id,player_name,visitinghome,order,position,entry_date)
values(%s, %s, %s, %s, %s, %s, %s, %s)
'''

sub_ins = '''
insert into prod.ev_sub(game_ndx,seq_num,player_id,player_name,visitinghome,bat_order,position,entry_date)
values(%s, %s, %s, %s, %s, %s, %s, %s)
'''

events_select = '''
select  seq_num,inning,visitinghome,player_id,event_string 
from    prod.ev_play 
where   game_id = %s
order by seq_num
'''
