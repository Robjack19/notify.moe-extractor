#replacing status
def replace(nstatus):
    astatus = ''
    watching =0
    completed = 0
    planned = 0
    hold = 0
    dropped = 0
   
    if nstatus == 'watching':
        astatus = (str('Watching'))
        watching =1

    elif nstatus == 'completed':       
        astatus = (str('Completed'))
        completed =1

    elif nstatus == 'planned':      
        astatus = (str('Plan to Watch'))
        planned = 1

    elif nstatus == 'hold':     
        astatus = (str('On-Hold'))
        hold = 1

    elif nstatus == 'dropped':    
        astatus = (str('Dropped'))
        dropped = 1

    else:    
        astatus = (str('Plan to Watch'))
        planned = 1
    
    return astatus, watching, completed, planned, hold, dropped