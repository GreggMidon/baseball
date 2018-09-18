class PlayerEvent(object):

    def __init__(self):
 
        #init members
        self.fielder_list = []
        self.is_out = False
        self.is_dp = False
        self.is_tp = False
        self.is_bb = False
        self.is_noplay = False
        self.is_hbp = False          # hit by pitch
        self.is_single = False
        self.is_double = False
        self.is_grd = False          # ground rule double
        self.is_triple = False
        self.is_hr = False
        self.is_balk = False
        self.is_stolen_base = False
        self.is_error = False
        self.is_non_abe = False      # non atbat event
        self.is_ce = False           # catcher interference
        
    def addToFielderList(self, fielder):
        self.fielder_list.append(fielder)
        
    def outCount(self):
        
        if self.is_out:
            if self.is_dp:
                return 2
           
            elif self.is_tp:
                return 3
           
            else:
                return 1
        
        return 0
    
    def isHit(self):
        
        if self.is_single or self.is_double or self.is_triple or self.is_hr:
            return True
        
        return False
    
    def advanceToBase(self):

        if self.is_single:
            return '1'
        
        elif self.is_double:
            return '2'
                   
        elif self.is_triple:
            return '3'
        
        elif self.is_bb:
            return '1'
        
        elif self.is_grd:
            return '2'
        
        elif self.is_hbp:
            return '1'
        
        elif self.is_hr:
            return 'H'
        
        elif self.is_ce:
            return '1'

        elif self.is_balk:
            return '1'
        
        return None