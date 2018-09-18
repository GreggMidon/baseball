from com.nop.bb.event_processor import processEvent
from com.nop.bb.modifier_processor import processModifier
from com.nop.bb.runner_advance_processor import processRunnerAdvance
from com.nop.bb.AtBat import AtBat

def play_game():
    source = open("C:\\Data\\bb\\2012\\testgame.txt", "r")
    dest = open("C:\\Data\\bb\\2012\\testgame.out", "w")
    
    out_count = 0
    home_runs = 0
    home_hits = 0
    home_errs = 0
    
    away_runs = 0
    away_hits = 0
    away_errs = 0
    
    on_first = 'NA'
    on_second = 'NA'
    on_third = 'NA'
    game_id = 'NA'
    
    batting_team = 'A'
    empty_string = ''

    play_count = 0
    for line in source:
        if line[-1] == '\n': line = line[:-1]
        fields = line.split(',')
        recordType = fields[0]
        pre_play = empty_string
        
        if recordType == 'id':
            game_id = fields[1]
        
        elif recordType == 'play':
            
            # end the inning or sidez2
                out_count = 1
                if batting_team == 'A':
                    batting_team = 'H'
                else:
                    batting_team = 'A'
            
            play_count += 1
            this_inning = fields[1]
            this_team = fields[2]
            this_batter = fields[3]
            
            pre_play = '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(game_id,play_count,this_inning,batting_team,this_team,this_batter,home_runs,home_hits,home_errs,away_runs,away_hits,away_errs,on_first,on_second,on_third,out_count)
            print(pre_play)

            buffer = empty_string
            token_list = []
            
            # tokenize event string (PLAY_DSC/MODIFIER+.PLAY_ADVL+);
            event = fields[6]
            for char in event:
                
                if char == '/':
                    token_list.append(buffer)
                    buffer = '/'
                    
                elif char == '.':
                    token_list.append(buffer)
                    buffer = '.'
                    
                elif char == ';':
                    token_list.append(buffer)
                    buffer = ';'
                
                else:
                    buffer += char
            
            token_list.append(buffer)
            
            # analyze tokens -> AtBat object    
            atbat = analyzeTokens(token_list)
            post_play = empty_string
                        
            # tabulate results
            player_event = atbat.PlayerEvent
            
            # was an out made?
            outs = player_event.outCount()
            if outs > 0:
                out_str = 'Y'
                out_count += outs
            else:
                out_str = 'N'
            
            # was there an error?
            if batting_team == 'H':
                home_errs += 1
            else:
                away_errs += 1
            
            # was there a hit?
            hit_string = 'NA'
            if player_event.isHit():
                if player_event.is_single:
                    hit_string = 'S'
                    #on_first = this_batter
                    
                elif player_event.is_double:
                    hit_string = 'D'
                    #on_second = this_batter
                    
                elif player_event.is_triple:
                    hit_string = 'T'
                    #on_third = this_batter

                if batting_team == 'H':
                    home_hits += 1
                else:
                    away_hits += 1
                    
            # was there any runner advancement                
            runner_adv_list = atbat.RunnerAdvanceList
            for runner_adv in runner_adv_list:
                
                if runner_adv.isOut:
                    outs += 1
                else:
                    strt = runner_adv.startingBase
                    endb = runner_adv.endingBase
                    
                    '''
         self.startingBase = 0
        self.endingBase = 0
        self.outAtBase = 0
        self.doesScore = False
        self.isOut = False
                    '''
                    
            post_play = '{},{},{}'.format(player_event.event_string,out_str,hit_string)            
            print('  POST:' + post_play)        
            dest.write(pre_play + ',' + post_play)

    source.close()
    dest.close()
    


def analyzeTokens(token_list):

    token_count = 0
    modifier_list = []
    runner_adv_list = []
    atbat = AtBat()

    for token in token_list:
        
        first_char = token[0]
        token_count += 1
        
        if first_char == '/':
            #print('token {} = Modifier: {}'.format(token_count, token))
            modifier_list.append(token)
            #processModifier(token)
            
        elif first_char == '.':
            #print('token {} = Runner Advancement: {}'.format(token_count, token))
            runner_adv = processRunnerAdvance(token)
            runner_adv_list.append(runner_adv)
            
        elif first_char == ';':
            #print('token {} = Runner Advancement: {}'.format(token_count, token))
            runner_adv = processRunnerAdvance(token)
            runner_adv_list.append(runner_adv)

        else:
            #print('token {} = Event: {}'.format(token_count, token))
            player_event = processEvent(token)
            atbat.PlayerEvent = player_event

    atbat.ModifierList = modifier_list    
    atbat.RunnerAdvanceList = runner_adv_list
    
    return atbat


if __name__ == '__main__':
    play_game()