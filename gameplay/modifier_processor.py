import re

def processModifier(modifier):

    modifier = modifier[1:]
    
    if modifier == 'B':
        print('bunt')

    elif modifier == 'BF':
        print('fly ball bunt')

    elif modifier == 'BG':
        print('ground ball bunt')

    elif modifier == 'BGDP':
        print('bunt grounded into double play')

    elif modifier == 'BL':
        print('line drive bunt')
        
    elif modifier == 'BP':
        print('bunt pop up')        
        
    elif modifier == 'BPDP':
        print('bunt popped into double play')        

    elif modifier == 'BR':
        print('runner hit by batted ball')
        
    elif modifier == 'C':
        print('called third strike')        
        
    elif modifier == 'DP':
        print('unspecified double play')        
        
    elif modifier == 'F':
        print('fly ball')
        
    elif modifier == 'F-':
        print('fly ball')
        
    elif modifier == 'F+':
        print('fly ball')
        
    elif modifier == 'FDP':
        print('fly ball double play')        
        
    elif modifier == 'FL':
        print('foul')        

    elif modifier == 'FO':
        print('force out') 
        
    elif modifier == 'G':
        print('ground ball') 

    elif modifier == 'G+':
        print('deep ground ball') 

    elif modifier == 'G-':
        print('short ground ball') 

    elif modifier == 'GDP':
        print('ground ball double play') 

    elif modifier == 'GTP':
        print('ground ball triple play') 

    elif modifier == 'INT':
        print('interference') 
        
    elif modifier == 'L':
        print('line drive')  
        
    elif modifier == 'L+':
        print('deep line drive')
        
    elif modifier == 'L-':
        print('short line drive')                     

    elif modifier == 'LDP':
        print('line drive double play') 
        
    elif modifier == 'LTP':
        print('line drive triple play') 

    elif modifier == 'P':
        print('pop fly') 

    elif modifier == 'SF':
        print('sacrifice fly') 

    elif modifier == 'SH':
        print('sacrifice hit (bunt)')         
        
    elif modifier == 'TH':
        print('throw')         
        
    elif modifier == 'TP':
        print('unspecified triple play') 

    else:
        if re.match(r'E\d{1}\b', modifier):
            print('error on {}'.format(modifier[1])) 

        elif re.match(r'R\d{1}\b', modifier):
            print('relay throw from the initial fielder to {} with no out made'.format(modifier[1])) 

        elif re.match(r'TH\d{1}\b', modifier):
            print('throw to base {}'.format(modifier[2])) 
            
            