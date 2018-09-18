import re
from com.nop.bb.RunnerAdvance import RunnerAdvance

def processRunnerAdvance(advance):
    
    advance = advance[1:]
    runner_adv = RunnerAdvance()
    
    if re.match(r'B\-\d.*', advance):
        runner_adv.startingBase = 0
        runner_adv.endingBase = advance[2]
        runner_adv.desc = 'batter advances to {}'.format(advance[2])

    elif re.match(r'1\-\d.*', advance):
        runner_adv.startingBase = 1
        runner_adv.endingBase = advance[2]
        runner_adv.desc = 'runner on 1st advances to {}'.format(advance[2])

    elif re.match(r'2\-\d.*', advance):
        runner_adv.startingBase = 0
        runner_adv.endingBase = advance[2]
        runner_adv.desc = 'runner on 2nd advances to {}'.format(advance[2])

    elif re.match(r'3\-H.*', advance):
        runner_adv.startingBase = 3
        runner_adv.endingBase = 0
        runner_adv.doesScore = True
        runner_adv.desc = 'runner on 3rd advances to home'

    elif re.match(r'\dX\d.*', advance):        
        runner_adv.startingBase = advance[0]
        runner_adv.outAtBase = advance[2]
        runner_adv.desc = 'runner on {} out at {}'.format(advance[0],advance[2])
        runner_adv.isOut = True
        
    return runner_adv    
        