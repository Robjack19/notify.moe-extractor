#replacing status
def replace(nstatus):
    astatus = ''
   
    if nstatus == 'watching':
        astatus = (str('Watching'))

    elif nstatus == 'completed':       
        astatus = (str('Completed'))

    elif nstatus == 'planned':      
        astatus = (str('Plan to Watch'))
        
    elif nstatus == 'hold':     
        astatus = (str('On-Hold'))

    elif nstatus == 'dropped':    
        astatus = (str('Dropped'))

    else:    
        astatus = (str('Plan to Watch'))
    
    return astatus