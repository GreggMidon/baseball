import re
from com.nop.bb.PlayerEvent import PlayerEvent

def processEvent(event):
    
    player_event = PlayerEvent()
    player_event.event_string = event
    
    # literal event set
    if event == 'K':
        player_event.desc = 'strike out'
        player_event.is_out = True

    elif event == 'K+WP':
        player_event.desc = 'strike out w/wild pitch'
        player_event.is_out = True
        
    elif event == 'K23':
        player_event.desc = 'strike-out w/throw to 1st'
        player_event.is_out = True
        player_event.addToFielderList(2)
        player_event.addToFielderList(3)

    elif event == 'IW':
        player_event.desc = 'intentional walk'
        player_event.is_bb = True
        
    elif event == 'W':
        player_event.desc = 'walk'
        player_event.is_bb = True    
        
    elif event == 'NP':
        player_event.desc = 'no play'
        player_event.is_noplay = True    
    
    elif event == 'C':
        player_event.desc = 'catcher interference'
        player_event.is_ce = True

    elif event == 'DGR':
        player_event.desc = 'ground rule double'
        player_event.is_grd = True
        
    elif event == 'H': 
        player_event.desc = 'homerun'
        player_event.is_hr = True   

    elif event == 'HR':
        player_event.desc = 'homerun'
        player_event.is_hr = True

    elif event == 'HP':
        player_event.desc = 'hit by pitch'
        player_event.is_hbp = True
        
    elif event == 'BK':
        player_event.desc = 'balk'
        player_event.is_balk = True    

    elif event == 'SB2':
        player_event.desc = 'stolen base: 2nd'
        player_event.is_stolen_base = True

    elif event == 'SB3':
        player_event.desc = 'stolen base: 3rd'
        player_event.is_stolen_base = True
        
    elif event == 'SBH':
        player_event.desc = 'stolen base: home'
        player_event.is_stolen_base = True

    else:
        # variable event set
        if re.match(r'\d{1}\b', event):
            player_event.desc = 'fly out'
            player_event.is_out = True
            player_event.addToFielderList(int(event[0]))

        elif re.match(r'\d{1}\(.{1}\)\d\b', event):
            player_event.desc = 'hit into a double play'
            player_event.is_out = True
            player_event.is_dp = True
            
        elif re.match(r'\d{2}\(.{1}\)\d\b', event):
            player_event.desc = 'hit into a double play'
            player_event.is_dp = True

        elif re.match(r'\d+\b', event):
            player_event.desc = 'ground out'
            player_event.is_out = True
            fielder_list = parseGroundOut(event)

            for fielder in fielder_list:
                player_event.addToFielderList(int(fielder))
                
        elif re.match(r'S\d*\b', event):
            player_event.desc = 'single'
            player_event.is_single = True
        
        elif re.match(r'D\d*\b', event):
            player_event.desc = 'double'
            player_event.is_double = True
        
        elif re.match(r'T\d*\b', event):
            player_event.desc = 'triple'
            player_event.is_triple = True
            
        elif re.match(r'E\d*', event):
            player_event.desc = 'error'
            player_event.is_error = True
            player_event.addToFielderList(int(event[1]))
                
        elif re.match(r'FLE\d*\b', event):
            player_event.desc = 'error fielding foul ball'
            player_event.is_error = True
            player_event.addToFielderList(int(event[3]))
            
        elif re.match(r'PO\d{1}\(\d*\)', event):
            player_event.desc = 'picked-off'
            player_event.is_out = True
            player_event.is_non_abe = True
            
        elif re.match(r'POCS\d{1}\(\d*\)', event):
            player_event.desc = 'pick-off, caught stealing'
            player_event.is_out = True
            player_event.is_non_abe = True

        elif re.match(r'CS2\(\d+\)', event):
            player_event.desc = 'caught stealing 2nd'
            player_event.is_out = True
            player_event.is_non_abe = True

        elif re.match(r'CS3\(\d+\)', event):
            player_event.desc = 'caught stealing 3rd'
            player_event.is_out = True
            player_event.is_non_abe = True
            
        elif re.match(r'CSH\(\d+\)', event):
            player_event.desc = 'caught stealing home'
            player_event.is_out = True
            player_event.is_non_abe = True
     
        elif re.match(r'FC\(\d+\)', event):
            player_event.desc = 'fielders choice'
            player_event.is_out = True

    return player_event
            
def parseGroundOut(event):

    fielder_list = []
    
    for fielder in event:
        fielder_list.append(fielder)
        
    return fielder_list


def baseHitLocation(event):
    
    if len(event) > 1:
        return event[1]
    
    else:
        return None
