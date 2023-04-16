##def count(rem):
##    
##    if rem < 2:
##        return rem
##    else:
##        return 2 + count(rem - 1) + count(rem - 2)


def count(rem: int) -> int:
    '''
    A short staircase consists of n steps. Sometimes you take 1 step
    at a time, sometimes 2. How many possible ways to go down the stairs
    are there?
    '''

    if rem < 2:
        return 1
    else:
        return count(rem - 1) + count(rem - 2) 
