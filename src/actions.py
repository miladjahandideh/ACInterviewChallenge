import time

def check_if_task_done(trigger,user_trigger):
    ## We should check and register it in DB or set a flag ##
    print("Checking if action is done or not \n")
    done_successfuly = True
    if done_successfuly:
        return True
    else:
        return False

def action_and_check(trigger,user_trigger):
    """ 
    Action Function. 
  
    If trigger happens this function will run to solve problem. 
  
    Parameters: 
    trigger (str): Trigger that happended 
    user_trigger (dic): User Defined Trigger from config file/DB
  
    Returns: 
    Boolean: If Every thing has gone OK it will return True 
  
    """
    print("trigger matching:{} - Running script: {} \n".format(trigger,user_trigger["action"])) 
    max_try = 10
    while max_try > 0:
        if check_if_task_done(trigger,user_trigger):
            return True
        max_try +=1
    return False